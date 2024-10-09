import os
import pathlib
import queue
import signal
import threading
import time
import typing
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from enum import Enum
from inspect import signature
from typing import Optional

import grpc
import yaml
from google.protobuf import json_format
from grpc._channel import _InactiveRpcError, _MultiThreadedRendezvous
from pydantic import ValidationError

from mlp_sdk.grpc import mlp_grpc_pb2, mlp_grpc_pb2_grpc
from mlp_sdk.grpc.mlp_grpc_pb2 import SimpleStatusProto
from mlp_sdk.log.setup_logging import get_logger

__default_config = pathlib.Path(__file__).parent / "config.yml"

CONFIG = yaml.safe_load(open(os.environ.get("MLP_CONFIG_FILE", __default_config)))
SDK_VERSION = 1

MlpResponseHeaders = threading.local()


class MlpServiceConnector:
    def __init__(self, url, sdk, grpc_secure=True, config=CONFIG):
        self.url = url
        self.sdk = sdk
        self.config = config
        self.grpc_secure = grpc_secure
        self.state = State.idle
        self.log = get_logger(f"MlpServiceConnector-{url}")
        self.heartbeat_thread_interval = None
        self.last_heartbeat_from_gate = None
        self.heartbeat_thread = None
        self.service_info = None
        self.action_to_gate_queue = queue.Queue()
        self.stopping_event = None
        self.channel = None
        self.stub = None
        self.shutdown_event = threading.Event()
        self.startup_thread = threading.Thread(target=self.__connect_to_gate)
        self.gateway_permanently_unavailable = True

    def start(self):
        self.log.info("Starting ...")
        self.startup_thread.start()

    @staticmethod
    def __startup_probe():
        with open("/tmp/startup-probe", "w") as f:
            f.write(str(int(time.time())))

    @staticmethod
    def __liveness_probe():
        with open("/tmp/liveness-probe", "w") as f:
            f.write(str(int(time.time())))

    def __connect_to_gate(self):
        self.__startup_probe()
        self.state = State.connecting
        self.log.info(" ... connecting to gate")
        while self.state == State.connecting:
            try:
                if self.grpc_secure:
                    if os.environ.keys().__contains__("GRPC_SSL_CA_FILE_PATH"):
                        with open(os.environ["GRPC_SSL_CA_FILE_PATH"], "rb") as f:
                            creds = grpc.ssl_channel_credentials(f.read())
                    else:
                        creds = grpc.ssl_channel_credentials()

                    self.channel = grpc.secure_channel(
                        self.url,
                        creds,
                        options=[
                            ("grpc.max_send_message_length", self.config["grpc"]["max_send_message_length"]),
                            ("grpc.max_receive_message_length", self.config["grpc"]["max_receive_message_length"]),
                        ],
                    )
                else:
                    self.channel = grpc.insecure_channel(
                        self.url,
                        options=[
                            ("grpc.max_send_message_length", self.config["grpc"]["max_send_message_length"]),
                            ("grpc.max_receive_message_length", self.config["grpc"]["max_receive_message_length"]),
                        ],
                    )
                self.stub = mlp_grpc_pb2_grpc.GateStub(self.channel)

                self.stub.healthCheck(mlp_grpc_pb2.HeartBeatProto())

                self.state = State.connected
                self.gateway_permanently_unavailable = False
                break
            except _InactiveRpcError:
                seconds = self.config["sdk"]["shutdown_event_timeout_seconds"]
                if self.gateway_permanently_unavailable:
                    self.log.debug(f"Cannot connect to {self.url} retry in {seconds} sec")
                self.gateway_permanently_unavailable = True

            except Exception as e:
                self.log.debug("Cannot connect to " + self.url + " " + type(e).__name__)
                self.log.debug(e, exc_info=True)

            self.shutdown_event.wait(self.config["sdk"]["shutdown_event_timeout_seconds"])

        if self.state == State.connected:
            try:
                self.__start_streaming()
            except Exception as e:
                self.log.error("Exception in streaming procedure " + type(e).__name__)
                self.log.error(e, exc_info=True)

    def __start_streaming(self):
        self.log.debug(" ... init streaming")
        self.stopping_event = threading.Event()

        def action_to_gate_generator():
            while True:
                msg = self.action_to_gate_queue.get()
                self.action_to_gate_queue.task_done()
                yield msg
                if msg.WhichOneof("body") == "stopServing":
                    return

        gate_to_action_generator = self.stub.processAsync(action_to_gate_generator())

        self.log.debug(" ... start serving")
        self.action_to_gate_queue.put_nowait(
            mlp_grpc_pb2.ServiceToGateProto(
                startServing=mlp_grpc_pb2.StartServingProto(
                    connectionToken=self.sdk.connection_token,
                    serviceDescriptor=self.sdk.descriptor,
                    hostname=os.environ.get("HOSTNAME", ""),
                    version=SDK_VERSION,
                    image=os.environ.get("IMAGE_NAME", ""),
                )
            )
        )

        self.log.info("Service is ready to serve!")

        self.state = State.serving
        self.__start_processing_requests_from_queue(gate_to_action_generator)

        self.log.info("Streaming thread stopped")
        if self.state != State.error:
            self.state = State.stopped
        self.stopping_event.set()

    def __start_processing_requests_from_queue(self, gate_to_action_generator):
        try:
            for request in gate_to_action_generator:
                self.__process_request(request)

        except _MultiThreadedRendezvous as e:
            # noinspection PyProtectedMember
            if e._state.code == grpc.StatusCode.CANCELLED:
                self.log.error("Channel closed. (Got StatusCode.CANCELLED exception)")
            elif e._state.code == grpc.StatusCode.UNAVAILABLE:
                self.log.error("... can't connect. (Got StatusCode.UNAVAILABLE exception)")
                if self.state == State.serving:
                    self.sdk.restart(self)
            else:
                self.log.error("Unknown MultiThreadedRendezvous exception")
                self.log.error(e, exc_info=True)

        except BaseException as e:
            self.log.error("Exception in action_to_gate_generator loop")
            self.log.error(e, exc_info=True)

    def __process_request(self, request):
        req_type = request.WhichOneof("body")
        if req_type != "heartBeat":
            self.__log_request(request)
        if req_type is None:
            self.log.error("Request with empty body", extra={"requestId": request.requestId})
        elif req_type == "serviceInfo":
            self.sdk.service_info = request.serviceInfo
        elif req_type == "heartBeat":
            self.last_heartbeat_from_gate = time.time()

            if self.heartbeat_thread is None:
                self.log.debug(" ... starting heartbeats", extra={"requestId": request.requestId})
                self.heartbeat_thread_interval = request.heartBeat.interval
                self.heartbeat_thread = threading.Thread(target=self.__heartbeat_proc)
                self.heartbeat_thread.start()
        elif req_type == "cluster":
            if self.url != request.cluster.currentServer:
                self.url = request.cluster.currentServer
            self.sdk.update_connectors(request.cluster.servers)
        elif req_type == "stopServing":
            self.log.info("Received stopServing from gate.")
            self.stop()
        elif req_type in ["predict", "fit", "ext", "batch"]:
            self.sdk.process_request_async(req_type, request, self)
        else:
            self.sdk.handle_unknown_request(req_type, request, self)

    def __log_request(self, request):
        stringified_request = json_format.MessageToJson(request, ensure_ascii=False)
        requestId = request.headers["Z-requestId"] if "Z-requestId" in request.headers else request.requestId
        if len(stringified_request) < self.config["sdk"]["large_body_length"]:
            self.log.debug("Request: " + stringified_request, extra={"requestId": requestId})
        else:
            self.log.debug("Request with large body. Id=" + str(request.requestId), extra={"requestId": requestId})

    def __heartbeat_proc(self):
        while self.state == State.connected or self.state == State.serving:
            self.action_to_gate_queue.put_nowait(
                mlp_grpc_pb2.ServiceToGateProto(heartBeat=mlp_grpc_pb2.HeartBeatProto())
            )
            self.shutdown_event.wait(self.heartbeat_thread_interval / 1000)

            if time.time() - self.last_heartbeat_from_gate > (self.heartbeat_thread_interval / 1000 * 3 + 1):
                self.log.error("No heartbeats from gate")
            self.__liveness_probe()

    def stop(self, state="stopping"):
        self.state = state

        self.log.info(" ... stop serving")
        self.action_to_gate_queue.put_nowait(
            mlp_grpc_pb2.ServiceToGateProto(stopServing=mlp_grpc_pb2.StopServingProto())
        )

        # waiting for close
        if self.stopping_event is not None:
            self.stopping_event.wait(self.config["sdk"]["stopping_event_timeout_seconds"])

        self.shutdown_event.set()
        if self.channel is not None:
            self.channel.close()
        if self.startup_thread is not None and threading.current_thread() != self.startup_thread:
            self.startup_thread.join(self.config["sdk"]["startup_thread_timeout_seconds"])
        if self.heartbeat_thread is not None:
            self.heartbeat_thread.join(self.config["sdk"]["heartbeat_thread_timeout_seconds"])


class MlpServiceSDK:
    def __init__(self, config=CONFIG):
        self.config = config
        self.log = get_logger("MlpServiceSDK")
        self.state = State.idle
        self.gate_urls: str = ""
        self.grpc_secure: bool = True
        self.connectors = list()  # noqa: C408
        self.client_api_url: str = ""
        self.client_api_token: str = ""
        self.connectors_lock = threading.Lock()
        self.connection_token: str = ""

        self.requests_executor = ThreadPoolExecutor(max_workers=self.config["sdk"]["requests_executor_pool_size"])

        self.impl = None
        self.schema = None
        self.descriptor = None
        self.shutdown_event = threading.Event()

    def register_impl(self, impl):
        self.impl = impl
        self.descriptor = impl.get_descriptor()
        # TODO: assert that descriptor is ServiceDescriptorProto type

    def start(self, url=None, connection_token=None, api_url=None, grpc_secure: Optional[bool] = None, api_token=None):
        self.log.info("Starting ...")

        self.gate_urls = os.environ.get("MLP_GRPC_HOSTS", os.environ["MLP_GRPC_HOST"]).split(",") if not url else url
        self.connection_token = os.environ["MLP_SERVICE_TOKEN"] if not connection_token else connection_token
        self.client_api_url = os.environ.get("MLP_REST_URL", None) if not api_url else api_url
        self.client_api_token = os.environ.get("MLP_CLIENT_TOKEN", None) if not api_token else api_token
        self.grpc_secure = (
            os.environ.get("MLP_GRPC_SECURE", "true").lower() == "true" if not grpc_secure else grpc_secure
        )

        with self.connectors_lock:
            for url in self.gate_urls:
                self.__start_connector(url)

        self.state = State.serving
        self.__start_keep_connection_thread()

    def __start_connector(self, url):
        connector = MlpServiceConnector(url, self, self.grpc_secure)
        self.connectors.append(connector)
        connector.start()

    def __stop_connector(self, connector: MlpServiceConnector, state: Optional[str] = None):
        if not state:
            connector.stop()
        else:
            connector.stop(state=state)  # TODO confirm
        self.connectors.remove(connector)

    def __start_keep_connection_thread(self):
        def body():
            last_active_time = time.time()
            while self.state == State.serving:
                time.sleep(1)

                self.connectors = [c for c in self.connectors if c.state not in (State.stopped, State.error)]

                if any(c.state == State.connected or c.state == State.serving for c in self.connectors):
                    last_active_time = time.time()
                    continue

                if len(self.connectors) == 0 or time.time() > last_active_time + 10:
                    self.log.warning("Service is not connected to gate: " + str(self.gate_urls))
                    self.update_connectors(self.gate_urls)
                    last_active_time = time.time()

        keep_connection_thread = threading.Thread(target=body)
        keep_connection_thread.start()

    def update_connectors(self, servers):
        with self.connectors_lock:
            # 1. compare with what we know
            current_urls = set(map(lambda x: x.url, self.connectors))  # noqa: C417
            new_urls = set(servers)
            if current_urls == new_urls:
                return

            # 2. start new
            urls_to_add = new_urls - current_urls
            if len(urls_to_add) > 0:
                self.log.info("Starting new connections: " + str(urls_to_add))
            for url in urls_to_add:
                self.__start_connector(url)

            # 3. remove obsolete
            urls_to_remove = current_urls - new_urls
            if len(urls_to_remove) > 0:
                self.log.info("Stopping connections: " + str(urls_to_remove))
            for url in urls_to_remove:
                connector = list(filter(lambda x: x.url == url, self.connectors))[0]
                threading.Thread(target=self.__stop_connector(connector)).start()

    def restart(self, connector):
        with self.connectors_lock:
            self.__stop_connector(connector, "error")

            self.log.info("Restarting ...")
            self.__start_connector(connector.url)

    def block_until_shutdown(self):
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        self.shutdown_event.wait()

    def shutdown(self, _signo=None, _stack_frame=None):
        if self.state == State.stopping:
            return

        self.log.info("Shutdown")
        self.state = State.stopping

        shutdown_deadline = time.time() + self.config["sdk"]["action_shutdown_timeout_seconds"]
        connectors = self.connectors.copy()
        for connector in connectors:
            connector.stop()
        for connector in connectors:
            connector.shutdown_event.wait(shutdown_deadline - time.time())
        self.shutdown_event.set()

    def handle_unknown_request(self, req_type, request, connector: MlpServiceConnector):
        self.log.error("Unknown request type " + req_type, extra={"requestId": request.requestId})
        self.log.error(request, extra={"requestId": request.requestId})
        response = mlp_grpc_pb2.ServiceToGateProto(
            error=mlp_grpc_pb2.ApiErrorProto(
                code="mlp-action.common.internal-error",
                message=f"Unknown request type: {req_type}",
                status=mlp_grpc_pb2.INTERNAL_SERVER_ERROR,
            )
        )
        response.requestId = request.requestId
        self.__log_response(request, response)
        connector.action_to_gate_queue.put_nowait(response)

    def process_request_async(self, req_type, request, connector: MlpServiceConnector):
        self.requests_executor.submit(self.__try_to_process_request, req_type, request, connector)

    def __try_to_process_request(self, req_type, request, connector: MlpServiceConnector):
        _t0 = time.perf_counter()

        try:
            response = self.__process_request(req_type, request)
        except MlpException as e:
            self.log.exception(e, extra={"requestId": request.requestId})
            response = mlp_grpc_pb2.ServiceToGateProto(
                error=mlp_grpc_pb2.ApiErrorProto(
                    code=e.code if e.code is not None else "mlp-action.common.internal-error",
                    message=e.message,
                    status=e.status,
                    args=e.source_error_data,
                )
            )
        except Exception as e:
            self.log.exception(e, extra={"requestId": request.requestId})
            response = mlp_grpc_pb2.ServiceToGateProto(
                error=mlp_grpc_pb2.ApiErrorProto(
                    code="mlp-action.common.processing-exception",
                    message=str(e),
                    status=mlp_grpc_pb2.INTERNAL_SERVER_ERROR,
                )
            )

        _elapsed = round((time.perf_counter() - _t0) * 1000)  # to ms and round mathematically

        response.requestId = request.requestId
        response.headers["Z-Server-Time"] = f"{_elapsed}"

        self.__log_response(request, response)
        connector.action_to_gate_queue.put_nowait(response)

    def __log_response(self, request, response):
        stringified_response = json_format.MessageToJson(response, ensure_ascii=False)
        requestId = request.headers["Z-requestId"] if "Z-requestId" in request.headers else request.requestId
        if len(stringified_response) < self.config["sdk"]["large_body_length"]:
            self.log.debug("Response: " + stringified_response, extra={"requestId": requestId})
        else:
            self.log.debug("Response with large body. Id=" + str(request.requestId), extra={"requestId": requestId})

    def __process_request(self, req_type, request):
        self.__setup_headers(request)
        if req_type == "predict":
            result = self.__handle_predict(request.predict)
            headers = {k: str(v) for k, v in MlpResponseHeaders.headers.items()}
            return mlp_grpc_pb2.ServiceToGateProto(predict=result, headers=headers)
        elif req_type == "fit":
            result = self.__handle_fit(request.fit)
            headers = {k: str(v) for k, v in MlpResponseHeaders.headers.items()}
            return mlp_grpc_pb2.ServiceToGateProto(fit=result, headers=headers)
        elif req_type == "ext":
            result = self.__handle_ext(request.ext)
            return mlp_grpc_pb2.ServiceToGateProto(ext=result)
        elif req_type == "batch":
            result = self.__handle_predict_batch(request.batch)
            return mlp_grpc_pb2.ServiceToGateProto(batch=result)
        else:
            raise ValueError("Unexpected request type: " + req_type)

    def __setup_headers(self, request):
        global MlpResponseHeaders
        MlpResponseHeaders.__dict__.clear()
        MlpResponseHeaders.headers = {}
        MlpResponseHeaders.batch_headers = {}

        if "Z-requestId" in request.headers:
            MlpResponseHeaders.headers["Z-requestId"] = str(request.headers["Z-requestId"])
        else:
            MlpResponseHeaders.headers["Z-requestId"] = str(request.requestId)

        if "MLP-BILLING-KEY" in request.headers:
            MlpResponseHeaders.headers["MLP-BILLING-KEY"] = str(request.headers["MLP-BILLING-KEY"])

    def __handle_predict(self, req):
        is_json = req.data.WhichOneof("body") == "json"
        desc = self.descriptor.methods["predict"]
        data = self.__convert_from_proto(req.data, desc.input["data"].type, is_json, self.impl, "predict", "data")
        if "config" in desc.input:
            config = self.__convert_from_proto(
                req.config, desc.input["config"].type, is_json, self.impl, "predict", "config"
            )
        else:
            config = None

        self.log.debug(f"Config: {config}")

        if not hasattr(self.impl, "predict"):
            raise NotImplementedError("Predict requests are not supported by this action")

        prediction = self.impl.predict(data, config)
        response = self.__convert_to_proto(prediction, desc.output.type, is_json)
        return mlp_grpc_pb2.PredictResponseProto(data=response)

    def __handle_fit(self, req):
        is_json = req.trainData.WhichOneof("body") == "json"
        desc = self.descriptor.methods["fit"]
        train = self.__convert_from_proto(
            req.trainData, desc.input["train_data"].type, is_json, self.impl, "fit", "train_data"
        )
        targets = self.__convert_from_proto(
            req.targetsData, desc.input["targets"].type, is_json, self.impl, "fit", "targets"
        )
        config = self.__convert_from_proto(req.config, desc.input["config"].type, is_json, self.impl, "fit", "config")

        target_service_info = self.__convert_from_proto(
            req.targetServiceInfo,
            desc.input["target_service_info"].type,
            False,
            self.impl,
            "fit",
            "target_service_info",
        )
        dataset_info = self.__convert_from_proto(
            req.datasetInfo, desc.input["dataset_info"].type, False, self.impl, "fit", "dataset_info"
        )

        if not hasattr(self.impl, "fit"):
            raise NotImplementedError("Fit requests are not supported by this action")

        self.impl.fit(train, targets, config, target_service_info, dataset_info, req.modelDir, req.previousModelDir)
        return mlp_grpc_pb2.FitResponseProto()

    def __handle_ext(self, req):
        is_json = True
        desc = self.descriptor.methods["ext"]

        if not hasattr(self.impl, "ext"):
            raise NotImplementedError("Ext requests are not supported by this action")

        response = self.impl.ext(req.methodName, req.params)
        converted_response = self.__convert_to_proto(response, desc.output.type, is_json)
        return mlp_grpc_pb2.ExtendedResponseProto(data=converted_response)

    def __handle_predict_batch(self, request: mlp_grpc_pb2.BatchRequestProto):
        if len(request.data) == 0:
            return mlp_grpc_pb2.BatchResponseProto(data=[])

        if not hasattr(self.impl, "predict_batch"):
            raise NotImplementedError("Batch requests are not supported by this action")

        desc = self.descriptor.methods["predict"]
        is_json = request.data[0].data.WhichOneof("body") == "json"

        self.__validate_batch_method_params(desc.input["data"].type, desc.input["config"].type)

        data_list = [self.__convert_batch_from_proto(r.data, is_json, "data") for r in request.data]
        config = self.__convert_batch_from_proto(request.config, is_json, "config")

        res_list = self.impl.predict_batch(data_list, config)

        if len(res_list) != len(data_list):
            raise RuntimeError("predict_batch method must return list of the same size as input list")

        responses_protos = []

        for index, result in enumerate(res_list):
            converted = self.__convert_to_proto(result, desc.output.type, is_json)
            request_id = request.data[index].requestId
            proto = mlp_grpc_pb2.BatchPayloadResponseProto(
                requestId=request_id,
                predict=mlp_grpc_pb2.PredictResponseProto(data=converted),
                headers=MlpResponseHeaders.batch_headers.get(index),
            )
            responses_protos.append(proto)

        return mlp_grpc_pb2.BatchResponseProto(data=responses_protos)

    def __convert_from_proto(self, payload, payload_type, is_json, action_impl, method, arg):
        class_ = signature(getattr(action_impl, method)).parameters[arg].annotation
        if class_ is None:
            return None

        name = class_.__name__ if hasattr(class_, "__name__") else class_._name
        if name == "PayloadProto":
            return payload

        if name != payload_type:
            self.log.error(
                "Types don't match. Type in ServiceDescriptor: " + payload_type + ", type in implementation: " + name
            )
        try:
            if is_json:
                if hasattr(class_, "parse_raw"):
                    converted = class_.parse_raw(payload.json)
                else:
                    converted = json_format.Parse(payload.json, class_())
            else:
                converted = class_.parse_raw(json_format.MessageToJson(payload))
        except ValidationError as ex:
            args = {"message": str(ex)}
            raise MlpException.create(CommonErrorCode.BAD_REQUEST, args)  # noqa: B904

        return converted

    def __validate_batch_method_params(self, predict_data_type, predict_config_type):
        method = "predict_batch"

        data_annotation = signature(getattr(self.impl, method)).parameters["data"].annotation
        config_annotation = signature(getattr(self.impl, method)).parameters["config"].annotation

        if typing.get_origin(data_annotation).__name__ != "list":
            self.log.error(f"Batch method should have list as first argument. Found {data_annotation}")

        if typing.get_origin(config_annotation) is not None and typing.get_origin(config_annotation).__name__ != "list":
            self.log.error(f"Batch method should have list as second argument. Found {config_annotation}")

        data_type = typing.get_args(data_annotation)[0]

        if data_type.__name__ != predict_data_type:
            self.log.error(
                f"Types don't match. Type in ServiceDescriptor: {predict_data_type}, "
                + f"type in implementation: {data_type.__name__}"
            )

        if len(typing.get_args(config_annotation)) > 0:
            config_type = typing.get_args(config_annotation)[0]
        else:
            config_type = None

        if config_type is not None and config_type.__name__ != predict_config_type:
            self.log.error(
                f"Types don't match. Type in ServiceDescriptor: {predict_config_type}, "
                + f"type in implementation: {config_type.__name__}"
            )

    def __convert_batch_from_proto(self, payload, is_json, arg):
        if not payload.HasField("json") and not payload.HasField("protobuf"):
            return None

        method = "_predict_batch" if hasattr(self.impl, "_predict_batch") else "predict_batch"

        args = typing.get_args(signature(getattr(self.impl, method)).parameters[arg].annotation)
        class_ = args[0] if len(args) > 0 else None
        if class_ is None or class_.__name__ == "NoneType":
            return None

        if is_json:
            if hasattr(class_, "parse_raw"):
                converted = class_.parse_raw(payload.json)
            else:
                converted = json_format.Parse(payload.json, class_())
        else:
            converted = class_().ParseFromString(payload.protobuf)
        return converted

    @staticmethod
    def __convert_to_proto(data, payload_type, is_json):
        if hasattr(data, "DESCRIPTOR") and data.DESCRIPTOR.name == "PayloadProto":
            return data

        res = mlp_grpc_pb2.PayloadProto(dataType=payload_type)
        if payload_type is None or payload_type == "null":
            return res
        if is_json:
            if hasattr(data, "json"):
                res.json = data.json()
            else:
                res.json = json_format.MessageToJson(data)
        else:
            res.protobuf = bytes(data)
        return res


@dataclass
class MlpErrorCode:
    code: str
    message: str
    status: SimpleStatusProto


class MlpException(Exception):
    def __init__(
        self,
        message: str,
        code: Optional[str] = None,
        status: SimpleStatusProto = SimpleStatusProto.INTERNAL_SERVER_ERROR,
        source_error_data: typing.Dict[str, str] = None,
    ):
        self.message = message
        self.code = code
        self.status = status
        self.source_error_data = source_error_data

    @staticmethod
    def create(mlp_error_code: MlpErrorCode, args: typing.Dict[str, str] = None):
        return MlpException(mlp_error_code.message, mlp_error_code.code, mlp_error_code.status, args)

    def __str__(self):
        return f"MlpException {self.message} has been raised"


class CommonErrorCode:
    INTERNAL_ERROR = MlpErrorCode(
        "mlp-action.common.internal-error",
        "Internal error. Message: {message}",
        SimpleStatusProto.INTERNAL_SERVER_ERROR,
    )

    BAD_REQUEST = MlpErrorCode("mlp-action.common.bad-request", "Bad request", SimpleStatusProto.BAD_REQUEST)

    PROCESSING_EXCEPTION = MlpErrorCode(
        "mlp-action.common.processing-exception",
        "Something went wrong during processing the request",
        SimpleStatusProto.INTERNAL_SERVER_ERROR,
    )

    REQUEST_TYPE_NOT_SUPPORTED = MlpErrorCode(
        "mlp-action.common.method-not-supported",
        "{type} requests are not supported by this action",
        SimpleStatusProto.BAD_REQUEST,
    )
    PARTIAL_RESPONSE_NOT_SUPPORTED_IN_BATCH = MlpErrorCode(
        "mlp-action.common.no-partial-in-batch",
        "Partial response can not be used in batch",
        SimpleStatusProto.BAD_REQUEST,
    )
    RAW_PAYLOAD_NOT_SUPPORTED_IN_BATCH = MlpErrorCode(
        "mlp-action.common.no-raw-payload-in-batch",
        "Raw payload can not be used in batch",
        SimpleStatusProto.BAD_REQUEST,
    )


class State(Enum):
    idle = "idle"
    connecting = "connecting"
    connected = "connected"
    serving = "serving"
    stopping = "stopping"
    stopped = "stopped"
    error = "error"
