from typing import Any

EXIT: int
PAUSE: int
RESUME: int
RUNNING: int
STATUS: int
STOP: int
SUSPEND: int
SUSPENDED: int
TERMINATED: int
WAITING: int

def allowsuspend(*args) -> Any: ...
def getReplID(*args) -> Any: ...
def getSelfName(*args) -> Any: ...
def getThreadName(*args) -> Any: ...
def getmsg(*args) -> Any: ...
def getnotification(*args) -> Any: ...
def isnotified(*args) -> Any: ...
def list(*args) -> Any: ...
def lock(*args) -> Any: ...
def notify(*args) -> Any: ...
def replAcceptMsg(*args) -> Any: ...
def resume(*args) -> Any: ...
def sendmsg(*args) -> Any: ...
def stack_size(*args) -> Any: ...
def start_new_thread(*args) -> Any: ...
def status(*args) -> Any: ...
def stop(*args) -> Any: ...
def suspend(*args) -> Any: ...
def unlock(*args) -> Any: ...
def wait(*args) -> Any: ...
