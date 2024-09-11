import os.path
from io import BytesIO, StringIO
from pathlib import Path
from typing import IO, Optional

import boto3
from botocore.exceptions import ClientError

from mlp_sdk.log import get_logger
from mlp_sdk.storage.abstract_storage import AbstractStorage
from mlp_sdk.utilities.misc import os_path_join_corrected

LOGGER = get_logger(__name__)


class S3BytesStream(BytesIO):
    def __init__(self, client, bucket, path):
        super().__init__()
        self.client = client
        self.bucket = bucket
        self.path = path

    def close(self):
        self.client.put_object(Body=self.getvalue(), Bucket=self.bucket, Key=self.path)
        BytesIO.close(self)


class S3StringStream(StringIO):
    def __init__(self, client, bucket, path):
        super().__init__()
        self.client = client
        self.bucket = bucket
        self.path = path

    def close(self):
        self.client.put_object(Body=self.getvalue(), Bucket=self.bucket, Key=self.path)
        StringIO.close(self)


class S3Storage(AbstractStorage):
    def __init__(
        self,
        bucket: str,
        service_name: str,
        region: str,
        access_key: str,
        secret_key: str,
        endpoint: str,
        data_dir: Optional[str] = None,
    ):
        self.bucket = bucket
        self.data_dir = data_dir

        try:
            LOGGER.info("Try to setup S3 storage")
            self.client = boto3.client(
                service_name=service_name,
                region_name=region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                endpoint_url=endpoint,
            )

            self.resource = boto3.resource(
                service_name=service_name,
                region_name=region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                endpoint_url=endpoint,
            )
        except Exception as exc:
            LOGGER.error(str(exc))
            raise

        try:
            LOGGER.debug(f"Check bucket {self.bucket} existence and accessibility")
            self.client.head_bucket(Bucket=self.bucket)
            LOGGER.info(f"Bucket {self.bucket} exists and is accessible")

        except ClientError as exc:
            LOGGER.error(str(exc))

            try:
                LOGGER.debug(f"Bucket {self.bucket} does not exist, try to create new one")
                self.client.create_bucket(Bucket=self.bucket)
                LOGGER.info(f"Bucket {self.bucket} was successfully created")

            except ClientError as exc_2:
                LOGGER.error(str(exc_2))
                raise

    def open(self, path: str, mode: str = "r") -> IO:
        modes = list(mode)

        if self.data_dir is not None:
            path = os_path_join_corrected(self.data_dir, path)

        LOGGER.debug(f"Try to open path {path}")

        if ("r" in modes or "w" in modes) and (len(modes) == 1 or (len(modes) == 2 and "b" in modes)):
            if "r" in mode:
                try:
                    object_ = self.client.get_object(Bucket=self.bucket, Key=path)["Body"].read()

                    if "b" in mode:
                        return BytesIO(object_)

                    else:
                        return StringIO(object_.decode("utf-8"))

                except ClientError as e:
                    if e.response["Error"]["Code"] == "404" or e.response["Error"]["Code"] == "NoSuchKey":
                        raise KeyError(f"No such key in s3 storage: {path}")  # noqa: B904

                    elif e.response["Error"]["Code"] == "403" or e.response["Error"]["Code"] == "Forbidden":
                        raise PermissionError("Access denied (probably invalid credentials are given)")  # noqa: B904

                    else:
                        raise RuntimeError(f"Unknown error: {str(e)}")  # noqa: B904

            elif "w" in mode:
                if "b" in mode:
                    return S3BytesStream(self.client, self.bucket, path)
                else:
                    return S3StringStream(self.client, self.bucket, path)
        else:
            raise ValueError(f"Invalid mode: '{mode}'")

    def remove(self, path: str) -> None:
        if self.data_dir is not None:
            path = os_path_join_corrected(self.data_dir, path)

        objects_count = 0
        for _ in self.resource.Bucket(self.bucket).objects.filter(Prefix=path):
            objects_count += 1

        if objects_count == 0:
            error_msg = f"File or directory doesn't exist: '{path}'"
            LOGGER.warning(error_msg)

        LOGGER.debug(f"Try to remove path {path}")
        if objects_count > 1:
            for obj in self.resource.Bucket(self.bucket).objects.filter(Prefix=path):
                self.client.delete_object(Bucket=self.bucket, Key=obj.key)
        else:
            self.client.delete_object(Bucket=self.bucket, Key=path)

    def download(self, remote_path: str, local_path: str) -> None:
        """
        Downloads file or directory from S3. Wrapper of
         https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.download_file
        Args:
            remote_path: S3 path to file or dir w/ its filename
            local_path: local path to file or dir w/ its (same or new) filename
        """
        if self.data_dir is not None:
            remote_path = os_path_join_corrected(self.data_dir, remote_path)

        objects_count = 0
        for _ in self.resource.Bucket(self.bucket).objects.filter(Prefix=remote_path):
            objects_count += 1

        LOGGER.debug(f"Try to download from {remote_path} to {local_path}, is directory: {objects_count > 1}")
        if objects_count > 1:
            Path(local_path).mkdir(parents=True, exist_ok=True)
            self._download_directory(remote_path, local_path)
        else:
            Path(local_path).parent.mkdir(parents=True, exist_ok=True)
            self.client.download_file(self.bucket, remote_path, local_path)

    def _download_directory(self, remote_path: str, local_path: str) -> None:
        if not os.path.exists(local_path):
            os.makedirs(local_path)

        if not os.path.isdir(local_path):
            error_msg = "For data directory downloading 'local_path' arg must be directory!"
            LOGGER.error(error_msg)
            raise NotADirectoryError(error_msg)

        for obj in self.resource.Bucket(self.bucket).objects.filter(Prefix=remote_path):
            local_file_path = str(Path(local_path) / obj.key.split("/")[-1])
            self.resource.Bucket(self.bucket).download_file(obj.key, local_file_path)

    def _upload_directory(self, local_path: str, remote_path: str) -> None:
        for name in os.listdir(local_path):
            local_path_file_name = str(Path(local_path) / name)
            remote_path_file_name = f"{remote_path}/{name}"

            if os.path.isfile(local_path_file_name):
                self.client.upload_file(local_path_file_name, self.bucket, remote_path_file_name)

    def upload(self, local_path: str, remote_path: str) -> None:
        """
        Uploads file or directory to S3. Wrapper of
         https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file
        Args:
            local_path: local path to uploaded file or dir
            s3_path: S3 path for uploaded file or dir w/ its (same or new) name
        """
        if self.data_dir is not None:
            remote_path = os_path_join_corrected(self.data_dir, remote_path)

        LOGGER.debug(f"Try to download from {remote_path} to {local_path}, is directory: {os.path.isdir(local_path)}")
        if os.path.isdir(local_path):
            self._upload_directory(local_path, remote_path)
        else:
            self.client.upload_file(local_path, self.bucket, remote_path)

        # check uploaded
        if "Contents" in self.client.list_objects(Bucket=self.bucket, Prefix=remote_path):
            LOGGER.info("Successfully uploaded.")
        else:
            raise ClientError(
                error_response={"Error": {"Code": 400, "Message": "Something goes wrong"}},
                operation_name="data uploading",
            )

    @staticmethod
    def name() -> str:
        return "s3"
