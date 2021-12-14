from XivCombat.utils import a
from XivCombat.strategies import *

provoke_and_shirk = {a('挑衅'), a('退避')}


def mo_provoke_and_shirk(func):
    def process_ability_use(cls, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        if action_id in provoke_and_shirk:
            mo_entity = api.get_mo_target()
            if mo_entity and api.action_type_check(action_id, mo_entity):
                return UseAbility(action_id, mo_entity.id)
        return func(cls, data, action_id, target_id)

    return process_ability_use
