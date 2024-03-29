from typing import Any

class Ev3devSensor:
    def _close_files(self, *argv) -> Any: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...

class Ev3devUartSensor:
    def _close_files(self, *argv) -> Any: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _reset(self, *argv) -> Any: ...
    def _reset_port(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...

class StopWatch:
    def pause(self, *argv) -> Any: ...
    def reset(self, *argv) -> Any: ...
    def resume(self, *argv) -> Any: ...
    def time(self, *argv) -> Any: ...

def get_sensor_path() -> None: ...
def listdir() -> None: ...

path: Any

def read_int() -> None: ...
def read_str() -> None: ...
def wait() -> None: ...
def write_int() -> None: ...
def write_str() -> None: ...
