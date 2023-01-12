import copy
import os
import pickle
import shutil
import tempfile

from pathlib import Path

from mlp_sdk.storage import S3Storage
TEMP_DATA_PATH = Path(__file__).parent / 'test_data'


def test_s3_storage():

    if 'S3_STORAGE_CONFIG' not in os.environ:
        raise RuntimeError('Unable to run s3 storage test without json config in S3_STORAGE_CONFIG variable')

    test_filename = 'test.pkl'

    config = eval(os.environ['S3_STORAGE_CONFIG'])

    storage = S3Storage(config['mlps_bucket'], config['service_name'], config['region'],
                        config['access_key'], config['secret_key'], config['endpoint'], config['data_dir'])

    test_object = [1, 2, [3, [4]]]
    test_object_copy = copy.deepcopy(test_object)

    with storage.open(test_filename, 'wb') as fout:
        pickle.dump(test_object, fout)

    with storage.open(test_filename, 'rb') as fin:
        test_object_loaded = pickle.loads(fin.read())

    test_object[2] = []

    assert test_object_loaded == test_object_copy

    storage.remove(test_filename)

    try:
        storage.open(test_filename, 'rb')
    except KeyError:
        pass
    else:
        assert False, 'Error: there should be KeyError after removing file'


def test_download_upload_dir():

    if 'S3_STORAGE_CONFIG' not in os.environ:
        raise RuntimeError('Unable to run s3 storage test without json config in S3_STORAGE_CONFIG variable')

    config = eval(os.environ['S3_STORAGE_CONFIG'])

    storage = S3Storage(config['mlps_bucket'], config['service_name'], config['region'],
                        config['access_key'], config['secret_key'], config['endpoint'], config['data_dir'])

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
                    Prefix=os.path.join(config['data_dir'], remote_path_to_be_uploaded)):
                objects_count += 1

            assert objects_count == REAL_FILES_NUMBER, "Something goes wrong w/ uploading"

        except Exception as exc:
            assert False, str(exc)

        finally:
            storage.remove(remote_path_to_be_uploaded)


def test_s3_download_upload_large_files():

    if 'S3_STORAGE_CONFIG' not in os.environ:
        raise RuntimeError('Unable to run s3 storage test without json config in S3_STORAGE_CONFIG variable')

    config = eval(os.environ['S3_STORAGE_CONFIG'])

    storage = S3Storage(config['mlps_bucket'], config['service_name'], config['region'],
                        config['access_key'], config['secret_key'], config['endpoint'], config['data_dir'])

    s3_path = 'caila/generative/models/dialog_ru/v2/default/model.ckpt'

    uploaded_file_s3_path = "temp/test_s3_download_upload_large_file.ckpt"

    try:
        downloaded_file_name = 'test_s3_download_upload_large_file.ckpt'
        storage.download(s3_path, str(TEMP_DATA_PATH / downloaded_file_name))

        try:
            if os.path.getsize(TEMP_DATA_PATH / downloaded_file_name) / 1024 / 1024 / 1024 < 4:
                assert False, "It's not large file. It should be more than 4Gb"
        except OSError as e:
            assert False, f"There should be file. It's not downloaded. Exception: {str(e)}"

        storage.upload(str(TEMP_DATA_PATH / downloaded_file_name), uploaded_file_s3_path)

        again_downloaded_file_name = 'test_s3_download_upload_large_file_again.ckpt'

        storage.download(uploaded_file_s3_path, str(TEMP_DATA_PATH / again_downloaded_file_name))

        try:
            if os.path.getsize(TEMP_DATA_PATH / again_downloaded_file_name) / 1024 / 1024 / 1024 < 4:
                assert False, "It's not large file. It should be more than 4Gb"
        except OSError as e:
            assert False, f"There should be file. It's not downloaded. Exception: {str(e)}"

    except Exception as e:
        assert False, str(e)

    finally:
        shutil.rmtree(TEMP_DATA_PATH)
        storage.remove(uploaded_file_s3_path)
