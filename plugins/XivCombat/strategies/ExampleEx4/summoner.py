from functools import cache
from math import radians

from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import FarCircle


def select_res_target_key(actor):
    return actor.job.is_tank, actor.job.is_healer, actor.job.is_dps


def search_swift_res(data: 'LogicData'):
    if not data.skill_unlocked(a('复生')):
        return
    match data.config['swift_res']:
        case 'party':
            d = data.valid_party
        case 'all':
            d = data.valid_players
        case 'alliance':
            d = data.valid_alliance
        case _:
            return
    return max(
        (member for member in d
         if not member.current_hp and
         not member.effects.has(s('复活')) and
         data.actor_distance_effective(member) < 30)
        , key=select_res_target_key, default=None
    )


aoe_area = FarCircle(25, 5)


class SmnLogic(Strategy):
    name = "ny/smn_logic"
    job = 'Summoner'
    default_data = {
        'swift_res': 'none',
        'jmp_distance': 0.,
        'use_swift': True,
    }

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if not data.pet_id: return UseAbility(a('宝石兽召唤'))

        if data.target and data.target_distance <= 25:
            single_target = data.target
            single_distance = data.target_distance
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('毁灭（召唤）')))
            if not single_target or data.actor_distance_effective(single_target) > 25: return
            single_distance = data.actor_distance_effective(single_target)

        if data.me.level >= 26:
            aoe_target, aoe_cnt = cnt_enemy(data, aoe_area, single_target)
        else:
            aoe_target, aoe_cnt = single_target, 0

        has_speed = s('即刻咏唱') in data.effects

        if res_lv(data):
            if not data[a('Searing Light')] and data.pet_id == 23:
                return UseAbility(a('Searing Light'), data.me.id,ability_type=define.AbilityType.oGCD)
            if not data[a('Aethercharge')] and data[a('Searing Light')] > 10:
                return UseAbility(a('Aethercharge'), single_target.id)

        if data.combo_id == 25835:
            if single_distance <= 3:
                return UseAbility(a('Astral Flow'), single_target.id)
            else:
                return

        if s("Ifrit's Favor") in data.effects and single_distance <= data.config['jmp_distance']:
            return UseAbility(a('Astral Flow'), single_target.id)
        if s("Titan's Favor") in data.effects:
            return UseAbility(a('Astral Flow'), single_target.id, ability_type=define.AbilityType.oGCD)
        if s("Garuda's Favor") in data.effects and aoe_cnt > len(data.valid_enemies) // 2:
            if has_speed or not data.is_moving:
                return UseAbility(a('Astral Flow'), aoe_target.id)
            elif not data[a('即刻咏唱')] and data.config['use_swift']:
                return UseAbility(a('即刻咏唱'), data.me.id)

        if data.gauge.attunement:
            if aoe_cnt >= 2:
                smn_use = UseAbility(a('Precious Brilliance'), aoe_target.id)
            else:
                smn_use = UseAbility(a('Gemshine'), single_target.id)
            match data.gauge.summon_type:
                case 1:  # Ifrit
                    if has_speed or not data.is_moving:
                        return smn_use
                    elif s('Further Ruin') in data.effects:
                        return UseAbility(a('毁绝'), aoe_target.id)
                    elif not data[a('即刻咏唱')] and data.config['use_swift']:
                        return UseAbility(a('即刻咏唱'), data.me.id)
                case 2 | 3:  # Titan
                    return smn_use
        if not data.gauge.stance_ms:
            if data.gauge.titan_ready: return UseAbility(a('Summon Topaz'), (aoe_target if data.me.level >= 35 else single_target).id)
            if data.gauge.ifrit_ready: return UseAbility(a('Summon Ruby'), (aoe_target if data.me.level >= 30 else single_target).id)
            if data.gauge.garuda_ready: return UseAbility(a('Summon Emerald'), (aoe_target if data.me.level >= 45 else single_target).id)
        if data.effect_time(s('Further Ruin')) and data.pet_id == 23: return UseAbility(a('毁绝'), aoe_target.id)

        if data.gauge.stance_ms or (not data.is_moving or has_speed):
            if aoe_cnt >= 3:
                return UseAbility(a('迸裂'), aoe_target.id)
            else:
                return UseAbility(a('毁灭（召唤）'), single_target.id)
        elif s('Further Ruin') in data.effects:
            return UseAbility(a('毁绝'), aoe_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if data.target and data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('毁灭（召唤）')))
            if not single_target or data.actor_distance_effective(single_target) > 25: return
        aoe_target, aoe_cnt = cnt_enemy(data, aoe_area, single_target) if data.me.level >= 40 else (single_target, 0)

        if not data[a('龙神迸发')] and (data.pet_id == 14 or data.pet_id == 10):
            return UseAbility(a('龙神迸发'), aoe_target.id)
        if not data[a('死星核爆')] and data.pet_id == 10:
            return UseAbility(a('死星核爆'), aoe_target.id)

        if data.gauge.aether_flow_stacks:
            if aoe_cnt >= 2 and data.me.level >= 40:
                return UseAbility(a('痛苦核爆'), aoe_target.id)
            else:
                return UseAbility(a('溃烂爆发'), single_target.id)
        elif not data[a('能量吸收（召唤师）')]:
            if aoe_cnt >= 2 and data.me.level >= 52:
                return UseAbility(a('Energy Siphon'), aoe_target.id)
            else:
                return UseAbility(a('能量吸收（召唤师）'), single_target.id)

        if data.me.current_mp < 8000:
            return UseAbility(a('醒梦'), data.me.id)
