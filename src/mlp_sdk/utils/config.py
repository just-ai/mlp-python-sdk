import dataclasses
import os
import types
from dataclasses import dataclass, field, fields, is_dataclass
from typing import Any, Callable, Dict, List, Type, TypeVar, cast

import yaml  # pyright: ignore[reportMissingModuleSource]


@dataclass
class LoggingConfigGraylog:
    enabled: bool = False
    host: str = field(default="localhost", metadata={"alias": ["MLP_GRAYLOG_SERVER"]})
    port: int = field(default=12201, metadata={"alias": ["MLP_GRAYLOG_PORT"]})
    udp: bool = False
    env_name: str = field(default="default", metadata={"alias": ["MLP_GRAYLOG_ENV"]})
    async_: bool = True


@dataclass
class LoggingConfigConsole:
    enabled: bool = True
    async_: bool = True


@dataclass
class LoggingConfig:
    console: LoggingConfigConsole = field(default_factory=LoggingConfigConsole)
    graylog: LoggingConfigGraylog = field(default_factory=LoggingConfigGraylog)
    app_name: str = "mlp_sdk"
    root_level: str = field(default="INFO", metadata={"alias": ["MLP_LOG_LEVEL"]})
    levels: dict[str, str] = field(default_factory=dict)


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
        return self.grpc_hosts.split(",") if self.grpc_hosts else [self.grpc_host]  # pragma: no cover


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
    mlp: MlpConfig = field(default_factory=MlpConfig)
    grpc: GrpcConfig = field(default_factory=GrpcConfig)
    sdk: MLpSdkConfig = field(default_factory=MLpSdkConfig)

    logging: LoggingConfig = field(default_factory=LoggingConfig)

    service_config: str = "{}"


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

    def load_config(self, cls: Type[T] = BaseConfig, required: bool = True) -> T:
        profile = os.environ.get("PROFILE", "dev")

        self.__load_if_exists(f"{_config_dir}/config-local.yml")
        self.__load_if_exists(f"{_config_dir}/config-{profile}.yml")
        self.__load_if_exists("./config.yml")
        self.__load_if_exists(f"{_config_dir}/config.yml", required=required)

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
            raise Exception(f"Cannot convert value {value} to a required type {required_type}")

    def __get_value(self, vname: str, required_type: Type) -> Any:
        env_name = vname.upper().replace(".", "_")
        if os.getenv(env_name) is not None:
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

                # Проверяем наличие алиасов в метаданных поля
                aliases = []
                if f.metadata and "alias" in f.metadata:
                    aliases = f.metadata["alias"]

                # Основное имя поля
                fname = f"{outer_name}{f.name}"

                # Пробуем получить значение сначала по алиасам, затем по основному имени
                val = None
                for alias_name in aliases:
                    val = get_value_func(alias_name, cast(type, f.type))
                    if val is not None:
                        break

                # Если значение не найдено по алиасам, пробуем по основному имени
                if val is None:
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


_config_dir: str = os.getenv("CONFIG_DIR", os.curdir)
_base_config: BaseConfig | None = None


def set_config_dir(folder: str):
    global _config_dir
    _config_dir = folder


def get_config() -> BaseConfig:
    global _base_config
    if _base_config is None:
        _base_config = ConfigLoader().load_config(BaseConfig, required=False)

    return _base_config


def load_application_config(type: Type[T], folder: str | None = None) -> T:
    global _base_config
    if folder is not None:
        set_config_dir(folder)
    cfg = ConfigLoader().load_config(type)
    _base_config = cfg
    return cfg
