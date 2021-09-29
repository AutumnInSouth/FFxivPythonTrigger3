from ctypes import *
from typing import Iterable, TYPE_CHECKING

from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

action_sheet = realm.game_data.get_sheet('Action')


class ComboState(OffsetStruct({
    'remain': (c_float, 0),
    'action_id': (c_uint, 4),
})):
    remain: float
    action_id: int


class CoolDownGroup(OffsetStruct({
    'duration': (c_float, 8),
    'total': (c_float, 12),
}, 0x14)):
    duration: float
    total: float

    @property
    def remain(self):
        return self.total - self.duration


class CoolDownGroups(CoolDownGroup * 100):
    if TYPE_CHECKING:
        def __iter__(self) -> Iterable[CoolDownGroup]: pass

        def __getitem__(self, item: int) -> CoolDownGroup: pass

    def by_skill(self, skill_id: int):
        return self[action_sheet[skill_id]['CooldownGroup']]

    @property
    def gcd_group(self):
        return self[58]

    @property
    def item_group(self):
        return self[59]


class Enemy(OffsetStruct({
    'id': (c_uint, 0),
    'can_select': (c_uint, 4),
    'hp_percent': (c_int, 8),
    'cast_percent': (c_int, 16),
})):
    id: int
    can_select: int
    hp_percent: int
    cast_percent: int


class SkillQueue(OffsetStruct({
    'mark1': (c_ulong, 0),
    'mark2': (c_ulong, 4),
    'ability_id': (c_ulong, 8),
    'target_id': (c_ulong, 16),
})):
    mark1: int
    mark2: int
    ability_id: int
    target_id: int

    @property
    def has_skill(self):
        return bool(self.mark1)

    def use_skill(self, skill_id, target_id=0xe0000000):
        self.target_id = target_id
        self.ability_id = skill_id
        self.mark1 = 1
        self.mark2 = 1


class Enemies(Enemy * 8):
    if TYPE_CHECKING:
        def __iter__(self) -> Iterable[Enemy]: pass

        def __getitem__(self, item: int) -> Enemy: pass

    def get_item(self):
        for enemy in self:
            if enemy.id != 0xe0000000:
                yield enemy

    def get_ids(self):
        for enemy in self:
            if enemy.id != 0xe0000000:
                yield enemy.id
