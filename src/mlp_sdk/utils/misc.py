from typing import Optional, Tuple, TypeVar
from urllib.parse import urlparse

T = TypeVar("T")
P = TypeVar("P")


def parse_grpc_url(url_str: str) -> Tuple[str, bool]:
    url = urlparse(url_str)

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
