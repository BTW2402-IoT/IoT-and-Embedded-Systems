from typing import Any

AP_IF: int
AUTH_OPEN: int
AUTH_WEP: int
AUTH_WPA2_PSK: int
AUTH_WPA_PSK: int
AUTH_WPA_WPA2_PSK: int
MODE_11B: int
MODE_11G: int
MODE_11N: int
STA_IF: int

def WLAN(*args) -> Any: ...

class ftp:
    def pause(self, *args) -> Any: ...
    def resume(self, *args) -> Any: ...
    def stack(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def status(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...

class mDNS:
    def addService(self, *args) -> Any: ...
    def queryHost(self, *args) -> Any: ...
    def queryService(self, *args) -> Any: ...
    def removeService(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...

class mqtt:
    def config(self, *args) -> Any: ...
    def free(self, *args) -> Any: ...
    def publish(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def status(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def subscribe(self, *args) -> Any: ...
    def unsubscribe(self, *args) -> Any: ...

def phy_mode(*args) -> Any: ...

class telnet:
    def pause(self, *args) -> Any: ...
    def resume(self, *args) -> Any: ...
    def stack(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def status(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
