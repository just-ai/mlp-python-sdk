import json
import os
from pathlib import Path

import pytest
import yaml

import mlp_sdk
from mlp_sdk.transport.config_enricher import enrich_config

__default_config = Path(mlp_sdk.transport.config_enricher.__file__).parent / "config.yml"
CONFIG = yaml.safe_load(open(__default_config))


def test_enrich_config_without_overriding():
    updated_config = enrich_config(CONFIG.copy())
    assert CONFIG == updated_config


@pytest.mark.parametrize(
    "env_var, config_key, value",
    [
        ("MLP_LOGGING_LEVEL", "logging.level", "INFO"),
        ("MLP_LOGGING_FORMAT", "logging.format", "%(message)s"),
        ("MLP_SDK_LARGE_BODY_LENGTH", "sdk.large_body_length", "1000000"),
        ("MLP_SDK_REQUESTS_EXECUTOR_POOL_SIZE", "sdk.requests_executor_pool_size", "11"),
        ("MLP_SDK_REQUEST_RETRY_TIMEOUT_SECONDS", "sdk.request_retry_timeout_seconds", "55"),
        ("MLP_SDK_SHUTDOWN_EVENT_TIMEOUT_SECONDS", "sdk.shutdown_event_timeout_seconds", "11"),
        ("MLP_SDK_STOPPING_EVENT_TIMEOUT_SECONDS", "sdk.stopping_event_timeout_seconds", "22"),
        ("MLP_SDK_STARTUP_THREAD_TIMEOUT_SECONDS", "sdk.startup_thread_timeout_seconds", "33"),
        ("MLP_SDK_HEARTBEAT_THREAD_TIMEOUT_SECONDS", "sdk.heartbeat_thread_timeout_seconds", "44"),
        ("MLP_SDK_ACTION_SHUTDOWN_TIMEOUT_SECONDS", "sdk.action_shutdown_timeout_seconds", "66"),
        ("MLP_SDK_REQUEST_RETRY_MAX_ATTEMPTS", "sdk.request_retry_max_attempts", "77"),
        ("MLP_SDK_REQUEST_RETRY_BACKOFF_SECONDS", "sdk.request_retry_backoff_seconds", "88"),
        ("MLP_GRPC_KEEPALIVE_TIME_MS", "grpc.keepalive_time_ms", "60000"),
        ("MLP_GRPC_KEEPALIVE_TIMEOUT_MS", "grpc.keepalive_timeout_ms", "20000"),
        ("MLP_GRPC_KEEPALIVE_PERMIT_WITHOUT_CALLS", "grpc.keepalive_permit_without_calls", "0"),
        ("MLP_GRPC_MAX_SEND_MESSAGE_LENGTH", "grpc.max_send_message_length", "4194304"),
        ("MLP_GRPC_MAX_RECEIVE_MESSAGE_LENGTH", "grpc.max_receive_message_length", "4194304"),
        ("MLP_SDK_ACTION_TO_GATE_QUEUE_MAX_SIZE", "sdk.action_to_gate_queue_max_size", "5000"),
    ],
)
def test_enrich_config_mlp_env(env_var, config_key, value):
    os.environ[env_var] = value

    updated_config = enrich_config(CONFIG.copy())

    keys = config_key.split(".")
    temp_config = updated_config
    for key in keys[:-1]:
        temp_config = temp_config[key]

    expected_value = int(value) if value.isdigit() else value
    assert temp_config[keys[-1]] == expected_value

    del os.environ[env_var]


def test_enrich_config_retry_codes():
    retry_error_codes = ["custom.error.code", "mlp-action.common.channel-closed-error"]
    os.environ.setdefault("MLP_SDK_REQUEST_RETRY_ERROR_CODES", json.dumps(retry_error_codes))
    updated_config = enrich_config(CONFIG.copy())
    assert updated_config["sdk"]["request_retry_error_codes"] == retry_error_codes


@pytest.mark.parametrize(
    "env_var, config_key, value",
    [
        ("MLP_REST_TIMEOUT", "rest.timeout", "10"),
        ("MLP_ACCOUNT_ID", "account_id", "just-ai"),
    ],
)
def test_enrich_config_unknown_env(env_var, config_key, value):
    os.environ[env_var] = value

    updated_config = enrich_config(CONFIG.copy())

    keys = config_key.split(".")
    temp_config = updated_config
    if len(keys) == 1:
        temp_config = updated_config.get(keys[0])
    for key in keys[:-1]:
        temp_config = temp_config.get(key)
        if temp_config is None:
            break

    assert temp_config is None

    del os.environ[env_var]
