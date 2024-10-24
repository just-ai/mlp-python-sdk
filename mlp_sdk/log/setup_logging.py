import logging
import os

from mlp_sdk.log.graylog_handler import GrayLogHandler


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def get_logger(name: str) -> logging.Logger:
    level = os.environ.get("MLP_LOG_LEVEL", "WARN")
    logging_level = logging.getLevelName(level)
    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    logger.propagate = False  # Global logger should not print messages again.

    # Avoiding log duplicates: do not add handlers again to already initialized logger
    # https://stackoverflow.com/questions/7173033/duplicate-log-output-when-using-python-logging-module
    if len(logger.handlers) != 0:
        return logger

    # create console handler
    if not str2bool(os.environ.get("MLP_LOG_NO_CONSOLE", "false")):
        ch = logging.StreamHandler()
        ch.setLevel(logging_level)

        # create formatter and add it to the handlers
        formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - [%(pathname)s: %(module)s.%(funcName)s:%(lineno)d]: %(message)s"
        )
        ch.setFormatter(formatter)

        logger.addHandler(ch)

    if not str2bool(os.environ.get("MLP_LOG_NO_GELF", "false")):
        if os.environ.get("MLP_GRAYLOG_SERVER") and os.environ.get("MLP_GRAYLOG_PORT"):
            graylog_handler = GrayLogHandler(
                os.environ.get("MLP_GRAYLOG_SERVER"), int(os.environ.get("MLP_GRAYLOG_PORT")), extra_fields=True
            )
            logger.addHandler(graylog_handler)

    return logger
