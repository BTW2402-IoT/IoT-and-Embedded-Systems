from typing import Any

class Ext_io:
    ALL_INPUT: int
    ALL_OUTPUT: int
    INPUT: int
    OUTPUT: int
    def _available(self, *argv) -> Any: ...
    def _get_mode(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def digitRead(self, *argv) -> Any: ...
    def digitReadPort(self, *argv) -> Any: ...
    def digitWrite(self, *argv) -> Any: ...
    def digitWritePort(self, *argv) -> Any: ...
    def setPinMode(self, *argv) -> Any: ...
    def setPortMode(self, *argv) -> Any: ...

def const() -> None: ...

i2c_bus: Any
unit: Any
ustruct: Any
