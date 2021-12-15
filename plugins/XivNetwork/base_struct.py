from ctypes import *
from datetime import datetime
from functools import cached_property

from FFxivPythonTrigger.logger import error
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class BundleHeader(OffsetStruct({
    'magic0': c_uint,
    'magic1': c_uint,
    'magic2': c_uint,
    'magic3': c_uint,
    'epoch': c_ulonglong,
    'length': c_ushort,
    'unk1': c_ushort,
    'unk2': c_ushort,
    'msg_count': c_ushort,
    'encoding': c_ushort,
    'unk3': c_ushort,
    'unk4': c_ushort,
    'unk5': c_ushort,
}, 40)):
    magic0: int
    magic1: int
    magic2: int
    magic3: int
    epoch: int
    length: int
    unk1: int
    unk2: int
    msg_count: int
    encoding: int
    unk3: int
    unk4: int
    unk5: int

    @cached_property
    def message_time(self):
        try:
            return datetime.fromtimestamp(self.epoch / 1000)
        except Exception:
            error('XivNetworkBundleHeaderStruct', f"invalid epoch {self.epoch}")
            return datetime.now()


class MessageHeader(OffsetStruct({
    'msg_length': c_uint,
    'actor_id': c_uint,
    'login_user_id': c_uint,
    'unk1': c_uint,
    'unk2': c_ushort,
    'msg_type': c_ushort,
    'unk3': c_uint,
    'sec': c_uint,
    'unk4': c_uint,
}, 32)):
    msg_length: int
    actor_id: int
    login_user_id: int
    unk1: int
    unk2: int
    msg_type: int
    unk3: int
    sec: int
    unk4: int
