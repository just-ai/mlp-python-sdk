import copy
import queue
import threading
import time
from unittest.mock import Mock

import grpc

from mlp_sdk.grpc.mlp_grpc_pb2 import (
    ClusterUpdateProto,
    GateToServiceProto,
    HeartBeatProto,
    PayloadProto,
    PredictRequestProto,
    ServiceDescriptorProto,
    ServiceInfoProto,
    ServiceToGateProto,
    StopServingProto,
)
from mlp_sdk.transport.MlpServiceSDK import (
    _PROCESS_INSTANCE_UUID,
    CONFIG,
    MlpServiceConnector,
    State,
)


def wait_for(predicate, timeout: float = 5.0, interval: float = 0.02):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if predicate():
            return True
        time.sleep(interval)
    raise AssertionError(f"timeout waiting for {predicate}")


def wait_for_state(state, getter, timeout: float = 5.0):
    wait_for(lambda: getter() == state, timeout=timeout)


class FakeRpcException(grpc.RpcError):
    def code(self):
        return grpc.StatusCode.CANCELLED


class FakeRpcExceptionUnavailable(grpc.RpcError):
    def code(self):
        return grpc.StatusCode.UNAVAILABLE


class FakeRpcExceptionWithCode(grpc.RpcError):
    def __init__(self, code):
        super().__init__()
        self._code = code

    def code(self):
        return self._code


def _make_config(**overrides):
    cfg = copy.deepcopy(CONFIG)
    # ускоряем тесты — overrides по умолчанию, можно перебить через kwargs
    fast_defaults = {
        "shutdown_event_timeout_seconds": 0.05,
        "heartbeat_thread_timeout_seconds": 1,
        "startup_thread_timeout_seconds": 1,
        "stopping_event_timeout_seconds": 1,
    }
    for k, v in fast_defaults.items():
        cfg["sdk"][k] = v
    cfg["sdk"].update(overrides)
    return cfg


class TestMlpServiceConnector:
    def setup_method(self):
        self.sdk = Mock()
        self.sdk.connection_token = "connection_token"
        self.sdk.descriptor = ServiceDescriptorProto()
        self.sdk.service_info = None

        self.connector = MlpServiceConnector(
            "host:9999", self.sdk, grpc_secure=True, config=_make_config()
        )

        self.channel_mock = Mock()
        self.stub_mock = Mock()
        self.stub_mock.healthCheck = Mock()

        self.service_to_gate = []
        self.gate_to_service = queue.Queue()
        self.__setup_process_async_mock()

        def create_mocks():
            return self.channel_mock, self.stub_mock

        self.connector._create_channel_and_stub = create_mocks
        self.no_teardown = False

        self.connector.start()
        wait_for_state(State.serving, lambda: self.connector.state)

    def teardown_method(self):
        if not self.no_teardown:
            self.connector.stop()
            wait_for_state(State.stopped, lambda: self.connector.state)

        self.gate_to_service.put_nowait(None)
        try:
            self.connector.action_to_gate_queue.put_nowait(
                ServiceToGateProto(stopServing=StopServingProto())
            )
        except queue.Full:
            pass
        if hasattr(self, "service_to_gate_thread"):
            self.service_to_gate_thread.join(timeout=2.0)

    def __setup_process_async_mock(self):
        def read_generator(generator):
            for request in generator:
                self.service_to_gate.append(request)
                if request.WhichOneof("body") == "stopServing":
                    # эмулируем gateway, закрывающий стрим при stopServing
                    self.gate_to_service.put_nowait(None)

        def process_async_mock(generator):
            self.service_to_gate_thread = threading.Thread(
                target=read_generator, args=(generator,)
            )
            self.service_to_gate_thread.start()

            while True:
                m = self.gate_to_service.get()
                self.gate_to_service.task_done()
                if m is None:
                    break
                if m == "rpc-exception":
                    raise FakeRpcException()
                if m == "rpc-exception-unavailable":
                    raise FakeRpcExceptionUnavailable()
                if isinstance(m, grpc.StatusCode):
                    raise FakeRpcExceptionWithCode(m)
                if isinstance(m, grpc.RpcError):
                    raise m
                yield m

        self.stub_mock.processAsync = Mock(side_effect=process_async_mock)

    def test_start_stop(self):
        self.stub_mock.healthCheck.assert_called_once()
        self.stub_mock.processAsync.assert_called_once()

    def test_stop_serving(self):
        self.gate_to_service.put(GateToServiceProto(stopServing=StopServingProto()))
        wait_for_state(State.stopped, lambda: self.connector.state)
        self.no_teardown = True

    def test_heartbeat_handling(self):
        assert self.connector.last_heartbeat_from_gate is None
        before = time.time()

        self.gate_to_service.put(
            GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1))
        )

        wait_for(
            lambda: self.connector.last_heartbeat_from_gate is not None
            and self.connector.last_heartbeat_from_gate > before
        )
        wait_for(
            lambda: self.connector.heartbeat_thread is not None
            and self.connector.heartbeat_thread.is_alive()
        )

    def test_cluster_update(self):
        self.gate_to_service.put(
            GateToServiceProto(
                cluster=ClusterUpdateProto(servers=["s1", "s2"], currentServer="s1")
            )
        )
        wait_for(lambda: self.sdk.update_connectors.call_count > 0)

    def test_service_info(self):
        self.gate_to_service.put(
            GateToServiceProto(
                serviceInfo=ServiceInfoProto(
                    accountId=1, modelId=2, modelName="test", authToken="test2"
                )
            )
        )
        wait_for(lambda: self.sdk.service_info is not None)

    def test_predict(self):
        self.gate_to_service.put(
            GateToServiceProto(
                predict=PredictRequestProto(data=PayloadProto(json="{}"))
            )
        )
        wait_for(lambda: self.sdk.process_request_async.call_count > 0)

    def test_no_logging_for_large_requests(self):
        self.gate_to_service.put(
            GateToServiceProto(
                predict=PredictRequestProto(data=PayloadProto(json="{}" * 3000))
            )
        )
        wait_for(lambda: self.sdk.process_request_async.call_count > 0)

    # --- CAILA-5355: reconnect-aware heartbeat ---

    def test_no_heartbeat_from_gate(self):
        # При включённом reconnect (default) HB-таймаут переводит коннектор в
        # reconnecting и форсит закрытие канала.
        assert self.connector.last_heartbeat_from_gate is None

        self.gate_to_service.put(
            GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1))
        )
        wait_for(
            lambda: self.connector.heartbeat_thread is not None
            and self.connector.heartbeat_thread.is_alive()
        )

        self.connector.last_heartbeat_from_gate = time.time() - 20
        # запускаем heartbeat-проц синхронно, чтобы детерминированно поймать таймаут
        self.connector._MlpServiceConnector__heartbeat_proc(
            self.connector.heartbeat_stop_event
        )

        assert self.connector.state == State.reconnecting
        self.channel_mock.close.assert_called()

    def test_no_heartbeat_from_gate_reconnect_disabled(self):
        self.connector.config["sdk"]["reconnect_enabled"] = False

        self.gate_to_service.put(
            GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1))
        )
        wait_for(
            lambda: self.connector.heartbeat_thread is not None
            and self.connector.heartbeat_thread.is_alive()
        )

        self.connector.last_heartbeat_from_gate = time.time() - 20
        self.connector._MlpServiceConnector__heartbeat_proc(
            self.connector.heartbeat_stop_event
        )

        assert self.connector.state == State.error
        self.no_teardown = True

    # --- CAILA-5355: instanceBootUuid ---

    def test_start_serving_contains_instance_boot_uuid(self):
        time.sleep(0.1)
        assert len(self.service_to_gate) > 0
        first_message = self.service_to_gate[0]
        assert first_message.WhichOneof("body") == "startServing"
        assert first_message.startServing.instanceBootUuid == _PROCESS_INSTANCE_UUID

    def test_process_instance_uuid_is_stable(self):
        from mlp_sdk.transport.MlpServiceSDK import _PROCESS_INSTANCE_UUID as uuid2

        assert _PROCESS_INSTANCE_UUID == uuid2
        assert len(_PROCESS_INSTANCE_UUID) == 36

    # --- CAILA-5355: reconnect on stream errors ---

    def test_reconnect_on_unavailable(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

    def test_reconnect_on_deadline_exceeded(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.DEADLINE_EXCEEDED)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

    def test_reconnect_on_internal(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.INTERNAL)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

    def test_reconnect_on_unknown(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.UNKNOWN)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

    def test_reconnect_on_aborted(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.ABORTED)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

    def test_reconnect_on_resource_exhausted(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.RESOURCE_EXHAUSTED)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

    def test_no_reconnect_on_unauthenticated(self):
        self.no_teardown = True
        self.gate_to_service.put(grpc.StatusCode.UNAUTHENTICATED)
        wait_for_state(State.error, lambda: self.connector.state)

    def test_no_reconnect_on_permission_denied(self):
        self.no_teardown = True
        self.gate_to_service.put(grpc.StatusCode.PERMISSION_DENIED)
        wait_for_state(State.error, lambda: self.connector.state)

    def test_no_reconnect_on_unimplemented(self):
        self.no_teardown = True
        self.gate_to_service.put(grpc.StatusCode.UNIMPLEMENTED)
        wait_for_state(State.error, lambda: self.connector.state)

    def test_reconnect_disabled_goes_to_error(self):
        self.connector.config["sdk"]["reconnect_enabled"] = False
        self.no_teardown = True
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for_state(State.error, lambda: self.connector.state)

    # --- CAILA-5355: replay queue + startServing first on reconnect ---

    def test_replay_queue_drained_on_reconnect(self):
        msg = ServiceToGateProto(heartBeat=HeartBeatProto())
        self.connector.replay_queue.put_nowait(msg)

        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)

        wait_for(lambda: msg in self.service_to_gate)
        assert self.connector.replay_queue.empty()

    def test_start_serving_first_on_reconnect(self):
        len_before = len(self.service_to_gate)
        initial_count = self.stub_mock.processAsync.call_count

        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)
        wait_for(lambda: len(self.service_to_gate) > len_before)

        new_messages = self.service_to_gate[len_before:]
        assert new_messages[0].WhichOneof("body") == "startServing"
        assert new_messages[0].startServing.instanceBootUuid == _PROCESS_INSTANCE_UUID

    def test_reconnect_restarts_heartbeat_thread(self):
        self.gate_to_service.put(
            GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1))
        )
        wait_for(
            lambda: self.connector.heartbeat_thread is not None
            and self.connector.heartbeat_thread.is_alive()
        )
        old_thread = self.connector.heartbeat_thread

        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

        wait_for(
            lambda: self.connector.heartbeat_thread is None
            or self.connector.heartbeat_thread is not old_thread
        )
        self.gate_to_service.put(
            GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1))
        )

        def fresh_thread_running() -> bool:
            t = self.connector.heartbeat_thread
            return t is not None and t is not old_thread and t.is_alive()

        wait_for(fresh_thread_running)
        assert not old_thread.is_alive()

    def test_old_heartbeat_thread_dies_quickly_on_reconnect_with_long_interval(self):
        self.gate_to_service.put(
            GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=30000))
        )
        wait_for(
            lambda: self.connector.heartbeat_thread is not None
            and self.connector.heartbeat_thread.is_alive()
        )
        old_thread = self.connector.heartbeat_thread

        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)

        old_thread.join(timeout=5.0)
        assert not old_thread.is_alive(), "Old heartbeat thread did not stop on reconnect"

    # --- CAILA-5355: bounded queue ---

    def test_enqueue_to_gate_drops_on_full(self):
        sdk = Mock()
        sdk.connection_token = "tok"
        sdk.descriptor = ServiceDescriptorProto()
        c = MlpServiceConnector(
            "h:1", sdk, grpc_secure=True, config=_make_config(action_to_gate_queue_max_size=2)
        )
        assert c.enqueue_to_gate(ServiceToGateProto(heartBeat=HeartBeatProto())) is True
        assert c.enqueue_to_gate(ServiceToGateProto(heartBeat=HeartBeatProto())) is True
        assert c.enqueue_to_gate(ServiceToGateProto(heartBeat=HeartBeatProto())) is False
        assert c.action_to_gate_queue.qsize() == 2

    def test_action_queue_maxsize_from_config(self):
        sdk = Mock()
        sdk.connection_token = "tok"
        sdk.descriptor = ServiceDescriptorProto()
        c = MlpServiceConnector(
            "h:1", sdk, grpc_secure=True, config=_make_config(action_to_gate_queue_max_size=7)
        )
        assert c.action_to_gate_queue.maxsize == 7

    # --- CAILA-5355: regression bugs ---

    def test_reconnect_on_stream_rpc_error_without_code(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.RpcError("simulated, no code attr"))
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(State.serving, lambda: self.connector.state)

    def test_close_channel_between_connect_retries(self):
        sdk = Mock()
        sdk.connection_token = "tok"
        sdk.descriptor = ServiceDescriptorProto()
        connector = MlpServiceConnector(
            "h:1", sdk, grpc_secure=True, config=_make_config()
        )

        channels = []

        def create_always_failing():
            ch = Mock()
            stub = Mock()
            stub.healthCheck = Mock(side_effect=FakeRpcExceptionUnavailable())
            channels.append(ch)
            return ch, stub

        connector._create_channel_and_stub = create_always_failing
        connector.start()
        try:
            wait_for(lambda: len(channels) >= 3, timeout=3.0)
            assert channels[0].close.called
            assert channels[1].close.called
        finally:
            connector.stop()

    def test_predict_with_unexpected_exception(self):
        self.sdk.process_request_async.side_effect = Exception("boom")
        self.gate_to_service.put(
            GateToServiceProto(
                predict=PredictRequestProto(data=PayloadProto(json="{}"))
            )
        )
        wait_for(lambda: self.sdk.process_request_async.call_count > 0)
        assert self.connector.state == State.serving


def test_config_has_reconnect_keys():
    assert "reconnect_enabled" in CONFIG["sdk"]
    assert "action_to_gate_queue_max_size" in CONFIG["sdk"]
    assert CONFIG["sdk"]["reconnect_enabled"] is True
    assert isinstance(CONFIG["sdk"]["action_to_gate_queue_max_size"], int)
