import logging
import os

from mlp_sdk.log.graylog_handler import GrayLogHandler

_NAME = 'root'


def get_logger(name: str = _NAME, level: str = 'INFO') -> logging.Logger:

    logging_level = logging.getLevelName(level)
    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging_level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - [%(pathname)s: %(module)s.%(funcName)s:%(lineno)d]: %(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    if os.environ.get('GRAYLOG_SERVER') and os.environ.get('GRAYLOG_PORT'):
        graylog_handler = GrayLogHandler(os.environ.get('GRAYLOG_SERVER'),
                                         int(os.environ.get('GRAYLOG_PORT')), extra_fields=True)
        logger.addHandler(graylog_handler)

    return logger
