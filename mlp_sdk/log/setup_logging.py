import logging
import os

from mlp_sdk.log.graylog_handler import GrayLogHandler


def get_logger(name: str, level: str = 'DEBUG') -> logging.Logger:

    logging_level = logging.getLevelName(level)
    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    logger.propagate = False  # Global logger should not print messages again.

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging_level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - [%(pathname)s: %(module)s.%(funcName)s:%(lineno)d]: %(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    if os.environ.get('MLP_GRAYLOG_SERVER') and os.environ.get('MLP_GRAYLOG_PORT'):
        graylog_handler = GrayLogHandler(os.environ.get('MLP_GRAYLOG_SERVER'),
                                         int(os.environ.get('MLP_GRAYLOG_PORT')), extra_fields=True)
        logger.addHandler(graylog_handler)

    return logger
