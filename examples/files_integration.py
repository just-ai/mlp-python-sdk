from io import BytesIO
from typing import IO, Optional, Type

from pydantic import BaseModel
from storage_api import FileOptions

from mlp_sdk.abstract.task import Task
from mlp_sdk.hosting.host import host_mlp_cloud
from mlp_sdk.storage.files_factory import get_files


class FileKeySchema(BaseModel):
    file_id: str
    version: Optional[int]


class ReplacingRequest(BaseModel):
    old: str
    new: str


class TextReplacementService(Task):
    def __init__(self, config: BaseModel, sdk) -> None:
        super().__init__(config, sdk)
        self.files = get_files()

    @property
    def init_config_schema(self) -> Type[BaseModel]:
        return BaseModel

    @property
    def predict_config_schema(self) -> Type[BaseModel]:
        return FileKeySchema

    def predict(self, data: ReplacingRequest, config: FileKeySchema) -> FileKeySchema:
        content_bytes = self.files.read(config.file_id, config.version)
        original_file_name = self.files.get_file_data(config.file_id, config.version).file_name
        replaced_content_bytes = self._replace(content_bytes, data.old, data.new)

        options = FileOptions(file_name=f"replacing-{original_file_name}", ttl_since_creation_seconds=360, replicate_to_all_backends=True)
        file_data = self.files.write(replaced_content_bytes, options=options)

        return FileKeySchema(file_id=file_data.key, version=file_data.version)

    @staticmethod
    def _replace(io_bytes: IO[bytes], old_str: str, new_str: str) -> IO[bytes]:
        content = io_bytes.read().decode("utf-8")
        updated_content = content.replace(old_str, new_str)
        updated_content_bytes = updated_content.encode("utf-8")
        return BytesIO(updated_content_bytes)


if __name__ == "__main__":
    host_mlp_cloud(task=TextReplacementService, params=BaseModel())
