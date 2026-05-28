import dataclasses
import inspect
import json
from collections.abc import Generator as GeneratorABC
from dataclasses import is_dataclass
from typing import Any, Generator, Optional, Type, TypeVar, cast

from dacite import from_dict
from google.protobuf.message import Message
from pydantic import BaseModel

from mlp_sdk.abstract.services import MlpErrorStatus, MlpException, MlpPredictServiceBase, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import BatchPayloadProto, BatchPayloadResponseProto, PayloadProto, PredictResponseProto
from mlp_sdk.mlp_connector.grpc_service_base import MlpGrpcServiceBase
from mlp_sdk.utils.json_ import JSON

T = TypeVar("T")
C = TypeVar("C")
R = TypeVar("R")


class MlpGrpcTypedAdapter(MlpGrpcServiceBase):
    def __init__(self, impl: MlpPredictServiceBase[Any, Any, Any]):
        self.impl = impl

    def predict(
        self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        if not isinstance(req, GeneratorABC):
            converted_req = self.convert_from_payload(req, self.impl.clazz_t)
        else:

            def convert_req() -> Generator[Any, None, None]:
                for x in req:
                    yield self.convert_from_payload(x, self.impl.clazz_t)

            converted_req = convert_req()

        converted_conf = None
        if config is not None:
            converted_conf = self.convert_from_payload(config, self.impl.clazz_c)

        typed_res = self.impl.predict(context, converted_req, converted_conf)

        if not isinstance(typed_res, GeneratorABC):
            converted_res = self.convert_to_payload(typed_res)
        else:

            def convert_res() -> Generator[PayloadProto, None, None]:
                for x in cast(Generator[Any, None, None], typed_res):
                    yield self.convert_to_payload(x)

            converted_res = convert_res()

        return converted_res

    def predict_batch(
        self,
        context: MlpRequestContext,
        req: list[BatchPayloadProto],
        config: Optional[PayloadProto],
    ) -> list[BatchPayloadResponseProto]:
        converted_conf = None
        if config is not None:
            converted_conf = self.convert_from_payload(config, self.impl.clazz_c)

        contexts = [
            MlpRequestContext(
                requestId=item.requestId,
                gatewayId=context.gatewayId,
                request_headers=context.request_headers,
                response_headers=dict(context.response_headers),
                content_hidden=context.content_hidden,
            )
            for item in req
        ]

        converted_requests: list[Any | None] = []
        item_errors = []
        for item in req:
            try:
                converted_requests.append(self.convert_from_payload(item.data, self.impl.clazz_t))
                item_errors.append(None)
            except BaseException as e:
                converted_requests.append(None)
                item_errors.append(MlpException.exception_to_proto(e))

        typed_responses = self.impl.predict_batch_simple(contexts, converted_requests, converted_conf)
        if len(typed_responses) != len(req):
            error = MlpException.exception_to_proto(
                MlpException(
                    code="mlp-action.common.internal-error",
                    message=f"Batch response length mismatch: expected {len(req)}, got {len(typed_responses)}",
                )
            )
            return [
                BatchPayloadResponseProto(requestId=item.requestId, predict=PredictResponseProto(), error=error, headers=contexts[i].response_headers)
                for i, item in enumerate(req)
            ]

        result: list[BatchPayloadResponseProto] = []
        for item, item_context, typed_response, item_error in zip(req, contexts, typed_responses, item_errors, strict=True):
            payload_response = None
            error = item_error
            if error is None and typed_response is not None:
                try:
                    if isinstance(typed_response, GeneratorABC):
                        raise Exception("Predict must not return streaming result to use in batch mode")
                    payload_response = self.convert_to_payload(typed_response)
                except BaseException as e:
                    error = MlpException.exception_to_proto(e)

            result.append(
                BatchPayloadResponseProto(
                    requestId=item.requestId,
                    predict=PredictResponseProto(data=payload_response) if payload_response is not None else PredictResponseProto(),
                    error=error,
                    headers=item_context.response_headers,
                )
            )

        return result

    def ext(self, context: MlpRequestContext, method_name: str, params: dict[str, PayloadProto]) -> PayloadProto:
        # Find the method in the child class with the name ext_method_name
        impl_name = f"ext_{method_name}"
        if not hasattr(self.impl, impl_name):
            raise MlpException(
                code="mlp-action.common.method-not-supported",
                message=f"Ext method {impl_name} not found in {self.impl.__class__.__name__}",
                status=MlpErrorStatus.BAD_REQUEST,
            )

        method = getattr(self.impl, impl_name)

        # Get method's arguments and their types
        signature = inspect.signature(method)
        method_params = {}

        # First parameter is always context
        if list(signature.parameters.keys())[0] != "context":
            raise MlpException(
                code="mlp-action.common.internal-error", message=f"First parameter of {impl_name} must be 'context'", status=MlpErrorStatus.BAD_REQUEST
            )

        # Check if the number of parameters matches (excluding context)
        expected_params = list(signature.parameters.keys())[1:]
        if len(expected_params) != len(params):
            raise MlpException(
                code="mlp-action.common.internal-error",
                message=f"Method {impl_name} expects {len(expected_params)} parameters, but {len(params)} were provided",
                status=MlpErrorStatus.BAD_REQUEST,
            )

        # Check if parameter names match and convert them
        for param_name in expected_params:
            if param_name not in params:
                raise MlpException(
                    code="mlp-action.common.internal-error", message=f"Parameter {param_name} not found in request", status=MlpErrorStatus.BAD_REQUEST
                )

            param_type = signature.parameters[param_name].annotation
            if param_type is inspect.Parameter.empty:
                # If no type annotation, use PayloadProto for no conversion
                param_type = PayloadProto

            method_params[param_name] = self.convert_from_payload(params[param_name], param_type)

        # Call the method
        result = method(context, **method_params)

        # Convert the result to Payload and return
        return self.convert_to_payload(result)

    @staticmethod
    def convert_from_payload(payload: PayloadProto, data_type: Type[T]) -> T:
        # Ожидаем что типом type будет либо Pydantic либо dataclass для json-формата и protobuf для proto формата
        if data_type == PayloadProto:
            return payload  # type: ignore
        elif payload.json:
            if issubclass(data_type, BaseModel):
                return data_type.model_validate_json(payload.json)
            elif is_dataclass(data_type):
                dd = json.loads(payload.json)
                return from_dict(data_class=data_type, data=dd)
            else:
                return JSON.parse_(payload.json)
        elif payload.protobuf:
            if issubclass(data_type, Message):
                msg = data_type()
                msg.ParseFromString(payload.protobuf)
                return msg
            else:
                raise Exception("It must be protobuf type to use with payload.protobuf")  # pragma: no cover

        raise Exception("Empty payload")  # pragma: no cover

    @staticmethod
    def convert_to_payload(data: Any) -> PayloadProto:
        if isinstance(data, PayloadProto):
            return data
        elif isinstance(data, BaseModel):
            return PayloadProto(json=data.model_dump_json())
        elif is_dataclass(data):
            return PayloadProto(json=json.dumps(dataclasses.asdict(data)))  # type: ignore
        elif isinstance(data, Message):
            return PayloadProto(protobuf=data.SerializeToString())
        else:
            return PayloadProto(json=JSON.stringify(data))
