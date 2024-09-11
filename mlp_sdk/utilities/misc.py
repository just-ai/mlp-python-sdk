import os.path
from pathlib import Path
from typing import Dict, Optional, Union

import yaml


def parse_config(config_path: Path) -> Dict:
    with open(config_path, "r") as cfg_file:
        return yaml.load(cfg_file, Loader=yaml.SafeLoader)


def get_env(name: str, default_value: Optional[str] = None) -> str:
    value = os.environ.get(name)

    if value is not None and len(value):
        return value

    elif default_value is not None:
        return default_value

    raise ValueError(f'Environment variable "{name}" is not defined or None or empty: "{str(value)}"')


def os_path_join_corrected(path_a: Union[str, Path], path_b: Union[str, Path]) -> str:
    """
    Correct os.path.join for cases like:
        - os.path.join('a/b/', '/c') -> '/c' instead of 'a/b/c'
        - os.path.join('a/b/', '/') -> '/' instead of 'a/b/'

    Args:
        path_a: first path piece
        path_b: second path piece

    Returns:
        joined path
    """

    if isinstance(path_b, Path):
        path_b = str(path_b)

    if path_b[0] == "/":
        path_b = path_b[1:]

    return os.path.join(path_a, path_b)
