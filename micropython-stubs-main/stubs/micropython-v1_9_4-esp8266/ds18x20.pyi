from typing import Any

class DS18X20:
    def convert_temp(self, *argv) -> Any: ...
    def read_scratch(self, *argv) -> Any: ...
    def read_temp(self, *argv) -> Any: ...
    def scan(self, *argv) -> Any: ...
    def write_scratch(self, *argv) -> Any: ...

def const() -> None: ...
