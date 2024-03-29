from typing import Any

class CC3K:
    WEP: int
    WPA: int
    WPA2: int
    def connect(self, *args) -> Any: ...
    def disconnect(self, *args) -> Any: ...
    def ifconfig(self, *args) -> Any: ...
    def isconnected(self, *args) -> Any: ...
    def patch_program(self, *args) -> Any: ...
    def patch_version(self, *args) -> Any: ...

class WIZNET5K:
    def ifconfig(self, *args) -> Any: ...
    def isconnected(self, *args) -> Any: ...
    def regs(self, *args) -> Any: ...

def route(*args) -> Any: ...
