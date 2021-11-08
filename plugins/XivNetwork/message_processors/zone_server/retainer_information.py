from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerRetainerInformation(OffsetStruct({
    'unk0': c_ulonglong,
    'retainer_id': c_uint,
    'server_id': c_uint,
    'type': c_ubyte,
    'inventory_count': c_ubyte,
    'unk2': c_ushort,
    'gold': c_uint,
    'selling_count': c_ubyte,
    'market': c_ubyte,
    'class_job': c_ubyte,
    'level': c_ubyte,
    'sell_end_time': c_uint,
    'mission_id': c_uint,
    'adv_end_time': c_uint,
    'reserved': c_ubyte,
    '_name': c_char * 39,
}, 80)):
    unk0: int
    retainer_id: int
    server_id: int
    type: int
    inventory_count: int
    unk2: int
    gold: int
    selling_count: int
    market: int
    class_job: int
    level: int
    sell_end_time: int
    mission_id: int
    adv_end_time: int
    reserved: int

    @property
    def name(self):
        return self._name.decode('utf-8', errors='ignore')


class ServerRetainerInformationEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'retainer_information'
    struct_message: ServerRetainerInformation

    def __str__(self):
        msg = self.struct_message
        return 'retainer: ' + (f"{msg.name} ({msg.retainer_id:x}/{msg.server_id:x})" if msg.reserved else 'n/a')


class RetainerInformation(BaseProcessors):
    opcode = "RetainerInformation"
    struct = ServerRetainerInformation
    event = ServerRetainerInformationEvent
