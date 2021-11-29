from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import circle

card_map_arc = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 2,
    6: 3,
}
card_map_range = {
    1: False,
    2: True,
    3: False,
    4: True,
    5: True,
    6: False,
}


def priority(data: 'LogicData', target, card_range):
    dps = data.dps(target) * (2 if card_range == target.job.is_range else 1)
    if target.job.is_dps:
        return 3, dps
    if target.job.is_tank:
        return 2, dps
    if target.job.is_healer:
        return 1, dps
    return 0, dps


def card_target(data: 'LogicData', card_id: int):
    if card_id not in card_map_range: return None
    card_range = card_map_range[card_id]
    party = [member for member in data.valid_party if data.actor_distance_effective(member) <= 30]
    if not len(party): return data.me
    return max(party, key=lambda member: priority(data, member, card_range))


class AstrologianLogic(Strategy):
    name = "astrologian_logic"
    job = "Astrologian"

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int):
        match action_id:
            case 17055 | 7443:
                return action_id, card_target(data, data.gauge.held_card.raw_value).id
            case 7439:
                if 1224 not in data.effects and 1248 not in data.effects:
                    return UseAbility(7439, target_position=api.get_mo_location())
                else:
                    return UseAbility(8324)

