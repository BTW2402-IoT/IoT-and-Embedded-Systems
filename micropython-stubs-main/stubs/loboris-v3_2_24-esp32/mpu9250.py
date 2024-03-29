"""
Module: 'mpu9250' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0 - updated
"""
from typing import Any


class AK8963:
    """"""

    def _register_char(self, *args) -> Any:
        pass

    def _register_short(self, *args) -> Any:
        pass

    def _register_three_shorts(self, *args) -> Any:
        pass

    adjustement = None
    magnetic = None
    whoami = None


class MPU6500:
    """"""

    def _accel_fs(self, *args) -> Any:
        pass

    def _gyro_fs(self, *args) -> Any:
        pass

    def _register_char(self, *args) -> Any:
        pass

    def _register_short(self, *args) -> Any:
        pass

    def _register_three_shorts(self, *args) -> Any:
        pass

    acceleration = None
    gyro = None
    whoami = None


class MPU9250:
    """"""

    acceleration = None
    gyro = None
    magnetic = None
    whoami = None


def const(*args) -> Any:
    pass
