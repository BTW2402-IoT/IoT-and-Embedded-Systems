from typing import Any

class ADC:
    CORE_TEMP: int
    def read_u16(self, *args) -> Any: ...

class I2C:
    def readinto(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def readfrom(self, *args) -> Any: ...
    def readfrom_into(self, *args) -> Any: ...
    def readfrom_mem(self, *args) -> Any: ...
    def readfrom_mem_into(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def writeto(self, *args) -> Any: ...
    def writeto_mem(self, *args) -> Any: ...
    def writevto(self, *args) -> Any: ...

class PWM:
    def deinit(self, *args) -> Any: ...
    def duty_ns(self, *args) -> Any: ...
    def duty_u16(self, *args) -> Any: ...
    def freq(self, *args) -> Any: ...

PWRON_RESET: int

class Pin:
    def value(self, *args) -> Any: ...
    ALT: int
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    PULL_DOWN: int
    PULL_UP: int
    def high(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def low(self, *args) -> Any: ...
    def off(self, *args) -> Any: ...
    def on(self, *args) -> Any: ...
    def toggle(self, *args) -> Any: ...

class RTC:
    def datetime(self, *args) -> Any: ...

class SPI:
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    LSB: int
    MSB: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def write_readinto(self, *args) -> Any: ...

class Signal:
    def value(self, *args) -> Any: ...
    def off(self, *args) -> Any: ...
    def on(self, *args) -> Any: ...

class SoftI2C:
    def readinto(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def readfrom(self, *args) -> Any: ...
    def readfrom_into(self, *args) -> Any: ...
    def readfrom_mem(self, *args) -> Any: ...
    def readfrom_mem_into(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def writeto(self, *args) -> Any: ...
    def writeto_mem(self, *args) -> Any: ...
    def writevto(self, *args) -> Any: ...

class SoftSPI:
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    LSB: int
    MSB: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def write_readinto(self, *args) -> Any: ...

class Timer:
    ONE_SHOT: int
    PERIODIC: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...

class UART:
    def any(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    CTS: int
    INV_RX: int
    INV_TX: int
    RTS: int
    def sendbreak(self, *args) -> Any: ...

class WDT:
    def feed(self, *args) -> Any: ...

WDT_RESET: int

def bootloader(*args) -> Any: ...
def deepsleep(*args) -> Any: ...
def disable_irq(*args) -> Any: ...
def enable_irq(*args) -> Any: ...
def freq(*args) -> Any: ...
def idle(*args) -> Any: ...
def lightsleep(*args) -> Any: ...

mem16: Any
mem32: Any
mem8: Any

def reset(*args) -> Any: ...
def reset_cause(*args) -> Any: ...
def soft_reset(*args) -> Any: ...
def time_pulse_us(*args) -> Any: ...
def unique_id(*args) -> Any: ...