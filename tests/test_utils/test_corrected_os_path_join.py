import os.path

from pathlib import Path

from mlp_sdk.utilities.misc import os_path_join_corrected


def test():
    # When in Python, there will be a bug fix, here we should get the exception
    assert os.path.join('a/b/', '/c') != 'a/b/c'

    assert os_path_join_corrected('a/b/', '/c') == 'a/b/c'

    # When in Python, there will be a bug fix, here we should get the exception
    assert os.path.join('a/b/', '/') != 'a/b/'

    assert os_path_join_corrected('a/b/', '/') == 'a/b/'

    assert os_path_join_corrected('/a/b/', 'c') == '/a/b/c'
    assert os_path_join_corrected('/a/b/', '/c') == '/a/b/c'

    assert os_path_join_corrected(Path('/a/b/'), Path('c')) == '/a/b/c'
    assert os_path_join_corrected('/a/b/', Path('c')) == '/a/b/c'
    assert os_path_join_corrected(Path('/a/b/'), 'c') == '/a/b/c'
