import logging
from logging.config import dictConfig
from typing import Optional

LOGGING_CONFIG_TEMPLATE = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": "%(asctime)s - [%(levelname)s] - [%(pathname)s: %(module)s.%(funcName)s:%(lineno)d]: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler", "formatter": "basic"
        },
    },
    "root": {
        "level": logging.INFO,
        "handlers": ("console", ),
    },
}


def get_logger(graylog_host: Optional[str] = None, graylog_udp_port: Optional[int] = None) -> logging.Logger:

    logging_config = LOGGING_CONFIG_TEMPLATE.copy()
    if graylog_host is not None and graylog_udp_port is not None:
        # TODO: Take host/port info from env variables
        # TODO: Add and handle custom required fields: task, instance, server, etc
        # TODO: Test graylog with mocking emit func?
        graylog_handler = {
            "class": "mpl_sdk.log.graylog_handler.GrayLogHandler",
            "host": graylog_host,
            "port": graylog_udp_port,
            "level_names": True,
            "formatter": "basic"
        }
        logging_config["handlers"]["graylog"] = graylog_handler
        logging_config["root"]["handlers"] += ("graylog", )

    dictConfig(logging_config)
    logger = logging.getLogger("root")
    return logger
