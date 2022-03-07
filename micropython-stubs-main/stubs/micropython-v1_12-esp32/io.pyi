from typing import Any

def open(*args) -> Any: ...

class BufferedWriter:
    def write(self, *args) -> Any: ...
    def flush(self, *args) -> Any: ...

class BytesIO:
    def close(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def flush(self, *args) -> Any: ...
    def getvalue(self, *args) -> Any: ...
    def seek(self, *args) -> Any: ...

class FileIO:
    def close(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def flush(self, *args) -> Any: ...
    def readlines(self, *args) -> Any: ...
    def seek(self, *args) -> Any: ...
    def tell(self, *args) -> Any: ...

class IOBase: ...

class StringIO:
    def close(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def flush(self, *args) -> Any: ...
    def getvalue(self, *args) -> Any: ...
    def seek(self, *args) -> Any: ...

class TextIOWrapper:
    def close(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def flush(self, *args) -> Any: ...
    def readlines(self, *args) -> Any: ...
    def seek(self, *args) -> Any: ...
    def tell(self, *args) -> Any: ...
