from mlp_sdk.log import get_logger


def test_logger():
    LOGGER = get_logger(__name__)
    LOGGER.info("Test message.")

    LOGGER2 = get_logger(__name__)
    LOGGER2.info("Test message number 2.")

    assert LOGGER is LOGGER2
