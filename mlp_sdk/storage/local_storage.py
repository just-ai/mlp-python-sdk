import os
import shutil

from distutils.dir_util import copy_tree
from pathlib import Path
from typing import IO

from mlp_sdk.storage.abstract_storage import AbstractStorage
from mlp_sdk.log import get_logger

LOGGER = get_logger()


class LocalStorage(AbstractStorage):

    def __init__(self, path: Path):
        self.path = path

        LOGGER.info(f'Try to setup local storage as path: {self.path}')

        if self.path.exists():
            LOGGER.info(f"'{self.path}' already exists")

            if self.path.is_dir():
                pass

            else:
                error_msg = f'Unable to create/use directory {self.path}: file with such name already exists'
                LOGGER.error(error_msg)
                raise NotADirectoryError(error_msg)

        else:
            self.path.mkdir(parents=True, exist_ok=True)

    def open(self, path: str, mode: str = 'r') -> IO:
        full_path = self.path / path

        try:
            LOGGER.info(f'Try to open path {full_path}')
            if 'w' in mode and len(full_path.parents) and not full_path.parents[0].exists():
                Path(full_path.parents[0]).mkdir(parents=True, exist_ok=True)

            return open(full_path, mode)
        except FileNotFoundError:
            raise KeyError(f'No such key in local storage: {full_path}')

    def remove(self, path: str) -> None:
        full_path = self.path / path

        LOGGER.info(f'Try to remove path {full_path}')
        if full_path.exists():
            if full_path.is_dir():
                LOGGER.info(f"'{full_path}' is directory")
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)
        else:
            LOGGER.warning(f"'{full_path}' doesn't exist")

    @staticmethod
    def name() -> str:
        return 'local'

    def download(self, remote_path: str, local_path: str) -> None:
        is_directory = not os.path.isfile(remote_path)
        LOGGER.info(f'Try to download from {remote_path} to {local_path}, is directory: {is_directory}')

        if is_directory:
            Path(local_path).mkdir(parents=True, exist_ok=True)
            copy_tree(remote_path, local_path)
        else:
            Path(local_path).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(remote_path, local_path)

    def upload(self, local_path: str, remote_path: str) -> None:
        if os.path.isfile(local_path):
            shutil.copyfile(local_path, remote_path)
        else:
            copy_tree(local_path, remote_path)
