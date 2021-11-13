from functools import cached_property
from typing import Optional, Union, Tuple, TYPE_CHECKING

from ..define import HQ_FIRST
from .. import api

if TYPE_CHECKING:
    from ..logic_data import LogicData


class _Using(object):
    target_id: int

    @cached_property
    def actor(self):
        return api.get_actor_by_id(self.target_id)


class UseAbility(_Using):
    def __init__(self, ability_id: int, target_id: int = None):
        self.ability_id = ability_id
        self.target_id = target_id


class UseItem(_Using):
    def __init__(self, item_id: int, priority: int = HQ_FIRST, target_id: int = None):
        self.item_id = item_id
        self.priority = priority
        self.target_id = target_id


class UseCommon(_Using):
    def __init__(self, ability_id: int, target_id: int = None):
        self.ability_id = ability_id
        self.target_id = target_id


class Strategy(object):
    name = ""
    job = ""
    fight_only: bool = True
    default_data = {}

    def global_cool_down_ability(self, data: 'LogicData') -> Optional[Union[UseAbility, UseItem, UseCommon]]:
        pass

    def non_global_cool_down_ability(self, data: 'LogicData') -> Optional[Union[UseAbility, UseItem, UseCommon]]:
        pass

    def common_ability(self, data: 'LogicData') -> Optional[Union[UseAbility, UseItem, UseCommon]]:
        pass

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> Optional[Tuple[int, int]]:
        pass
