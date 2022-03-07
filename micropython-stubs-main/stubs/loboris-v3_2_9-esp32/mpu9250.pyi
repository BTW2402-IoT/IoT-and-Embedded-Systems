from typing import Any

class AK8963:
    def _register_char(self, *args) -> Any: ...
    def _register_short(self, *args) -> Any: ...
    def _register_three_shorts(self, *args) -> Any: ...
    adjustement: Any
    magnetic: Any
    whoami: Any

class MPU6500:
    def _accel_fs(self, *args) -> Any: ...
    def _gyro_fs(self, *args) -> Any: ...
    def _register_char(self, *args) -> Any: ...
    def _register_short(self, *args) -> Any: ...
    def _register_three_shorts(self, *args) -> Any: ...
    acceleration: Any
    gyro: Any
    whoami: Any

class MPU9250:
    acceleration: Any
    gyro: Any
    magnetic: Any
    whoami: Any

def const(*args) -> Any: ...
