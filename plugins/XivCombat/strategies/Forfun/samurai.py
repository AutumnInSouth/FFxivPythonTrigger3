from .. import *
from .samurai_meta import *

samurai_auras = {
    'MeikyoShisui': 1233,
    'Jinpu': 1298,
    'Shifu': 1299,
    'Higanbana': 1228,
    'Kaiten': 1229,
    'OpenEyes': 1252
}


def at_most_N_gcds_in_time_period(time_period, N, gcd):
    return N * gcd <= time_period < (N + 1) * gcd


def time_period_between_A_and_B_times_of_gcd(time_period, A, B, gcd):
    return A * gcd <= time_period < B * gcd


class SamuraiLogic(Strategy):
    name = "samurai_logic"
    #fight_only = False
    job = 'Samurai'
    default_data = {}
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
        jinpu_remain = effects[samurai_auras['Jinpu']].timer if samurai_auras['Jinpu'] in effects else 0
        shifu_remain = effects[samurai_auras['Shifu']].timer if samurai_auras['Shifu'] in effects else 0
        higanbana_remain = target_effects[samurai_auras['Higanbana']].timer if samurai_auras['Higanbana'] in target_effects else 0

        # huh, less codes, better codes
        def use_ability_to_target(spell_name: str, ability_type: str = None):
            return data.use_ability_to_target(samurai_spells[spell_name]['id'], ability_type)

        def skill_cd(skill_name: str):
            return data.skill_cd(samurai_spells[skill_name]['id'])

        def next_combo():
            if combo_id == samurai_spells['Shifu']['id']:
                return use_ability_to_target('Kasha')
            elif combo_id == samurai_spells['Jinpu']['id']:
                return use_ability_to_target('Gekko')
            elif combo_id == samurai_spells['Hakaze']['id']:
                return use_ability_to_target('Jinpu' if jinpu_remain <= shifu_remain else 'Shifu')
            else:
                return use_ability_to_target('Hakaze')

        if gauge.prev_kaeshi_lv == 3 and skill_cd('Tsubamegaeshi') == 0:
            return use_ability_to_target('Tsubamegaeshi')

        # in case we have MeikyoShisui aura -- a rather simple situation
        if samurai_auras['MeikyoShisui'] in effects:
            execution_left = effects[samurai_auras['MeikyoShisui']].param
            if num_sen == 1 and \
                time_period_between_A_and_B_times_of_gcd(higanbana_remain, 0, 2, self.gcd) and \
                jinpu_remain > 0:
                if samurai_auras['Kaiten'] in effects:
                    return use_ability_to_target('Higanbana')
                if kenki >= 40:
                    return use_ability_to_target('HissatsuKaiten', 'oGCD')

            # in meikyoshisu, we try to use Gekko/Kasha first
            if not gauge.moon:
                return use_ability_to_target('Gekko')
            elif not gauge.flower:
                return use_ability_to_target('Kasha')
            elif not gauge.snow:
                return use_ability_to_target('Yukikaze')
            else:
                if samurai_auras['Kaiten'] in effects and jinpu_remain > 0:
                    return use_ability_to_target('MidareSetsugekka')
                if samurai_auras['Kaiten'] not in effects and jinpu_remain > 0:
                    if kenki >= 20:
                        return use_ability_to_target('HissatsuKaiten', 'oGCD')
                    else:
                        return use_ability_to_target('Yukikaze' if combo_id == samurai_spells['Hakaze']['id'] else 'Hakaze')

        # second, if now we got 3 sens, consider using midare setsugekka
        if num_sen == 3:
            # special cases, kaeshi setsugekka very close but not ready
            if time_period_between_A_and_B_times_of_gcd(skill_cd('Tsubamegaeshi'), 1, 3, self.gcd):
                return next_combo()
            # if we got Jinpu aura
            if jinpu_remain > 0:
                # if kenki is enough for Kaiten, Midare Setsugekka!
                if samurai_auras['Kaiten'] in effects:
                    return use_ability_to_target('MidareSetsugekka')
                if kenki >= 20:
                    return use_ability_to_target('HissatsuKaiten', 'oGCD')
                # sadly, we do not have enough kenki, go get some!
                else:
                    return use_ability_to_target('Yukikaze' if combo_id == samurai_spells['Hakaze']['id'] else 'Hakaze')
            # if we do not have Jinpu aura, go get it!
            else:
                return use_ability_to_target('Jinpu' if combo_id == samurai_spells['Hakaze']['id'] else 'Hakaze')

        if num_sen == 1:
            if time_period_between_A_and_B_times_of_gcd(higanbana_remain, 0, 2, self.gcd):
                if jinpu_remain > 0:
                    if samurai_auras['Kaiten'] in effects:
                        return use_ability_to_target('Higanbana')
                    if kenki >= 20:
                        return use_ability_to_target('HissatsuKaiten', 'oGCD')
                    else:
                        return next_combo()
            elif time_period_between_A_and_B_times_of_gcd(higanbana_remain, 3, 5, self.gcd):
                return use_ability_to_target('Hagakure', 'oGCD')

        # third, in general, if we are in middle of a combo, we finish it
        if combo_id == samurai_spells['Shifu']['id']:
            return use_ability_to_target('Kasha')

        if combo_id == samurai_spells['Jinpu']['id']:
            return use_ability_to_target('Gekko')

        if combo_id == samurai_spells['Hakaze']['id']:
            if samurai_auras['Shifu'] not in effects:
                return use_ability_to_target('Shifu')
            if samurai_auras['Jinpu'] not in effects:
                return use_ability_to_target('Jinpu')

        if shifu_remain == 0 or jinpu_remain == 0:
            return use_ability_to_target('Hakaze')

        if skill_cd('MeikyoShisui') == 0:
            if time_period_between_A_and_B_times_of_gcd(skill_cd('Tsubamegaeshi'), 4 - num_sen, 6 - num_sen, self.gcd):
                return next_combo()
            return use_ability_to_target('MeikyoShisui', 'oGCD')
        # special case: catch up with kaeshi setsugekka

        # special case: in rush to catch up with higanbana

        # special case: use Hagakure to catch up with higanbana / KaeshiSetsugekka

        # basically, go get sens
        if combo_id == samurai_spells['Hakaze']['id']:
            # consider to use yukikaze first
            if not gauge.snow:
                return use_ability_to_target('Yukikaze')
            if not gauge.moon:
                return use_ability_to_target('Jinpu')
            if not gauge.flower:
                return use_ability_to_target('Shifu')

        return use_ability_to_target('Hakaze')

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

        if kenki < 50 and skill_cd('Ikishoten') == 0:
            return use_ability_to_target('Ikishoten')

        if gauge.meditation > 2:
            return use_ability_to_target('Shoha')

        if jinpu_remain > 0 and kenki >= 70 and skill_cd('HissatsuSenei') == 0:
            return use_ability_to_target('HissatsuSenei')

        if (skill_cd('HissatsuSenei') > skill_cd('Ikishoten') or skill_cd('HissatsuSenei') > 6 * self.gcd or kenki >= 85) and \
            kenki >= 35 and \
            samurai_auras['OpenEyes'] in effects:
            return use_ability_to_target('HissatsuSeigan')

        if (skill_cd('HissatsuSenei') > skill_cd('Ikishoten') or skill_cd('HissatsuSenei') > 6 * self.gcd or kenki >= 95) and kenki >= 45:
            return use_ability_to_target('HissatsuShinten')


