from typing import Any

class Calibrate:
    tft: Any
    rx: Any
    ry: Any
    def __init__(self, tft) -> None: ...
    def drawCrossHair(self, x, y, clr) -> None: ...
    def readCoordinates(self): ...
    def calibrate(self, x, y, i): ...
    def calibError(self) -> None: ...
    def tpcalib(self, save: bool = ...): ...
