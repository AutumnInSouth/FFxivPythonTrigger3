from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, EnumStruct, _EnumStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerHousingInfo(OffsetStruct({
    'house_id': c_ushort,
    'ward_id': c_ushort,
    'territory_id': c_ushort,
    'unk1': c_ushort,
    'FC_info_1': c_uint,
    'FC_info_2': c_uint,
    'unk2': c_uint,
    'is_open': c_bool,
    'size': EnumStruct(c_ubyte, {0: "S", 1: "M", 2: "L"}),
    'is_FC': EnumStruct(c_ubyte, {0: True, 2: False}),
    '_house_name': c_char * 23,
    '_house_description': c_char * 193,
    '_owner_name': c_char * 31,
    '_owner_nick': c_char * 7,
    'housing_appeal_1': c_ubyte,
    'housing_appeal_2': c_ubyte,
    'housing_appeal_3': c_ubyte,
}, full_size=0x118)):
    house_id: int
    ward_id: int
    territory_id: int
    unk1: int
    FC_info_1: int
    FC_info_2: int
    unk2: int
    is_open: bool
    size: _EnumStruct
    is_FC: _EnumStruct
    housing_appeal_1: int
    housing_appeal_2: int
    housing_appeal_3: int

    @property
    def house_name(self):
        return self._house_name.decode('utf-8', errors='ignore')

    @property
    def house_description(self):
        return self._house_description.decode('utf-8', errors='ignore')

    @property
    def owner_name(self):
        return self._owner_name.decode('utf-8', errors='ignore')

    @property
    def owner_nick(self):
        return self._owner_nick.decode('utf-8', errors='ignore')


class ServerHousingInfoEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'housing_info'
    struct_message: ServerHousingInfo

    def __str__(self):
        return f"housing info of {self.struct_message.territory_id} - {self.struct_message.ward_id} - {self.struct_message.house_id}"


class HousingInfo(BaseProcessors):
    opcode = "HousingInfo"
    struct = ServerHousingInfo
    event = ServerHousingInfoEvent
