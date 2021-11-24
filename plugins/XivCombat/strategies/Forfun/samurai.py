from math import radians
from .. import *
from .samurai_meta import *
from XivCombat.multi_enemy_selector import NearCircle, Sector, select
from ...define import AbilityType, FORCE_SINGLE, FORCE_MULTI

samurai_auras = {
    'MeikyoShisui': 1233,
    'EnhancedEnpi': 1236,
    'Jinpu': 1298,
    'Shifu': 1299,
    'Higanbana': 1228,
    'Kaiten': 1229,
    'OpenEyes': 1252,
    'TrueNorth': 1250
}


# Note that there is a discipline when calling this one: if wanna use this to determine an oGCD spell,
# it's necessary to consider current GCD spent
def time_period_between_A_and_B_times_of_gcd(time_period, A, B, gcd):
    return A * gcd <= time_period < B * gcd


circle_aoe = NearCircle(5)
sector_aoe = Sector(8, radians(90))


def count_enemy(data: 'LogicData', aoe_shape):
    if data.config['single'] == FORCE_SINGLE:
        return data.target, 1
    selected, cnt = select(data, data.valid_enemies, aoe_shape)
    if not cnt:
        return data.target, 0
    if data.config['single'] == FORCE_MULTI:
        return selected, 3
    return selected, cnt


class SamuraiLogic(Strategy):
    name = "samurai_logic"
    # fight_only = False
    job = 'Samurai'
    default_data = {
        'auto_true_north': True,
        'use_hissatsu_guren': True
    }
    gcd = 0

    def global_cool_down_ability(self, data: 'LogicData'):

        # to make a decision, we always need quite a lot information first
        lv = data.me.level
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        gauge = data.gauge
        effects = data.effects
        target_effects = data.target.effects.get_dict(source=data.me.id)
        num_sen = sum([gauge.moon, gauge.flower, gauge.snow])
        combo_id = data.combo_id
        kenki = gauge.kenki
        target = data.target
        jinpu_remain = effects[samurai_auras['Jinpu']].timer if samurai_auras['Jinpu'] in effects else 0
        shifu_remain = effects[samurai_auras['Shifu']].timer if samurai_auras['Shifu'] in effects else 0
        higanbana_remain = target_effects[samurai_auras['Higanbana']].timer if samurai_auras[
                                                                                   'Higanbana'] in target_effects else 0

        # huh, less codes, better codes
        def use_ability_to_target(spell_name: str, ability_type: AbilityType = None,
                                  wait_until: Callable = None):
            return data.use_ability_to_target(samurai_spells[spell_name]['id'], ability_type, wait_until)

        def skill_cd(skill_name: str):
            return data.skill_cd(samurai_spells[skill_name]['id'])

        auto_true_north = data.config['auto_true_north'] and lv >= samurai_spells['TrueNorth'][
            'lv'] and target.is_positional and skill_cd('TrueNorth') < 45

        def next_combo():
            if combo_id == samurai_spells['Shifu']['id']:
                if auto_true_north and \
                        target.target_position(data.me) != 'SIDE' and \
                        samurai_auras['TrueNorth'] not in effects and \
                        data.target_distance <= 5:
                    return use_ability_to_target('TrueNorth', AbilityType.oGCD)
                return use_ability_to_target('Kasha', AbilityType.GCD,
                                             lambda: data.refresh_cache('gauge').flower)
            elif combo_id == samurai_spells['Jinpu']['id']:
                if auto_true_north and \
                        target.target_position(data.me) != 'BACK' and \
                        samurai_auras['TrueNorth'] not in effects and \
                        data.target_distance <= 5:
                    return use_ability_to_target('TrueNorth', AbilityType.oGCD)
                return use_ability_to_target('Gekko', AbilityType.GCD, lambda: data.refresh_cache('gauge').moon)
            elif combo_id == samurai_spells['Hakaze']['id']:
                if jinpu_remain <= shifu_remain:
                    return use_ability_to_target('Jinpu', AbilityType.GCD,
                                                 lambda: samurai_auras['Jinpu'] in data.refresh_cache('effects'))
                else:
                    return use_ability_to_target('Shifu', AbilityType.GCD,
                                                 lambda: samurai_auras['Shifu'] in data.refresh_cache('effects'))
            else:
                return use_ability_to_target('Hakaze')

        # deal with multiple enemies
        if combo_id == samurai_spells['Fuga']['id']:
            aoe_target, enemy_cnt = count_enemy(data, circle_aoe)
            if enemy_cnt >= 3 and num_sen < 2:
                if 0 < shifu_remain < self.gcd * 2:
                    return UseAbility(ability_id=samurai_spells['Oka']['id'], target_id=aoe_target.id)
                if 0 < jinpu_remain < self.gcd * 2:
                    return UseAbility(ability_id=samurai_spells['Mangetsu']['id'], target_id=aoe_target.id)
                if not gauge.flower and not gauge.moon:
                    return UseAbility(
                        ability_id=samurai_spells['Mangetsu' if jinpu_remain < shifu_remain else 'Oka']['id'],
                        target_id=aoe_target.id)
                if not gauge.flower:
                    return UseAbility(ability_id=samurai_spells['Oka']['id'], target_id=aoe_target.id)
                if not gauge.moon:
                    return UseAbility(ability_id=samurai_spells['Mangetsu']['id'], target_id=aoe_target.id)
        aoe_target, enemy_cnt = count_enemy(data, sector_aoe)
        if enemy_cnt >= 3:
            if gauge.prev_kaeshi_lv == 2 and skill_cd('Tsubamegaeshi') < 0.2:
                return UseAbility(ability_id=samurai_spells['Tsubamegaeshi']['id'], target_id=aoe_target.id)
            if num_sen == 2:
                if kenki >= 20 and samurai_auras['Kaiten'] not in effects:
                    return use_ability_to_target('HissatsuKaiten', AbilityType.oGCD,
                                                 lambda: samurai_auras['Kaiten'] in data.refresh_cache('effects'))
                return UseAbility(ability_id=samurai_spells['TenkaGoken']['id'], target_id=aoe_target.id)
            if combo_id == samurai_spells['Shifu']['id'] and not gauge.flower:
                return UseAbility(ability_id=samurai_spells['Kasha']['id'], target_id=aoe_target.id)
            if combo_id == samurai_spells['Jinpu']['id'] and not gauge.moon:
                return UseAbility(ability_id=samurai_spells['Gekko']['id'], target_id=aoe_target.id)
            if combo_id == samurai_spells['Hakaze']['id']:
                if shifu_remain < self.gcd:
                    return UseAbility(ability_id=samurai_spells['Shifu']['id'], target_id=aoe_target.id)
                if jinpu_remain < self.gcd:
                    return UseAbility(ability_id=samurai_spells['Jinpu']['id'], target_id=aoe_target.id)
            if shifu_remain < self.gcd * 2 or jinpu_remain < self.gcd * 2:
                return UseAbility(ability_id=samurai_spells['Hakaze']['id'], target_id=aoe_target.id)
            if num_sen < 2:
                return UseAbility(ability_id=samurai_spells['Fuga']['id'], target_id=aoe_target.id)
            if num_sen > 2:
                return UseAbility(ability_id=samurai_spells['MidareSetsugekka']['id'], target_id=aoe_target.id)

        if gauge.prev_kaeshi_lv == 3 and skill_cd('Tsubamegaeshi') < 0.2:
            return use_ability_to_target('Tsubamegaeshi')

        # in case we have MeikyoShisui aura -- a rather simple situation
        if samurai_auras['MeikyoShisui'] in effects:
            execution_left = effects[samurai_auras['MeikyoShisui']].param
            if num_sen == 1 and \
                    time_period_between_A_and_B_times_of_gcd(max(0, higanbana_remain - data.gcd), 0, 2, self.gcd) and \
                    jinpu_remain > 0:
                if samurai_auras['Kaiten'] in effects:
                    return use_ability_to_target('Higanbana')
                if kenki >= 40:
                    return use_ability_to_target('HissatsuKaiten', AbilityType.oGCD,
                                                 lambda: samurai_auras['Kaiten'] in data.refresh_cache('effects'))

            # in meikyoshisu, we try to use Gekko/Kasha first
            if not gauge.moon:
                return use_ability_to_target('Gekko', AbilityType.GCD, lambda: data.refresh_cache('gauge').moon)
            elif not gauge.flower:
                return use_ability_to_target('Kasha', AbilityType.GCD, lambda: data.refresh_cache('gauge').flower)
            elif not gauge.snow:
                return use_ability_to_target('Yukikaze', AbilityType.GCD, lambda: data.refresh_cache('gauge').snow)
            else:
                if samurai_auras['Kaiten'] in effects and jinpu_remain > 0:
                    return use_ability_to_target('MidareSetsugekka')
                if samurai_auras['Kaiten'] not in effects and jinpu_remain > 0:
                    if kenki >= 20:
                        return use_ability_to_target('HissatsuKaiten', AbilityType.oGCD,
                                                     lambda: samurai_auras['Kaiten'] in data.refresh_cache('effects'))
                    else:
                        return use_ability_to_target(
                            'Yukikaze', AbilityType.GCD, lambda x=kenki: data.refresh_cache('gauge').kenki > x)

        # second, if now we got 3 sens, consider using midare setsugekka
        if num_sen == 3:
            # special cases, kaeshi setsugekka very close but not ready
            if time_period_between_A_and_B_times_of_gcd(max(0, skill_cd('Tsubamegaeshi') - data.gcd), 1, 3, self.gcd):
                return next_combo()
            # if we got Jinpu aura
            if jinpu_remain > 0:
                # if kenki is enough for Kaiten, Midare Setsugekka!
                if samurai_auras['Kaiten'] in effects:
                    return use_ability_to_target('MidareSetsugekka')
                if kenki >= 20:
                    return use_ability_to_target('HissatsuKaiten', AbilityType.oGCD,
                                                 lambda: samurai_auras['Kaiten'] in data.refresh_cache('effects'))
                # sadly, we do not have enough kenki, go get some!
                else:
                    if combo_id == samurai_spells['Hakaze']['id']:
                        return use_ability_to_target(
                            'Yukikaze', AbilityType.GCD, lambda x=kenki: data.refresh_cache('gauge').kenki > x)
                    else:
                        return use_ability_to_target('Hakaze')
            # if we do not have Jinpu aura, go get it!
            else:
                if combo_id == samurai_spells['Hakaze']['id']:
                    return use_ability_to_target('Jinpu', AbilityType.GCD,
                                                 lambda: samurai_auras['Jinpu'] in data.refresh_cache('effects'))
                else:
                    return use_ability_to_target('Hakaze')

        if num_sen == 1:
            if time_period_between_A_and_B_times_of_gcd(max(0, higanbana_remain - data.gcd), 0, 2, self.gcd):
                if jinpu_remain > 0:
                    if samurai_auras['Kaiten'] in effects:
                        return use_ability_to_target('Higanbana')
                    if kenki >= 20:
                        return use_ability_to_target('HissatsuKaiten', AbilityType.oGCD,
                                                     lambda: samurai_auras['Kaiten'] in data.refresh_cache('effects'))
                    else:
                        return next_combo()
            elif time_period_between_A_and_B_times_of_gcd(max(0, higanbana_remain - data.gcd), 3.5, 5.5, self.gcd):
                return use_ability_to_target('Hagakure', AbilityType.oGCD)

        # third, in general, if we are in middle of a combo, we finish it
        if combo_id == samurai_spells['Shifu']['id']:
            if auto_true_north and \
                    target.target_position(data.me) != 'SIDE' and \
                    samurai_auras['TrueNorth'] not in effects and \
                    data.target_distance <= 5:
                return use_ability_to_target('TrueNorth', AbilityType.oGCD)
            return use_ability_to_target('Kasha', AbilityType.GCD, lambda: data.refresh_cache('gauge').flower)

        if combo_id == samurai_spells['Jinpu']['id']:
            if auto_true_north and \
                    target.target_position(data.me) != 'BACK' and \
                    samurai_auras['TrueNorth'] not in effects and \
                    data.target_distance <= 5:
                return use_ability_to_target('TrueNorth', AbilityType.oGCD)
            return use_ability_to_target('Gekko', AbilityType.GCD, lambda: data.refresh_cache('gauge').moon)

        if combo_id == samurai_spells['Hakaze']['id']:
            if shifu_remain < self.gcd * 3:
                return use_ability_to_target('Shifu', AbilityType.GCD,
                                             lambda: samurai_auras['Shifu'] in data.refresh_cache('effects'))
            if jinpu_remain < self.gcd * 3:
                return use_ability_to_target('Jinpu', AbilityType.GCD,
                                             lambda: samurai_auras['Jinpu'] in data.refresh_cache('effects'))
            if higanbana_remain < self.gcd * 3 and num_sen == 0:
                return use_ability_to_target('Yukikaze', AbilityType.GCD, lambda: data.refresh_cache('gauge').snow)

        if shifu_remain < self.gcd * 3 or jinpu_remain < self.gcd * 3:
            return use_ability_to_target('Hakaze')

        if skill_cd('MeikyoShisui') < self.gcd / 2:
            if time_period_between_A_and_B_times_of_gcd(max(0, skill_cd('Tsubamegaeshi') - data.gcd), 4 - num_sen,
                                                        6 - num_sen,
                                                        self.gcd):
                return next_combo()
            return use_ability_to_target('MeikyoShisui', AbilityType.oGCD)
        # special case: catch up with kaeshi setsugekka

        # special case: in rush to catch up with higanbana

        # special case: use Hagakure to catch up with higanbana / KaeshiSetsugekka

        # basically, go get sens
        if combo_id == samurai_spells['Hakaze']['id']:
            # consider to use yukikaze first
            if not gauge.snow:
                return use_ability_to_target('Yukikaze', AbilityType.GCD, lambda: data.refresh_cache('gauge').snow)
            if not gauge.moon:
                return use_ability_to_target('Jinpu', AbilityType.GCD,
                                             lambda: samurai_auras['Jinpu'] in data.refresh_cache('effects'))
            if not gauge.flower:
                return use_ability_to_target('Shifu', AbilityType.GCD,
                                             lambda: samurai_auras['Shifu'] in data.refresh_cache('effects'))

        return next_combo()

    def non_global_cool_down_ability(self, data: 'LogicData'):

        # huh, less codes, better codes
        def use_ability_to_target(spell_name: str):
            return data.use_ability_to_target(samurai_spells[spell_name]['id'])

        def skill_cd(skill_name: str):
            return data.skill_cd(samurai_spells[skill_name]['id'])

        # To make a decision, we need quit a lot information
        gauge = data.gauge
        effects = data.effects
        kenki = data.gauge.kenki
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        jinpu_remain = effects[samurai_auras['Jinpu']].timer if samurai_auras['Jinpu'] in effects else 0

        if kenki < 50 and skill_cd('Ikishoten') < self.gcd / 2:
            return use_ability_to_target('Ikishoten')

        if samurai_auras['MeikyoShisui'] not in effects and samurai_auras['EnhancedEnpi'] in effects:
            return use_ability_to_target('Enpi')

        if gauge.meditation > 2:
            return use_ability_to_target('Shoha')

        aoe_target, enemy_cnt = count_enemy(data, circle_aoe)
        if enemy_cnt >= 3:
            if data.config['use_hissatsu_guren'] and skill_cd('HissatsuGuren') < self.gcd / 2:
                return UseAbility(ability_id=samurai_spells['HissatsuGuren']['id'], target_id=aoe_target.id)
            if kenki >= 45 and (not data.config['use_hissatsu_guren'] or skill_cd('HissatsuGuren') > skill_cd(
                    'Ikishoten') or skill_cd('HissatsuGuren') > 4 * self.gcd or kenki >= 95):
                return UseAbility(ability_id=samurai_spells['HissatsuKyuten']['id'], target_id=aoe_target.id)
            return None

        if jinpu_remain > 0 and kenki >= 70 and skill_cd('HissatsuSenei') < self.gcd / 2:
            return use_ability_to_target('HissatsuSenei')

        if (skill_cd('HissatsuSenei') > skill_cd('Ikishoten') or skill_cd(
                'HissatsuSenei') > 6 * self.gcd or kenki >= 85) and \
                kenki >= 35 and \
                samurai_auras['OpenEyes'] in effects:
            return use_ability_to_target('HissatsuSeigan')

        if (skill_cd('HissatsuSenei') > skill_cd('Ikishoten') or skill_cd(
                'HissatsuSenei') > 6 * self.gcd or kenki >= 95) and kenki >= 45:
            return use_ability_to_target('HissatsuShinten')
