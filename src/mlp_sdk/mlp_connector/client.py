import logging
import time
from dataclasses import dataclass, field
from typing import Any, Dict, Generator, List, MutableMapping, Optional, Type, TypeVar, Union, cast

import grpc

from mlp_sdk.abstract.services import MlpErrorStatus, MlpException, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_ import mlp_grpc_pb2
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import ClientRequestProto, ClientResponseProto, ExtendedRequestProto, PayloadProto, PredictRequestProto
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2_grpc import GateStub
from mlp_sdk.mlp_connector.grpc_typed_adapter import MlpGrpcTypedAdapter
from mlp_sdk.utils.config import get_config
from mlp_sdk.utils.logger import get_logger
from mlp_sdk.utils.misc import get_one_of, parse_grpc_url

RECONNECT_ERROR_CODES: List[str] = ["mlp.gate.gate_is_shut_down"]

log: logging.Logger = get_logger("MlpGrpcClient")
config = get_config()

T = TypeVar("T")
C = TypeVar("C")
R = TypeVar("R")


@dataclass
class MlpGrpcClientException(Exception):
    error_code: str
    error_message: str
    error_args: Dict[str, str] = field(default_factory=dict)


class MlpGrpcClient:
    def __init__(self, url: Optional[str] = None, token: Optional[str] = None):
        if url:
            host_port, secure = parse_grpc_url(url)
            self.url = host_port
            self.grpc_secure = secure
        else:
            self.url: str = config.mlp.grpc_host
            self.grpc_secure: bool = config.mlp.grpc_secure

        self.client_token: str = get_one_of(token, config.mlp.client_token, error_message="MLP_CLIENT_TOKEN is required")

        self.channel: Optional[grpc.Channel] = None
        self.stub: Optional[GateStub] = None

        self.connect()

    @staticmethod
    def open_grpc_channel(host_port: str, secure: bool) -> grpc.Channel:
        channel_options: List[tuple[str, Union[str, int]]] = [
            ("grpc.keepalive_time_ms", config.grpc.keepalive_time_ms),
            ("grpc.keepalive_timeout_ms", config.grpc.keepalive_timeout_ms),
            ("grpc.keepalive_permit_without_calls", config.grpc.keepalive_permit_without_calls),
            ("grpc.max_send_message_length", config.grpc.max_send_message_length),
            ("grpc.max_receive_message_length", config.grpc.max_receive_message_length),
        ]

        if secure:
            if config.grpc.ssl_ca_file_path:
                with open(config.grpc.ssl_ca_file_path, "rb") as f:
                    creds = grpc.ssl_channel_credentials(f.read())
            else:
                creds = grpc.ssl_channel_credentials()

            new_channel = grpc.secure_channel(host_port, creds, options=channel_options)
        else:
            new_channel = grpc.insecure_channel(host_port, options=channel_options)

        return new_channel

    def connect(self) -> None:
        """Устанавливает соединение с gRPC сервером."""
        log.warning(f"Starting mpl client for url: {self.url}, secure: {self.grpc_secure}")

        new_channel: grpc.Channel = self.open_grpc_channel(self.url, self.grpc_secure)

        self.stub = GateStub(new_channel)
        try:
            self.stub.healthCheck()
        except Exception:
            log.error(f"healthCheck is failed for url: {self.url}, secure: {self.grpc_secure}")
            return

        previous_channel: Optional[grpc.Channel] = self.channel
        self.channel = new_channel

        if previous_channel is not None:
            previous_channel.close()

    def shutdown(self) -> None:
        """Закрывает gRPC канал."""
        # Нужно проверить, что канал существует перед его закрытием
        if self.channel is not None:
            self.channel.close()

    def __process_request_with_retry(self, request: ClientRequestProto) -> ClientResponseProto | Generator[ClientResponseProto, None, None]:
        """
        Отправляет запрос с поддержкой повторных попыток при ошибках.

        Args:
            request: Запрос для отправки

        Returns:
            Ответ от сервера

        Raises:
            MlpGrpcClientException: При ошибках соединения или превышении лимита повторных попыток
        """
        request_retry_timeout_seconds = config.sdk.request_retry_timeout_seconds
        end_time: float = time.time() + request_retry_timeout_seconds

        request_retry_max_attempts = config.sdk.request_retry_max_attempts
        request_retry_backoff_seconds = config.sdk.request_retry_backoff_seconds
        request_retry_error_codes = config.sdk.request_retry_error_codes

        request_retry_failures: int = 0
        single_response: ClientResponseProto | None = None

        while time.time() < end_time:
            try:
                if self.stub is None:
                    raise MlpGrpcClientException("UNAVAILABLE", "gRPC stub is not initialized")

                response_generator: Generator[ClientResponseProto, None, None] = self.stub.processResponseStream(request)

                single_response = next(response_generator)
                # Проверяем тип ответа и обрабатываем ошибки
                response_type = single_response.WhichOneof("body")

                if response_type == "predict":
                    return single_response

                if response_type == "partialPredict":

                    def generator(single_response, response_generator):
                        yield single_response
                        yield from response_generator

                    return generator(single_response, response_generator)

                if response_type == "error":
                    if single_response.error.code in RECONNECT_ERROR_CODES:
                        self.connect()
                        break

                    if single_response.error.code in request_retry_error_codes:
                        # повторяем без увеличения счётчика ошибок
                        break

                    request_retry_failures += 1
                    if request_retry_failures >= request_retry_max_attempts:
                        break

                    # Если это неопознанная ошибка, то выводим в лог и делаем sleep
                    log.error(f"Error from gate, attempt {request_retry_failures}:\n{single_response.error}")
                    time.sleep(request_retry_backoff_seconds)
            except grpc.RpcError as rpc_error:
                if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                    self.connect()
                else:
                    log.error(f"Error from grpc channel. Error \n{rpc_error.details()}")
                    raise MlpGrpcClientException(f"{rpc_error.code()}", f"{rpc_error.details()}") from rpc_error

        if single_response is None:
            raise MlpGrpcClientException("UNAVAILABLE", f"Cannot connect after {request_retry_timeout_seconds} seconds")

        # тут возможно будет ответ с error_code
        return single_response

    def __pass_request_headers(self, inner_request_headers: MutableMapping[str, str], outer_context: Optional[MlpRequestContext] = None) -> None:
        """
        Копирует важные заголовки из внешнего контекста во внутренние заголовки запроса.

        Args:
            inner_request_headers: Заголовки запроса, которые будут отправлены
            outer_context: Внешний контекст запроса, содержащий заголовки для копирования
        """
        if not outer_context:
            return

        # Проверяем наличие request_id и копируем его если есть
        request_id = outer_context.request_headers.get("Z-requestId")
        if request_id is not None:
            inner_request_headers["Z-requestId"] = str(request_id)

        # Проверяем наличие billing_key и копируем его если есть
        billing_key = outer_context.request_headers.get("MLP-BILLING-KEY")
        if billing_key is not None:
            inner_request_headers["MLP-BILLING-KEY"] = str(billing_key)

    def __process_response(
        self, response: ClientResponseProto | Generator[ClientResponseProto, None, None], response_clazz: Type[R]
    ) -> R | Generator[R, None, None]:
        if isinstance(response, ClientResponseProto):
            return self.__process_single_response(response, response_clazz)
        if isinstance(response, Generator):
            return self.__process_stream_response(response, response_clazz)
        raise Exception("Unexpected value")

    def __process_stream_response(self, response: Generator[ClientResponseProto, None, None], response_clazz: Type[R]) -> Generator[R, None, None]:
        for r in response:
            yield self.__process_single_response(r, response_clazz)

    def __process_single_response(self, response: ClientResponseProto, response_clazz: Type[R]) -> R:
        """
        Обрабатывает ответ от сервера и преобразует его в нужный формат.

        Args:
            response: Ответ от сервера
            response_clazz: Класс для преобразования данных ответа

        Returns:
            Преобразованные данные ответа

        Raises:
            MlpException: Если сервис вернул ошибку
            MlpGrpcClientException: Если получен неожиданный тип ответа
        """
        if response_clazz == ClientResponseProto:
            return response  # type: ignore

        # Проверяем тип ответа
        response_type = response.WhichOneof("body")
        if response_type == "predict":
            return MlpGrpcTypedAdapter.convert_from_payload(response.predict.data, response_clazz)
        elif response_type == "partialPredict":
            return MlpGrpcTypedAdapter.convert_from_payload(response.partialPredict.data, response_clazz)
        elif response_type == "error":
            log.error(f"Error from gate. Error \n{response.error.status}")
            raise MlpException(
                code=response.error.code,
                message=response.error.message,
                status=MlpErrorStatus.from_proto(response.error.status),
                named_args=dict(response.error.args),
                headers=dict(response.headers),
            )
        else:
            raise MlpGrpcClientException("wrong-response", f"Wrong response type: {response_type}", {})

    def predict(
        self,
        model_id: str,
        request: Any,
        config: Optional[Any] = None,
        response_clazz: Type[R] = dict[str, Any],
        outer_context: Optional[MlpRequestContext] = None,
    ) -> R | Generator[R, None, None]:
        converted_request = MlpGrpcTypedAdapter.convert_to_payload(request)
        converted_config = None
        if config is not None:
            converted_config = MlpGrpcTypedAdapter.convert_to_payload(config)

        owner_name, model_name = self.parse_model_id(model_id)

        grpc_request = mlp_grpc_pb2.ClientRequestProto(
            account=owner_name,
            model=model_name,
            authToken=self.client_token,
            predict=PredictRequestProto(data=converted_request, config=converted_config),
            headers={},
        )

        self.__pass_request_headers(grpc_request.headers, outer_context)

        response = self.__process_request_with_retry(grpc_request)
        return self.__process_response(response, response_clazz)

    @staticmethod
    def parse_model_id(model_id: str):
        try:
            return model_id.split("/")[0], "/".join(model_id.split("/")[1:])
        except Exception:
            raise Exception("model_id must be in a form <owner_name>/<model_name>")  # noqa: B904

    def ext(
        self,
        model_id: str,
        method_name: str,
        params: dict[str, PayloadProto],
        response_clazz: Type[R] = PayloadProto,
        outer_context: Optional[MlpRequestContext] = None,
    ) -> R:
        owner_name, model_name = self.parse_model_id(model_id)

        grpc_request = mlp_grpc_pb2.ClientRequestProto(
            account=owner_name,
            model=model_name,
            authToken=self.client_token,
            ext=ExtendedRequestProto(methodName=method_name, params=params),
            headers={},
        )
        self.__pass_request_headers(grpc_request.headers, outer_context)

        response = cast(ClientResponseProto, self.__process_request_with_retry(grpc_request))

        return self.__process_single_response(response, response_clazz)
