import queue
import threading
import time
from unittest.mock import Mock

import grpc

from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import (
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
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2_grpc import GateStub
from mlp_sdk.mlp_connector.single_host_connector import _PROCESS_INSTANCE_UUID, MlpConnectorState, MlpSingleHostConnector
from mlp_sdk.utils.config import get_config
from mlp_sdk.utils.utils import wait_for, wait_for_state


class FakeRpcException(grpc.RpcError):
    def code(self):
        return grpc.StatusCode.CANCELLED


class FakeRpcExceptionUnavailable(grpc.RpcError):
    def code(self):
        return grpc.StatusCode.UNAVAILABLE


class FakeRpcExceptionWithCode(grpc.RpcError):
    def __init__(self, code: grpc.StatusCode):
        super().__init__()
        self._code = code

    def code(self):
        return self._code


class TestMlpSingleHostConnector:
    def setup_method(self):
        self.service_descriptor = ServiceDescriptorProto()
        self.callback = Mock()
        self.connector = MlpSingleHostConnector("host:9999", True, "connection_token", self.service_descriptor, self.callback)
        self.channel_mock = Mock()
        self.stub_mock = Mock()

        # Setup health check mock
        self.stub_mock.healthCheck = Mock()

        # Setup process async mock with a queue for responses
        self.service_to_gate = []
        self.gate_to_service = queue.Queue()

        # Setup the process_async_mock method
        self.__setup_process_async_mock()

        def create_mocks() -> tuple[grpc.Channel, GateStub]:
            return self.channel_mock, self.stub_mock

        self.connector._create_channel_and_stub = create_mocks
        self.no_teardown = False

        with open("./version-info.json", "w") as f:
            f.write('{"version":"test"}')

        self.connector.start()
        wait_for_state(MlpConnectorState.serving, lambda: self.connector.state)

    def teardown_method(self):
        if not self.no_teardown:
            self.connector.stop_and_wait()
            wait_for_state(MlpConnectorState.stopped, lambda: self.connector.state)

        self.gate_to_service.put_nowait(None)
        self.connector.action_to_gate_queue.put(ServiceToGateProto(stopServing=StopServingProto()))
        if hasattr(self, "service_to_gate_thread"):
            self.service_to_gate_thread.join()

    def __setup_process_async_mock(self):
        def read_generator(generator):
            for request in generator:
                self.service_to_gate.append(request)
                if request.WhichOneof("body") == "stopServing":
                    # симулируем поведение, при котором gateway закрывает соединение когда получает stopServing
                    self.gate_to_service.put_nowait(None)
                    # pass

        def process_async_mock(generator):
            # Consume the generator to get the requests
            self.service_to_gate_thread = threading.Thread(target=read_generator, args=(generator,))
            self.service_to_gate_thread.start()

            # Return our predefined responses
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
                    # raw RpcError без code() — для Bug 3 теста
                    raise m
                yield m

        self.stub_mock.processAsync = Mock(side_effect=process_async_mock)

    def test_start_stop(self):
        # Starting the connector and waiting for the connector to reach connected state are performed in the setup method

        # Verify that healthCheck was called
        self.stub_mock.healthCheck.assert_called_once()

        # Verify that processAsync was called
        self.stub_mock.processAsync.assert_called_once()

        # Stopping the connector and wating for the connector to reach stopped state are performed in the teardown method

    def test_stop_serving(self):
        # Send StopServing message from gate to service
        stop_serving_message = GateToServiceProto(stopServing=StopServingProto())
        self.gate_to_service.put(stop_serving_message)

        # Wait for the connector to reach stopped state
        wait_for_state(MlpConnectorState.stopped, lambda: self.connector.state)
        self.no_teardown = True

    def test_heartbeat_handling(self):
        assert self.connector.last_heartbeat_from_gate is None
        time_before = time.time()

        # Получение первого хартбита запускает поток проверки хартбитов
        self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1)))

        wait_for(lambda: self.connector.last_heartbeat_from_gate is not None and self.connector.last_heartbeat_from_gate > time_before)
        wait_for(lambda: self.connector.heartbeat_thread is not None and self.connector.heartbeat_thread.is_alive())

    def test_cluster_update(self):
        # Получение первого хартбита запускает поток проверки хартбитов
        self.gate_to_service.put(GateToServiceProto(cluster=ClusterUpdateProto(servers=["s1", "s2"], currentServer="s1")))

        wait_for(lambda: self.callback.cluster_update.call_count > 0)

    def test_service_info(self):
        self.gate_to_service.put(GateToServiceProto(serviceInfo=ServiceInfoProto(accountId=1, modelId=2, modelName="test", authToken="test2")))

    def test_predict(self):
        self.gate_to_service.put(GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        wait_for(lambda: self.callback.request.call_count > 0)

    def test_no_logging_for_large_requests(self):
        self.gate_to_service.put(GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}" * 3000))))

        wait_for(lambda: self.callback.request.call_count > 0)

    def test_no_heartbeat_from_gate(self):
        # Bug 2: с включённым reconnect (default) таймаут HB переводит коннектор
        # в reconnecting и принудительно закрывает канал — иначе пришлось бы
        # ждать TCP keepalive (десятки секунд), пока gRPC сам заметит обрыв.
        assert self.connector.last_heartbeat_from_gate is None
        time_before = time.time()

        self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1)))

        assert self.connector.state == MlpConnectorState.serving
        wait_for(lambda: self.connector.last_heartbeat_from_gate is not None and self.connector.last_heartbeat_from_gate > time_before)
        wait_for(lambda: self.connector.heartbeat_thread is not None and self.connector.heartbeat_thread.is_alive())

        self.connector.last_heartbeat_from_gate = time.time() - 20
        self.connector._heartbeat_proc(self.connector.heartbeat_stop_event)

        assert self.connector.state == MlpConnectorState.reconnecting
        self.channel_mock.close.assert_called()

    def test_no_heartbeat_from_gate_reconnect_disabled(self):
        # Bug 2: с отключённым reconnect таймаут HB ведёт в error (старое поведение,
        # дальше MultiHost пересоздаёт коннектор).
        import mlp_sdk.mlp_connector.single_host_connector as shc

        original = shc._RECONNECT_ENABLED
        try:
            shc._RECONNECT_ENABLED = False
            self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1)))
            wait_for(lambda: self.connector.heartbeat_thread is not None and self.connector.heartbeat_thread.is_alive())

            self.connector.last_heartbeat_from_gate = time.time() - 20
            self.connector._heartbeat_proc(self.connector.heartbeat_stop_event)

            assert self.connector.state == MlpConnectorState.error
            self.no_teardown = True
        finally:
            shc._RECONNECT_ENABLED = original

    def test_version(self):
        # Check that the first message in the service_to_gate list is a StartServingProto
        # and that it contains the correct version information
        time.sleep(0.1)

        assert len(self.service_to_gate) > 0
        first_message = self.service_to_gate[0]
        assert first_message.WhichOneof("body") == "startServing"
        assert first_message.startServing.imageVersionJson == '{"version":"test"}'

    def test_rpc_error_during_connection(self):
        config = get_config()
        # Create a new connector for this test
        connector = MlpSingleHostConnector("host:9999", True, "connection_token", self.service_descriptor, self.callback)

        # Mock the _create_channel_and_stub method to raise an RpcError
        counter = 0

        def create_mocks_with_error():
            nonlocal counter
            counter += 1
            if counter % 2 == 0:
                raise grpc.RpcError("Simulated RPC error during connection")
            else:
                raise Exception("Simulated RPC error during connection")

        connector._create_channel_and_stub = create_mocks_with_error

        # Set a short timeout for faster test execution
        config.sdk.shutdown_event_timeout_seconds = 0.02

        try:
            # Start the connector
            connector.start()

            # Wait for the connector to attempt connection and handle the error
            time.sleep(0.2)

            # Verify that the connector is still in connecting state
            assert connector.state == MlpConnectorState.connecting

        finally:
            # Clean up
            connector.stop_and_wait()

    def test_predict_with_unexpected_exception(self):
        # Mock the callback.request method to raise an exception
        self.callback.request.side_effect = Exception("Test exception from callback")

        # Send a predict request
        self.gate_to_service.put(GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        # Wait for the callback to be called
        wait_for(lambda: self.callback.request.call_count > 0)

        # Verify that the connector is still in serving state despite the exception
        assert self.connector.state == MlpConnectorState.serving

    def test_predict_with_rpc_exception(self):
        import mlp_sdk.mlp_connector.single_host_connector as shc

        original = shc._RECONNECT_ENABLED
        try:
            shc._RECONNECT_ENABLED = False
            self.no_teardown = True
            # Send a predict request
            self.gate_to_service.put("rpc-exception")

            # Wait for the callback to be called
            wait_for_state(MlpConnectorState.error, lambda: self.connector.state)
        finally:
            shc._RECONNECT_ENABLED = original

    def test_start_serving_contains_instance_boot_uuid(self):
        time.sleep(0.1)

        assert len(self.service_to_gate) > 0
        first_message = self.service_to_gate[0]
        assert first_message.WhichOneof("body") == "startServing"
        assert first_message.startServing.instanceBootUuid == _PROCESS_INSTANCE_UUID

    def test_process_instance_uuid_is_stable(self):
        # Re-importing the module should yield the same UUID (module cache)
        from mlp_sdk.mlp_connector.single_host_connector import _PROCESS_INSTANCE_UUID as uuid2

        assert _PROCESS_INSTANCE_UUID == uuid2
        assert len(_PROCESS_INSTANCE_UUID) == 36  # standard UUID string length

    def test_reconnect_on_unavailable(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")

        # Wait for the connector to reconnect (processAsync called again)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)

        # After reconnect, state should be serving again
        assert self.connector.state == MlpConnectorState.serving

    def test_replay_queue_drained_on_reconnect(self):
        # Имитируем failed yield: кладём сообщение в replay_queue (это и делает
        # генератор в catch'е при разрыве). На реконнекте оно должно быть
        # отправлено гейту — после startServing, раньше новых сообщений из
        # action_to_gate_queue.
        msg = ServiceToGateProto(heartBeat=HeartBeatProto())
        self.connector.replay_queue.put_nowait(msg)

        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)

        wait_for(lambda: msg in self.service_to_gate)
        # И replay_queue после слива пустая.
        assert self.connector.replay_queue.empty()

    def test_reconnect_restarts_heartbeat_thread(self):
        # До реконнекта поднимаем heartbeat-поток "первым HB от gate"
        self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1)))
        wait_for(lambda: self.connector.heartbeat_thread is not None and self.connector.heartbeat_thread.is_alive())
        old_thread = self.connector.heartbeat_thread

        # Ломаем стрим, ждём реконнекта
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(MlpConnectorState.serving, lambda: self.connector.state)

        # После реконнекта старый поток обнулён и новый HB поднимет свежий поток
        wait_for(lambda: self.connector.heartbeat_thread is None or self.connector.heartbeat_thread is not old_thread)
        self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1)))

        def fresh_thread_running() -> bool:
            t = self.connector.heartbeat_thread
            return t is not None and t is not old_thread and t.is_alive()

        wait_for(fresh_thread_running)
        assert not old_thread.is_alive()

    def test_reconnect_disabled_goes_to_error(self):
        import mlp_sdk.mlp_connector.single_host_connector as shc

        original = shc._RECONNECT_ENABLED
        try:
            shc._RECONNECT_ENABLED = False
            self.no_teardown = True
            self.gate_to_service.put("rpc-exception-unavailable")
            wait_for_state(MlpConnectorState.error, lambda: self.connector.state)
        finally:
            shc._RECONNECT_ENABLED = original

    def test_start_serving_first_on_reconnect(self):
        # На каждом новом стриме (включая реконнект) startServing — первое сообщение,
        # чтобы гейт сматчил сессию по instanceBootUuid до прихода replayed-сообщений.
        len_before = len(self.service_to_gate)
        initial_count = self.stub_mock.processAsync.call_count

        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(MlpConnectorState.serving, lambda: self.connector.state)
        wait_for(lambda: len(self.service_to_gate) > len_before)

        new_messages = self.service_to_gate[len_before:]
        assert new_messages[0].WhichOneof("body") == "startServing"
        assert new_messages[0].startServing.instanceBootUuid == _PROCESS_INSTANCE_UUID

    def test_old_heartbeat_thread_dies_quickly_on_reconnect_with_long_interval(self):
        # Регрессионный тест: раньше при длинном интервале HB старый поток мог
        # пережить реконнект (heartbeat_thread.join таймаутится за 3 сек, а поток
        # спит на интервале гейта — например 30 сек). С heartbeat_stop_event
        # старый поток должен выйти быстро, не дожидаясь конца интервала.
        # interval=30000 ms = 30 сек; если бы баг остался, поток жил бы ~30 сек.
        self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=30000)))
        wait_for(lambda: self.connector.heartbeat_thread is not None and self.connector.heartbeat_thread.is_alive())
        old_thread = self.connector.heartbeat_thread

        # Ломаем стрим — реконнект сетит heartbeat_stop_event.
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put("rpc-exception-unavailable")
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)

        # Старый поток должен умереть в пределах 5 сек (а не 30).
        old_thread.join(timeout=5.0)
        assert not old_thread.is_alive(), "Old heartbeat thread did not stop on reconnect"

    def test_reconnect_on_deadline_exceeded(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.DEADLINE_EXCEEDED)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        assert self.connector.state == MlpConnectorState.serving

    def test_reconnect_on_internal(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.INTERNAL)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        assert self.connector.state == MlpConnectorState.serving

    def test_reconnect_on_unknown(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.UNKNOWN)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        assert self.connector.state == MlpConnectorState.serving

    def test_reconnect_on_aborted(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.ABORTED)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        assert self.connector.state == MlpConnectorState.serving

    def test_reconnect_on_resource_exhausted(self):
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.StatusCode.RESOURCE_EXHAUSTED)
        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        assert self.connector.state == MlpConnectorState.serving

    def test_no_reconnect_on_unauthenticated(self):
        # Постоянная ошибка авторизации — реконнект не поможет, идём в error.
        self.no_teardown = True
        self.gate_to_service.put(grpc.StatusCode.UNAUTHENTICATED)
        wait_for_state(MlpConnectorState.error, lambda: self.connector.state)

    def test_no_reconnect_on_permission_denied(self):
        self.no_teardown = True
        self.gate_to_service.put(grpc.StatusCode.PERMISSION_DENIED)
        wait_for_state(MlpConnectorState.error, lambda: self.connector.state)

    def test_no_reconnect_on_unimplemented(self):
        self.no_teardown = True
        self.gate_to_service.put(grpc.StatusCode.UNIMPLEMENTED)
        wait_for_state(MlpConnectorState.error, lambda: self.connector.state)

    def test_stop_during_reconnect_does_not_busy_loop(self):
        # Регрессия: если стрим порвался и __connect_to_gate ушёл в retry-loop
        # (гейт долго недоступен), вызов stop_and_wait должен корректно завершить
        # worker. Без фикса __connect_to_gate перезатирал state на connecting,
        # а stopping.wait возвращался мгновенно — busy-loop, worker не выходил.
        real_create = self.connector._create_channel_and_stub
        fail_create = threading.Event()

        def maybe_failing_create():
            if fail_create.is_set():
                raise grpc.RpcError("simulated gateway down")
            return real_create()

        self.connector._create_channel_and_stub = maybe_failing_create

        cfg = get_config()
        original_timeout = cfg.sdk.shutdown_event_timeout_seconds
        cfg.sdk.shutdown_event_timeout_seconds = 0.05
        try:
            # Включаем падение _create_channel_and_stub перед реконнектом.
            fail_create.set()
            # Ломаем стрим — коннектор уйдёт в reconnect, попытки коннекта будут падать.
            self.gate_to_service.put("rpc-exception-unavailable")
            wait_for_state(MlpConnectorState.connecting, lambda: self.connector.state)

            # Stop во время retry-loop: worker должен выйти быстро, без busy-loop.
            self.connector.stop_and_wait()
            self.connector.worker_thread.join(timeout=3.0)
            assert not self.connector.worker_thread.is_alive(), \
                "Worker thread did not exit after stop_and_wait during reconnect"
            self.no_teardown = True
        finally:
            cfg.sdk.shutdown_event_timeout_seconds = original_timeout

    def test_enqueue_to_gate_drops_on_full(self):
        # При переполнении action_to_gate_queue сообщение дропается,
        # producer не блокируется.
        cfg = get_config()
        original = cfg.sdk.action_to_gate_queue_max_size
        cfg.sdk.action_to_gate_queue_max_size = 2
        try:
            c = MlpSingleHostConnector("h:1", True, "t", self.service_descriptor, self.callback)
            assert c.enqueue_to_gate(ServiceToGateProto(heartBeat=HeartBeatProto())) is True
            assert c.enqueue_to_gate(ServiceToGateProto(heartBeat=HeartBeatProto())) is True
            # Третье — очередь полна, дроп.
            assert c.enqueue_to_gate(ServiceToGateProto(heartBeat=HeartBeatProto())) is False
            assert c.action_to_gate_queue.qsize() == 2
        finally:
            cfg.sdk.action_to_gate_queue_max_size = original

    def test_action_queue_maxsize_from_config(self):
        cfg = get_config()
        original = cfg.sdk.action_to_gate_queue_max_size
        cfg.sdk.action_to_gate_queue_max_size = 7
        try:
            c = MlpSingleHostConnector("h:1", True, "t", self.service_descriptor, self.callback)
            assert c.action_to_gate_queue.maxsize == 7
        finally:
            cfg.sdk.action_to_gate_queue_max_size = original

    def __reconnect_with_failing_healthcheck(self, code: grpc.StatusCode) -> None:
        """Хелпер: ломает стрим reconnectable-ошибкой и подменяет healthCheck так,
        чтобы он бросал указанный код. Используется для проверки поведения
        __connect_to_gate при разных кодах от healthCheck во время reconnect."""
        new_stub = Mock()
        new_stub.healthCheck = Mock(side_effect=FakeRpcExceptionWithCode(code))
        new_stub.processAsync = self.stub_mock.processAsync

        def replaced_create():
            return self.channel_mock, new_stub

        self.connector._create_channel_and_stub = replaced_create

        # Ускоряем ретраи коннекта.
        cfg = get_config()
        self.__original_shutdown_timeout = cfg.sdk.shutdown_event_timeout_seconds
        cfg.sdk.shutdown_event_timeout_seconds = 0.05

        # Ломаем стрим reconnectable-ошибкой → коннектор пойдёт в reconnect → healthCheck.
        self.gate_to_service.put("rpc-exception-unavailable")

    def test_no_reconnect_on_healthcheck_unauthenticated(self):
        # Регрессия: транзиентная ошибка стрима + UNAUTHENTICATED от healthCheck во время
        # reconnect не должны приводить к бесконечным ретраям. Идём в error, чтобы
        # MultiHost мог пересоздать коннектор.
        try:
            self.__reconnect_with_failing_healthcheck(grpc.StatusCode.UNAUTHENTICATED)
            wait_for_state(MlpConnectorState.error, lambda: self.connector.state)
            self.no_teardown = True
        finally:
            get_config().sdk.shutdown_event_timeout_seconds = self.__original_shutdown_timeout

    def test_no_reconnect_on_healthcheck_permission_denied(self):
        try:
            self.__reconnect_with_failing_healthcheck(grpc.StatusCode.PERMISSION_DENIED)
            wait_for_state(MlpConnectorState.error, lambda: self.connector.state)
            self.no_teardown = True
        finally:
            get_config().sdk.shutdown_event_timeout_seconds = self.__original_shutdown_timeout

    def test_no_reconnect_on_healthcheck_unimplemented(self):
        try:
            self.__reconnect_with_failing_healthcheck(grpc.StatusCode.UNIMPLEMENTED)
            wait_for_state(MlpConnectorState.error, lambda: self.connector.state)
            self.no_teardown = True
        finally:
            get_config().sdk.shutdown_event_timeout_seconds = self.__original_shutdown_timeout

    def test_reconnect_on_healthcheck_unavailable_then_recovers(self):
        # Транзиентный UNAVAILABLE от healthCheck — ретраим, не уходим в error.
        # Проверяем, что коннектор остаётся в connecting, а не падает в error.
        cfg = get_config()
        original_timeout = cfg.sdk.shutdown_event_timeout_seconds
        cfg.sdk.shutdown_event_timeout_seconds = 0.05
        try:
            new_stub = Mock()
            new_stub.healthCheck = Mock(side_effect=FakeRpcExceptionWithCode(grpc.StatusCode.UNAVAILABLE))
            new_stub.processAsync = self.stub_mock.processAsync

            def replaced_create():
                return self.channel_mock, new_stub

            self.connector._create_channel_and_stub = replaced_create
            self.gate_to_service.put("rpc-exception-unavailable")

            # Ждём, пока коннектор перейдёт в connecting и начнёт ретраить.
            wait_for_state(MlpConnectorState.connecting, lambda: self.connector.state)

            # Дать ретраям пару циклов, убедиться что не свалились в error.
            time.sleep(0.2)
            assert self.connector.state == MlpConnectorState.connecting
            assert new_stub.healthCheck.call_count >= 2, "healthCheck должен ретраиться"

            self.connector.stop_and_wait()
            self.no_teardown = True
        finally:
            cfg.sdk.shutdown_event_timeout_seconds = original_timeout

    def test_reconnect_on_healthcheck_raw_rpc_error_without_code(self):
        # Защитный тест: некоторые grpc.RpcError не имеют метода code() (например,
        # raw RpcError("text") в тестах). На таких — ретраим (как до фикса).
        cfg = get_config()
        original_timeout = cfg.sdk.shutdown_event_timeout_seconds
        cfg.sdk.shutdown_event_timeout_seconds = 0.05
        try:
            new_stub = Mock()
            new_stub.healthCheck = Mock(side_effect=grpc.RpcError("simulated, no code"))
            new_stub.processAsync = self.stub_mock.processAsync

            def replaced_create():
                return self.channel_mock, new_stub

            self.connector._create_channel_and_stub = replaced_create
            self.gate_to_service.put("rpc-exception-unavailable")

            wait_for_state(MlpConnectorState.connecting, lambda: self.connector.state)
            time.sleep(0.2)
            assert self.connector.state == MlpConnectorState.connecting

            self.connector.stop_and_wait()
            self.no_teardown = True
        finally:
            cfg.sdk.shutdown_event_timeout_seconds = original_timeout

    def test_stop_and_wait_on_error_state_completes_shutdown(self):
        # Bug 1: stop_and_wait при state=error не должен возвращаться рано без
        # set(stopping), close(channel) и join(worker). Иначе с включённым
        # reconnect worker может "воскреснуть" через RpcError → reconnecting и
        # крутиться в reconnect-цикле вечно, пока пользователь думает, что
        # коннектор уже остановлен.
        # Имитируем закрытие стрима (в реале channel.close() форсит CANCELLED;
        # mock processAsync — нет, кладём None чтобы мок-генератор завершился).
        self.gate_to_service.put_nowait(None)
        # Эмулируем последствие heartbeat-таймаута / non-recoverable RpcError.
        self.connector.state = MlpConnectorState.error

        self.connector.stop_and_wait()

        assert self.connector.stopping.is_set(), \
            "stopping flag должен быть выставлен даже на early-return пути"
        self.channel_mock.close.assert_called()
        assert self.connector.state == MlpConnectorState.stopped
        self.connector.worker_thread.join(timeout=3.0)
        assert not self.connector.worker_thread.is_alive(), \
            "worker должен быть остановлен, а не оставлен жить для reconnect-loop"
        self.no_teardown = True

    def test_reconnect_on_stream_rpc_error_without_code(self):
        # Bug 3: stream RpcError без code() — это нативный сетевой сбой, а не
        # auth/permission ошибка. Считаем транзиентным и реконнектим. До фикса:
        # e.code() падало с AttributeError, ловилось в except BaseException →
        # state=error, реконнекта не было — несимметрично с __connect_to_gate.
        initial_count = self.stub_mock.processAsync.call_count
        self.gate_to_service.put(grpc.RpcError("simulated, no code attr"))

        wait_for(lambda: self.stub_mock.processAsync.call_count > initial_count)
        wait_for_state(MlpConnectorState.serving, lambda: self.connector.state)

    def test_close_channel_between_connect_retries(self):
        # Bug 4: на каждом ретрае __connect_to_gate должен закрыть предыдущий
        # канал. gRPC channel держит сокеты и фоновые потоки — без close
        # они утекают на каждом retry-цикле reconnect'а.
        cfg = get_config()
        original_timeout = cfg.sdk.shutdown_event_timeout_seconds
        cfg.sdk.shutdown_event_timeout_seconds = 0.05
        try:
            connector = MlpSingleHostConnector("h:1", True, "t", self.service_descriptor, self.callback)

            channels: list[Mock] = []

            def create_always_failing():
                ch = Mock()
                stub = Mock()
                stub.healthCheck = Mock(side_effect=FakeRpcExceptionUnavailable())
                channels.append(ch)
                return ch, stub

            connector._create_channel_and_stub = create_always_failing
            connector.start()

            # Ждём минимум 3 попытки коннекта.
            wait_for(lambda: len(channels) >= 3)

            # Каналы из попыток 1 и 2 должны быть закрыты __close_channel'ом
            # на старте следующей итерации.
            assert channels[0].close.called, \
                "Канал из попытки #1 должен быть закрыт перед попыткой #2"
            assert channels[1].close.called, \
                "Канал из попытки #2 должен быть закрыт перед попыткой #3"

            connector.stop_and_wait()
        finally:
            cfg.sdk.shutdown_event_timeout_seconds = original_timeout

