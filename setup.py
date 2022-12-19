import logging
import pathlib
import sys

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler(sys.stdout))
LOGGER.setLevel(logging.DEBUG)

_THIS_DIR = pathlib.Path(__file__).parent


def install_requirements():
    req = subprocess.Popen([
        f"cat {_THIS_DIR / 'requirements.txt'} | grep -v 'caila-transport' | xargs pip install"
    ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    installation_info = req.communicate()[0].decode()
    LOGGER.info(installation_info)


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    install_requirements()

    def run(self):
        develop.run(self)


class PostInstallCommand(install):

    install_requirements()

    def run(self):
        install.run(self)


def _get_requirements():
    with (_THIS_DIR / 'requirements.txt').open() as fp:
        return [e for e in fp.read().splitlines() if 'caila-transport' not in e]


MAJOR_VERSION = "0"
MINOR_VERSION = "4"
BUILD_NUMBER = "0"

print("================================================")
print(sys.argv)
print("================================================")

if '--branch' in sys.argv:
    index = sys.argv.index('--branch')
    sys.argv.pop(index)
    branch = sys.argv.pop(index)
    if branch != 'master' and branch != 'dev' and branch != 'release':
        MINOR_VERSION = MINOR_VERSION + "+" + branch

if '--build_number' in sys.argv:
    index = sys.argv.index('--build_number')
    sys.argv.pop(index)
    BUILD_NUMBER = sys.argv.pop(index)

setup(
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    name='caila_sdk',
    version=MAJOR_VERSION + "." + MINOR_VERSION + "." + BUILD_NUMBER,
    install_requires=_get_requirements(),
    package_dir={'caila_sdk': 'caila_sdk'},
    package_data={'': ['*.yml']},
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests.*'])
)
