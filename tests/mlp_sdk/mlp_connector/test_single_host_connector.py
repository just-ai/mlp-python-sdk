import queue

from unittest.mock import Mock

import grpc
import pytest
import time

from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import ServiceDescriptorProto, GateToServiceProto, HeartBeatProto
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

    def __setup_process_async_mock(self):
        def process_async_mock(generator):
            # Consume the generator to get the requests
            for request in generator:
                self.service_to_gate.append(request)
            # Return our predefined responses
            while not self.gate_to_service.empty():
                yield self.gate_to_service.get()
        
        self.stub_mock.processAsync = Mock(side_effect=process_async_mock)

    def wait_for(self, condition, timeout=5):
        """Wait for a condition to be true with a timeout."""
        start_time = time.time()
        while not condition() and time.time() - start_time < timeout:
            time.sleep(0.1)
        return condition()

    def test_start_stop(self):
        # Start the connector
        self.connector.start()
        
        # Wait for the connector to reach connected state
        assert self.wait_for(lambda: self.connector.state == MlpConnectorState.serving)
        
        # Verify that the connector reached the connected state
        assert self.connector.state == MlpConnectorState.serving
        
        # Verify that healthCheck was called
        self.stub_mock.healthCheck.assert_called_once()
        
        # Verify that processAsync was called
        self.stub_mock.processAsync.assert_called_once()
        
        # Stop the connector
        self.connector.stop_and_wait()

        # Wait for the connector to reach stopped state
        self.wait_for(lambda: self.connector.state == MlpConnectorState.stopped)
        print(self.connector.state)
        
        # Verify that the connector reached the stopped state
        assert self.connector.state == MlpConnectorState.stopped
