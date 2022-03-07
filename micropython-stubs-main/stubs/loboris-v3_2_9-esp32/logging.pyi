from typing import Any

CRITICAL: int
DEBUG: int
ERROR: int
INFO: int

class Logger:
    def _level_str(self, *args) -> Any: ...
    def critical(self, *args) -> Any: ...
    def debug(self, *args) -> Any: ...
    def error(self, *args) -> Any: ...
    def info(self, *args) -> Any: ...
    def log(self, *args) -> Any: ...
    def warning(self, *args) -> Any: ...

NOTSET: int
WARNING: int
_level: int
_level_dict: Any
_loggers: Any
_stream: Any

def basicConfig(*args) -> Any: ...
def debug(*args) -> Any: ...
def getLogger(*args) -> Any: ...
def info(*args) -> Any: ...

sys: Any
