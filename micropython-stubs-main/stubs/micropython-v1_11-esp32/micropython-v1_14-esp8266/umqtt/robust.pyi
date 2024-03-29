from typing import Any

class MQTTClient:
    def __init__(self, *args) -> None: ...
    def connect(self, *args) -> Any: ...
    def disconnect(self, *args) -> Any: ...
    def log(self, *args) -> Any: ...
    DEBUG: bool
    def set_callback(self, *args) -> Any: ...
    def set_last_will(self, *args) -> Any: ...
    def ping(self, *args) -> Any: ...
    publish: Any
    def subscribe(self, *args) -> Any: ...
    wait_msg: Any
    def check_msg(self, *args) -> Any: ...
    DELAY: int
    def delay(self, *args) -> Any: ...
    reconnect: Any
