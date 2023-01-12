from abc import ABC, abstractmethod
from typing import IO


class AbstractStorage(ABC):

    @abstractmethod
    def open(self, path: str, mode: str = 'r') -> IO:
        pass

    @abstractmethod
    def remove(self, path: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def name() -> str:
        pass

    @abstractmethod
    def download(self, remote_path: str, local_path: str) -> None:
        pass

    @abstractmethod
    def upload(self, local_path: str, remote_path: str) -> None:
        pass
