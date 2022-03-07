from typing import Any

AF_INET: int
AF_INET6: int
AF_UNIX: int
MSG_DONTROUTE: int
MSG_DONTWAIT: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_STREAM: int
SOL_SOCKET: int
SO_BROADCAST: int
SO_ERROR: int
SO_KEEPALIVE: int
SO_LINGER: int
SO_REUSEADDR: int

def getaddrinfo() -> None: ...
def inet_ntop() -> None: ...
def inet_pton() -> None: ...
def sockaddr() -> None: ...

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