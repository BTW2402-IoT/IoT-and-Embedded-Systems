from typing import Any

class Event:
    def __init__(self, *args) -> None: ...
    def clear(self, *args) -> Any: ...
    def set(self, *args) -> Any: ...
    def is_set(self, *args) -> Any: ...
    wait: Any
