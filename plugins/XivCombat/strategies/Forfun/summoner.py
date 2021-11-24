from .. import *
from .summoner_meta import summoner_spells
from ...define import AbilityType

summoner_auras = {
    'MeikyoShisui': 179,
    'EnhancedEnpi': 180,
    'Jinpu': 189,
    'Shifu': 1214,
    'Higanbana': 1215,
    'Kaiten': 1212,
    'HellishConduit': 1867
}


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

        def use_ability_to_target(spell_name: str, ability_type: AbilityType = None,
                                  wait_until: Callable = None):
            return data.use_ability_to_target(summoner_spells[spell_name]['id'], ability_type, wait_until)

        # TODO: pet auto target
        # TODO: summon bahamut/ only if gcd is half passed
        # TODO: 55s/60s combat loop switch

        def bio():
            # TODO: here we may consider if the player has the spell, not only use level to decide
            return use_ability_to_target('BioIII')

        def miasma():
            # TODO: same as bio
            return use_ability_to_target('MiasmaIII')

        # when we have firebird alongside
        if pet == 14:
            return use_ability_to_target('BrandOfPurgatory' if summoner_auras['HellishConduit'] in effects else 'FountainOfFire')

        return use_ability_to_target('RuinII')

    def non_global_cool_down_ability(self, data: 'LogicData'):

        pet = data.pet_id
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        gauge = data.gauge

        def skill_cd(skill_name: str):
            return data.skill_cd(summoner_spells[skill_name]['id'])

        def use_ability_to_target(spell_name: str, ability_type: AbilityType = None,
                                  wait_until: Callable = None):
            return data.use_ability_to_target(summoner_spells[spell_name]['id'], ability_type, wait_until)

        if pet not in [3, 10, 14]:
            return use_ability_to_target('SummonIII')

        if skill_cd('DreadwyrmTrance') < self.gcd / 2:
            if skill_cd('TriDisaster') < self.gcd / 2 and (self.gcd / 2 < data.gcd or data.gcd > self.gcd - 0.2):
                return use_ability_to_target('TriDisaster')
            else:
                return use_ability_to_target('DreadwyrmTrance')

        if gauge.phoenix_ready and skill_cd('FirebirdTrance') < self.gcd / 2:
            if skill_cd('TriDisaster') < self.gcd / 2 and (self.gcd / 2 < data.gcd or data.gcd > self.gcd - 0.2):
                return use_ability_to_target('TriDisaster')
            elif data.gcd <= self.gcd / 2:
                return use_ability_to_target('FirebirdTrance')

        if gauge.bahamut_ready:
            return use_ability_to_target('SummonBahamut')
