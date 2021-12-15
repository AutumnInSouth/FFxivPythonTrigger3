from ctypes import *
from typing import Iterable, TYPE_CHECKING

from FFxivPythonTrigger import game_ext
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
    'hp_percent': (c_int, 0),
    'enmity_percent': (c_int, 4),
    'id': (c_uint, 0xc),
    'can_select': (c_uint, 0x10),
}, 0x18 if game_ext == 4 else 0x14)):
    id: int
    can_select: int
    hp_percent: int
    enmity_percent: int


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
        return bool(self.ability_id)

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


class MissionAction(OffsetStruct({
    'action_1_id': (c_uint, 0x1c),
    'action_2_id': (c_uint, 0x20),
    'action_2_cool_down_duration': (c_float, 0x34),
    'action_2_cool_down_total': (c_float, 0x38),
    'action_1_cool_down_duration': (c_float, 0x48),
    'action_1_cool_down_total': (c_float, 0x4c),
    'action_2_remain': (c_ubyte, 0x54),
    'action_1_remain': (c_ubyte, 0x55),
})):
    action_1_id: int
    action_2_id: int
    action_1_cool_down_duration: float
    action_1_cool_down_total: float
    action_2_cool_down_duration: float
    action_2_cool_down_total: float
    action_1_remain: int
    action_2_remain: int


class MissionInfo(OffsetStruct({
    '_mission_name': (c_char * 18, 0x372),
    'mission_action': (MissionAction, 0x568),
    'remain_time': (c_float, 0x6f8),
})):
    mission_action: MissionAction
    remain_time: float
    _mission_name: bytes

    @property
    def mission_name(self):
        return self._mission_name.decode('utf-8', errors='ignore')


class PvpAction(OffsetStruct({
    'action_1_id': (c_uint, 32),
    'action_2_id': (c_uint, 36)
})):
    action_1_id: int
    action_2_id: int


class BlueMage(OffsetStruct({
    'select_skills': (c_uint * 18, 0x13c)
})):
    select_skills: list[int]
