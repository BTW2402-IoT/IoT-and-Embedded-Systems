from typing import Any

class DHT11:
    def humidity(self, *argv) -> Any: ...
    def temperature(self, *argv) -> Any: ...

class DHT22:
    def humidity(self, *argv) -> Any: ...
    def temperature(self, *argv) -> Any: ...

class DHTBase:
    def measure(self, *argv) -> Any: ...

esp: Any
