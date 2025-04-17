import dataclasses
import os
import types
from dataclasses import dataclass, field, fields, is_dataclass
from typing import Any, Callable, Dict, List, Type, TypeVar, cast

import yaml  # pyright: ignore[reportMissingModuleSource]

ROOT_PATH: str


def set_root_path(path: str):
    global ROOT_PATH
    ROOT_PATH = path  # pyright: ignore[reportConstantRedefinition]


@dataclass
class LoggingConfigGraylog:
    enabled: bool
    host: str
    port: int
    udp: bool


@dataclass
class LoggingConfigConsole:
    enabled: bool


@dataclass
class LoggingConfig:
    console: LoggingConfigConsole
    graylog: LoggingConfigGraylog
    app_name: str
    root_level: str
    levels: dict[str, str]


@dataclass
class MlpConfig:
    account_id: str | None = None
    model_id: str | None = None
    grpc_host: str = "gate.caila.io"
    grpc_hosts: str = "gate.caila.io"
    grpc_secure: bool = True
    client_token: str | None = None
    service_token: str | None = None

    def get_grpc_hosts(self) -> list[str]:
        return self.grpc_hosts.split(",") if self.grpc_hosts else [self.grpc_host]


@dataclass
class GrpcConfig:
    keepalive_time_ms: int = 120000
    keepalive_timeout_ms: int = 30000
    keepalive_permit_without_calls: int = 1
    max_send_message_length: int = 104857600  # 100 MB
    max_receive_message_length: int = 104857600  # 100 MB
    ssl_ca_file_path: str | None = None


@dataclass
class MLpSdkConfig:
    large_body_length: int = 3000
    requests_executor_pool_size: int = 10

    shutdown_event_timeout_seconds: int = 10
    stopping_event_timeout_seconds: int = 3
    startup_thread_timeout_seconds: int = 3
    heartbeat_thread_timeout_seconds: int = 3
    action_shutdown_timeout_seconds: int = 10

    request_retry_timeout_seconds: int = 60
    request_retry_max_attempts: int = 10
    request_retry_backoff_seconds: float = 0.3
    request_retry_error_codes: list[str] = field(default_factory=lambda: ["mlp.gate.pps_limit_exceeded", "mlp-action.common.channel-closed-error"])


@dataclass
class BaseConfig:
    mlp: MlpConfig
    grpc: GrpcConfig
    sdk: MLpSdkConfig

    logging: LoggingConfig


T = TypeVar("T", bound=BaseConfig)


class ConfigLoader:
    def __init__(self) -> None:
        self.configs: List[Dict[str, Any]] = []

    def __load_if_exists(self, filename: str, required: bool = False) -> None:
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                yy = yaml.safe_load(f)
                if yy:
                    self.configs.append(yy)
        else:
            if required:
                raise Exception(f"Configuration file {filename} does not exists. Check the working folder.")

    def load_config(self, cls: Type[T] = BaseConfig) -> T:
        profile = os.environ.get("PROFILE", "dev")

        self.__load_if_exists(f"{ROOT_PATH}/config-local.yml")
        self.__load_if_exists(f"{ROOT_PATH}/config-{profile}.yml")
        self.__load_if_exists("./config.yml")
        self.__load_if_exists(f"{ROOT_PATH}/config.yml", required=True)

        return self.__create_class_from_values(cls, self.__get_value, "")

    def __get_value_from_yaml(self, data: Dict[str, Any], key: str) -> Any:
        keys = key.split(".")  # Разбиваем строку ключа на отдельные части
        value = data
        for k in keys:
            value = value.get(k)  # Проходим по каждому уровню вложенности
            if value is None:  # Если ключ не найден, возвращаем None
                return None
        return value

    def __convert_to_type(self, value: Any, required_type: Type) -> Any:
        """Convert a value to the required type."""
        if value is None:
            return None

        # If the value is already of the required type, return it
        if isinstance(required_type, types.GenericAlias) or isinstance(value, required_type):
            return value

        try:
            if required_type is bool:
                if isinstance(value, str):
                    return value.lower() in ("true", "yes", "y", "1", "on")
                return bool(value)
            elif required_type is int:
                return int(value)
            elif required_type is str:
                return str(value)
            else:
                return value
        except (ValueError, TypeError):
            # If conversion fails, return the original value
            return value

    def __get_value(self, vname: str, required_type: Type) -> Any:
        env_name = vname.upper().replace(".", "_")
        if os.getenv(env_name):
            res = os.getenv(env_name)
            return self.__convert_to_type(res, required_type)

        for c in self.configs:
            v = self.__get_value_from_yaml(c, vname)
            if v is not None:
                return self.__convert_to_type(v, required_type)

        return None

    def __create_class_from_values(
        self,
        cls: Type[T],
        get_value_func: Callable[[str, type], Any],
        outer_name: str,
    ) -> T:
        """Создает экземпляр дата-класса на основе функции получения значений, включая вложенные дата-классы."""
        kwargs: Dict[str, Any] = {}

        for f in fields(cls):
            # Проверяем, является ли поле вложенным дата-классом
            if is_dataclass(f.type):
                # Рекурсивно создаем вложенный дата-класс
                kwargs[f.name] = self.__create_class_from_values(f.type, get_value_func, f"{outer_name}{f.name}.")  # type: ignore
            else:
                # Получаем значение для обычного поля
                fname = f"{outer_name}{f.name}"
                val = get_value_func(fname, cast(type, f.type))
                if val is None:
                    # Проверяем, имеет ли поле значение по умолчанию
                    if f.default is not dataclasses.MISSING:
                        # Поле имеет явное значение по умолчанию, используем его
                        kwargs[f.name] = f.default
                    elif f.default_factory is not dataclasses.MISSING:
                        # Поле имеет фабрику по умолчанию, используем её
                        kwargs[f.name] = f.default_factory()
                    else:
                        # Поле не имеет значения по умолчанию, выбрасываем исключение
                        msg = f"Field {fname} is not specified"
                        raise Exception(msg)
                else:
                    kwargs[f.name] = val

        return cls(**kwargs)


_base_config: BaseConfig | None = None


def get_config() -> BaseConfig:
    if _base_config is None:
        raise Exception("Configuration is not initialized. It needs to call load_application_config() before accessing get_config().")

    return _base_config


def load_application_config(type: Type[T]) -> T:
    global _base_config
    cfg = ConfigLoader().load_config(type)
    _base_config = cfg
    return cfg
