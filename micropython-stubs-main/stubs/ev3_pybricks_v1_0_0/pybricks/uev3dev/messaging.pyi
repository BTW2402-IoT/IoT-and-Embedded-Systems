from typing import Any

ARRAY: int
SOCK_STREAM: int
UINT16: int
UINT8: int
_thread: Any

def addressof() -> None: ...
def sizeof() -> None: ...

class socket:
    def accept(self, *argv) -> Any: ...
    def bind(self, *argv) -> Any: ...
    def close(self, *argv) -> Any: ...
    def connect(self, *argv) -> Any: ...
    def fileno(self, *argv) -> Any: ...
    def listen(self, *argv) -> Any: ...
    def makefile(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def readinto(self, *argv) -> Any: ...
    def readline(self, *argv) -> Any: ...
    def recv(self, *argv) -> Any: ...
    def recvfrom(self, *argv) -> Any: ...
    def send(self, *argv) -> Any: ...
    def sendto(self, *argv) -> Any: ...
    def setblocking(self, *argv) -> Any: ...
    def setsockopt(self, *argv) -> Any: ...
    def write(self, *argv) -> Any: ...

class struct: ...

time: Any