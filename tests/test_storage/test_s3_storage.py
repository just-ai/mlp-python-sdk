import copy
import os
import pickle
import shutil
import tempfile
from pathlib import Path

import pytest

from mlp_sdk.storage import S3Storage

TEMP_DATA_PATH = Path(__file__).parent / "test_data"


def _build_storage_or_skip():
    """Live-интеграционные S3-тесты. Скипаем (а не валим suite), если окружение
    не предоставляет рабочий S3: нет S3_STORAGE_CONFIG (локально) либо endpoint
    недоступен / SSL / креды битые (напр. в CI-контейнере нет CA-bundle).
    Возвращает (storage, config)."""
    if "S3_STORAGE_CONFIG" not in os.environ:
        pytest.skip("S3_STORAGE_CONFIG is not set — skipping live S3 integration test")

    config = eval(os.environ["S3_STORAGE_CONFIG"])

    # Конструктор S3Storage уже устанавливает соединение (может упасть по SSL/сети),
    # затем лёгкий list как connectivity probe. Любая ошибка соединения/SSL/доступа =>
    # окружение не пригодно для live-теста, скипаем (тело теста при этом не маскируется).
    try:
        storage = S3Storage(
            config["mlp_bucket"],
            config["service_name"],
            config["region"],
            config["access_key"],
            config["secret_key"],
            config["endpoint"],
            config["data_dir"],
        )
        next(iter(storage.resource.Bucket(storage.bucket).objects.limit(1)), None)
    except Exception as exc:  # noqa: BLE001
        pytest.skip(f"S3 endpoint not usable in this environment: {type(exc).__name__}: {exc}")

    return storage, config


def test_s3_storage():
    storage, _config = _build_storage_or_skip()

    test_filename = "test.pkl"

    test_object = [1, 2, [3, [4]]]
    test_object_copy = copy.deepcopy(test_object)

    with storage.open(test_filename, "wb") as fout:
        pickle.dump(test_object, fout)

    with storage.open(test_filename, "rb") as fin:
        test_object_loaded = pickle.loads(fin.read())

    test_object[2] = []

    assert test_object_loaded == test_object_copy

    storage.remove(test_filename)

    try:
        storage.open(test_filename, "rb")
    except KeyError:
        pass
    else:
        assert False, "Error: there should be KeyError after removing file"  # noqa: B011


def test_download_upload_dir():
    storage, config = _build_storage_or_skip()

    remote_path = "huggingface/models/cointegrated/rubert-tiny2/default"

    remote_path_to_be_uploaded = "temp/test_s3_storage/models/cointegrated/rubert-tiny2-uploaded"

    REAL_FILES_NUMBER = 14

    with tempfile.TemporaryDirectory() as directory:
        local_path = Path(directory) / "cointegrated/rubert-tiny2"

        try:
            storage.download(remote_path, str(local_path))

            assert len(os.listdir(local_path)) == REAL_FILES_NUMBER, "Something goes wrong w/ downloading"

            storage.upload(str(local_path), remote_path_to_be_uploaded)

            objects_count = 0

            for _ in storage.resource.Bucket(storage.bucket).objects.filter(
                Prefix=os.path.join(config["data_dir"], remote_path_to_be_uploaded)
            ):
                objects_count += 1

            assert objects_count == REAL_FILES_NUMBER, "Something goes wrong w/ uploading"

        except Exception as exc:
            assert False, str(exc)  # noqa: B011

        finally:
            storage.remove(remote_path_to_be_uploaded)


def test_s3_download_upload_large_files():
    storage, _config = _build_storage_or_skip()

    s3_path = "caila/generative/models/dialog_ru/v2/default/model.ckpt"

    uploaded_file_s3_path = "temp/test_s3_download_upload_large_file.ckpt"

    try:
        downloaded_file_name = "test_s3_download_upload_large_file.ckpt"
        storage.download(s3_path, str(TEMP_DATA_PATH / downloaded_file_name))

        try:
            if os.path.getsize(TEMP_DATA_PATH / downloaded_file_name) / 1024 / 1024 / 1024 < 4:
                assert False, "It's not large file. It should be more than 4Gb"  # noqa: B011
        except OSError as e:
            assert False, f"There should be file. It's not downloaded. Exception: {str(e)}"  # noqa: B011

        storage.upload(str(TEMP_DATA_PATH / downloaded_file_name), uploaded_file_s3_path)

        again_downloaded_file_name = "test_s3_download_upload_large_file_again.ckpt"

        storage.download(uploaded_file_s3_path, str(TEMP_DATA_PATH / again_downloaded_file_name))

        try:
            if os.path.getsize(TEMP_DATA_PATH / again_downloaded_file_name) / 1024 / 1024 / 1024 < 4:
                assert False, "It's not large file. It should be more than 4Gb"  # noqa: B011
        except OSError as e:
            assert False, f"There should be file. It's not downloaded. Exception: {str(e)}"  # noqa: B011

    except Exception as e:
        assert False, str(e)  # noqa: B011

    finally:
        shutil.rmtree(TEMP_DATA_PATH)
        storage.remove(uploaded_file_s3_path)
