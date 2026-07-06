from collections.abc import Generator as GeneratorABC
from dataclasses import dataclass, field
from enum import Enum
from typing import Generator, Generic, Optional, Type, TypeVar

from pydantic import ValidationError

from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import ApiErrorProto, SimpleStatusProto


@dataclass
class MlpRequestContext:
    requestId: int
    gatewayId: str
    request_headers: dict[str, str]
    response_headers: dict[str, str] = field(default_factory=dict)
    cancelled: bool = False
    content_hidden: bool = False


class MlpErrorStatus(Enum):
    OK = 0
    BAD_REQUEST = 400
    ACCESS_DENIED = 403
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

    def to_proto(self) -> SimpleStatusProto:
        return getattr(SimpleStatusProto, self.name)

    @staticmethod
    def from_proto(val: SimpleStatusProto) -> "MlpErrorStatus":
        for v in SimpleStatusProto.DESCRIPTOR.values:
            if v.number == val:
                return getattr(MlpErrorStatus, v.name)
        raise Exception(f"Unknown SimpleStatusProto value {val}")  # pragma: no cover


@dataclass
class MlpException(Exception):
    code: str  # короткий код ошибки
    message: str  # дефолтный текст описания ошибки на английском языке
    status: MlpErrorStatus = MlpErrorStatus.INTERNAL_SERVER_ERROR
    named_args: dict[str, str] = field(default_factory=dict)
    headers: dict[str, str] | None = None

    def __str__(self) -> str:
        return f"{self.code}: {self.message}"

    @staticmethod
    def exception_to_proto(e: BaseException):
        if isinstance(e, MlpException):
            try:
                return ApiErrorProto(code=e.code, message=e.message, status=e.status.to_proto(), args=e.named_args)
            except:  # noqa: E722
                pass

        if isinstance(e, ValidationError):
            return ApiErrorProto(code="mlp-action.common.bad-request", message=str(e), status=SimpleStatusProto.BAD_REQUEST, args={})

        return ApiErrorProto(code="mlp-action.common.internal-error", message=str(e), status=SimpleStatusProto.INTERNAL_SERVER_ERROR, args={})


T = TypeVar("T")
C = TypeVar("C")
R = TypeVar("R")


@dataclass
class EmptyData:
    pass


class MlpPredictServiceBase(Generic[T, C, R]):
    def __init__(self, clazz_t: Type[T], clazz_c: Type[C], clazz_r: Type[R]):
        self.clazz_t = clazz_t
        self.clazz_c = clazz_c
        self.clazz_r = clazz_r

    def predict(self, context: MlpRequestContext, req: T | Generator[T, None, None], config: Optional[C]) -> R | Generator[R, None, None]:
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
            if isinstance(req, GeneratorABC):
                raise Exception("Streaming request is not allowed for predict_simple")  # pragma: no cover
            else:
                # Если одиночный объект, просто вызываем predict_simple
                return self.predict_simple(context, req, config)
        else:
            # Если predict_simple не переопределен, выбрасываем исключение
            raise NotImplementedError("Method predict is not implemented")  # pragma: no cover

    def predict_simple(self, context: MlpRequestContext, req: T, config: Optional[C]) -> R:
        raise NotImplementedError()  # pragma: no cover

    def predict_batch_simple(
        self,
        contexts: list[MlpRequestContext],
        req: list[T | None],
        config: Optional[C],
    ) -> list[R | None]:
        if len(contexts) != len(req):
            raise ValueError("Batch contexts and requests length mismatch")  # pragma: no cover

        result: list[R | None] = []
        for context, item in zip(contexts, req, strict=True):
            if item is None:
                result.append(None)
                continue

            response = self.predict(context, item, config)
            if isinstance(response, GeneratorABC):
                raise Exception("Predict must not return streaming result to use in batch mode")
            result.append(response)

        return result
