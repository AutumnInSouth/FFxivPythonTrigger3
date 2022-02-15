from functools import cached_property
from typing import Tuple, Callable, TYPE_CHECKING

from XivCombat import api
from XivCombat.define import HQ_FIRST
from ..define import AbilityType

if TYPE_CHECKING:
    from ..logic_data import LogicData


class _Using(object):
    target_id: int

    @cached_property
    def actor(self):
        return api.get_actor_by_id(self.target_id)


class UseAbility(_Using):
    def __init__(self, ability_id: int,
                 target_id: int = None,
                 ability_type: AbilityType = None,
                 target_position: Tuple[float, float, float] = None,
                 wait_until: Callable = None,
                 wait_period: float = .1,
                 max_wait_time: float = 2.,
                 rtn_period: float = .2,
                 ):
        self.ability_id = ability_id
        self.target_id = target_id
        self.ability_type = ability_type
        self.target_position = target_position
        self.wait_until = wait_until
        self.wait_period = wait_period
        self.max_wait_time = max_wait_time
        self.rtn_period = rtn_period


class UseItem(_Using):
    def __init__(self, item_id: int, priority: int = HQ_FIRST, target_id: int = None):
        self.item_id = item_id
        self.priority = priority
        self.target_id = target_id


class UseCommon(_Using):
    def __init__(self, ability_id: int, target_id: int = None):
        self.ability_id = ability_id
        self.target_id = target_id


AnyUse = UseAbility | UseItem | UseCommon | None


class Strategy(object):
    name = ""
    job = ""
    fight_only: bool = True
    default_data = {}

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        pass

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        pass

    def common_ability(self, data: 'LogicData') -> AnyUse:
        pass

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        pass

    def global_cool_down_ability_on_count_down(self, data: 'LogicData') -> AnyUse:
        pass

    def non_global_cool_down_ability_on_count_down(self, data: 'LogicData') -> AnyUse:
        pass
