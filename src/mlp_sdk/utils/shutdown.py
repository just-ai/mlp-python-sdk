import signal
import threading
from typing import Any, Optional

GLOBAL_SHUTDOWN_EVENT = threading.Event()


def _handle_shutdown(_signo: Optional[int] = None, _stack_frame: Optional[Any] = None) -> None:
    GLOBAL_SHUTDOWN_EVENT.set()


def register_shutdown_handler() -> None:
    signal.signal(signal.SIGINT, _handle_shutdown)
    signal.signal(signal.SIGTERM, _handle_shutdown)


def block_until_shutdown() -> None:
    register_shutdown_handler()
    GLOBAL_SHUTDOWN_EVENT.wait()
