from typing import Any

bdev: Any

class FlashBdev:
    def __init__(self, *args) -> None: ...
    def ioctl(self, *args) -> Any: ...
    def readblocks(self, *args) -> Any: ...
    def writeblocks(self, *args) -> Any: ...
    SEC_SIZE: int

size: int
start_sec: int
