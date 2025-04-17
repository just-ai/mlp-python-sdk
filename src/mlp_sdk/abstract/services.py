from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable, Optional, Type, TypeVar

from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import SimpleStatusProto


@dataclass
class MlpRequestContext:
    requestId: int
    gatewayId: str
    request_headers: dict[str, str]
    response_headers: dict[str, str] = field(default_factory=dict)


class MlpErrorStatus(Enum):
    OK = 0
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

    def to_proto(self) -> SimpleStatusProto:
        return getattr(SimpleStatusProto, self.name)

    @staticmethod
    def from_proto(val: SimpleStatusProto) -> "MlpErrorStatus":
        for v in SimpleStatusProto.DESCRIPTOR.values:
            if v.number == val:
                return getattr(MlpErrorStatus, v.name)
        raise Exception(f"Unknown SimpleStatusProto value {val}")


@dataclass
class MlpException(Exception):
    code: str  # короткий код ошибки
    message: str  # дефолтный текст описания ошибки на английском языке
    status: MlpErrorStatus = MlpErrorStatus.INTERNAL_SERVER_ERROR
    named_args: dict[str, str] = field(default_factory=dict)
    headers: dict[str, str] | None = None

    def __str__(self) -> str:
        return f"{self.code}: {self.message}"


T = TypeVar("T")
C = TypeVar("C")
R = TypeVar("R")


@dataclass
class EmptyData:
    pass


class MlpPredictServiceBase[T, C, R]:
    def __init__(self, clazz_t: Type[T], clazz_c: Type[C], clazz_r: Type[R]):
        self.clazz_t = clazz_t
        self.clazz_c = clazz_c
        self.clazz_r = clazz_r

    def predict(self, context: MlpRequestContext, req: T | Iterable[T], config: Optional[C]) -> R | Iterable[R]:
        """
        Эта функция предназначена для обработки predict'а во всех режимах со стриммингом и без.
        В дочерних классах могут быть переопределны отдельные упрощённые функции, например predict_simple.
        Проверим наличие такой функции в дочернем классе и вызовем её. А транспорт будет всегда вызывать predict.
        """
        # Проверяем, переопределен ли метод predict_simple в дочернем классе
        child_predict_simple = getattr(self.__class__, "predict_simple", None)
        base_predict_simple = getattr(MlpPredictServiceBase, "predict_simple", None)

        # Если метод переопределен в наследнике (не равен методу базового класса)
        if callable(child_predict_simple) and child_predict_simple is not base_predict_simple:
            # Проверяем, является ли req одиночным объектом или коллекцией
            if isinstance(req, Iterable):
                raise Exception("Streaming request is not allowed for predict_simmple")
            else:
                # Если одиночный объект, просто вызываем predict_simple
                return self.predict_simple(context, req, config)
        else:
            # Если predict_simple не переопределен, выбрасываем исключение
            raise NotImplementedError("Method predict is not immplemented")

    def predict_simple(self, context: MlpRequestContext, req: T, config: Optional[C]) -> R:
        raise NotImplementedError()
