import logging
import pathlib
import sys

from setuptools import find_packages, setup

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler(sys.stdout))
LOGGER.setLevel(logging.DEBUG)

_THIS_DIR = pathlib.Path(__file__).parent


def get_requirements():
    with (_THIS_DIR / "requirements.txt").open() as fp:
        return fp.read().splitlines()

setup(
    name='mlp_sdk',
    version='1.0.0',
    install_requires=get_requirements(),
    package_dir={"mlp_sdk": "mlp_sdk"},
    package_data={"": ["*.yml"]},
    include_package_data=True,
    packages=find_packages(exclude=["tests", "examples", "specs"]),
)

