from typing import Any

class VfsFat:
    def chdir(self, *argv) -> Any: ...
    def getcwd(self, *argv) -> Any: ...
    def ilistdir(self, *argv) -> Any: ...
    def mkdir(self, *argv) -> Any: ...
    def mkfs(self, *argv) -> Any: ...
    def mount(self, *argv) -> Any: ...
    def open(self, *argv) -> Any: ...
    def remove(self, *argv) -> Any: ...
    def rename(self, *argv) -> Any: ...
    def rmdir(self, *argv) -> Any: ...
    def stat(self, *argv) -> Any: ...
    def statvfs(self, *argv) -> Any: ...
    def umount(self, *argv) -> Any: ...

def chdir() -> None: ...
def dupterm() -> None: ...
def dupterm_notify() -> None: ...
def getcwd() -> None: ...
def ilistdir() -> None: ...
def listdir() -> None: ...
def mkdir() -> None: ...
def mount() -> None: ...
def remove() -> None: ...
def rename() -> None: ...
def rmdir() -> None: ...
def stat() -> None: ...
def statvfs() -> None: ...
def umount() -> None: ...
def uname() -> None: ...
def urandom() -> None: ...
