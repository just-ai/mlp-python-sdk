import threading

import queue

from unittest.mock import Mock

import grpc
import pytest
import time

from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import ServiceDescriptorProto, GateToServiceProto, HeartBeatProto, \
    StopServingProto
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2_grpc import GateStub
from mlp_sdk.mlp_connector.single_host_connector import MlpSingleHostConnector, MlpConnectorState


class TestMlpSingleHostConnector:

    def setup_method(self):
        self.service_descriptor = ServiceDescriptorProto()
        self.callback = Mock()
        self.connector = MlpSingleHostConnector(
            "host:9999", True, "connection_token", self.service_descriptor, self.callback
        )
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

    def teardown_method(self):
        self.gate_to_service.put_nowait(None)
        self.service_to_gate_thread.join()

    def __setup_process_async_mock(self):
        def read_generator(generator):
            for request in generator:
                self.service_to_gate.append(request)

        def process_async_mock(generator):
            # Consume the generator to get the requests
            self.service_to_gate_thread = threading.Thread(target=read_generator, args=generator)
            self.service_to_gate_thread.start()

            # Return our predefined responses
            while True:
                m = self.gate_to_service.get()
                if m is not None:
                    yield m
                else:
                    break

        self.stub_mock.processAsync = Mock(side_effect=process_async_mock)

    def wait_for(self, condition, timeout=5):
        """Wait for a condition to be true with a timeout."""
        start_time = time.time()
        while not condition() and time.time() - start_time < timeout:
            time.sleep(0.1)
        return condition()

    def wait_for_state(self, expected_state, timeout=5):
        """Wait for the connector to reach the expected state with a timeout."""
        start_time = time.time()
        counter = 0
        while self.connector.state != expected_state and time.time() - start_time < timeout:
            if counter % 10 == 0:
                print(f"Waiting for transition to state: {expected_state}, current state: {self.connector.state} ...")
            time.sleep(0.1)
            counter += 1
        return self.connector.state == expected_state

    def test_start_stop(self):
        # Start the connector
        self.connector.start()

        # Wait for the connector to reach connected state
        assert self.wait_for_state(MlpConnectorState.serving)

        # Verify that healthCheck was called
        self.stub_mock.healthCheck.assert_called_once()

        # Verify that processAsync was called
        self.stub_mock.processAsync.assert_called_once()

        # Stop the connector
        self.connector.stop_and_wait()

        # Wait for the connector to reach stopped state
        assert self.wait_for_state(MlpConnectorState.stopped)

    def test_stop_serving(self):
        # Start the connector
        self.connector.start()

        # Wait for the connector to reach connected state
        assert self.wait_for_state(MlpConnectorState.serving)

        # Send StopServing message from gate to service
        stop_serving_message = GateToServiceProto(stopServing=StopServingProto())
        self.gate_to_service.put(stop_serving_message)

        # Wait for the connector to reach stopped state
        assert self.wait_for_state(MlpConnectorState.stopped)
