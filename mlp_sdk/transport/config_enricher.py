import json
import os

__mlp_environment_override = {
    "MLP_LOGGING_LEVEL": "logging.level",
    "MLP_LOGGING_FORMAT": "logging.format",
    "MLP_SDK_LARGE_BODY_LENGTH": "sdk.large_body_length",
    "MLP_SDK_REQUESTS_EXECUTOR_POOL_SIZE": "sdk.requests_executor_pool_size",
    "MLP_SDK_REQUEST_RETRY_TIMEOUT_SECONDS": "sdk.request_retry_timeout_seconds",
    "MLP_SDK_SHUTDOWN_EVENT_TIMEOUT_SECONDS": "sdk.shutdown_event_timeout_seconds",
    "MLP_SDK_STOPPING_EVENT_TIMEOUT_SECONDS": "sdk.stopping_event_timeout_seconds",
    "MLP_SDK_STARTUP_THREAD_TIMEOUT_SECONDS": "sdk.startup_thread_timeout_seconds",
    "MLP_SDK_HEARTBEAT_THREAD_TIMEOUT_SECONDS": "sdk.heartbeat_thread_timeout_seconds",
    "MLP_SDK_ACTION_SHUTDOWN_TIMEOUT_SECONDS": "sdk.action_shutdown_timeout_seconds",
    "MLP_SDK_REQUEST_RETRY_MAX_ATTEMPTS": "sdk.request_retry_max_attempts",
    "MLP_SDK_REQUEST_RETRY_BACKOFF_SECONDS": "sdk.request_retry_backoff_seconds",
    "MLP_SDK_REQUEST_RETRY_ERROR_CODES": "sdk.request_retry_error_codes",
    "MLP_SDK_RECONNECT_ENABLED": "sdk.reconnect_enabled",
    "MLP_SDK_ACTION_TO_GATE_QUEUE_MAX_SIZE": "sdk.action_to_gate_queue_max_size",
    "MLP_GRPC_KEEPALIVE_TIME_MS": "grpc.keepalive_time_ms",
    "MLP_GRPC_KEEPALIVE_TIMEOUT_MS": "grpc.keepalive_timeout_ms",
    "MLP_GRPC_KEEPALIVE_PERMIT_WITHOUT_CALLS": "grpc.keepalive_permit_without_calls",
    "MLP_GRPC_MAX_SEND_MESSAGE_LENGTH": "grpc.max_send_message_length",
    "MLP_GRPC_MAX_RECEIVE_MESSAGE_LENGTH": "grpc.max_receive_message_length",
}


def enrich_config(config: dict) -> dict:
    for env_key, config_key in __mlp_environment_override.items():
        env_value = os.environ.get(env_key)
        if env_value is not None:
            config = __set_nested_value(config, config_key, env_value)
    return config


def __set_nested_value(config: dict, key: str, value: str):
    keys = key.split(".")
    target_key = keys[-1]
    target_config_by_key = config
    for sub_key in keys[:-1]:
        target_config_by_key.setdefault(sub_key, {})
        target_config_by_key = target_config_by_key[sub_key]
    old_value = target_config_by_key.get(target_key)
    if old_value is not None:
        target_config_by_key[target_key] = (
            json.loads(value) if isinstance(old_value, (list, dict)) else type(old_value)(value)
        )
    else:
        target_config_by_key[target_key] = value
    return config
