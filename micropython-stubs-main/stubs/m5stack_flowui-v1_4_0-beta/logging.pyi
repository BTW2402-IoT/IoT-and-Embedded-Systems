from typing import Any

CRITICAL: int
DEBUG: int
ERROR: int
INFO: int

class Logger:
    def _level_str(self, *argv) -> Any: ...
    def critical(self, *argv) -> Any: ...
    def debug(self, *argv) -> Any: ...
    def error(self, *argv) -> Any: ...
    def exc(self, *argv) -> Any: ...
    def exception(self, *argv) -> Any: ...
    def info(self, *argv) -> Any: ...
    def isEnabledFor(self, *argv) -> Any: ...
    level: int
    def log(self, *argv) -> Any: ...
    def setLevel(self, *argv) -> Any: ...
    def warning(self, *argv) -> Any: ...

NOTSET: int
WARNING: int
_level: int
_level_dict: Any
_loggers: Any
_stream: Any

def basicConfig() -> None: ...
def debug() -> None: ...
def getLogger() -> None: ...
def info() -> None: ...

sys: Any
