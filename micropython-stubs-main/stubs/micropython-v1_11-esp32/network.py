"""
Module: 'network' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.0
from typing import Any


def __init__(*args) -> Any:
    ...


AP_IF = 1  # type: int
AUTH_MAX = 6  # type: int
AUTH_OPEN = 0  # type: int
AUTH_WEP = 1  # type: int
AUTH_WPA2_PSK = 3  # type: int
AUTH_WPA_PSK = 2  # type: int
AUTH_WPA_WPA2_PSK = 4  # type: int
ETH_CLOCK_GPIO0_IN = 0  # type: int
ETH_CLOCK_GPIO16_OUT = 2  # type: int
ETH_CLOCK_GPIO17_OUT = 3  # type: int


def LAN(*args) -> Any:
    ...


MODE_11B = 1  # type: int
MODE_11G = 2  # type: int
MODE_11N = 4  # type: int
PHY_LAN8720 = 0  # type: int
PHY_TLK110 = 1  # type: int


def PPP(*args) -> Any:
    ...


STAT_ASSOC_FAIL = 203  # type: int
STAT_BEACON_TIMEOUT = 200  # type: int
STAT_CONNECTING = 1001  # type: int
STAT_GOT_IP = 1010  # type: int
STAT_HANDSHAKE_TIMEOUT = 204  # type: int
STAT_IDLE = 1000  # type: int
STAT_NO_AP_FOUND = 201  # type: int
STAT_WRONG_PASSWORD = 202  # type: int
STA_IF = 0  # type: int


def WLAN(*args) -> Any:
    ...


def phy_mode(*args) -> Any:
    ...
