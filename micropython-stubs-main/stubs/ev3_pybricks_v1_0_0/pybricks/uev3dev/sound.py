"""
Module: 'pybricks.uev3dev.sound' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any

INT32 = 671088640


class Mixer:
    """"""

    _attach = None
    _close = None
    _find_selem = None
    _load = None
    _open = None
    _selem_get_playback_volume_range = None
    _selem_id_set_index = None
    _selem_id_set_name = None
    _selem_id_sizeof = None
    _selem_register = None
    _selem_set_playback_volume_all = None

    def close(self, *argv) -> Any:
        pass

    def set_beep_volume(self, *argv) -> Any:
        pass

    def set_pcm_volume(self, *argv) -> Any:
        pass


class PCM:
    """"""

    _ACCESS_RW_INTERLEAVED = 3
    _FORMAT_S16_LE = 2
    _STREAM_PLAYBACK = 0
    _close = None
    _drain = None
    _drop = None
    _hw_params = None
    _hw_params_any = None
    _hw_params_get_period_size = None
    _hw_params_set_access = None
    _hw_params_set_channels = None
    _hw_params_set_format = None
    _hw_params_set_rate = None
    _hw_params_sizeof = None
    _open = None
    _prepare = None
    _writei = None

    def close(self, *argv) -> Any:
        pass

    def play(self, *argv) -> Any:
        pass


class PlayType:
    """"""

    ONCE = 1
    REPEAT = 2
    WAIT = 0


class Sound:
    """"""

    def _beep(self, *argv) -> Any:
        pass

    def _play_tone(self, *argv) -> Any:
        pass

    def _stop(self, *argv) -> Any:
        pass

    def play_file(self, *argv) -> Any:
        pass

    def play_note(self, *argv) -> Any:
        pass

    def play_tone(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass


class SoundFile:
    """"""

    def _cancel_token(self, *argv) -> Any:
        pass

    _read = None

    def close(self, *argv) -> Any:
        pass


class SoundFileError(Exception):
    """"""


class Timeout:
    """"""

    _ONE = None

    def _run(self, *argv) -> Any:
        pass

    def cancel(self, *argv) -> Any:
        pass

    def close(self, *argv) -> Any:
        pass

    def start(self, *argv) -> Any:
        pass

    def wait(self, *argv) -> Any:
        pass


UINT16 = 268435456
UINT32 = 536870912
UINT64 = 805306368
_BEEP_DEV = "/dev/input/by-path/platform-sound-event"


class _CancelToken:
    """"""

    def cancel(self, *argv) -> Any:
        pass


_EV_SND = 18
_NOTES = None
_SEEK_SET = 0
_SF_INFO = None
_SMF_READ = 16
_SND_TONE = 2
_input_event = None
_libsndfile = None
_sf_close = None
_sf_count_t = 805306368
_sf_open = None
_sf_readf_short = None
_sf_seek = None
_sf_strerror = None
_thread = None


def addressof():
    pass


def calcsize():
    pass


def debug_print():
    pass


ffilib = None
os = None


def pack():
    pass


def sizeof():
    pass


def sleep():
    pass


def sleep_ms():
    pass


class struct:
    """"""


def unpack():
    pass
