import copy
import os
import pickle
import shutil
import tempfile
from pathlib import Path

from mlp_sdk.storage import LocalStorage

TEMP_DATA_PATH = Path(__file__).parent / "data"


def test_local_storage():
    test_filename = "test.pkl"

    with tempfile.TemporaryDirectory() as directory:
        storage = LocalStorage(path=Path(directory))

        test_object = [1, 2, [3, [4]]]
        test_object_copy = copy.deepcopy(test_object)

        with storage.open(test_filename, "wb") as fout:
            pickle.dump(test_object, fout)

        with storage.open(test_filename, "rb") as fin:
            test_object_loaded = pickle.loads(fin.read())

        test_object[2] = []

        assert test_object_loaded == test_object_copy

        try:
            os.makedirs(TEMP_DATA_PATH, exist_ok=False)

            # test downloading/uploading
            test_downloaded_filename = "test_downloaded.pkl"
            storage.download(str(Path(directory) / test_filename), str(TEMP_DATA_PATH / test_downloaded_filename))

            assert os.path.exists(TEMP_DATA_PATH / test_downloaded_filename), "Not downloaded"

            # test data directory downloading
            storage.download(str(Path(directory)), str(TEMP_DATA_PATH / "new_downloaded_data_dir"))

            assert os.path.exists(TEMP_DATA_PATH / "new_downloaded_data_dir"), "Not downloaded"
            assert os.path.exists(TEMP_DATA_PATH / "new_downloaded_data_dir" / test_filename), "Not downloaded"

            test_uploaded_filename = "test_uploaded.pkl"
            storage.upload(
                str(TEMP_DATA_PATH / test_downloaded_filename), str(Path(directory) / test_uploaded_filename)
            )

            assert os.path.exists(Path(directory) / test_uploaded_filename), "Not uploaded"

            # test data directory uploading
            storage.upload(str(TEMP_DATA_PATH), str(Path(directory) / "new_uploaded_dir"))

            assert os.path.exists(Path(directory) / "new_uploaded_dir"), "Not uploaded"
            assert os.path.exists(Path(directory) / "new_uploaded_dir" / test_downloaded_filename), "Not uploaded"

            # test removing
            storage.remove(test_filename)
            assert not os.path.exists(test_filename), "Not removed"
            storage.remove(test_uploaded_filename)
            assert not os.path.exists(test_uploaded_filename), "Not removed"

            storage.remove("new_uploaded_dir")
            assert not os.path.exists(Path(directory) / "new_uploaded_dir"), "Not removed"

        except Exception as e:
            assert False, str(e)

        finally:
            shutil.rmtree(TEMP_DATA_PATH)
