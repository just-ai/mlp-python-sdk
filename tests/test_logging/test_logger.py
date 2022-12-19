from mpl_sdk.log import get_logger


def test_logger():
    LOGGER = get_logger()
    LOGGER.info("Test message.")

    LOGGER2 = get_logger()
    LOGGER2.info("Test message number 2.")

    assert LOGGER is LOGGER2
