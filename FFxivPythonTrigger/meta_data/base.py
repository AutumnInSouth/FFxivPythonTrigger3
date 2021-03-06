from functools import cache
from typing import TYPE_CHECKING, Type
from FFxivPythonTrigger.saint_coinach import action_sheet, status_sheet

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor

physic = 1
magic = 2


class ActionBase:
    id = 0
    name: set[str] = set()  # 名字
    cure_potency: int = 0  # 治疗威力
    damage_potency: int = 0  # 伤害威力
    aoe_scale: float = 1.  # 复数目标时副目标的伤害比利
    combo_action: 'int | Type[ActionBase] | str' = None  # 连击技能
    direction_require: int = 0  # 身位需求 1为前 2为后 3为侧
    combo_damage_potency: int = 0  # 连击正确伤害威力
    direction_damage_potency: int = 0  # 身位正确伤害威力
    combo_direction_damage_potency: int = 0  # 连击身位正确伤害威力
    attack_type: int = None  # 攻击类型 physic / magic
    status_to_target: 'StatusBase|int|tuple[StatusBase|int]' = None  # 对目标造成的状态
    status_to_source: 'StatusBase|int|tuple[StatusBase|int]' = None  # 对来源造成的状态

    @classmethod
    @cache
    def row(cls):
        return action_sheet[cls.id]

    @cache
    def __getitem__(self, item):
        return self.row()[item]

    def __hash__(self):
        return self.id

    def __init__(self, source: 'Actor|None', target: 'Actor|None'):
        self.source = source
        self.target = target


class StatusBase:
    id = 0
    name: set[str] = set()  # 名字
    over_time_status: bool = True  # 是否是区域状态
    direct_rate: float = 0  # 额外直击
    critical_rate: float = 0  # 额外暴击
    damage_potency: int = 0  # dot 威力
    cure_potency: int = 0  # hot 威力
    damage_modify: float = 1.  # 威力修正
    taken_damage_modify: float = 1.  # 受到伤害修正
    cure_modify: float = 1.  # 治疗修正
    taken_cure_modify: float = 1.  # 受到治疗修正
    modify_type: int = None  # 修正类型

    @classmethod
    @cache
    def row(cls):
        return status_sheet[cls.id]

    @cache
    def __getitem__(self, item):
        return self.row()[item]

    def __hash__(self):
        return self.id

    def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool, stack: int):
        self.source = source
        self.target = target
        self.source_action = source_action
        self.is_main_target = is_main_target
        self.stack = stack
