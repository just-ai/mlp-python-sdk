from dataclasses import dataclass
from typing import Any

import pytest
from pydantic import BaseModel

from mlp_sdk.abstract.services import MlpException, MlpPredictServiceBase, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import HeartBeatProto, PayloadProto
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


class ImplOutputStream(MlpPredictServiceBase[InputModel, None, OutputModel]):
    def __init__(self):
        super().__init__(InputModel, None, OutputModel)

    def predict(self, context, request, config):
        for i in range(0, 10):
            yield OutputModel(result=str(i))


class ImplInputStream(MlpPredictServiceBase[InputModel, None, OutputModel]):
    def __init__(self):
        super().__init__(InputModel, None, OutputModel)

    def predict(self, context, request, config):
        # Process a stream of inputs and return a single result
        count = 0
        result = ""
        for req in request:
            count += 1
            result += req.value

        return OutputModel(result=f"{result}_{count}")


class ImplProtobuf(MlpPredictServiceBase[HeartBeatProto, None, HeartBeatProto]):
    def __init__(self):
        super().__init__(HeartBeatProto, None, HeartBeatProto)

    def predict_simple(self, context, request: HeartBeatProto, config: None):
        # Echo the request with a modified timestamp
        response = HeartBeatProto(status="res", interval=request.interval * 2)
        return response


class ImplRawPayload(MlpPredictServiceBase[PayloadProto, None, PayloadProto]):
    def __init__(self):
        super().__init__(PayloadProto, None, PayloadProto)

    def predict_simple(self, context, request: PayloadProto, config: None):
        # Create a new payload with modified content
        if request.json:
            # If JSON, add a new field
            data = JSON.parse_(request.json)
            data["processed"] = True
            return PayloadProto(json=JSON.stringify(data))
        elif request.protobuf:
            # If protobuf, just echo it back
            return PayloadProto(protobuf=request.protobuf)
        else:
            # Empty payload case
            return PayloadProto(json=JSON.stringify({"error": "Empty payload received"}))


class ImplExt(MlpPredictServiceBase[InputModel, None, OutputModel]):
    def __init__(self):
        super().__init__(InputModel, None, OutputModel)

    def ext_models(self, context: MlpRequestContext, param1: str, param2: int) -> OutputModel:
        return OutputModel(result=param1 * param2)

    def ext_no_context(self, param1: str, param2: int) -> OutputModel:
        return OutputModel(result=param1 * param2)

    def ext_payload(self, context: MlpRequestContext, param1) -> str:
        return param1.json

    def ext_wrong_first_param(self, wrong_param: str, param2: int) -> OutputModel:
        return OutputModel(result=wrong_param * param2)


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

    def test_ext_method(self):
        # Initialize with the implementation that has ext methods
        self.init(ImplExt())

        # Create parameters for the ext method
        param1 = payload("test")
        param2 = payload(3)
        params = {"param1": param1, "param2": param2}

        # Call the ext method
        result = self.adapter.ext(self.context, "models", params)

        # Verify the result
        assert isinstance(result, PayloadProto)
        result_data = JSON.parse_(result.json)
        assert result_data["result"] == "testtesttest"  # "test" * 3

    def test_ext_method_not_found(self):
        self.init(ImplExt())

        params = {}

        # Call a non-existent ext method
        with pytest.raises(MlpException) as excinfo:
            self.adapter.ext(self.context, "model2", params)

        # Verify the exception details
        assert excinfo.value.code == "mlp-action.common.method-not-supported"
        assert "Ext method ext_model2 not found" in excinfo.value.message

    def test_output_stream(self):
        # Initialize with the implementation that returns a stream
        self.init(ImplOutputStream())

        # Create test request
        req = payload(InputModel(value="test"))

        # Call the adapter's predict method
        result = self.adapter.predict(self.context, req, None)

        # Verify the result is a generator
        assert hasattr(result, "__next__")

        # Collect all results from the generator
        results = list(result)

        # Verify we got 10 results
        assert len(results) == 10

        # Verify each result is a PayloadProto
        for i, res in enumerate(results):
            assert isinstance(res, PayloadProto)
            result_data = JSON.parse_(res.json)
            assert result_data["result"] == str(i)

    def test_input_stream(self):
        # Initialize with the implementation that accepts a stream
        self.init(ImplInputStream())

        # Create a generator of input requests
        def input_stream():
            for i in range(5):
                yield payload(InputModel(value=f"input{i}"))

        # Call the adapter's predict method with a stream
        result = self.adapter.predict(self.context, input_stream(), None)

        # Verify the result is a single PayloadProto (not a generator)
        assert isinstance(result, PayloadProto)

        # Parse the result JSON
        result_data = JSON.parse_(result.json)

        # Verify the result contains all inputs concatenated and the count
        assert result_data["result"] == "input0input1input2input3input4_5"

    def test_protobuf_data(self):
        # Initialize with the implementation that works with protobuf
        self.init(ImplProtobuf())

        # Create a protobuf message
        heartbeat = HeartBeatProto(status="test", interval=5)

        # Create a PayloadProto with protobuf data
        proto_payload = PayloadProto(protobuf=heartbeat.SerializeToString())

        # Call the adapter's predict method
        result = self.adapter.predict(self.context, proto_payload, None)

        # Verify the result is a PayloadProto with protobuf data
        assert isinstance(result, PayloadProto)
        assert result.protobuf
        assert not result.json

        # Parse the protobuf result
        result_heartbeat = HeartBeatProto()
        result_heartbeat.ParseFromString(result.protobuf)

        # Verify the result has the expected values
        assert result_heartbeat.status == "res"
        assert result_heartbeat.interval == 10

    def test_raw_payload(self):
        # Initialize with the implementation that works directly with PayloadProto
        self.init(ImplRawPayload())

        # Create a JSON payload
        json_data = {"test": "value"}
        json_payload = PayloadProto(json=JSON.stringify(json_data))

        # Call the adapter's predict method
        result = self.adapter.predict(self.context, json_payload, None)

        # Verify the result is a PayloadProto with JSON data
        assert isinstance(result, PayloadProto)
        assert result.json

        # Parse the JSON result
        result_data = JSON.parse_(result.json)

        # Verify the result has the expected values
        assert result_data["test"] == "value"
        assert result_data["processed"] is True

        # Test with protobuf payload
        heartbeat = HeartBeatProto(status="test", interval=5)
        proto_payload = PayloadProto(protobuf=heartbeat.SerializeToString())

        # Call the adapter's predict method
        result = self.adapter.predict(self.context, proto_payload, None)

        # Verify the result is a PayloadProto with protobuf data
        assert isinstance(result, PayloadProto)
        assert result.protobuf

        # Test with empty payload
        empty_payload = PayloadProto()
        result = self.adapter.predict(self.context, empty_payload, None)

        # Verify the result contains the error message
        assert isinstance(result, PayloadProto)
        assert result.json
        result_data = JSON.parse_(result.json)
        assert "error" in result_data

    def test_ext_payload_method(self):
        # Initialize with the implementation that has ext_payload method
        self.init(ImplExt())

        # Create a JSON payload
        json_data = {"test": "value"}
        json_payload = PayloadProto(json=JSON.stringify(json_data))
        params = {"param1": json_payload}

        # Call the ext_payload method
        result = self.adapter.ext(self.context, "payload", params)

        # Verify the result is the JSON string from the payload
        assert isinstance(result, PayloadProto)
        assert result.json
        assert JSON.parse_(result.json) == JSON.stringify(json_data)

    def test_ext_wrong_first_param(self):
        # Initialize with the implementation that has a method with wrong first parameter
        self.init(ImplExt())

        params = {"wrong_param": payload("test"), "param2": payload(3)}

        # Call the method with wrong first parameter
        with pytest.raises(MlpException) as excinfo:
            self.adapter.ext(self.context, "wrong_first_param", params)

        # Verify the exception details
        assert excinfo.value.code == "mlp-action.common.internal-error"
        assert "First parameter of ext_wrong_first_param must be 'context'" in excinfo.value.message

    def test_ext_param_count_mismatch(self):
        # Initialize with the implementation
        self.init(ImplExt())

        # Create parameters with wrong count (missing param2)
        params = {"param1": payload("test")}

        # Call the ext method with wrong parameter count
        with pytest.raises(MlpException) as excinfo:
            self.adapter.ext(self.context, "models", params)

        # Verify the exception details
        assert excinfo.value.code == "mlp-action.common.internal-error"
        assert "Method ext_models expects 2 parameters" in excinfo.value.message

    def test_ext_param_name_mismatch(self):
        # Initialize with the implementation
        self.init(ImplExt())

        # Create parameters with wrong name
        params = {"wrong_name": payload("test"), "param2": payload(3)}

        # Call the ext method with wrong parameter name
        with pytest.raises(MlpException) as excinfo:
            self.adapter.ext(self.context, "models", params)

        # Verify the exception details
        assert excinfo.value.code == "mlp-action.common.internal-error"
        assert "Parameter param1 not found in request" in excinfo.value.message
