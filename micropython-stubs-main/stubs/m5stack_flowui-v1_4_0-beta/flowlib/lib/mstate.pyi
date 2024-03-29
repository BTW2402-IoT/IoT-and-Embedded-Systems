from typing import Any

class MState:
    def end(self, *argv) -> Any: ...
    def loop(self, *argv) -> Any: ...
    def start(self, *argv) -> Any: ...

class MStateManager:
    def change(self, *argv) -> Any: ...
    def nextState(self, *argv) -> Any: ...
    def register(self, *argv) -> Any: ...
    def run(self, *argv) -> Any: ...
    def start(self, *argv) -> Any: ...
    def stop(self, *argv) -> Any: ...
    def unregister(self, *argv) -> Any: ...

gc: Any
utime: Any
