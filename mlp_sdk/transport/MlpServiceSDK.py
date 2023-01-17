import logging
import os
import pathlib
import queue
import sched
import signal
import sys
import threading
import time
import typing
from concurrent.futures import Future, ThreadPoolExecutor
from enum import Enum
from inspect import signature
from typing import Optional

import grpc
import yaml
from google.protobuf import json_format
from grpc._channel import _MultiThreadedRendezvous, _InactiveRpcError

from mlp_api import Configuration, ApiClient
from mlp_sdk.grpc import mlp_grpc_pb2, mlp_grpc_pb2_grpc

__default_config = pathlib.Path(__file__).parent / "config.yml"

CONFIG = yaml.safe_load(open(os.environ.get("MLP_CONFIG_FILE", __default_config)))

logging.basicConfig(format=CONFIG["logging"]["format"],
                    level=logging.getLevelName(CONFIG["logging"]["level"]),
                    stream=sys.stdout)


class MlpServiceConnector:

    def __init__(self, url, sdk, grpc_secure=True):
        self.url = url
        self.sdk = sdk
        self.grpc_secure = grpc_secure
        self.state = State.idle
        self.log = logging.getLogger(f'MlpServiceConnector-{url}')
        self.heartbeat_thread_interval = None
        self.last_heartbeat_from_gate = None
        self.heartbeat_thread = None
        self.action_to_gate_queue = queue.Queue()
        self.stopping_event = None
        self.channel = None
        self.stub = None
        self.shutdown_event = threading.Event()
        self.startup_thread = threading.Thread(target=self.__connect_to_gate)

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
                        with open(os.environ["GRPC_SSL_CA_FILE_PATH"], 'rb') as f:
                            creds = grpc.ssl_channel_credentials(f.read())
                    else:
                        creds = grpc.ssl_channel_credentials()

                    self.channel = grpc.secure_channel(self.url, creds, options=[
                        ('grpc.max_send_message_length', CONFIG["grpc"]["max_send_message_length"]),
                        ('grpc.max_receive_message_length', CONFIG["grpc"]["max_receive_message_length"])
                    ])
                else:
                    self.channel = grpc.insecure_channel(self.url, options=[
                        ('grpc.max_send_message_length', CONFIG["grpc"]["max_send_message_length"]),
                        ('grpc.max_receive_message_length', CONFIG["grpc"]["max_receive_message_length"])
                    ])
                self.stub = mlp_grpc_pb2_grpc.GateStub(self.channel)

                self.stub.healthCheck(mlp_grpc_pb2.HeartBeatProto())

                self.state = State.connected
                break
            except _InactiveRpcError:
                self.log.info("Cannot connect to " + self.url + " retry in 3 sec")

            except Exception as e:
                self.log.info("Cannot connect to " + self.url + " " + type(e).__name__)
                self.log.info(e, exc_info=True)

            self.shutdown_event.wait(CONFIG["sdk"]["shutdown_event_timeout_seconds"])

        if self.state == State.connected:
            try:
                self.__start_streaming()
            except Exception as e:
                self.log.error("Exception in streaming procedure " + type(e).__name__)
                self.log.error(e, exc_info=True)

    def __start_streaming(self):
        self.log.info(" ... init streaming")
        self.stopping_event = threading.Event()

        def action_to_gate_generator():
            while True:
                msg = self.action_to_gate_queue.get()
                self.action_to_gate_queue.task_done()
                yield msg

        gate_to_action_generator = self.stub.processAsync(action_to_gate_generator())

        self.log.info(" ... start serving")
        self.action_to_gate_queue.put_nowait(mlp_grpc_pb2.ServiceToGateProto(
            startServing=mlp_grpc_pb2.StartServingProto(
                connectionToken=self.sdk.connection_token,
                serviceDescriptor=self.sdk.descriptor
            )
        ))

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
                self.log.info("Channel closed. (Got StatusCode.CANCELLED exception)")
            elif e._state.code == grpc.StatusCode.UNAVAILABLE:
                self.log.info("... can't connect. (Got StatusCode.UNAVAILABLE exception)")
                if self.state == State.serving:
                    self.sdk.restart(self)
            else:
                self.log.info("Unknown MultiThreadedRendezvous exception")
                self.log.error(e, exc_info=True)

        except BaseException as e:
            self.log.error("Exception in action_to_gate_generator loop")
            self.log.error(e, exc_info=True)

    def __process_request(self, request):
        req_type = request.WhichOneof('body')
        if req_type != 'heartBeat':
            self.__log_request(request)
        if req_type is None:
            self.log.error("Request with empty body")
        elif req_type == 'serviceInfo':
            self.sdk.pipeline_client.service_info = request.serviceInfo
        elif req_type == 'heartBeat':
            self.last_heartbeat_from_gate = time.time()

            if self.heartbeat_thread is None:
                self.log.info(" ... starting heartbeats")
                self.heartbeat_thread_interval = request.heartBeat.interval
                self.heartbeat_thread = threading.Thread(target=self.__heartbeat_proc)
                self.heartbeat_thread.start()
        elif req_type == 'cluster':
            if self.url != request.cluster.currentServer:
                self.url = request.cluster.currentServer
            self.sdk.update_connectors(request.cluster.servers)
        elif req_type in ['predict', 'fit', 'ext', 'batch']:
            self.sdk.process_request_async(req_type, request, self)
        elif req_type == 'response':
            self.sdk.pipeline_client.registry_response(request.requestId, request.response)
        else:
            self.sdk.handle_unknown_request(req_type, request, self)

    def __log_request(self, request):
        stringified_request = str(request)
        if len(stringified_request) < CONFIG["sdk"]["large_body_length"]:
            self.log.info("Request: " + stringified_request)
        else:
            self.log.info("Request with large body. Id=" + str(request.requestId))

    def __heartbeat_proc(self):
        while self.state == State.connected or self.state == State.serving:
            self.action_to_gate_queue.put_nowait(mlp_grpc_pb2.ServiceToGateProto(
                heartBeat=mlp_grpc_pb2.HeartBeatProto()
            ))
            self.shutdown_event.wait(self.heartbeat_thread_interval / 1000)

            if time.time() - self.last_heartbeat_from_gate > (self.heartbeat_thread_interval / 1000 * 3 + 1):
                self.log.error("No heartbeats from gate")
            self.__liveness_probe()

    def stop(self, state='stopping'):
        self.state = state

        self.log.info(" ... stop serving")
        self.action_to_gate_queue.put_nowait(mlp_grpc_pb2.ServiceToGateProto(
            stopServing=mlp_grpc_pb2.StopServingProto()
        ))

        # waiting for close
        if self.stopping_event is not None:
            self.stopping_event.wait(CONFIG["sdk"]["stopping_event_timeout_seconds"])

        self.shutdown_event.set()
        if self.channel is not None:
            self.channel.close()
        if self.startup_thread is not None and threading.current_thread() != self.startup_thread:
            self.startup_thread.join(CONFIG["sdk"]["startup_thread_timeout_seconds"])
        if self.heartbeat_thread is not None:
            self.heartbeat_thread.join(CONFIG["sdk"]["heartbeat_thread_timeout_seconds"])


class MlpServiceSDK:

    def __init__(self):
        self.log = logging.getLogger('MlpServiceSDK')
        self.state = State.idle
        self.gate_urls: str = ''
        self.grpc_secure: bool = True
        self.connectors = list()
        self.client_api_url: str = ''
        self.connectors_lock = threading.Lock()
        self.pipeline_client = PipelineClient(self)
        self.connection_token: str = ''

        self.requests_executor = ThreadPoolExecutor(max_workers=CONFIG["sdk"]["requests_executor_pool_size"])

        self.impl = None
        self.schema = None
        self.descriptor = None

    def register_impl(self, impl):
        self.impl = impl
        self.descriptor = impl.get_descriptor()
        # TODO: assert that descriptor is ServiceDescriptorProto type

    def start(self, url=None, connection_token=None, api_url=None, grpc_secure: Optional[bool] = None):
        self.log.info("Starting ...")

        self.gate_urls = os.environ['MLP_GRPC_HOST'].split(",") if not url else url
        self.connection_token = os.environ['MLP_SERVICE_TOKEN'] if not connection_token else connection_token
        self.client_api_url = os.environ.get('MLP_REST_URL', None) if not api_url else api_url
        self.grpc_secure = os.environ.get('MLP_GRPC_SECURE',
                                          'true').lower() == 'true' if not grpc_secure else grpc_secure

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

                if time.time() > last_active_time + 10:
                    self.log.info("Service is not connected to gate: " + str(self.gate_urls))
                    self.update_connectors(self.gate_urls)
                    last_active_time = time.time()

        keep_connection_thread = threading.Thread(target=body)
        keep_connection_thread.start()

    def update_connectors(self, servers):
        with self.connectors_lock:
            # 1. compare with what we know
            current_urls = set(map(lambda x: x.url, self.connectors))
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
            self.__stop_connector(connector, 'error')

            self.log.info("Restarting ...")
            self.__start_connector(connector.url)

    def block_until_shutdown(self):
        barrier = threading.Event()

        # TODO think about lock
        def shutdown(_signo, _stack_frame):
            self.log.info("Shutdown")
            self.state = State.stopping
            for connector in self.connectors:
                connector.stop()
            barrier.set()

        signal.signal(signal.SIGINT, shutdown)
        signal.signal(signal.SIGTERM, shutdown)
        barrier.wait(CONFIG["sdk"]["action_shutdown_timeout_seconds"])

    def handle_unknown_request(self, req_type, request, connector: MlpServiceConnector):
        self.log.error("Unknown request type " + req_type)
        self.log.error(request)
        response = mlp_grpc_pb2.ServiceToGateProto(
            error=mlp_grpc_pb2.ApiErrorProto(
                code='mlp-action.common.internal-error',
                message=f'Unknown request type: {req_type}',
                status=mlp_grpc_pb2.INTERNAL_SERVER_ERROR
            )
        )
        response.requestId = request.requestId
        self.__log_response(request, response)
        connector.action_to_gate_queue.put_nowait(response)

    def process_request_async(self, req_type, request, connector: MlpServiceConnector):
        self.requests_executor.submit(self.__try_to_process_request, req_type, request, connector)

    def __try_to_process_request(self, req_type, request, connector: MlpServiceConnector):
        try:
            response = self.__process_request(req_type, request)
        except MlpException as e:
            self.log.exception(e)
            response = mlp_grpc_pb2.ServiceToGateProto(
                error=mlp_grpc_pb2.ApiErrorProto(
                    code=e.code if e.code is not None else 'mlp-action.common.internal-error',
                    message=f'Internal error. Message: {e.message}',
                    status=mlp_grpc_pb2.INTERNAL_SERVER_ERROR
                )
            )
        except Exception as e:
            self.log.exception(e)
            response = mlp_grpc_pb2.ServiceToGateProto(
                error=mlp_grpc_pb2.ApiErrorProto(
                    code="mlp-action.common.processing-exception",
                    message=str(e),
                    status=mlp_grpc_pb2.INTERNAL_SERVER_ERROR
                )
            )
        response.requestId = request.requestId
        self.__log_response(request, response)
        connector.action_to_gate_queue.put_nowait(response)

    def __log_response(self, request, response):
        stringified_response = str(response)
        if len(stringified_response) < CONFIG["sdk"]["large_body_length"]:
            self.log.info("Response: " + stringified_response)
        else:
            self.log.info("Response with large body. Id=" + str(request.requestId))

    def __process_request(self, req_type, request):
        if req_type == 'predict':
            result = self.__handle_predict(request.predict)
            return mlp_grpc_pb2.ServiceToGateProto(predict=result)
        elif req_type == 'fit':
            result = self.__handle_fit(request.fit)
            return mlp_grpc_pb2.ServiceToGateProto(fit=result)
        elif req_type == 'ext':
            result = self.__handle_ext(request.ext)
            return mlp_grpc_pb2.ServiceToGateProto(ext=result)
        elif req_type == 'batch':
            result = self.__handle_predict_batch(request.batch)
            return mlp_grpc_pb2.ServiceToGateProto(batch=result)
        else:
            raise ValueError('Unexpected request type: ' + req_type)

    def __handle_predict(self, req):
        is_json = req.data.WhichOneof('body') == 'json'
        desc = self.descriptor.methods['predict']
        self.log.info(f"Descriptor: {desc}")
        self.log.info(f"Descriptor.input: {desc.input}")
        self.log.info(f"Descriptor.input type: {type(desc.input)}")
        data = self.__convert_from_proto(req.data, desc.input['data'].type, is_json, self.impl, 'predict', 'data')
        self.log.info(f"Data: {data}")
        if hasattr(desc.input, 'config'):
            config = self.__convert_from_proto(
                req.config, desc.input['config'].type, is_json, self.impl, 'predict', 'config')
        else:
            config = None

        self.log.info(f"Config: {config}")

        if not hasattr(self.impl, 'predict'):
            raise NotImplementedError('Predict requests are not supported by this action')

        prediction = self.impl.predict(data, config)
        response = self.__convert_to_proto(prediction, desc.output.type, is_json)
        return mlp_grpc_pb2.PredictResponseProto(data=response)

    def __handle_fit(self, req):
        is_json = req.trainData.WhichOneof('body') == 'json'
        desc = self.descriptor.methods['fit']
        train = self.__convert_from_proto(
            req.trainData, desc.input['train_data'].type, is_json, self.impl, 'fit', 'train_data')
        targets = self.__convert_from_proto(
            req.targetsData, desc.input['targets'].type, is_json, self.impl, 'fit', 'targets')
        config = self.__convert_from_proto(req.config, desc.input['config'].type, is_json, self.impl, 'fit', 'config')

        if not hasattr(self.impl, 'fit'):
            raise NotImplementedError('Fit requests are not supported by this action')

        self.impl.fit(train, targets, config, req.modelDir, req.previousModelDir)
        return mlp_grpc_pb2.FitResponseProto()

    def __handle_ext(self, req):
        converted_requests = {}
        is_json = True
        desc = self.descriptor.methods['ext.' + req.methodName]

        if len(list(req.params)) > 0:
            first_key = list(req.params)[0]
            is_json = req.params[first_key].WhichOneof('body') == 'json'

            for key in desc.input.keys():
                converted_requests[key] = self.__convert_from_proto(
                    req.params[key], desc.input[key].type, is_json, self.impl, "ext", key)

        if not hasattr(self.impl, 'ext'):
            raise NotImplementedError('Ext requests are not supported by this action')

        response = self.impl.ext(req.methodName, converted_requests)
        converted_response = self.__convert_to_proto(response, desc.output.type, is_json)
        return mlp_grpc_pb2.ExtendedResponseProto(data=converted_response)

    def __handle_predict_batch(self, request: mlp_grpc_pb2.BatchRequestProto):
        if len(request.data) == 0:
            return mlp_grpc_pb2.BatchResponseProto(data=[])

        if not hasattr(self.impl, 'predict_batch'):
            raise NotImplementedError('Batch requests are not supported by this action')

        desc = self.descriptor.methods['predict']
        is_json = request.data[0].data.WhichOneof('body') == 'json'

        self.__validate_batch_method_params(desc.input['data'].type, desc.input['config'].type)

        data_list = [self.__convert_batch_from_proto(r.data, is_json, 'data') for r in request.data]
        config = self.__convert_batch_from_proto(request.config, is_json, 'config')

        res_list = self.impl.predict_batch(data_list, config)

        if len(res_list) != len(data_list):
            raise RuntimeError('predict_batch method must return list of the same size as input list')

        responses_protos = []

        for index, result in enumerate(res_list):
            converted = self.__convert_to_proto(result, desc.output.type, is_json)
            request_id = request.data[index].requestId
            proto = mlp_grpc_pb2.BatchPayloadResponseProto(requestId=request_id,
                                                           predict=mlp_grpc_pb2.PredictResponseProto(data=converted))
            responses_protos.append(proto)

        return mlp_grpc_pb2.BatchResponseProto(data=responses_protos)

    def __convert_from_proto(self, payload, payload_type, is_json, action_impl, method, arg):
        if not payload.HasField('json') and not payload.HasField('protobuf'):
            return None

        class_ = signature(getattr(action_impl, method)).parameters[arg].annotation
        if class_ is None:
            return None

        name = class_.__name__ if hasattr(class_, '__name__') else class_._name
        if name == 'PayloadProto':
            return payload

        if name != payload_type:
            self.log.error("Types don't match. Type in ServiceDescriptor: " + payload_type
                           + ", type in implementation: " + name)

        if is_json:
            if hasattr(class_, 'parse_raw'):
                converted = class_.parse_raw(payload.json)
            else:
                converted = json_format.Parse(payload.json, class_())
        else:
            converted = class_().ParseFromString(payload.protobuf)
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
            self.log.error(f"Types don't match. Type in ServiceDescriptor: {predict_data_type}, "
                           + f"type in implementation: {data_type.__name__}")

        if len(typing.get_args(config_annotation)) > 0:
            config_type = typing.get_args(config_annotation)[0]
        else:
            config_type = None

        if config_type is not None and config_type.__name__ != predict_config_type:
            self.log.error(f"Types don't match. Type in ServiceDescriptor: {predict_config_type}, "
                           + f"type in implementation: {config_type.__name__}")

    def __convert_batch_from_proto(self, payload, is_json, arg):
        if not payload.HasField('json') and not payload.HasField('protobuf'):
            return None

        method = "_predict_batch" if hasattr(self.impl, "_predict_batch") else "predict_batch"

        args = typing.get_args(signature(getattr(self.impl, method)).parameters[arg].annotation)
        class_ = args[0] if len(args) > 0 else None
        if class_ is None or class_.__name__ == "NoneType":
            return None

        if is_json:
            if hasattr(class_, 'parse_raw'):
                converted = class_.parse_raw(payload.json)
            else:
                converted = json_format.Parse(payload.json, class_())
        else:
            converted = class_().ParseFromString(payload.protobuf)
        return converted

    @staticmethod
    def __convert_to_proto(data, payload_type, is_json):
        if hasattr(data, 'DESCRIPTOR') and data.DESCRIPTOR.name == 'PayloadProto':
            return data

        res = mlp_grpc_pb2.PayloadProto(dataType=payload_type)
        if payload_type is None or payload_type == 'null':
            return res
        if is_json:
            if hasattr(data, 'json'):
                res.json = data.json()
            else:
                res.json = json_format.MessageToJson(data)
        else:
            res.protobuf = bytes(data)
        return res


class PipelineClient:

    def __init__(self, sdk: MlpServiceSDK):
        self._last_request_id = 0
        self.active_requests = {}
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.sdk = sdk
        self._request_id_lock = threading.Lock()
        self.service_info = None
        self.client_api_token = None
        self.log = logging.getLogger('PipelineClient')

    def get_api_client(self):
        configuration = Configuration(host=self.sdk.client_api_url)
        return ApiClient(configuration, "MLP-API-KEY", self.__get_client_api_token())

    def predict(self, account: Optional[str], model: str, data: str, config: Optional[str]) -> Future:
        client_proto = self.__build_predict_request_proto(account, model, data, config)

        return self.send_request(client_proto)

    def ext(self, account: Optional[str], model: str, methodName: str, data: typing.Dict[str, typing.Any]) -> Future:
        client_proto = self.__build_ext_request_proto(account, model, methodName, data)

        return self.send_request(client_proto)

    def send_request(self, client_proto: mlp_grpc_pb2.PipelineRequestProto) -> Future:
        with self._request_id_lock:
            request_id = self._last_request_id
            self._last_request_id -= 1

        action_to_gate_proto = mlp_grpc_pb2.ServiceToGateProto(
            requestId=request_id,
            request=client_proto
        )

        sent = False
        for connector in self.sdk.connectors:
            if connector.state == State.serving:
                connector.action_to_gate_queue.put_nowait(action_to_gate_proto)
                sent = True
                break

        if not sent:
            raise RuntimeError('There is no active connector')

        future: Future = Future()
        self.active_requests[request_id] = future
        self.scheduler.enter(60, 1, self.__remove_request_future, argument=(request_id,))

        return future

    @staticmethod
    def __build_predict_request_proto(account: Optional[str], model, data, config):
        proto = mlp_grpc_pb2.PipelineRequestProto(
            model=model,
            predict=mlp_grpc_pb2.PredictRequestProto(
                data=mlp_grpc_pb2.PayloadProto(json=data),
                config=mlp_grpc_pb2.PayloadProto(json=config),
            )
        )
        if account is not None:
            proto.account = account

        return proto

    @staticmethod
    def __build_ext_request_proto(account: Optional[str], model, method_name, data):
        proto = mlp_grpc_pb2.PipelineRequestProto(
            model=model,
            ext=mlp_grpc_pb2.ExtendedRequestProto(
                methodName=method_name,
                params={k: mlp_grpc_pb2.PayloadProto(json=v) for k, v in data.items()}
            )
        )
        if account is not None:
            proto.account = account

        return proto

    @staticmethod
    def __build_token_request_proto():
        return mlp_grpc_pb2.PipelineRequestProto(
            token=mlp_grpc_pb2.ClientTokenRequestProto()
        )

    def __get_client_api_token(self):
        if self.client_api_token is not None:
            return self.client_api_token

        client_proto = self.__build_token_request_proto()

        self.client_api_token = self.send_request(client_proto).result(None).token.token
        return self.client_api_token

    def registry_response(self, request_id: int, response_proto: mlp_grpc_pb2.PipelineResponseProto):
        result_future: Future = self.active_requests.get(request_id)
        if result_future is not None:
            result_future.set_result(response_proto)

    def __remove_request_future(self, request_id: int):
        del self.active_requests[request_id]


class MlpException(Exception):
    def __init__(self, message: str, code: Optional[str] = None):
        self.message = message
        self.code = code

    def __str__(self):
        return f'MlpException {self.message} has been raised'


class State(Enum):
    idle = 'idle'
    connecting = 'connecting'
    connected = 'connected'
    serving = 'serving'
    stopping = 'stopping'
    stopped = 'stopped'
    error = 'error'