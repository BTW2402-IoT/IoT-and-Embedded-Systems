from typing import Any

class ADC:
    def read(self, *args) -> Any: ...
    def read_timed(self, *args) -> Any: ...
    def read_timed_multi(self, *args) -> Any: ...

class ADCAll:
    def read_channel(self, *args) -> Any: ...
    def read_core_temp(self, *args) -> Any: ...
    def read_core_vbat(self, *args) -> Any: ...
    def read_core_vref(self, *args) -> Any: ...
    def read_vref(self, *args) -> Any: ...

class Accel:
    def filtered_xyz(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def tilt(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def x(self, *args) -> Any: ...
    def y(self, *args) -> Any: ...
    def z(self, *args) -> Any: ...

class CAN:
    BUS_OFF: int
    ERROR_ACTIVE: int
    ERROR_PASSIVE: int
    ERROR_WARNING: int
    LIST16: int
    LIST32: int
    LOOPBACK: int
    MASK16: int
    MASK32: int
    NORMAL: int
    SILENT: int
    SILENT_LOOPBACK: int
    STOPPED: int
    def any(self, *args) -> Any: ...
    def clearfilter(self, *args) -> Any: ...
    def deinit(self, *args) -> Any: ...
    def info(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def initfilterbanks(self, *args) -> Any: ...
    def recv(self, *args) -> Any: ...
    def restart(self, *args) -> Any: ...
    def rxcallback(self, *args) -> Any: ...
    def send(self, *args) -> Any: ...
    def setfilter(self, *args) -> Any: ...
    def state(self, *args) -> Any: ...

class DAC:
    CIRCULAR: int
    NORMAL: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def noise(self, *args) -> Any: ...
    def triangle(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def write_timed(self, *args) -> Any: ...

class ExtInt:
    EVT_FALLING: int
    EVT_RISING: int
    EVT_RISING_FALLING: int
    IRQ_FALLING: int
    IRQ_RISING: int
    IRQ_RISING_FALLING: int
    def disable(self, *args) -> Any: ...
    def enable(self, *args) -> Any: ...
    def line(self, *args) -> Any: ...
    def regs(self, *args) -> Any: ...
    def swint(self, *args) -> Any: ...

class Flash:
    def ioctl(self, *args) -> Any: ...
    def readblocks(self, *args) -> Any: ...
    def writeblocks(self, *args) -> Any: ...

class I2C:
    MASTER: int
    SLAVE: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def is_ready(self, *args) -> Any: ...
    def mem_read(self, *args) -> Any: ...
    def mem_write(self, *args) -> Any: ...
    def recv(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def send(self, *args) -> Any: ...

class LCD:
    def command(self, *args) -> Any: ...
    def contrast(self, *args) -> Any: ...
    def fill(self, *args) -> Any: ...
    def get(self, *args) -> Any: ...
    def light(self, *args) -> Any: ...
    def pixel(self, *args) -> Any: ...
    def show(self, *args) -> Any: ...
    def text(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...

class LED:
    def intensity(self, *args) -> Any: ...
    def off(self, *args) -> Any: ...
    def on(self, *args) -> Any: ...
    def toggle(self, *args) -> Any: ...

class Pin:
    AF1_TIM1: int
    AF1_TIM2: int
    AF2_TIM3: int
    AF2_TIM4: int
    AF2_TIM5: int
    AF3_TIM10: int
    AF3_TIM11: int
    AF3_TIM8: int
    AF3_TIM9: int
    AF4_I2C1: int
    AF4_I2C2: int
    AF5_SPI1: int
    AF5_SPI2: int
    AF7_USART1: int
    AF7_USART2: int
    AF7_USART3: int
    AF8_UART4: int
    AF8_USART6: int
    AF9_CAN1: int
    AF9_CAN2: int
    AF9_TIM12: int
    AF9_TIM13: int
    AF9_TIM14: int
    AF_OD: int
    AF_PP: int
    ALT: int
    ALT_OPEN_DRAIN: int
    ANALOG: int
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    OUT_OD: int
    OUT_PP: int
    PULL_DOWN: int
    PULL_NONE: int
    PULL_UP: int
    def af(self, *args) -> Any: ...
    def af_list(self, *args) -> Any: ...
    board: Any
    cpu: Any
    def debug(self, *args) -> Any: ...
    def dict(self, *args) -> Any: ...
    def gpio(self, *args) -> Any: ...
    def high(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def low(self, *args) -> Any: ...
    def mapper(self, *args) -> Any: ...
    def mode(self, *args) -> Any: ...
    def name(self, *args) -> Any: ...
    def names(self, *args) -> Any: ...
    def off(self, *args) -> Any: ...
    def on(self, *args) -> Any: ...
    def pin(self, *args) -> Any: ...
    def port(self, *args) -> Any: ...
    def pull(self, *args) -> Any: ...
    def value(self, *args) -> Any: ...

class RTC:
    def calibration(self, *args) -> Any: ...
    def datetime(self, *args) -> Any: ...
    def info(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def wakeup(self, *args) -> Any: ...

SD: Any

class SDCard:
    def info(self, *args) -> Any: ...
    def ioctl(self, *args) -> Any: ...
    def power(self, *args) -> Any: ...
    def present(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readblocks(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def writeblocks(self, *args) -> Any: ...

class SPI:
    LSB: int
    MASTER: int
    MSB: int
    SLAVE: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def recv(self, *args) -> Any: ...
    def send(self, *args) -> Any: ...
    def send_recv(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def write_readinto(self, *args) -> Any: ...

class Servo:
    def angle(self, *args) -> Any: ...
    def calibration(self, *args) -> Any: ...
    def pulse_width(self, *args) -> Any: ...
    def speed(self, *args) -> Any: ...

class Switch:
    def callback(self, *args) -> Any: ...
    def value(self, *args) -> Any: ...

class Timer:
    BOTH: int
    BRK_HIGH: int
    BRK_LOW: int
    BRK_OFF: int
    CENTER: int
    DOWN: int
    ENC_A: int
    ENC_AB: int
    ENC_B: int
    FALLING: int
    HIGH: int
    IC: int
    LOW: int
    OC_ACTIVE: int
    OC_FORCED_ACTIVE: int
    OC_FORCED_INACTIVE: int
    OC_INACTIVE: int
    OC_TIMING: int
    OC_TOGGLE: int
    PWM: int
    PWM_INVERTED: int
    RISING: int
    UP: int
    def callback(self, *args) -> Any: ...
    def channel(self, *args) -> Any: ...
    def counter(self, *args) -> Any: ...
    def deinit(self, *args) -> Any: ...
    def freq(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def period(self, *args) -> Any: ...
    def prescaler(self, *args) -> Any: ...
    def source_freq(self, *args) -> Any: ...

class UART:
    CTS: int
    IRQ_RXIDLE: int
    RTS: int
    def any(self, *args) -> Any: ...
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readchar(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def sendbreak(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def writechar(self, *args) -> Any: ...

class USB_HID:
    def recv(self, *args) -> Any: ...
    def send(self, *args) -> Any: ...

class USB_VCP:
    CTS: int
    RTS: int
    def any(self, *args) -> Any: ...
    def close(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def isconnected(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def readlines(self, *args) -> Any: ...
    def recv(self, *args) -> Any: ...
    def send(self, *args) -> Any: ...
    def setinterrupt(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...

def bootloader(*args) -> Any: ...
def country(*args) -> Any: ...
def delay(*args) -> Any: ...
def dht_readinto(*args) -> Any: ...
def disable_irq(*args) -> Any: ...
def elapsed_micros(*args) -> Any: ...
def elapsed_millis(*args) -> Any: ...
def enable_irq(*args) -> Any: ...
def fault_debug(*args) -> Any: ...
def freq(*args) -> Any: ...
def hard_reset(*args) -> Any: ...
def have_cdc(*args) -> Any: ...
def hid(*args) -> Any: ...

hid_keyboard: Any
hid_mouse: Any

def info(*args) -> Any: ...
def main(*args) -> Any: ...
def micros(*args) -> Any: ...
def millis(*args) -> Any: ...
def mount(*args) -> Any: ...
def pwm(*args) -> Any: ...
def repl_info(*args) -> Any: ...
def repl_uart(*args) -> Any: ...
def rng(*args) -> Any: ...
def servo(*args) -> Any: ...
def standby(*args) -> Any: ...
def stop(*args) -> Any: ...
def sync(*args) -> Any: ...
def udelay(*args) -> Any: ...
def unique_id(*args) -> Any: ...
def usb_mode(*args) -> Any: ...
def wfi(*args) -> Any: ...