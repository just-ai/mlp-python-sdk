import os

from mlp_sdk.files import FilesAccessor


def get_files():
    return FilesAccessor(
        url=os.environ["MLP_STORAGE_ENDPOINT"],
        token=os.environ["MLP_SERVICE_TOKEN"],
        mount_path=os.environ.get("MLP_STORAGE_MOUNT_PATH"),
        backend_name=os.environ.get("MLP_STORAGE_BACKEND_NAME"),
    )
