from typing import Any

class Dac:
    WRITE: int
    WRITE_EEPROM: int
    def _available(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    portMethod: int
    def setVoltage(self, *argv) -> Any: ...
    def writeData(self, *argv) -> Any: ...

def const() -> None: ...

i2c_bus: Any
unit: Any