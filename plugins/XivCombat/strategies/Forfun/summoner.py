from .. import *
from .summoner_meta import summoner_spells
from ...define import AbilityType

summoner_auras = {
    'Bio': 179,
    'Miasma': 180,
    'BioII': 189,
    'BioIII': 1214,
    'MiasmaIII': 1215,
    'FurtherRuin': 1212,
    'HellishConduit': 1867
}


# Note that there is a discipline when calling this one: if wanna use this to determine an oGCD spell,
# it's necessary to consider current GCD spent
def time_period_between_A_and_B_times_of_gcd(time_period, A, B, gcd):
    return A * gcd <= time_period < B * gcd


def get_bio_and_miasma_aura_ids(data: 'LogicData'):
    return summoner_auras['BioIII'], summoner_auras['MiasmaIII']


class SummonerLogic(Strategy):
    name = "summoner_logic"
    job = 'Summoner'
    default_data = {}
    gcd = 0

    def global_cool_down_ability(self, data: 'LogicData'):

        lv = data.me.level
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        gauge = data.gauge
        effects = data.effects
        target_effects = data.target.effects.get_dict(source=data.me.id)
        combo_id = data.combo_id
        pet = data.pet_id
        bio_aura_id, miasma_aura_id = get_bio_and_miasma_aura_ids(data)
        bio_remain = target_effects[bio_aura_id].timer if bio_aura_id in target_effects else 0
        miasma_remain = target_effects[miasma_aura_id].timer if miasma_aura_id in target_effects else 0

        def use_ability_to_target(spell_name: str, ability_type: AbilityType = None,
                                  wait_until: Callable = None):
            return data.use_ability_to_target(summoner_spells[spell_name]['id'], ability_type, wait_until)

        def skill_cd(skill_name: str):
            return data.skill_cd(summoner_spells[skill_name]['id'])

        # TODO: pet auto target
        # TODO: summon bahamut/ only if gcd is half passed
        # TODO: 55s/60s combat loop switch
        def check_bio_effect(x=bio_remain):
            refreshed_target_effects = data.refresh_cache('target').effects.get_dict(source=data.me.id)
            return refreshed_target_effects[bio_aura_id].timer if bio_aura_id in refreshed_target_effects else 0 > x

        def bio():
            # TODO: here we may consider if the player has the spell, not only use level to decide
            return use_ability_to_target('BioIII', AbilityType.GCD, check_bio_effect)

        def miasma():
            # TODO: same as bio
            return use_ability_to_target('MiasmaIII')

        # when we have firebird alongside
        if pet == 14:
            return use_ability_to_target(
                'BrandOfPurgatory' if summoner_auras['HellishConduit'] in effects else 'FountainOfFire')

        if time_period_between_A_and_B_times_of_gcd(max(0, bio_remain - data.gcd), 0, 1, self.gcd) and skill_cd(
                'TriDisaster') > self.gcd * 2:
            return bio()

        if time_period_between_A_and_B_times_of_gcd(max(0, miasma_remain - data.gcd), 0, 1, self.gcd) and skill_cd(
                'TriDisaster') > self.gcd * 2:
            return miasma()

        return use_ability_to_target('RuinII')

    def non_global_cool_down_ability(self, data: 'LogicData'):

        pet = data.pet_id
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        gauge = data.gauge
        target_effects = data.target.effects.get_dict(source=data.me.id)
        bio_aura_id, miasma_aura_id = get_bio_and_miasma_aura_ids(data)
        bio_remain = target_effects[bio_aura_id].timer if bio_aura_id in target_effects else 0
        miasma_remain = target_effects[miasma_aura_id].timer if miasma_aura_id in target_effects else 0

        def skill_cd(skill_name: str):
            return data.skill_cd(summoner_spells[skill_name]['id'])

        def use_ability_to_target(spell_name: str, ability_type: AbilityType = None,
                                  wait_until: Callable = None):
            return data.use_ability_to_target(summoner_spells[spell_name]['id'], ability_type, wait_until)

        if pet not in [3, 10, 14]:
            return use_ability_to_target('SummonIII')

        if skill_cd('DreadwyrmTrance') < self.gcd / 2:
            if skill_cd('TriDisaster') < self.gcd / 2:
                return use_ability_to_target('TriDisaster')
            elif data.gcd <= self.gcd / 2:
                return use_ability_to_target('DreadwyrmTrance')

        if gauge.phoenix_ready and skill_cd('FirebirdTrance') < self.gcd / 2:
            if skill_cd('TriDisaster') < self.gcd / 2:
                return use_ability_to_target('TriDisaster')
            elif data.gcd <= self.gcd / 2:
                return use_ability_to_target('FirebirdTrance')

        if gauge.bahamut_ready and data.gcd <= self.gcd / 2:
            return use_ability_to_target('SummonBahamut')

        if (time_period_between_A_and_B_times_of_gcd(max(0, bio_remain - data.gcd), 0, 1,
                                                     self.gcd) or time_period_between_A_and_B_times_of_gcd(
            max(0, miasma_remain - data.gcd), 0, 1, self.gcd)) and skill_cd('TriDisaster') < self.gcd / 2:
            return use_ability_to_target('TriDisaster')
