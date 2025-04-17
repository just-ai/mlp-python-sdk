from typing import TypeVar

from mlp_sdk.abstract.services import MlpPredictServiceBase
from mlp_sdk.mlp_connector.grpc_service_adapter import MlpGrpcServiceAdapter
from mlp_sdk.mlp_connector.grpc_service_base import MlpGrpcServiceBase
from mlp_sdk.mlp_connector.grpc_typed_adapter import MlpGrpcTypedAdapter
from mlp_sdk.mlp_connector.multi_host_connector import MlpMultiHostConnector

T = TypeVar("T")
C = TypeVar("C")
R = TypeVar("R")


class MlpGrpcServicer:
    def __init__(self, service: MlpPredictServiceBase[T, C, R] | MlpGrpcServiceBase):
        if isinstance(service, MlpGrpcServiceBase):
            self.grpc_service = service
        else:
            self.grpc_service = MlpGrpcTypedAdapter(service)
        self.grpc_adapter = MlpGrpcServiceAdapter(self.grpc_service)
        self.connector = MlpMultiHostConnector(self.grpc_service.get_descriptor())
        self.connector.set_receiver(self.grpc_adapter)
        self.grpc_adapter.set_response_receiver(self.connector)

    def start(self):
        self.connector.start()

    def stop(self):
        self.connector.stop_and_wait()
