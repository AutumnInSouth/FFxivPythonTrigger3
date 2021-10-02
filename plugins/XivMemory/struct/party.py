from ctypes import *
from typing import Tuple, Optional, Dict, Iterator, TYPE_CHECKING

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.popular_struct import Vector3
from .enum import Jobs


class Effect(OffsetStruct({
    'buff_id': (c_ushort, 0),
    'param': (c_ushort, 2),
    'actor_id': (c_uint, 8),
})):
    buff_id: int
    param: int
    actor_id: int


class Effects(Effect * 30):
    if TYPE_CHECKING:
        def __iter__(self) -> Iterator[Effect]: pass

        def __getitem__(self, item: int) -> Effect: pass

    def get_dict(self, source_id: Optional[int] = None) -> Dict[int, Effect]:
        return {e_id: effect for e_id, effect in self.get_items(source_id)}

    def get_items(self, source_id: Optional[int] = None) -> Iterator[Tuple[int, Effect]]:
        for effect in self:
            if effect.buffId and (source_id is None or effect.actorId == source_id):
                yield effect.buffId, effect


class PartyMember(OffsetStruct({
    "effects": (Effects, 0x8),
    "current_hp": (c_uint, 0x1b4),
    "max_hp": (c_uint, 0x1b8),
    "current_mp": (c_ushort, 0x1bc),
    "max_mp": (c_ushort, 0x1be),
    "pos": (Vector3, 0x190),
    "id": (c_uint, 0x1a8),
    "_name": (c_char * 64, 0x1c4),
    "job": (Jobs, 0x205),
    "flag": (c_ubyte, 544),
}, full_size=0x230)):
    effects: Effects
    current_hp: int
    max_hp: int
    current_mp: int
    max_mp: int
    pos: Vector3
    id: int
    _name: bytes
    job: Jobs
    flag: int

    @property
    def name(self):
        return self._name.decode('utf-8')


class PartyList(OffsetStruct({
    'members': (PartyMember * 28, 0),
    'flag': (c_ubyte, 15700),
    'main_size': (c_ubyte, 15708),
})):
    members: list[PartyMember]
    flag: int
    main_size: int

    def main_party(self) -> Iterator[PartyMember]:
        for i in range(self.main_size):
            if self.members[i].id != 0xe0000000:
                yield self.members[i]

    def party_2(self) -> Iterator[PartyMember]:
        for i in range(8, 16):
            if self.members[i].id != 0xe0000000:
                yield self.members[i]

    def party_3(self) -> Iterator[PartyMember]:
        for i in range(16, 24):
            if self.members[i].id != 0xe0000000:
                yield self.members[i]

    def alliance(self) -> Iterator[PartyMember]:
        for i in self.main_party(): yield i
        for i in self.party_2(): yield i
        for i in self.party_3(): yield i
