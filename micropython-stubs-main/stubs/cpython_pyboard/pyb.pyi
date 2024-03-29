from typing import Any

def delay(ms) -> None: ...
def udelay(us) -> None: ...
def millis() -> None: ...
def micros() -> None: ...
def elapsed_millis(start) -> None: ...
def elapsed_micros(start) -> None: ...
def hard_reset() -> None: ...
def bootloader() -> None: ...
def disable_irq() -> None: ...
def enable_irq(state: bool = ...) -> None: ...
def freq(sysclk, hclk, pclk1, pclk2) -> None: ...
def wfi() -> None: ...
def stop() -> None: ...
def standby() -> None: ...
def info(dump_alloc_table) -> None: ...
def main(filename) -> None: ...
def mount(device, mountpoint, readonly: bool = ..., mkfs: bool = ...) -> None: ...
def repl_uart(uart) -> None: ...
def rng() -> None: ...
def sync() -> None: ...
def unique_id() -> None: ...
def usb_mode(modestr, vid: int = ..., pid: int = ..., hid: int = ...) -> None: ...

class Accel:
    def filtered_xyz(self) -> None: ...
    def tilt(self) -> None: ...
    def x(self) -> None: ...
    def y(self) -> None: ...
    def z(self) -> None: ...
    def write(self, register, value) -> None: ...
    def read(self, register) -> None: ...

class ADC:
    def __init__(self, pin) -> None: ...
    def read_timed_stop(self) -> None: ...
    def read(self) -> None: ...
    def read_timed(self, buf, timer) -> None: ...

class CAN:
    NORMAL: str
    LOOPBACK: str
    SILENT: str
    SILENT_LOOPBACK: str
    LIST16: str
    MASK16: str
    LIST32: str
    MASK32: str
    def __init__(
        self, bus, mode: Any | None = ..., extframe: bool = ..., prescaler: int = ..., sjw: int = ..., bs1: int = ..., bs2: int = ...
    ) -> None: ...
    @classmethod
    def initfilterbanks(cls, nr) -> None: ...
    def init(self, mode, extframe: bool = ..., prescaler: int = ..., sjw: int = ..., bs1: int = ..., bs2: int = ...) -> None: ...
    def deinit(self) -> None: ...
    def setfilter(self, bank, mode, fifo, params, rtr) -> None: ...
    def clearfilter(self, bank) -> None: ...
    def any(self, fifo) -> None: ...
    def recv(self, fifo, timeout: int = ...) -> None: ...
    def send(self, data, id, timeout: int = ..., rtr: bool = ...) -> None: ...
    def rxcallback(self, fifo, fun) -> None: ...

class DAC:
    NORMAL: str
    CIRCULAR: str
    def __init__(self, port, bits: int = ...) -> None: ...
    def init(self, bits: int = ...) -> None: ...
    def deinit(self) -> None: ...
    def noise(self, freq) -> None: ...
    def triangle(self, freq) -> None: ...
    def write(self, value) -> None: ...
    def write_timed(self, data, freq, mode=...) -> None: ...

class ExtInt:
    IRQ_FALLING: str
    IRQ_RISING: str
    IRQ_RISING_FALLING: str
    def __init__(self, pin, mode, pull, callback) -> None: ...
    @classmethod
    def regs(cls) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    def line(self) -> None: ...
    def swint(self) -> None: ...

class I2C:
    MASTER: str
    SLAVE: str
    def __init__(self, *args, **kwargs) -> None: ...
    def deinit(self) -> None: ...
    def init(self, mode, addr: int = ..., baudrate: int = ..., gencall: bool = ...) -> None: ...
    def is_ready(self, addr) -> None: ...
    def mem_read(self, data, addr, memaddr, timeout: int = ..., addr_size: int = ...) -> None: ...
    def mem_write(self, data, addr, memaddr, timeout: int = ..., addr_size: int = ...) -> None: ...
    def recv(self, recv, addr: int = ..., timeout: int = ...) -> None: ...
    def send(self, send, addr: int = ..., timeout: int = ...) -> None: ...
    def scan(self) -> None: ...

class LCD:
    def __init__(self, skin_position) -> None: ...
    def command(self, instr_data, buf) -> None: ...
    def contrast(self, value) -> None: ...
    def fill(self, colour) -> None: ...
    def get(self, x, y) -> None: ...
    def light(self, value) -> None: ...
    def pixel(self, x, y, colour) -> None: ...
    def show(self) -> None: ...
    def text(self, str, x, y, colour) -> None: ...
    def write(self, str) -> None: ...

class LED:
    def __init__(self, id) -> None: ...
    def intensity(self, value) -> None: ...
    def off(self) -> None: ...
    def on(self) -> None: ...
    def toggle(self) -> None: ...

class _board:
    def __getattr__(self, *args, **kwargs): ...

class Pin:
    AF_OD: str
    AF_PP: str
    ANALOG: str
    IN: str
    OUT: str
    OUT_OD: str
    OUT_PP: str
    PULL_DOWN: str
    PULL_NONE: str
    PULL_UP: str
    board: Any
    cpu: Any
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def debug(cls, state) -> None: ...
    @classmethod
    def dict(cls, dict) -> None: ...
    @classmethod
    def mapper(cls, fun) -> None: ...
    def init(self, mode, pull=..., af: int = ...) -> None: ...
    def value(self, value) -> None: ...
    def __str__(self) -> None: ...
    def af(self) -> None: ...
    @classmethod
    def af_list(cls) -> None: ...
    def gpio(self) -> None: ...
    def mode(self) -> None: ...
    def name(self) -> None: ...
    def names(self) -> None: ...
    def pin(self) -> None: ...
    def port(self) -> None: ...
    def pull(self) -> None: ...

class PinAF:
    def __str__(self) -> None: ...
    def index(self) -> None: ...
    def name(self) -> None: ...
    def reg(self) -> None: ...

class RTC:
    def __init__(self) -> None: ...
    def datetime(self, datetimetuple) -> None: ...
    def wakeup(self, timeout, callback: Any | None = ...) -> None: ...
    def info(self) -> None: ...
    def calibration(self, cal) -> None: ...

class Servo:
    def __init__(self, id) -> None: ...
    def angle(self, angle, time: int = ...) -> None: ...
    def speed(self, speed, time: int = ...) -> None: ...
    def pulse_width(self, value) -> None: ...
    def calibration(self, pulse_min, pulse_max, pulse_centre, pulse_angle_90, pulse_speed_100) -> None: ...

class SPI:
    MASTER: str
    SLAVE: str
    LSB: str
    MSB: str
    def __init__(self, bus) -> None: ...
    def deinit(self) -> None: ...
    def init(
        self,
        mode,
        prescaler,
        baudrate: int = ...,
        polarity: int = ...,
        phase: int = ...,
        bits: int = ...,
        firstbit=...,
        ti: bool = ...,
        crc: Any | None = ...,
    ) -> None: ...
    def recv(self, recv, timeout: int = ...) -> None: ...
    def send(self, send, timeout: int = ...) -> None: ...
    def send_recv(self, send, recv: Any | None = ..., timeout: int = ...) -> None: ...

class Switch:
    def __init__(self) -> None: ...
    def __call__(self) -> None: ...
    def callback(self, fun) -> None: ...

class Timer:
    def __init__(self, *args, **kwargs) -> None: ...
    def init(self, freq, prescaler, period) -> None: ...
    def deinit(self) -> None: ...
    def callback(self, fun) -> None: ...
    def channel(self, channel, mode) -> None: ...
    def counter(self, value) -> None: ...
    def freq(self, value) -> None: ...
    def period(self, value) -> None: ...
    def prescaler(self, value) -> None: ...
    def source_freq(self) -> None: ...

class TimerChannel:
    def callback(self, fun) -> None: ...
    def capture(self, value) -> None: ...
    def compare(self, value) -> None: ...
    def pulse_width(self, value) -> None: ...
    def pulse_width_percent(self, value) -> None: ...

class UART:
    RTS: str
    CTS: str
    def __init__(self, bus) -> None: ...
    def init(
        self,
        baudrate,
        bits: int = ...,
        parity: Any | None = ...,
        stop: int = ...,
        timeout: int = ...,
        flow: Any | None = ...,
        timeout_char: int = ...,
        read_buf_len: int = ...,
    ) -> None: ...
    def deinit(self) -> None: ...
    def any(self) -> None: ...
    def writechar(self, char) -> None: ...
    def read(self, nbytes) -> None: ...
    def readchar(self) -> None: ...
    def readinto(self, buf, nbytes) -> None: ...
    def readline(self) -> None: ...
    def write(self, buf) -> None: ...
    def sendbreak(self) -> None: ...

class USB_HID:
    def recv(self, data, timeout: int = ...) -> None: ...
    def send(self, data) -> None: ...

class USB_VCP:
    def __init__(self) -> None: ...
    def setinterrupt(self, chr) -> None: ...
    def isconnected(self) -> None: ...
    def any(self) -> None: ...
    def close(self) -> None: ...
    def read(self, nbytes) -> None: ...
    def readinto(self, buf, maxlen) -> None: ...
    def readline(self) -> None: ...
    def readlines(self) -> None: ...
    def write(self, buf) -> None: ...
    def recv(self, data, timeout: int = ...) -> None: ...
    def send(self, data, timeout: int = ...) -> None: ...
