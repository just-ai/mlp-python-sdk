import os
import shutil
from pathlib import Path
from typing import IO, Any, Dict, Optional, Union
from uuid import uuid4

import requests

from storage_api import ApiClient, Configuration, FileData, FileOptions
from storage_api.api import files_endpoint_api

# TODO: it needs to be checked with version 2


class FilesAccessor:
    def __init__(
        self,
        url: str,
        token: str,
        mount_path: Optional[str] = None,
        backend_name: Optional[str] = None,
        default_timeout: float = 60,
    ):
        self._api_base_url = url
        self._auth_token = token
        self._client = ApiClient(Configuration(host=url), "MLP-API-KEY", token)
        self._files_api = files_endpoint_api.FilesEndpointApi(self._client)
        self._mount_path = Path(mount_path) if mount_path else None
        self._backend_name = backend_name
        self._default_timeout = float(os.environ.get("MLP_STORAGE_DEFAULT_TIMEOUT_SECONDS", default_timeout))

    def read(self, file_id: str, version: Optional[int] = None, timeout: Optional[float] = None) -> IO[bytes]:
        if self._only_api:
            return self._read_by_api(file_id, version, timeout)

        file_relative_path = self._files_api.get_file_path(file_id, self._backend_name, version)
        file_path = self._mount_path / file_relative_path

        if not file_path.exists():
            return self._read_by_api(file_id, version, timeout)

        return file_path.open("rb")

    def get_file_data(self, file_id: str, version: Optional[int] = None) -> FileData:
        return self._files_api.get_file_data(file_id, version)

    def write(
        self,
        stream: IO[bytes],
        key: Optional[str] = None,
        options: Optional[FileOptions] = None,
        timeout: Optional[float] = None,
    ) -> FileData:
        if self._only_api:
            return self._write_by_api(stream, key, options, timeout)

        temp_name = str(uuid4())
        temp_file_path = self._mount_path / temp_name
        self._write_to_file(temp_file_path, stream)

        return self._files_api.register_file(key, temp_name, options)

    def write_by_file(
        self,
        file: Path,
        key: Optional[str] = None,
        options: Optional[FileOptions] = None,
        timeout: Optional[float] = None,
    ) -> FileData:
        if self._only_api:
            return self._write_by_api(file, key, options, timeout)

        temp_name = str(uuid4())
        temp_file_path = self._mount_path / temp_name
        self._copy_to_temp_file(file, temp_file_path)

        return self._files_api.register_file(key, temp_name, options)

    def _read_by_api(self, file_id: str, version: Optional[int] = None, timeout: Optional[float] = None) -> IO[bytes]:
        url = f"{self._api_base_url}/api/mlpstorage/files/{file_id}/content"
        headers = {"MLP-API-KEY": self._auth_token}
        params = {"version": version} if version is not None else {}

        request_timeout = timeout if timeout is not None else self._default_timeout
        response = requests.get(url, headers=headers, params=params, timeout=request_timeout, stream=True)
        response.raise_for_status()

        return response.raw.read()

    def _write_by_api(
        self,
        file: Union[bytes, Path, IO[bytes]],
        key: Optional[str] = None,
        options: Optional[FileOptions] = None,
        timeout: Optional[int] = None,
    ) -> FileData:
        url = f"{self._api_base_url}/api/mlpstorage/files/multipart"
        headers = {"MLP-API-KEY": self._auth_token}

        data = {"key": key}
        body = self._prepare_file_payload(file)
        if options:
            body["options"] = (None, options.to_json(), "application/json")

        request_timeout = timeout if timeout is not None else self._default_timeout
        response = requests.post(url, headers=headers, files=body, data=data, timeout=request_timeout)
        response.raise_for_status()

        return FileData.from_dict(response.json())

    @staticmethod
    def _prepare_file_payload(file: Union[bytes, Path, IO[bytes]]) -> Dict[str, Any]:
        if isinstance(file, Path):
            file_name = file.name
            file_obj = file.open("rb")
        elif isinstance(file, bytes):
            file_name = "file.bin"
            file_obj = file
        else:
            file_name = "file.bin"
            file_obj = file

        return {"file": (file_name, file_obj, "application/octet-stream")}

    @staticmethod
    def _copy_to_temp_file(src_file: Path, temp_file_path: Path) -> None:
        with src_file.open("rb") as src, temp_file_path.open("wb") as dst:
            shutil.copyfileobj(src, dst)

    @staticmethod
    def _write_to_file(temp_file_path: Path, stream: IO[bytes]) -> None:
        with temp_file_path.open("wb") as temp_file:
            temp_file.write(stream.read())

    @property
    def _only_api(self) -> bool:
        return self._mount_path is None or self._backend_name is None
