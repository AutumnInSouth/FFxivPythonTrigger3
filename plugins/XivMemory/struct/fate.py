from ctypes import *
from typing import Iterable, TYPE_CHECKING

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, EnumStruct
from FFxivPythonTrigger.popular_struct import Vector3, StdVector


class FateState(EnumStruct(c_ubyte, {
    2: 'Active',
    4: 'NotActive',
    7: 'Preparing',
    8: 'Complete'
})):
    pass


class FateContext(OffsetStruct({
    'fate_id': (c_ushort, 0x18),
    'start_time_epoch': (c_int, 0x20),
    'duration': (c_short, 0x28),

    '_name': (c_char * 0x68, 0xC0),
    '_description': (c_char * 0x68, 0x128),
    '_objective': (c_char * 0x68, 0x190),

    'state': (FateState, 0x3AC),
    'hand_in_count': (c_byte, 0x3AF),
    'progress': (c_byte, 0x3B8),
    'icon_id': (c_uint, 0x3D8),
    'level': (c_byte, 0x3F9),
    'max_level': (c_byte, 0x3FA),
    'location': (Vector3, 0x450),
    'radius': (c_float, 0x464),

    'map_icon_id': (c_uint, 0x720),
    'territory_id': (c_ushort, 0x74E),
}, 0x1000)):
    fate_id: int
    start_time_epoch: int
    duration: int
    state: FateState
    hand_in_count: int
    progress: int
    icon_id: int
    level: int
    max_level: int
    location: Vector3
    radius: float
    map_icon_id: int
    territory_id: int

    @property
    def name(self) -> str:
        return self._name.decode('utf-8', errors='ignore')

    @property
    def description(self) -> str:
        return self._description.decode('utf-8', errors='ignore')

    @property
    def objective(self) -> str:
        return self._objective.decode('utf-8', errors='ignore')


class FateDirector(OffsetStruct({
    '_lua_state': (c_void_p, 0x210),
    'fate_name': (c_char * 0x68, 0x350),
    'fate_description': (c_char * 0x68, 0x3B8),
    'fate_level': (c_byte, 0x4B8),
    'fate_npc_object_id': (c_uint, 0x4C0),
    'fate_id': (c_ushort, 0x4CC),
}, 0x4f8)):
    fate_name: str
    fate_description: str
    fate_level: int
    fate_npc_object_id: int
    fate_id: int


class FateManager(OffsetStruct({
    '_fate_director': (POINTER(FateDirector), 0x80),
    '_current_fate': (POINTER(FateContext), 0x88),
    '_fates': (StdVector(POINTER(FateContext)), 0x90),
    'synced_fate_id': (c_ushort, 0xA8),
    'fate_joined': (c_byte, 0xAC)
}, 0xB0)):
    synced_fate_id: int
    fate_joined: int

    @property
    def fate_director(self) -> FateDirector:
        return self._fate_director[0] if self._fate_director else None

    @property
    def current_fate(self) -> FateContext:
        return self._current_fate[0] if self._current_fate else None

    def iter_fates(self) -> Iterable[FateContext]:
        for i in range(len(self._fates)):
            yield self._fates[i][0]

    def get_fate(self, idx: int) -> FateContext:
        return self._fates[idx][0]
