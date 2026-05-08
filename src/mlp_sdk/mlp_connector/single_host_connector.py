import os
import queue
import threading
import time
import uuid
from enum import Enum
from typing import Any, Generator, Optional

import grpc
from google.protobuf.json_format import MessageToJson

from mlp_sdk.abstract.services import MlpException
from mlp_sdk.mlp_connector.client import MlpGrpcClient
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import (
    ClusterUpdateProto,
    GateToServiceProto,
    HeartBeatProto,
    ServiceDescriptorProto,
    ServiceToGateProto,
    StartServingProto,
    StopServingProto,
)
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2_grpc import GateStub
from mlp_sdk.utils.config import get_config
from mlp_sdk.utils.json_ import JSON
from mlp_sdk.utils.logger import get_logger

log = get_logger("MlpSingleHostConnector")
config = get_config()

_PROCESS_INSTANCE_UUID = str(uuid.uuid4())
_RECONNECT_ENABLED: bool = config.sdk.reconnect_enabled

_RECONNECTABLE_GRPC_CODES: frozenset = frozenset({
    grpc.StatusCode.CANCELLED,
    grpc.StatusCode.UNAVAILABLE,
    grpc.StatusCode.DEADLINE_EXCEEDED,
    grpc.StatusCode.INTERNAL,
    grpc.StatusCode.UNKNOWN,
    grpc.StatusCode.ABORTED,
    grpc.StatusCode.RESOURCE_EXHAUSTED,
})


class MlpConnectorState(Enum):
    idle = "idle"
    connecting = "connecting"
    connected = "connected"
    serving = "serving"
    reconnecting = "reconnecting"
    stopping = "stopping"
    stopped = "stopped"
    error = "error"


class MlpSingleHostConnectorCallback:
    def cluster_update(self, message: ClusterUpdateProto): ...

    def request(self, request: GateToServiceProto, connector: "MlpSingleHostConnector"): ...


class MlpSingleHostConnector:
    SDK_VERSION = 2

    def __init__(
        self, host_port: str, grpc_secure: bool, connection_token: str, service_descriptor: ServiceDescriptorProto, callback: MlpSingleHostConnectorCallback
    ):
        self.host_port = host_port
        self.grpc_secure = grpc_secure
        self.callback = callback
        self.connection_token = connection_token
        self.service_descriptor = service_descriptor

        self.state = MlpConnectorState.idle

        self.log = get_logger(f"MlpServiceConnector-{self.host_port}")

        self.heartbeat_thread: Optional[threading.Thread] = None
        self.heartbeat_thread_interval_from_gate_ms: Optional[int] = None
        self.last_heartbeat_from_gate: Optional[float] = None
        self.heartbeat_stop_event: threading.Event = threading.Event()

        self.action_to_gate_queue: queue.Queue[ServiceToGateProto] = queue.Queue(
            maxsize=config.sdk.action_to_gate_queue_max_size
        )
        self._queue_full_warned: bool = False

        self.replay_queue: queue.Queue[ServiceToGateProto] = queue.Queue()
        self.channel: Optional[grpc.Channel] = None
        self.stub: Optional[GateStub] = None
        self.stopping_event: Optional[threading.Event] = None
        self.stopping: threading.Event = threading.Event()

        self.worker_thread: threading.Thread = threading.Thread(target=self.__worker_proc)

    def start(self):
        self.worker_thread.start()

    @staticmethod
    def __startup_probe():
        with open("/tmp/startup-probe", "w") as f:
            f.write(str(int(time.time())))

    @staticmethod
    def __liveness_probe():
        with open("/tmp/liveness-probe", "w") as f:
            f.write(str(int(time.time())))

    def __worker_proc(self):
        try:
            while not self.stopping.is_set():
                self.__connect_to_gate()

                if self.stopping.is_set():
                    break

                if self.state == MlpConnectorState.connected:
                    self.__start_processing()

                # __start_processing returned; determine why
                if self.stopping.is_set():
                    break
                if self.state == MlpConnectorState.reconnecting and _RECONNECT_ENABLED:
                    self.log.info("Reconnecting to gate ...")
                    self.__close_channel()
                    self.__reset_heartbeat_state()
                    continue
                # On error / stopped — exit loop
                break
        except Exception as e:  # pragma: no cover
            self.log.error("Exception in __worker_proc " + type(e).__name__, exc_info=True)  # pragma: no cover

    def __connect_to_gate(self):
        if self.stopping.is_set():
            return
        gateway_permanently_unavailable = False
        self.__startup_probe()
        self.state = MlpConnectorState.connecting
        self.log.info(f"trying to connect to {self.host_port} ... ")
        reconnect_timeout = config.sdk.shutdown_event_timeout_seconds
        while self.state == MlpConnectorState.connecting and not self.stopping.is_set():
            try:
                self.__close_channel()
                self.channel, self.stub = self._create_channel_and_stub()

                self.stub.healthCheck(HeartBeatProto())  # type: ignore

                self.state = MlpConnectorState.connected
                gateway_permanently_unavailable = False
                self.log.info(f" ... {self.host_port} connected")
                break
            except grpc.RpcError as e:
                code_attr = getattr(e, "code", None)
                code = code_attr() if callable(code_attr) else None

                if code is not None and code not in _RECONNECTABLE_GRPC_CODES:
                    self.log.error(
                        f"Cannot connect to {self.host_port}: non-recoverable gRPC code {code}, giving up reconnect"
                    )
                    self.state = MlpConnectorState.error
                    return
                if not gateway_permanently_unavailable:
                    self.log.debug(f"Cannot connect to {self.host_port} retry in {reconnect_timeout} sec")
                gateway_permanently_unavailable = True

            except Exception as e:
                self.log.debug("Cannot connect to " + self.host_port + " " + type(e).__name__)
                self.log.debug(e, exc_info=True)

            self.stopping.wait(reconnect_timeout)

    def _create_channel_and_stub(self) -> tuple[grpc.Channel, GateStub]:  # pragma: no cover
        # Этот метод переопределяется в юнит-тестах, потому он помечен как no cover
        channel = MlpGrpcClient.open_grpc_channel(self.host_port, self.grpc_secure)
        stub = GateStub(channel)
        return channel, stub

    def enqueue_to_gate(self, msg: ServiceToGateProto) -> bool:
        try:
            self.action_to_gate_queue.put_nowait(msg)
            if self._queue_full_warned:
                self._queue_full_warned = False
            return True
        except queue.Full:
            body = msg.WhichOneof("body")

            if not self._queue_full_warned:
                self.log.warning(
                    "action_to_gate_queue is full (maxsize=%d), dropping message of type=%s. "
                    "Probably gate is unavailable for too long. "
                    "Consider increasing MLP_SDK_ACTION_TO_GATE_QUEUE_MAX_SIZE.",
                    self.action_to_gate_queue.maxsize,
                    body,
                )
                self._queue_full_warned = True
            else:
                self.log.debug("action_to_gate_queue still full, dropping message of type=%s", body)
            return False

    def __close_channel(self) -> None:
        if self.channel is not None:
            try:
                self.channel.close()
            except BaseException:
                pass
            self.channel = None
        self.stub = None

    def __reset_heartbeat_state(self) -> None:
        if self.heartbeat_thread is not None:
            self.heartbeat_stop_event.set()
            self.heartbeat_thread.join(timeout=config.sdk.heartbeat_thread_timeout_seconds)
            self.heartbeat_thread = None

        self.heartbeat_stop_event = threading.Event()
        self.last_heartbeat_from_gate = None
        self.heartbeat_thread_interval_from_gate_ms = None

    def __build_start_serving_message(self) -> ServiceToGateProto:
        return ServiceToGateProto(
            startServing=StartServingProto(
                connectionToken=self.connection_token,
                serviceDescriptor=self.service_descriptor,
                hostname=os.environ.get("HOSTNAME", ""),
                sdkVersion=self.SDK_VERSION,
                image=os.environ.get("IMAGE_NAME", ""),
                imageVersionJson=self.__get_version_info(),
                instanceBootUuid=_PROCESS_INSTANCE_UUID,
            )
        )

    def __start_processing(self, reconnect: bool = False):
        self.log.debug(" ... init processing (reconnect=%s)", reconnect)

        def action_to_gate_generator() -> Generator[ServiceToGateProto, None, None]:
            # startServing — обязательно первое сообщение каждого нового стрима
            yield self.__build_start_serving_message()

            # На реконнекте — сначала сливаем replay_queue (failed yields с предыдущего
            # стрима)
            while True:
                try:
                    msg = self.replay_queue.get_nowait()
                except queue.Empty:
                    break
                try:
                    yield msg
                except BaseException:
                    self.replay_queue.put_nowait(msg)
                    raise
                if msg.WhichOneof("body") == "stopServing":
                    return

            # Основная очередь: новые сообщения от heartbeat-потока, predict-ответы
            # от multi_host_connector, stopServing от stop_and_wait.
            while True:
                msg = self.action_to_gate_queue.get()
                self.action_to_gate_queue.task_done()
                try:
                    yield msg
                except BaseException:
                    self.replay_queue.put_nowait(msg)
                    raise
                if msg.WhichOneof("body") == "stopServing":
                    return

        gate_to_action_generator = self.stub.processAsync(action_to_gate_generator())  # type: ignore

        self.log.debug(" ... start serving.")
        self.log.info("Service is ready to serve!")
        self.state = MlpConnectorState.serving
        self.__request_processing(gate_to_action_generator)

        self.log.info("Processing thread stopped")
        if self.state not in (MlpConnectorState.error, MlpConnectorState.reconnecting):
            self.state = MlpConnectorState.stopped

    def __get_version_info(self) -> str:
        if os.path.exists("./version-info.json"):
            with open("./version-info.json") as f:
                return f.read()
        return ""  # pragma: no cover

    def __request_processing(self, gate_to_action_generator: Any):
        try:
            for request in gate_to_action_generator:
                try:
                    self.__process_request(request)
                except BaseException:
                    self.log.error("Exception in __process_request", exc_info=True)

                if self.stopping.is_set():
                    break

        except grpc.RpcError as e:
            code_attr = getattr(e, "code", None)
            code = code_attr() if callable(code_attr) else None
            if code == grpc.StatusCode.CANCELLED:
                self.log.error("Channel closed. (Got StatusCode.CANCELLED exception)")
            elif code == grpc.StatusCode.UNAVAILABLE:  # pragma: no cover
                self.log.error("... can't connect. (Got StatusCode.UNAVAILABLE exception)")
            else:  # pragma: no cover
                self.log.error(f"gRPC exception with code {code}", exc_info=True)

            if _RECONNECT_ENABLED and (code is None or code in _RECONNECTABLE_GRPC_CODES):
                self.state = MlpConnectorState.reconnecting
            else:
                self.state = MlpConnectorState.error
        except BaseException:  # pragma: no cover
            self.log.error("Exception in action_to_gate_generator loop", exc_info=True)
            self.state = MlpConnectorState.error

    def __process_request(self, request: GateToServiceProto):
        req_type = request.WhichOneof("body")
        if req_type != "heartBeat":
            self.__log_request(request)

        if req_type is None:
            self.log.error("Request with empty body", extra={"requestId": request.requestId})  # pragma: no cover
        elif req_type == "serviceInfo":
            self.log.info(f"ServiceInfo: {JSON.stringify(request, pretty=False)}")
        elif req_type == "heartBeat":
            self.last_heartbeat_from_gate = time.time()

            if self.heartbeat_thread is None:
                self.log.debug(" ... starting heartbeats", extra={"requestId": request.requestId})
                self.heartbeat_thread_interval_from_gate_ms = request.heartBeat.interval
                self.heartbeat_thread = threading.Thread(
                    target=self._heartbeat_proc,
                    args=(self.heartbeat_stop_event,),
                )
                self.heartbeat_thread.start()

        elif req_type == "cluster":
            self.host_port = request.cluster.currentServer
            self.callback.cluster_update(request.cluster)
        elif req_type == "stopServing":
            self.log.info("Received stopServing from gate.")
            self.state = MlpConnectorState.stopped
            self.stopping.set()
            # self.stop_and_wait()
        elif req_type in ["predict", "fit", "ext", "batch", "partialPredict"]:
            self.callback.request(request, self)
        else:  # pragma: no cover
            raise MlpException(
                code="mlp-action.common.internal-error",
                message=f"Unknown request type: {req_type}. Probably there is a client-server version missmatch",
            )

    def __log_request(self, request: GateToServiceProto) -> None:
        stringified_request = MessageToJson(request, ensure_ascii=False)
        requestId = request.headers["Z-requestId"] if "Z-requestId" in request.headers else request.requestId
        if len(stringified_request) < config.sdk.large_body_length:
            self.log.debug("Request: " + stringified_request, extra={"requestId": requestId})
        else:
            self.log.debug("Request with large body. Id=" + str(request.requestId), extra={"requestId": requestId})

    def _heartbeat_proc(self, stop_event: threading.Event) -> None:
        while not stop_event.is_set() and self.state in (MlpConnectorState.connected, MlpConnectorState.serving):
            self.enqueue_to_gate(ServiceToGateProto(heartBeat=HeartBeatProto()))

            if self.heartbeat_thread_interval_from_gate_ms is not None:
                if stop_event.wait(self.heartbeat_thread_interval_from_gate_ms / 1000):
                    break

                if self.last_heartbeat_from_gate is not None and time.time() - self.last_heartbeat_from_gate > (
                    self.heartbeat_thread_interval_from_gate_ms / 1000 * 3 + 1
                ):
                    self.log.error("No heartbeats from gate")
                    if _RECONNECT_ENABLED:
                        self.state = MlpConnectorState.reconnecting
                        if self.channel is not None:
                            try:
                                self.channel.close()
                            except BaseException:
                                pass
                    else:
                        self.state = MlpConnectorState.error
            else:  # pragma: no cover
                # теоретически невозможная ситуация
                if stop_event.wait(5.0):
                    break

            self.__liveness_probe()

    def stop_and_wait(self, state: MlpConnectorState | None = None) -> None:
        if state is None:
            state = MlpConnectorState.stopping

        if self.state == MlpConnectorState.serving:
            self.log.info(" ... stop serving")

        if self.state == MlpConnectorState.stopping:  # pragma: no cover
            self.log.error(" ... stopping in another thread")
            return

        already_stopped = self.state in (MlpConnectorState.stopped, MlpConnectorState.error)

        if not already_stopped:
            self.state = state
            if not self.enqueue_to_gate(ServiceToGateProto(stopServing=StopServingProto())):
                self.log.warning("Could not enqueue stopServing — channel close will terminate the stream.")
        else:
            self.log.info(" ... already stopped, completing shutdown")

        self.stopping.set()
        self.heartbeat_stop_event.set()

        if already_stopped and self.channel is not None:
            try:
                self.channel.close()
            except BaseException:
                pass

        if threading.current_thread() != self.worker_thread:
            self.worker_thread.join(config.sdk.startup_thread_timeout_seconds)
        if self.heartbeat_thread is not None:
            self.heartbeat_thread.join(config.sdk.heartbeat_thread_timeout_seconds)

        self.state = MlpConnectorState.stopped

        if self.channel is not None:
            try:
                self.channel.close()
            except BaseException:
                pass
            self.channel = None
