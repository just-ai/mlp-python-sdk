import json
import os

__mlp_config_dict = {
    'MLP_LOGGING_LEVEL': 'logging.level',
    'MLP_LOGGING_FORMAT': 'logging.format',
    'MLP_SDK_LARGE_BODY_LENGTH': 'sdk.large_body_length',
    'MLP_SDK_REQUESTS_EXECUTOR_POOL_SIZE': 'sdk.requests_executor_pool_size',
    'MLP_SDK_REQUEST_RETRY_TIMEOUT_SECONDS': 'sdk.request_retry_timeout_seconds',
    'MLP_SDK_SHUTDOWN_EVENT_TIMEOUT_SECONDS': 'sdk.shutdown_event_timeout_seconds',
    'MLP_SDK_STOPPING_EVENT_TIMEOUT_SECONDS': 'sdk.stopping_event_timeout_seconds',
    'MLP_SDK_STARTUP_THREAD_TIMEOUT_SECONDS': 'sdk.startup_thread_timeout_seconds',
    'MLP_SDK_HEARTBEAT_THREAD_TIMEOUT_SECONDS': 'sdk.heartbeat_thread_timeout_seconds',
    'MLP_SDK_ACTION_SHUTDOWN_TIMEOUT_SECONDS': 'sdk.action_shutdown_timeout_seconds',
    'MLP_SDK_REQUEST_RETRY_MAX_ATTEMPTS': 'sdk.request_retry_max_attempts',
    'MLP_SDK_REQUEST_RETRY_BACKOFF_SECONDS': 'sdk.request_retry_backoff_seconds',
    'MLP_SDK_REQUEST_RETRY_ERROR_CODES': 'sdk.request_retry_error_codes',
    'MLP_GRPC_KEEPALIVE_TIME_MS': 'grpc.keepalive_time_ms',
    'MLP_GRPC_KEEPALIVE_TIMEOUT_MS': 'grpc.keepalive_timeout_ms',
    'MLP_GRPC_KEEPALIVE_PERMIT_WITHOUT_CALLS': 'grpc.keepalive_permit_without_calls',
    'MLP_GRPC_MAX_SEND_MESSAGE_LENGTH': 'grpc.max_send_message_length',
    'MLP_GRPC_MAX_RECEIVE_MESSAGE_LENGTH': 'grpc.max_receive_message_length',
}


def enrich_config(config):
    for env_key, config_key in __mlp_config_dict.items():
        env_value = os.environ.get(env_key)
        if env_value is not None:
            __set_nested_value(config, config_key, env_value)
    return config


def __set_nested_value(d, key, value):
    keys = key.split(".")
    current = d
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]
    old_value = current[keys[-1]]
    if old_value is not None:
        if isinstance(old_value, (list, dict)):
            value = json.loads(value)
        current[keys[-1]] = type(old_value)(value)
    else:
        current[keys[-1]] = value
