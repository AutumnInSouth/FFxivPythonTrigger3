from math import radians
from time import perf_counter

from XivCombat.utils import a, s
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Rectangle, Sector, select, FarCircle

pet_name = {
    0: 'NoPet',
    23: 'Carbuncle',
    1: 'Ruby',
    2: 'Topaz',
    3: 'Emerald',
    27: 'IfritEgi',
    28: 'TitanEgi',
    29: 'GarudaEgi',
    7: 'Ifrit',
    8: 'Titan',
    9: 'Garuda',
    10: 'Bahamut',
    14: 'Firebird'
}

summoner_auras = {
    'Further Ruin': 2701,
    'Titan\s Favor': -1,
    'Garuda\s Favor': -2,
    'Ifrit\s Favor': -3
}

area_shape = FarCircle(25, 5)


def cnt_enemy(data: 'LogicData', ability):
    target, cnt = select(data, data.valid_enemies, ability)
    if not cnt:
        return data.target, 0
    if data.config['single'] == define.FORCE_SINGLE:
        return data.target, 1
    if data.config['single'] == define.FORCE_MULTI:
        return data.target, 3
    return target, cnt


class SummonerLogic(Strategy):
    name = "summoner_logic"
    job = "Summoner"
    gcd = 0

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        target = data.target
        selected, enemy_count = cnt_enemy(data, area_shape)
        gauge = data.gauge
        effects = data.effects
        current_pet = pet_name[data.pet_id]
        combo_id = data.combo_id
        if current_pet == 'NoPet':
            return UseAbility(a('Summon Carbuncle'), target.id)

        if current_pet in ['Bahamut', 'Firebird']:
            return UseAbility(a('Tri-disaster'), selected.id) if enemy_count \
                else UseAbility(a('Ruin III'), target.id)

        if data[a('Summon Bahamut')] < self.gcd / 2:
            return UseAbility(a('Summon Bahamut'), target.id)

        if summoner_auras['Ifrit\s Favor'] in effects or combo_id == a('Crimson Strike'):
            return UseAbility(a('Astral Flow'), target.id)

        if gauge.attunement > 0:
            return UseAbility(a('Precious Brilliance'), selected.id) if enemy_count \
                else UseAbility(a('Gemshine'), target.id)

        if gauge.titan_ready:
            return UseAbility(a('Summon Titan'), target.id)

        if gauge.garuda_ready:
            return UseAbility(a('Summon Garuda'), target.id)

        if gauge.ifrit_ready:
            return UseAbility(a('Summon Ifrit'), target.id)

        if summoner_auras['Further Ruin'] in effects:
            return UseAbility(a('Ruin IV'), target.id)

        return UseAbility(a('Tri-disaster'), target.id) if enemy_count \
            else UseAbility(a('Ruin III'), selected.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        target = data.target
        selected, enemy_count = cnt_enemy(data, area_shape)
        gauge = data.gauge
        effects = data.effects
        current_pet = pet_name[data.pet_id]

        if summoner_auras['Titan\s Favor'] in effects:
            return UseAbility(a('Astral Flow'), target.id)

        if summoner_auras['Garuda\s Favor'] in effects:
            if not data[a('Swiftcast')]:
                return UseAbility(a('Swiftcast'))
            return UseAbility(a('Astral Flow'), target.id)

        # lucid dreaming
        if not data[7562] and data.me.current_mp < 5000: 
            return UseAbility(7562)

        # TODO: auto searing light
        # if data[a('Searing Light')] <= self.gcd / 2 and current_pet == 'Carbuncle':
        #     return UseAbility(a('Searing Light'), selected.id, wait_until=lambda: 2703 in data.refresh_cache('effects'))

        if current_pet in ['Bahamut', 'Firebird'] and data[a('Enkindle Bahamut')] <= self.gcd / 2:
            return UseAbility(a('Enkindle Bahamut'), target.id)

        if current_pet in ['Bahamut', 'Firebird'] and data[a('Astral Flow')] <= self.gcd / 2:
            return UseAbility(a('Astral Flow'), target.id)

        if gauge.aether_flow_stacks > 0:
            return UseAbility(a('Painflare'), selected.id) if enemy_count \
                else UseAbility(a('Fester'), selected.id)

        # Aetherflow related
        if data[16508] <= self.gcd / 2:
            return UseAbility(a('Energy Siphon'), selected.id) if enemy_count \
                else UseAbility(16508, selected.id)



