import time
from queue import Queue
from unittest.mock import Mock

import pytest

from mlp_sdk.abstract.services import MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import ClusterUpdateProto, GateToServiceProto, ServiceDescriptorProto, ServiceToGateProto
from mlp_sdk.mlp_connector.multi_host_connector import MlpGrpcRequestReceiver, MlpMultiHostConnector
from mlp_sdk.mlp_connector.single_host_connector import MlpConnectorState
from mlp_sdk.utils.config import BaseConfig
from mlp_sdk.utils.utils import wait_for


class TestMlpMultiHostConnector(MlpGrpcRequestReceiver):
    def create_single_connector(self, host_port: str):
        m = Mock()
        m.host_port = host_port
        m.action_to_gate_queue = Queue()
        # Mock enqueue_to_gate как реальный продюсер в очередь — иначе ассерты по
        # action_to_gate_queue не сработают.
        m.enqueue_to_gate.side_effect = lambda msg: m.action_to_gate_queue.put_nowait(msg) or True
        self.connectors[host_port] = m
        return m

    def setup_config(self):
        self.config = BaseConfig()
        self.config.mlp.grpc_hosts = "host1,host2"
        self.config.mlp.grpc_secure = True
        self.config.mlp.service_token = "test"

    def setup_method(self):
        self.descriptor = ServiceDescriptorProto(name=self.__class__.__name__, fittable=False, methods={}, schemaFiles={})
        self.setup_config()
        self.connector = MlpMultiHostConnector(self.descriptor, config=self.config)
        self.connectors = {}
        self.requests = []
        self.connector._create_single_connector = self.create_single_connector
        self.connector.set_receiver(self)
        self.connector.start()

    def message_from_gate(self, context: MlpRequestContext, request: GateToServiceProto) -> None:
        self.requests.append((context, request))

    def teardown_method(self):
        self.connector.stop_and_wait()

    def test_start(self):
        assert len(self.connector.connectors) == 2
        self.connectors["host1"].start.assert_called_once()
        self.connectors["host2"].start.assert_called_once()

        old_active_time = self.connector.last_active_time
        self.connector._check_connected()
        assert self.connector.last_active_time == old_active_time

        self.connectors["host1"].state = MlpConnectorState.serving
        self.connector._check_connected()

        self.connector._check_connected()
        assert self.connector.last_active_time > old_active_time

    def test_restart_broken_connection(self):
        old_connector = self.connectors["host1"]
        old_connector.state = MlpConnectorState.error

        self.connector._check_connected()

        new_connector = self.connectors["host1"]
        old_connector.stop_and_wait.assert_called_once()
        new_connector.start.assert_called_once()

    def test_cluster_update(self):
        h1 = self.connectors["host1"]
        h2 = self.connectors["host2"]

        self.connector.cluster_update(ClusterUpdateProto(servers=["host2", "host3"]))
        h3 = self.connectors["host3"]

        h1.start.assert_called_once()
        wait_for(lambda: h1.stop_and_wait.call_count == 1)
        h2.start.assert_called_once()
        h3.start.assert_called_once()

    def test_reset_to_initial(self):
        self.connector.cluster_update(ClusterUpdateProto(servers=[]))

        wait_for(lambda: len(self.connector.connectors) == 0)

        self.connector.last_active_time = time.time() - 10
        self.connector._check_connected()

        assert len(self.connector.connectors) == 2

        self.connectors["host1"].start.assert_called_once()
        self.connectors["host2"].start.assert_called_once()

    def test_cluster_update_with_same_servers(self):
        h1 = self.connectors["host1"]
        h1.start.assert_called_once()

        self.connector.cluster_update(ClusterUpdateProto(servers=["host1", "host2"]))

        assert self.connectors["host1"] == h1
        h1.start.assert_called_once()

    def test_predict(self):
        self.connectors["host1"].state = MlpConnectorState.serving

        self.connector.request(GateToServiceProto(), self.connectors["host1"])

        assert len(self.requests) == 1
        assert self.requests[0][0].gatewayId == "host1"

        self.connector.message_from_service(self.requests[0][0], ServiceToGateProto())

        res = self.connectors["host1"].action_to_gate_queue.get_nowait()
        assert res

    def test_cant_send_response_to_inactive_gateway(self):
        self.connectors["host1"].state = MlpConnectorState.stopped

        with pytest.raises(ValueError):
            self.connector.message_from_service(MlpRequestContext(requestId=1, gatewayId="host1", request_headers={}), ServiceToGateProto())

    def test_restart_does_not_hold_lock_during_stop(self):
        # Bug 5: stop_and_wait может джойнить worker_thread / heartbeat_thread —
        # это секунды (особенно при долгом reconnect-цикле). Раньше
        # restart_single_connection держал connectors_lock всё это время,
        # блокируя cluster_update / message_from_service / shutdown.
        import threading

        h1 = self.connectors["host1"]
        h1.state = MlpConnectorState.error

        stop_started = threading.Event()
        stop_can_finish = threading.Event()

        def slow_stop(*args, **kwargs):
            stop_started.set()
            stop_can_finish.wait(timeout=5.0)

        h1.stop_and_wait.side_effect = slow_stop

        restart_thread = threading.Thread(
            target=lambda: self.connector.restart_single_connection(h1),
            daemon=True,
        )
        restart_thread.start()

        try:
            assert stop_started.wait(timeout=2.0), "stop_and_wait должен быть вызван"

            # Пока stop_and_wait висит — connectors_lock должен быть свободен
            # для других операций (cluster_update, message_from_service, shutdown).
            got_lock = self.connector.connectors_lock.acquire(timeout=1.0)
            try:
                assert got_lock, "connectors_lock не должен держаться во время stop_and_wait"
            finally:
                if got_lock:
                    self.connector.connectors_lock.release()
        finally:
            stop_can_finish.set()
            restart_thread.join(timeout=2.0)
