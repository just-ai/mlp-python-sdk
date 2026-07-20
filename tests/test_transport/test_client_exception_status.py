from mlp_sdk.grpc.mlp_grpc_pb2 import (
    BAD_REQUEST,
    INTERNAL_SERVER_ERROR,
    OK,
    SERVICE_UNAVAILABLE,
    TOO_MANY_REQUESTS,
)
from mlp_sdk.transport.MlpClientSDK import MlpClientException
from mlp_sdk.transport.MlpServiceSDK import MlpException, is_client_error_status

# CAILA-5717: вложенный клиентский вызов внутри predict (напр. классификатор ->
# векторизатор) может получить от гейтвея терминальную rate-limit ошибку
# (mlp.gateway.pps_limit_exceeded, status=429). Раньше MlpClientException наследовался
# от Exception и не нёс status, поэтому обработчик запроса MlpServiceSDK ловил его в
# ветке `except Exception` и схлопывал в mlp-action.common.processing-exception / 500 —
# клиент получал 500 + ERROR-лог (шум в error-monitor). Теперь MlpClientException
# наследует MlpException и несёт исходные code/status, поэтому существующая ветка
# `except MlpException` сохраняет их, и наружу уходит корректный 429.


def test_client_exception_is_mlp_exception():
    exc = MlpClientException("mlp.gateway.pps_limit_exceeded", "Too many predictions", {}, TOO_MANY_REQUESTS)
    assert isinstance(exc, MlpException)


def test_client_exception_preserves_code_and_status():
    args = {"accountId": "1000229487"}
    exc = MlpClientException("mlp.gateway.pps_limit_exceeded", "Too many predictions", args, TOO_MANY_REQUESTS)

    # атрибуты MlpException, которые читает обработчик запроса в MlpServiceSDK
    assert exc.code == "mlp.gateway.pps_limit_exceeded"
    assert exc.status == TOO_MANY_REQUESTS
    assert exc.message == "Too many predictions"
    assert exc.source_error_data == args

    # обратная совместимость со старым публичным контрактом MlpClientException
    assert exc.error_code == "mlp.gateway.pps_limit_exceeded"
    assert exc.error_message == "Too many predictions"
    assert exc.error_args == args


def test_client_exception_defaults_to_internal_server_error():
    # транспортные/непонятные ошибки клиента остаются 500 — они не rate-limit
    exc = MlpClientException("wrong-response", "Wrong response type", {})
    assert exc.status == INTERNAL_SERVER_ERROR


# CAILA-5717 (WARN-часть): 4xx (rate-limit и прочие клиентские) логируются на WARN,
# 5xx / OK — на ERROR. Определяет уровень лога и в MlpClientSDK (raise site), и в
# обработчике MlpServiceSDK.
def test_is_client_error_status_4xx_true():
    assert is_client_error_status(TOO_MANY_REQUESTS) is True
    assert is_client_error_status(BAD_REQUEST) is True


def test_is_client_error_status_non_4xx_false():
    assert is_client_error_status(INTERNAL_SERVER_ERROR) is False
    assert is_client_error_status(SERVICE_UNAVAILABLE) is False
    assert is_client_error_status(OK) is False
    assert is_client_error_status(None) is False
