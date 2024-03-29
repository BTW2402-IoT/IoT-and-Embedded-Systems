from typing import Any

class Cellular:
    def _getResponse(self, *argv) -> Any: ...
    def _waitResponse(self, *argv) -> Any: ...
    def _writeAT(self, *argv) -> Any: ...
    def connect(self, *argv) -> Any: ...
    def connected(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def getAvailable(self, *argv) -> Any: ...
    def getLocalIP(self, *argv) -> Any: ...
    def getNetworkState(self, *argv) -> Any: ...
    def getSimState(self, *argv) -> Any: ...
    def gprsConnect(self, *argv) -> Any: ...
    def gprsDisconnect(self, *argv) -> Any: ...
    def init(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def restart(self, *argv) -> Any: ...
    def send(self, *argv) -> Any: ...
    def sendline(self, *argv) -> Any: ...
    def testAT(self, *argv) -> Any: ...

machine: Any
time: Any

def wait_ms() -> None: ...
