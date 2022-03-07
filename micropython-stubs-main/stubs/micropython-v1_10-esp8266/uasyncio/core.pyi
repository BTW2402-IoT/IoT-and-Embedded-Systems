from typing import Any

class CancelledError(Exception): ...

DEBUG: int

class EventLoop:
    def call_at_(self, *args) -> Any: ...
    def call_later(self, *args) -> Any: ...
    def call_later_ms(self, *args) -> Any: ...
    def call_soon(self, *args) -> Any: ...
    def close(self, *args) -> Any: ...
    def create_task(self, *args) -> Any: ...
    def run_forever(self, *args) -> Any: ...
    def run_until_complete(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def time(self, *args) -> Any: ...
    def wait(self, *args) -> Any: ...

class IORead:
    def handle(self, *args) -> Any: ...

class IOReadDone:
    def handle(self, *args) -> Any: ...

class IOWrite:
    def handle(self, *args) -> Any: ...

class IOWriteDone:
    def handle(self, *args) -> Any: ...

class PollEventLoop:
    def add_reader(self, *args) -> Any: ...
    def add_writer(self, *args) -> Any: ...
    def call_at_(self, *args) -> Any: ...
    def call_later(self, *args) -> Any: ...
    def call_later_ms(self, *args) -> Any: ...
    def call_soon(self, *args) -> Any: ...
    def close(self, *args) -> Any: ...
    def create_task(self, *args) -> Any: ...
    def remove_reader(self, *args) -> Any: ...
    def remove_writer(self, *args) -> Any: ...
    def run_forever(self, *args) -> Any: ...
    def run_until_complete(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def time(self, *args) -> Any: ...
    def wait(self, *args) -> Any: ...

class SleepMs:
    def handle(self, *args) -> Any: ...

class StopLoop:
    def handle(self, *args) -> Any: ...

class StreamReader:
    aclose: Any
    read: Any
    readexactly: Any
    readline: Any

class StreamWriter:
    aclose: Any
    awrite: Any
    awriteiter: Any
    def get_extra_info(self, *args) -> Any: ...

class SysCall:
    def handle(self, *args) -> Any: ...

class SysCall1:
    def handle(self, *args) -> Any: ...

def Task(*args) -> Any: ...

class TimeoutError(Exception): ...
class TimeoutObj: ...

_socket: Any

def cancel(*args) -> Any: ...

core: Any

def coroutine(*args) -> Any: ...
def ensure_future(*args) -> Any: ...
def get_event_loop(*args) -> Any: ...

log: Any
open_connection: Any
select: Any

def set_debug(*args) -> Any: ...

sleep: Any
sleep_ms: Any
start_server: Any
time: Any

class type_gen:
    def close(self, *args) -> Any: ...
    def pend_throw(self, *args) -> Any: ...
    def send(self, *args) -> Any: ...
    def throw(self, *args) -> Any: ...

uasyncio: Any
ucollections: Any
uerrno: Any
utimeq: Any

def wait_for(*args) -> Any: ...

wait_for_ms: Any