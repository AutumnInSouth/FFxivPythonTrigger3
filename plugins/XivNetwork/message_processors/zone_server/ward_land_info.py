from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class LandHouseEntry(OffsetStruct({
    'price': c_uint,
    '_flag': c_ubyte,
    'appeals': c_ubyte * 3,
    '_owner': c_char * 32
})):
    price: int
    appeals: list[int]

    @property
    def owner(self):
        return self._owner.decode('utf-8', errors='ignore')

    @property
    def is_fc(self):
        return bool(self._flag & 0b10000)

    @property
    def allow_visit(self):
        return bool(self._flag & 0b10)


class ServerWardLandInfo(OffsetStruct({
    'land_id': c_ushort,
    'ward_id': c_ushort,
    'territory_id': c_ushort,
    'world_id': c_ushort,
    'houses': LandHouseEntry * 60
})):
    land_id: int
    ward_id: int
    territory_id: int
    world_id: int
    houses: list[LandHouseEntry]

    def houses_without_owner(self):
        for house in self.houses:
            if not house.owner:
                yield house


class ServerWardLandInfoEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'ward_land_info'
    struct_message: ServerWardLandInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.houses_without_owner = []

    def init(self):
        self.houses_without_owner = list(self.struct_message.houses_without_owner())

    def _text(self):
        msg = self.struct_message
        return (f'land_id={msg.land_id} ward_id={msg.ward_id} territory_id={msg.territory_id} '
                f'world_id={msg.world_id} empty={len(self.houses_without_owner)}')


class WardLandInfo(BaseProcessors):
    opcode = 'WardLandInfo'
    event = ServerWardLandInfoEvent
    struct = ServerWardLandInfo
