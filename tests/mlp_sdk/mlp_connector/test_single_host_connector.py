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
    StopServingProto,
)
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2_grpc import GateStub
from mlp_sdk.mlp_connector.single_host_connector import MlpConnectorState, MlpSingleHostConnector


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

        self.connector.start()
        assert self.wait_for_state(MlpConnectorState.serving)

    def teardown_method(self):
        if not self.no_teardown:
            self.connector.stop_and_wait()
            assert self.wait_for_state(MlpConnectorState.stopped)

        self.gate_to_service.put_nowait(None)
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
                if m is not None:
                    yield m
                else:
                    break

        self.stub_mock.processAsync = Mock(side_effect=process_async_mock)

    def wait_for(self, condition, timeout=5):
        """Wait for a condition to be true with a timeout."""
        start_time = time.time()
        counter = 1
        while not condition() and time.time() - start_time < timeout:
            if counter % 10 == 0:
                print(f"Waiting for condition {condition} ...")
            time.sleep(0.1)
            counter += 1
        return condition()

    def wait_for_state(self, expected_state, timeout=5):
        """Wait for the connector to reach the expected state with a timeout."""
        start_time = time.time()
        counter = 1
        while self.connector.state != expected_state and time.time() - start_time < timeout:
            if counter % 10 == 0:
                print(f"Waiting for transition to state: {expected_state}, current state: {self.connector.state} ...")
            time.sleep(0.1)
            counter += 1
        return self.connector.state == expected_state

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
        assert self.wait_for_state(MlpConnectorState.stopped)
        self.no_teardown = True

    def test_heartbeat_handling(self):
        assert self.connector.last_heartbeat_from_gate is None
        time_before = time.time()

        # Получение первого хартбита запускает поток проверки хартбитов
        self.gate_to_service.put(GateToServiceProto(heartBeat=HeartBeatProto(status="Ok", interval=1)))

        self.wait_for(lambda: self.connector.last_heartbeat_from_gate is not None and self.connector.last_heartbeat_from_gate > time_before)
        self.wait_for(lambda: self.connector.heartbeat_thread is not None and self.connector.heartbeat_thread.is_alive())

    def test_cluster_update(self):
        # Получение первого хартбита запускает поток проверки хартбитов
        self.gate_to_service.put(GateToServiceProto(cluster=ClusterUpdateProto(servers=["s1", "s2"], currentServer="s1")))

        self.wait_for(lambda: self.callback.cluster_update.call_count > 0)

    def test_service_info(self):
        self.gate_to_service.put(GateToServiceProto(serviceInfo=ServiceInfoProto(accountId=1, modelId=2, modelName="test", authToken="test2")))

    def test_predict(self):
        self.gate_to_service.put(GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        self.wait_for(lambda: self.callback.request.call_count > 0)
