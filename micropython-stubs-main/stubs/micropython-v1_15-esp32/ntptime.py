"""
Module: 'ntptime' on micropython-v1.15-esp32
"""
# MCU: {'ver': 'v1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


def time(*args) -> Any:
    ...


NTP_DELTA = 3155673600  # type: int
host = "pool.ntp.org"  # type: str


def settime(*args) -> Any:
    ...
