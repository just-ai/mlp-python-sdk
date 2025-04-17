import dataclasses
import json
from dataclasses import is_dataclass
from typing import Any, Generator, Optional, Type, TypeVar, cast

from dacite import from_dict
from google.protobuf.message import Message
from pydantic import BaseModel

from mlp_sdk.abstract.services import MlpPredictServiceBase, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import PayloadProto
from mlp_sdk.mlp_connector.grpc_service_base import MlpGrpcServiceBase

T = TypeVar("T")
C = TypeVar("C")
R = TypeVar("R")


class MlpGrpcTypedAdapter(MlpGrpcServiceBase):
    def __init__(self, impl: MlpPredictServiceBase[Any, Any, Any]):
        self.impl = impl

    def predict(
        self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        if not isinstance(req, Generator):
            converted_req = self.convert_from_payload(req, self.impl.clazz_t)
        else:

            def convert_req() -> Generator[Any]:
                for x in req:
                    yield self.convert_from_payload(x, self.impl.clazz_t)

            converted_req = convert_req()

        converted_conf = None
        if config is not None:
            converted_conf = self.convert_from_payload(config, self.impl.clazz_c)

        typed_res = self.impl.predict(context, converted_req, converted_conf)

        if not isinstance(typed_res, Generator):
            converted_res = self.convert_to_payload(typed_res)
        else:

            def convert_res() -> Generator[PayloadProto, None, None]:
                for x in cast(Generator[Any], typed_res):
                    yield self.convert_to_payload(x)

            converted_res = convert_res()

        return converted_res

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
            elif isinstance(data_type, dict):
                return cast(T, json.loads(payload.json))
            else:
                raise Exception("Unsupported type")
        elif payload.protobuf:
            if issubclass(data_type, Message):
                msg = data_type()
                msg.ParseFromString(payload.protobuf)
                return msg
            else:
                raise Exception("It must be protobuf type to use with payload.protobuf")

        raise Exception("Empty payload")

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

        raise Exception("Unsupported response type")
