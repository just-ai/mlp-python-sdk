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
from mlp_sdk.mlp_connector.single_host_connector import MlpConnectorState, MlpSingleHostConnector
from mlp_sdk.utils.config import get_config
from mlp_sdk.utils.utils import wait_for, wait_for_state


class FakeRpcException(grpc.RpcError):
    def code(self):
        return grpc.StatusCode.CANCELLED


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
        assert self.connector.last_heartbeat_from_gate is None
        time_before = time.time()

        # Получение первого хартбита запускает поток проверки хартбитов
        self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1)))

        assert self.connector.state == MlpConnectorState.serving
        wait_for(lambda: self.connector.last_heartbeat_from_gate is not None and self.connector.last_heartbeat_from_gate > time_before)
        wait_for(lambda: self.connector.heartbeat_thread is not None and self.connector.heartbeat_thread.is_alive())

        self.connector.last_heartbeat_from_gate = time.time() - 20
        self.connector._heartbeat_proc()

        assert self.connector.state == MlpConnectorState.error

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
        self.no_teardown = True
        # Send a predict request
        self.gate_to_service.put("rpc-exception")

        # Wait for the callback to be called
        wait_for_state(MlpConnectorState.error, lambda: self.connector.state)
