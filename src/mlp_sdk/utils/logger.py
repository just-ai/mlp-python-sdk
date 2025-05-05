import contextvars
import logging
import sys
from logging.handlers import QueueHandler, QueueListener
from queue import Queue

import graypy  # type: ignore

from mlp_sdk.utils.config import get_config

request_id_var = contextvars.ContextVar("request_id", default=0)
config = get_config()


class GraylogFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        # Добавляем app_name как дополнительное поле
        record.app = config.logging.app_name
        record.env = config.logging.app_name
        record.account_id = config.mlp.account_id
        record.request_id = request_id_var.get()
        return super().format(record)


if config.logging.graylog.enabled:
    if config.logging.graylog.udp:
        graylog_handler = graypy.GELFUDPHandler(config.logging.graylog.host, config.logging.graylog.port)
    else:
        graylog_handler = graypy.GELFTCPHandler(config.logging.graylog.host, config.logging.graylog.port)

    graylog_formatter = GraylogFormatter("[%(name)s]: %(message)s")
    graylog_handler.setFormatter(graylog_formatter)

    graylog_logging_queue = Queue(-1)
    graylog_async_handler = QueueHandler(graylog_logging_queue)

    graylog_queue_listener = QueueListener(graylog_logging_queue, graylog_handler)
    graylog_queue_listener.start()
else:
    graylog_handler = None
    graylog_async_handler = None

if config.logging.console.enabled:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s"))

    console_logging_queue = Queue(-1)
    console_async_handler = QueueHandler(console_logging_queue)

    console_queue_listener = QueueListener(console_logging_queue, console_handler)
    console_queue_listener.start()
else:
    console_handler = None
    console_async_handler = None

logging.getLogger().setLevel(config.logging.root_level)
for log, level in config.logging.levels.items():
    logging.getLogger(log).setLevel(level)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.propagate = False  # Global logger should not print messages again.

    # Avoiding log duplicates: do not add handlers again to already initialized logger
    # https://stackoverflow.com/questions/7173033/duplicate-log-output-when-using-python-logging-module
    if len(logger.handlers) != 0:
        return logger

    if console_async_handler:
        logger.addHandler(console_async_handler)

    if graylog_async_handler:
        logger.addHandler(graylog_async_handler)

    return logger
