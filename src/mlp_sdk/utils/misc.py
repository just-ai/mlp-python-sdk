from typing import Optional, Tuple, TypeVar
from urllib.parse import urlparse

T = TypeVar("T")
P = TypeVar("P")


def parse_grpc_url(url_str: str) -> Tuple[str, bool]:
    if "://" not in url_str:
        url_str = "https://" + url_str

    url = urlparse(url_str)

    if not url.hostname:
        raise Exception("Invalid url")

    secure = url.scheme == "https"
    if url.port:
        port = url.port
    else:
        if secure:
            port = 443
        else:
            port = 80

    return f"{url.hostname}:{port}", secure


def required(val: T | None, message: str = "Value is required") -> T:
    if val is None:
        raise Exception(message)
    return val


def get_one_of(*args: Optional[P], error_message: Optional[str] = None) -> P:
    for x in args:
        if x is not None:
            return x
    if error_message:
        raise Exception(error_message)
    else:
        raise Exception("No value for required field")


def remove_null_fields(obj: dict) -> dict:
    """
    Recursively removes all fields with None values from dictionaries,
    including nested dictionaries and lists.

    Args:
        obj: Dictionary to process

    Returns:
        Dictionary with all None values removed
    """
    if not isinstance(obj, dict):
        return obj

    result = {}
    for key, value in obj.items():
        if value is None:
            continue
        elif isinstance(value, dict):
            result[key] = remove_null_fields(value)
        elif isinstance(value, list):
            result[key] = [remove_null_fields(item) if isinstance(item, dict) else item for item in value]
        else:
            result[key] = value

    return result
