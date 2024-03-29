from typing import Any

class MicroWebSocket:
    def Close(self, *argv) -> Any: ...
    def IsClosed(self, *argv) -> Any: ...
    def SendBinary(self, *argv) -> Any: ...
    def SendText(self, *argv) -> Any: ...
    def _handshake(self, *argv) -> Any: ...
    _handshakeSign: str
    _msgTypeBin: int
    _msgTypeText: int
    _opBinFrame: int
    _opCloseFrame: int
    _opContFrame: int
    _opPingFrame: int
    _opPongFrame: int
    _opTextFrame: int
    def _receiveFrame(self, *argv) -> Any: ...
    def _sendFrame(self, *argv) -> Any: ...
    def _tryAllocByteArray(self, *argv) -> Any: ...
    def _tryStartThread(self, *argv) -> Any: ...
    def _wsProcess(self, *argv) -> Any: ...
    def threadID(self, *argv) -> Any: ...

_thread: Any

def b2a_base64() -> None: ...

gc: Any

def pack() -> None: ...

class sha1:
    def digest(self, *argv) -> Any: ...
    def update(self, *argv) -> Any: ...

time: Any
