import threading
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, Optional, Set

from mlp_sdk.abstract.services import MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import ClusterUpdateProto, GateToServiceProto, ServiceDescriptorProto, ServiceToGateProto
from mlp_sdk.mlp_connector.single_host_connector import MlpConnectorState, MlpSingleHostConnector, MlpSingleHostConnectorCallback
from mlp_sdk.utils.config import get_config
from mlp_sdk.utils.logger import get_logger

log = get_logger("MlpMultiHostConnector")
config = get_config()


class MlpGrpcRequestReceiver:
    def message_from_gate(self, context: MlpRequestContext, request: GateToServiceProto) -> None:
        pass


class MlpGrpcResponseReceiver:
    def message_from_service(self, context: MlpRequestContext, response: ServiceToGateProto) -> None:
        pass


class MlpMultiHostConnector(MlpSingleHostConnectorCallback, MlpGrpcResponseReceiver):
    def __init__(self, service_info: ServiceDescriptorProto):  # mlp_gate_url: str | None = None, mlp_service_token: str | None =None):
        self.state: MlpConnectorState = MlpConnectorState.idle
        self.gate_urls: List[str] = config.mlp.get_grpc_hosts()
        self.grpc_secure: bool = config.mlp.grpc_secure
        log.info(f"Initializing multi-host-connector with urls: {self.gate_urls}, secure: {self.grpc_secure}")

        self.connectors: List[MlpSingleHostConnector] = []
        self.connectors_lock: threading.Lock = threading.Lock()
        if not config.mlp.service_token:
            raise Exception("MLP_SERVICE_TOKEN is required")
        self.connection_token: str = config.mlp.service_token

        self.requests_executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=config.sdk.requests_executor_pool_size)

        self.receiver: Optional[MlpGrpcRequestReceiver] = None
        self.descriptor: ServiceDescriptorProto = service_info

        self.keep_connection_thread: threading.Thread = threading.Thread(target=self.__keep_connected())

    def set_receiver(self, receiver: MlpGrpcRequestReceiver) -> None:
        self.receiver = receiver

    def start(
        self,
    ) -> None:
        with self.connectors_lock:
            for url in self.gate_urls:
                self.__start_connector(url)

        self.state = MlpConnectorState.serving
        self.keep_connection_thread.start()

    def __start_connector(self, host_port: str) -> None:
        connector = MlpSingleHostConnector(host_port, self.grpc_secure, self.connection_token, self.descriptor, self)
        self.connectors.append(connector)
        connector.start()

    def __stop_connector(self, connector: MlpSingleHostConnector, state: Optional[MlpConnectorState] = None) -> None:
        if not state:
            connector.stop_and_wait()
        else:
            connector.stop_and_wait(state=state)
        if connector in self.connectors:
            self.connectors.remove(connector)

    def __keep_connected(self) -> Callable[[], None]:
        def _keep_connected_impl() -> None:
            last_active_time = time.time()
            while self.state == MlpConnectorState.serving:
                time.sleep(1)

                stopped_connectors: List[MlpSingleHostConnector] = [
                    c for c in self.connectors if c.state in (MlpConnectorState.stopped, MlpConnectorState.error)
                ]
                for stopped_connector in stopped_connectors:
                    self.restart_single_connection(stopped_connector)

                with self.connectors_lock:
                    if any(c.state == MlpConnectorState.connected or c.state == MlpConnectorState.serving for c in self.connectors):
                        last_active_time = time.time()
                        continue

                    # сюда попадаем только если нет ни одного активного подключения
                    if time.time() > last_active_time + 5:
                        log.warning("Reset connection list to the initial: " + str(self.gate_urls))
                        self.update_connectors(self.gate_urls)
                        last_active_time = time.time()

        return _keep_connected_impl

    def cluster_update(self, message: ClusterUpdateProto) -> None:
        self.update_connectors(list(message.servers))

    def update_connectors(self, servers: List[str]) -> None:
        with self.connectors_lock:
            # 1. compare with what we know
            current_urls: Set[str] = {x.host_port for x in self.connectors}
            new_urls: Set[str] = set(servers)
            if current_urls == new_urls:
                return

            # 2. start new
            urls_to_add: Set[str] = new_urls - current_urls
            if len(urls_to_add) > 0:
                log.info("Add active hosts: " + str(urls_to_add))
            for url in urls_to_add:
                self.__start_connector(url)

            # 3. remove obsolete
            urls_to_remove: Set[str] = current_urls - new_urls
            if len(urls_to_remove) > 0:
                log.info("remove from active list: " + str(urls_to_remove))
            for url in urls_to_remove:
                connector: MlpSingleHostConnector | None = next(filter(lambda x: x.host_port == url, self.connectors), None)
                if connector is not None:
                    threading.Thread(target=self.__stop_connector, args=(connector,)).start()

    def restart_single_connection(self, connector: MlpSingleHostConnector) -> None:
        with self.connectors_lock:
            self.__stop_connector(connector, MlpConnectorState.error)

            log.info(f"Restart single connection {connector.host_port} ...")
            self.__start_connector(connector.host_port)

    def stop_and_wait(self) -> None:
        if self.state == MlpConnectorState.stopping:
            return

        log.info("Shutdown")
        self.state = MlpConnectorState.stopping

        connectors: List[MlpSingleHostConnector] = self.connectors.copy()
        for connector in connectors:
            connector.stop_and_wait()

    def message_from_service(self, context: MlpRequestContext, response: ServiceToGateProto) -> None:
        response.requestId = context.requestId
        connector: Optional[MlpSingleHostConnector] = next(
            (x for x in self.connectors if x.host_port == context.gatewayId and x.state == MlpConnectorState.serving), None
        )
        if not connector:
            raise Exception(f"Gateway {context.gatewayId} went offline")

        connector.action_to_gate_queue.put(response)

    def request(self, request: GateToServiceProto, connector: MlpSingleHostConnector) -> None:
        context: MlpRequestContext = MlpRequestContext(requestId=request.requestId, gatewayId=connector.host_port, request_headers=dict(request.headers))

        if self.receiver is None:
            raise Exception("receiver must be set")
        self.receiver.message_from_gate(context, request)
