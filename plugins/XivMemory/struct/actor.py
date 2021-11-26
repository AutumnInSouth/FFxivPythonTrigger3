import math
from ctypes import *
from typing import Dict, Set, Iterator, Tuple, Optional, TYPE_CHECKING

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

from FFxivPythonTrigger.utils.shape import circle
from .enum import Jobs, ActorType

ACTOR_TABLE_SIZE = 424


class Effect(OffsetStruct({
    'buff_id': (c_ushort, 0),
    'param': (c_ushort, 2),
    'timer': (c_float, 4),
    'actor_id': (c_uint, 8),
})):
    buff_id: int
    param: int
    timer: float
    actor_id: int


class Effects(Effect * 30):
    if TYPE_CHECKING:
        def __iter__(self) -> Iterator[Effect]:
            pass

        def __getitem__(self, item: int) -> Effect:
            pass

    def get_dict(self, source: Optional[int] = None) -> Dict[int, Effect]:
        return {e_id: effect for e_id, effect in self.get_items(source)}

    def get_set(self, source: Optional[int] = None) -> Set[Effect]:
        return {e_id for e_id, effect in self.get_items(source)}

    def get_items(self, source: Optional[int] = None) -> Iterator[Tuple[int, Effect]]:
        for effect in self:
            if effect.buff_id and (source is None or effect.actor_id == source):
                yield effect.buff_id, effect

    def has(self, status_id: int, source: Optional[int] = None):
        for effect in self:
            if effect.buff_id == status_id and (source is None or effect.actor_id == source):
                return True
        return False


class ActorPosition(OffsetStruct({
    'x': c_float,
    'z': c_float,
    'y': c_float,
    'r': (c_float, 16)
})):
    x: float
    y: float
    z: float
    r: float


class Actor(OffsetStruct({
    '_name': (c_char * 68, 0x30),
    'id': (c_uint, 0x74),
    'b_npc_id': (c_uint, 0x78),
    'e_npc_id': (c_uint, 0x80),
    'owner_id': (c_uint, 0x84),
    'type': (ActorType, 0x8c),
    'sub_type': (ActorType, 0x8d),
    'is_friendly': (c_byte, 0x8e),
    'effective_distance_x': (c_byte, 0x90),
    'player_target_status': (c_byte, 0x91),
    'effective_distance_y': (c_byte, 0x92),
    '_unit_status_1': (c_ubyte, 0x94),
    'pos': (ActorPosition, 0xa0),
    'hitbox_radius': (c_float, 0xc0),
    '_unit_status_2': (c_uint, 0x104),
    'current_hp': (c_uint, 0x1c4),
    'max_hp': (c_uint, 0x1c8),
    'current_mp': (c_uint, 0x1cc),
    'max_mp': (c_uint, 0x1d0),
    'current_gp': (c_ushort, 0x1d4),
    'max_gp': (c_ushort, 0x1d6),
    'current_cp': (c_ushort, 0x1d8),
    'max_cp': (c_ushort, 0x1da),
    'job': (Jobs, 0x1e2),
    'level': (c_byte, 0x1e3),
    'pc_target_id': (c_uint, 0x1f0),
    'pc_target_id_2': (c_uint, 0x230),
    'npc_target_id': (c_uint, 0x1818),
    'b_npc_target_id': (c_uint, 0x18d8),
    'shield_percent': (c_ubyte, 0x1997),
    '_status_flags': (c_ubyte, 0x19a0),
    '_status_flags_2': (c_ubyte, 0x19a5),
    'effects': (Effects, 0x19f8),
    'is_casting_1': (c_bool, 0x1b80),
    'is_casting_2': (c_bool, 0x1b82),
    'casting_id': (c_uint, 0x1b84),
    'casting_target_id': (c_uint, 0x1b90),
    'casting_progress': (c_float, 0x1bb4),
    'casting_time': (c_float, 0x1bb8),
})):
    _name: bytes
    id: int
    b_npc_id: int
    e_npc_id: int
    owner_id: int
    type: ActorType
    sub_type: ActorType
    is_friendly: int
    effective_distance_x: int
    player_target_status: int
    effective_distance_y: int
    _unit_status_1: int
    pos: ActorPosition
    hitbox_radius: float
    _unit_status_2: int
    current_hp: int
    max_hp: int
    current_mp: int
    max_mp: int
    current_gp: int
    max_gp: int
    current_cp: int
    max_cp: int
    job: Jobs
    level: int
    pc_target_id: int
    pc_target_id_2: int
    npc_target_id: int
    b_npc_target_id: int
    shield_percent: int
    _status_flags: int
    _status_flags_2: int
    effects: Effects
    is_casting_1: bool
    is_casting_2: bool
    casting_id: int
    casting_target_id: int
    casting_progress: float
    casting_time: float

    def __hash__(self):
        return self.id | self.b_npc_id

    def __eq__(self, other):
        if type(other) == Actor:
            return self.id == other.id
        if type(other) == int:
            return self.id == other
        if type(other) == str:
            return self.name == other

    def hitbox(self):
        return circle(self.pos.x, self.pos.y, self.hitbox_radius)

    def absolute_distance_xy(self, target: 'Actor'):
        return math.sqrt((self.pos.x - target.pos.x) ** 2 + (self.pos.y - target.pos.y) ** 2)

    def target_radian(self, target: 'Actor'):
        return math.atan2(target.pos.x - self.pos.x, target.pos.y - self.pos.y)

    def target_position(self, target: 'Actor'):
        a = abs(abs(self.target_radian(target) - self.pos.r) - math.pi)
        if a < math.pi / 4:
            return "BACK"
        elif a < math.pi / 4 * 3:
            return "SIDE"
        else:
            return "FRONT"

    @property
    def name(self):
        return self._name.decode('utf-8', errors='ignore') or f"{self.type.value}_{self.id:x}"

    @property
    def can_select(self):
        a1 = self._unit_status_1
        a2 = self._unit_status_2
        return bool(a1 & 0b10 and a1 & 0b100 and ((a2 >> 11 & 1) <= 0 or a1 >= 128) and not a2 & 0xffffe7f7)

    @property
    def is_hostile(self):
        return bool(self._status_flags & 0b1)

    @property
    def is_in_combat(self):
        return bool(self._status_flags & 0b10)

    @property
    def is_weapon_out(self):
        return bool(self._status_flags & 0b100)

    @property
    def is_party_member(self):
        return bool(self._status_flags & 0b10000)

    @property
    def is_alliance_member(self):
        return bool(self._status_flags & 0b100000)

    @property
    def is_friend(self):
        return bool(self._status_flags & 0b1000000)

    @property
    def is_casting(self):
        return bool(self._status_flags & 0x10000000)

    @property
    def is_positional(self):
        return not bool(self._status_flags_2 & 0x1)


class ActorTable(POINTER(Actor) * ACTOR_TABLE_SIZE):
    _aid_to_idx_cache: dict

    @property
    def me(self):
        return self.get_actor(0)

    def get_actor(self, idx: int) -> Optional[Actor]:
        return self[idx][0] if self[idx] else None

    def __iter__(self) -> Iterator[Actor]:
        for i in range(ACTOR_TABLE_SIZE):
            actor = self.get_actor(i)
            if actor is not None:
                yield actor

    def items(self) -> Iterator[Tuple[int, Actor]]:
        for i in range(ACTOR_TABLE_SIZE):
            actor = self.get_actor(i)
            if actor is not None:
                yield i, actor

    def get_actor_by_id(self, actor_id: int) -> Optional[Actor]:
        if not actor_id or actor_id == 0xe0000000: return
        if actor_id in self._aid_to_idx_cache:
            actor = self.get_actor(self._aid_to_idx_cache[actor_id])
            if actor and actor.id == actor_id:
                return actor
        for i, actor in self.items():
            self._aid_to_idx_cache[actor.id] = i
            if actor.id == actor_id: return actor

    def get_actors_by_ids(self, _actor_ids: Set[int]) -> Iterator[Actor]:
        actor_ids = set(_actor_ids)
        for actor_id in actor_ids.copy():
            if actor_id in self._aid_to_idx_cache:
                actor = self.get_actor(self._aid_to_idx_cache[actor_id])
                if actor and actor.id == actor_id:
                    actor_ids.remove(actor_id)
                    yield actor
        for i, actor in self.items():
            self._aid_to_idx_cache[actor.id] = i
            if actor.id in actor_ids:
                actor_ids.remove(actor.id)
                yield actor
                if not actor_ids: return

    def get_actors_by_name(self, name: str) -> Iterator[Actor]:
        for actor in self:
            if actor.name == name:
                yield actor
