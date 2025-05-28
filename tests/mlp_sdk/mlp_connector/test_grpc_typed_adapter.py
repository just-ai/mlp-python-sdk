from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from mlp_sdk.abstract.services import MlpPredictServiceBase, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import PayloadProto
from mlp_sdk.mlp_connector.grpc_typed_adapter import MlpGrpcTypedAdapter
from mlp_sdk.utils.json_ import JSON


class InputModel(BaseModel):
    value: str


class ConfigModel(BaseModel):
    multiplier: int = 1


class OutputModel(BaseModel):
    result: str


@dataclass
class DataclassInput:
    value: str


@dataclass
class DataclassConfig:
    multiplier: int = 1


@dataclass
class DataclassOutput:
    result: str


class Impl1(MlpPredictServiceBase[InputModel, ConfigModel, OutputModel]):
    def __init__(self):
        super().__init__(InputModel, ConfigModel, OutputModel)

    def predict_simple(self, context, request, config):
        multiplier = config.multiplier if config else 1
        return OutputModel(result=request.value * multiplier)


class ImplDataclass(MlpPredictServiceBase[DataclassInput, DataclassConfig, DataclassOutput]):
    def __init__(self):
        super().__init__(DataclassInput, DataclassConfig, DataclassOutput)

    def predict_simple(self, context, request, config):
        multiplier = config.multiplier if config else 1
        return DataclassOutput(result=request.value * multiplier)


def payload(data: Any) -> PayloadProto:
    return PayloadProto(json=JSON.stringify(data))


class TestMlpGrpcTypedAdapter:
    def init(self, impl):
        self.impl = impl
        self.adapter = MlpGrpcTypedAdapter(impl)
        self.context = MlpRequestContext(requestId=123, gatewayId="test", request_headers={})

    def test_simple(self):
        # Initialize with the test implementation
        self.init(Impl1())

        # Create test request and config as PayloadProto objects
        req = payload(InputModel(value="test"))

        config = payload(ConfigModel(multiplier=3))

        # Call the adapter's predict method
        result = self.adapter.predict(self.context, req, config)

        # Verify the result
        assert isinstance(result, PayloadProto)
        result_data = JSON.parse_(result.json)
        assert result_data["result"] == "testtesttest"  # "test" * 3

    def test_dataclass(self):
        # Initialize with the dataclass implementation
        self.init(ImplDataclass())

        # Create test request and config as PayloadProto objects
        req = payload({"value": "abc"})

        config = payload({"multiplier": 2})

        # Call the adapter's predict method
        result = self.adapter.predict(self.context, req, config)

        # Verify the result
        assert isinstance(result, PayloadProto)
        result_data = JSON.parse_(result.json)
        assert result_data["result"] == "abcabc"  # "abc" * 2

    def test_without_config(self):
        # Initialize with the test implementation
        self.init(Impl1())

        # Create test request without config
        req = payload(InputModel(value="x"))

        # Call the adapter's predict method without config
        result = self.adapter.predict(self.context, req, None)

        # Verify the result
        assert isinstance(result, PayloadProto)
        result_data = JSON.parse_(result.json)
        assert result_data["result"] == "x"  # Default multiplier is 1
