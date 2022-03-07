"""
Module: 'dht' on esp8266 v1.10
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.10-8-g8b7039d7d on 2019-01-26', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any


class DHT11:
    """"""

    def humidity(self, *args) -> Any:
        pass

    def measure(self, *args) -> Any:
        pass

    def temperature(self, *args) -> Any:
        pass


class DHT22:
    """"""

    def humidity(self, *args) -> Any:
        pass

    def measure(self, *args) -> Any:
        pass

    def temperature(self, *args) -> Any:
        pass


class DHTBase:
    """"""

    def measure(self, *args) -> Any:
        pass


def dht_readinto(*args) -> Any:
    pass
