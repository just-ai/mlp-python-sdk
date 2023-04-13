import os
from ..log import get_logger

LOGGER = get_logger(__name__)


def heavy_test(test_function):
    """
    The purpose of this decorator is to mark tests, that should be skipped
    when `SKIP_HEAVY_TESTS` environment variable is equal to 1.

    Usage:
    1. Add variable to your environment via
        - terminal (system local build)
        - Dockerfile (docker local build)
        - bitbucket-pipelines (docker CI build)
    2. Decorate necessary test functions with `@heavy_test`
    """

    def heavy_test_func(*args, **kwargs):
        flag = 'SKIP_HEAVY_TESTS'
        if flag in os.environ and os.environ[flag].isdigit() and int(os.environ[flag]) == 1:
            LOGGER.info(f'Test {test_function.__name__} is skipped! To run this test set `{flag}` '
                        ' env variable to `0` or create PR from `dev` branch to `master` one')
            return

        return test_function(*args, **kwargs)
    return heavy_test_func
