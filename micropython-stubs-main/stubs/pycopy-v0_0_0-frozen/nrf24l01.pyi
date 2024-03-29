from typing import Any

CONFIG: Any
EN_RXADDR: Any
SETUP_AW: Any
SETUP_RETR: Any
RF_CH: Any
RF_SETUP: Any
STATUS: Any
RX_ADDR_P0: Any
TX_ADDR: Any
RX_PW_P0: Any
FIFO_STATUS: Any
DYNPD: Any
EN_CRC: Any
CRCO: Any
PWR_UP: Any
PRIM_RX: Any
POWER_0: Any
POWER_1: Any
POWER_2: Any
POWER_3: Any
SPEED_1M: Any
SPEED_2M: Any
SPEED_250K: Any
RX_DR: Any
TX_DS: Any
MAX_RT: Any
RX_EMPTY: Any
R_RX_PL_WID: Any
R_RX_PAYLOAD: Any
W_TX_PAYLOAD: Any
FLUSH_TX: Any
FLUSH_RX: Any
NOP: Any

class NRF24L01:
    buf: Any
    spi: Any
    cs: Any
    ce: Any
    payload_size: Any
    pipe0_read_addr: Any
    def __init__(self, spi, cs, ce, channel: int = ..., payload_size: int = ...) -> None: ...
    def init_spi(self, baudrate) -> None: ...
    def reg_read(self, reg): ...
    def reg_write_bytes(self, reg, buf): ...
    def reg_write(self, reg, value): ...
    def flush_rx(self) -> None: ...
    def flush_tx(self) -> None: ...
    def set_power_speed(self, power, speed) -> None: ...
    def set_crc(self, length) -> None: ...
    def set_channel(self, channel) -> None: ...
    def open_tx_pipe(self, address) -> None: ...
    def open_rx_pipe(self, pipe_id, address) -> None: ...
    def start_listening(self) -> None: ...
    def stop_listening(self) -> None: ...
    def any(self): ...
    def recv(self): ...
    def send(self, buf, timeout: int = ...) -> None: ...
    def send_start(self, buf) -> None: ...
    def send_done(self): ...
