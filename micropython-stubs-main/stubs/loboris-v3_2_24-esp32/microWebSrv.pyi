from typing import Any

class MicroWebSocket:
    def Close(self, *args) -> Any: ...
    def IsClosed(self, *args) -> Any: ...
    def SendBinary(self, *args) -> Any: ...
    def SendText(self, *args) -> Any: ...
    def _handshake(self, *args) -> Any: ...
    _handshakeSign: str
    _msgTypeBin: int
    _msgTypeText: int
    _opBinFrame: int
    _opCloseFrame: int
    _opContFrame: int
    _opPingFrame: int
    _opPongFrame: int
    _opTextFrame: int
    def _receiveFrame(self, *args) -> Any: ...
    def _sendFrame(self, *args) -> Any: ...
    def _tryAllocByteArray(self, *args) -> Any: ...
    def _tryStartThread(self, *args) -> Any: ...
    def _wsProcess(self, *args) -> Any: ...
    def threadID(self, *args) -> Any: ...

class MicroWebSrv:
    def GetMimeTypeFromFilename(self, *args) -> Any: ...
    def GetRouteHandler(self, *args) -> Any: ...
    def HTMLEscape(self, *args) -> Any: ...
    def IsStarted(self, *args) -> Any: ...
    def SetNotFoundPageUrl(self, *args) -> Any: ...
    def Start(self, *args) -> Any: ...
    def State(self, *args) -> Any: ...
    def Stop(self, *args) -> Any: ...
    _client: Any
    _docoratedRouteHandlers: Any
    def _fileExists(self, *args) -> Any: ...
    _html_escape_chars: Any
    _indexPages: Any
    def _isPyHTMLFile(self, *args) -> Any: ...
    _mimeTypes: Any
    def _physPathFromURLPath(self, *args) -> Any: ...
    _pyhtmlPagesExt: str
    _response: Any
    def _serverProcess(self, *args) -> Any: ...
    def _tryAllocByteArray(self, *args) -> Any: ...
    def _tryStartThread(self, *args) -> Any: ...
    def _unquote(self, *args) -> Any: ...
    def _unquote_plus(self, *args) -> Any: ...
    def route(self, *args) -> Any: ...
    def threadID(self, *args) -> Any: ...

class MicroWebSrvRoute: ...

class MicroWebTemplate:
    def Execute(self, *args) -> Any: ...
    INSTRUCTION_ELIF: str
    INSTRUCTION_ELSE: str
    INSTRUCTION_END: str
    INSTRUCTION_FOR: str
    INSTRUCTION_IF: str
    INSTRUCTION_INCLUDE: str
    INSTRUCTION_PYTHON: str
    TOKEN_CLOSE: str
    TOKEN_CLOSE_LEN: int
    TOKEN_OPEN: str
    TOKEN_OPEN_LEN: int
    def Validate(self, *args) -> Any: ...
    def _parseBloc(self, *args) -> Any: ...
    def _parseCode(self, *args) -> Any: ...
    def _processInstructionELIF(self, *args) -> Any: ...
    def _processInstructionELSE(self, *args) -> Any: ...
    def _processInstructionEND(self, *args) -> Any: ...
    def _processInstructionFOR(self, *args) -> Any: ...
    def _processInstructionIF(self, *args) -> Any: ...
    def _processInstructionINCLUDE(self, *args) -> Any: ...
    def _processInstructionPYTHON(self, *args) -> Any: ...
    def _processToken(self, *args) -> Any: ...

_thread: Any

def dumps(*args) -> Any: ...

gc: Any

def loads(*args) -> Any: ...

network: Any
re: Any
socket: Any

def stat(*args) -> Any: ...

time: Any
