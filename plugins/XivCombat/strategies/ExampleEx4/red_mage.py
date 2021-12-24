from functools import cache
from math import radians

from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Rectangle, FarCircle, Sector

aoe_area = FarCircle(25, 5)
resolution = Rectangle(25, 2)
moulienet = Sector(8, radians(120))
contre_sixte = FarCircle(25, 6)

rdm_prepares = {s('赤火炎预备'), s('赤飞石预备')}
speed_swing = {s('即刻咏唱'), s('连续咏唱')}


def select_res_target_key(actor):
    return actor.job.is_tank, actor.job.is_healer, actor.job.is_dps


def search_swift_res(data: 'LogicData'):
    if not data.skill_unlocked(a('赤复活')):
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


def use_acceleration(data: 'LogicData', is_must=False):
    return UseAbility(
        a('促进'), data.me.id,
        ability_type=AbilityType.oGCD if is_must else AbilityType.GCD,
        wait_until=lambda: s('促进') in data.refresh_cache('effects')
    )


def use_swift_cast(data: 'LogicData'):
    return UseAbility(
        a('即刻咏唱'), data.me.id,
        wait_until=lambda: s('即刻咏唱') in data.refresh_cache('effects')
    )


@cache
def combo_should_not_break(lv: int):
    ans = {a('回刺'), a('交击斩')}
    if lv >= 80:
        ans |= {a('赤核爆'), a('赤神圣')}
        if lv >= 90:
            ans.add(a('焦热'))
    return ans


class RDMLogic(Strategy):
    name = "rdm_logic"
    fight_only = False
    job = 'RedMage'
    default_data = {
        'swift_res': 'none',
        'jmp_distance': 0.,
        'use_swift': False,
    }

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        effects = data.me.effects.get_set()
        speed = speed_swing.intersection(effects)
        swift_res_target = search_swift_res(data)

        if data.target is None and swift_res_target is not None and data.me.current_mp >= (2400 if speed else 3100):
            if speed:
                return UseAbility(a('赤复活'), swift_res_target.id)
            elif not data.is_moving:
                return UseAbility(a('赤治疗'), data.me.id)
            elif not data[a('即刻咏唱')]:
                return use_swift_cast(data)

        if not data.valid_enemies: return
        if data.target and data.target_distance <= 25:
            single_target = data.target
            single_distance = data.target_distance
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('摇荡')))
            if not single_target or data.actor_distance_effective(single_target) > 25: return
            single_distance = data.actor_distance_effective(single_target)

        prepare = rdm_prepares.intersection(effects)
        prepare_cnt = len(prepare)

        aoe_target, aoe_cnt = cnt_enemy(data, aoe_area) if data.me.level >= 15 else (single_target, 0)

        if data.gauge.mana_stacks >= 3:
            if not aoe_cnt: return
            if not data.skill_unlocked(a('赤神圣')):
                return UseAbility(a('赤核爆'), aoe_target.id)
            return UseAbility(a('赤神圣') if (
                next(iter(prepare)) == s('赤火炎预备')
                if prepare_cnt == 1 else
                data.gauge.white_mana < data.gauge.black_mana
            ) else a('赤核爆'), aoe_target.id)

        if data.combo_id == a('回刺'):
            if data.me.level > 35:
                return UseAbility(a('交击斩'), single_target.id) if single_distance <= 3 else None
        elif data.combo_id == a('交击斩'):
            if data.me.level >= 50:
                return UseAbility(a('连攻'), single_target.id) if single_distance <= 3 else None
        elif data.combo_id == a('赤核爆') or data.combo_id == a('赤神圣'):
            if data.me.level >= 80:
                return UseAbility(a('焦热'), aoe_target.id) if aoe_cnt else None
        elif data.combo_id == a('焦热'):
            if data.me.level >= 90:
                resolution_target, resolution_cnt = cnt_enemy(data, resolution)
                return UseAbility(a('Resolution'), resolution_target.id) if resolution_cnt > 0 else None

        if swift_res_target is not None and data.me.current_mp >= 2400 and speed:
            return UseAbility(a('赤复活'), swift_res_target.id)

        res = res_lv(data)
        has_acceleration = s('促进') in effects
        acceleration_cd = data[a('促进')]
        if data.me.level <= 88:
            must_acceleration = can_acceleration = acceleration_cd - 55 <= 0
        else:
            can_acceleration = acceleration_cd <= 55
            must_acceleration = acceleration_cd <= 10

        # data.plugin.logger(acceleration_cd,can_acceleration, must_acceleration)

        if data.me.level >= 4 and (speed or has_acceleration) and not data.gauge.mana_stacks:
            if aoe_cnt > 1:
                return UseAbility(a('散碎'), aoe_target.id)
            else:
                return UseAbility(a('赤疾风') if (
                    next(iter(prepare)) == s('赤火炎预备')
                    if prepare_cnt == 1 else
                    (data.gauge.white_mana < data.gauge.black_mana and data.me.level >= 10)
                ) else a('赤闪雷'), single_target.id)
        min_mana = min(data.gauge.white_mana, data.gauge.black_mana)

        if res and min_mana >= 20:
            if data.me.level >= 52 and (data.me.level < 68 or min_mana >= 60 - data.gauge.mana_stacks * 20):
                moulienet_target, moulienet_cnt = cnt_enemy(data, moulienet)
                if moulienet_cnt > 2: return UseAbility(a('魔划圆斩'), moulienet_target.id)
            if data.gauge.mana_stacks or data[7520] > 100 or max(data.gauge.white_mana, data.gauge.black_mana) > 90:
                if min_mana >= (50 if data.me.level >= 50 else 35 if data.me.level >= 35 else 20) - data.gauge.mana_stacks * 15:
                    if single_distance <= 3:
                        return UseAbility(a('魔回刺'), single_target.id)
                    elif data.gauge.mana_stacks:
                        return

        if data.is_moving:
            if res:
                if data.config['use_swift'] and not data[a('即刻咏唱')]:
                    return use_swift_cast(data)
                if can_acceleration:
                    return use_acceleration(data)
            return

        if prepare_cnt and aoe_cnt < 3:
            return UseAbility(
                a('赤飞石') if (
                    data.gauge.white_mana < data.gauge.black_mana
                    if prepare_cnt == 0 else
                    s('赤飞石预备') in prepare
                ) else a('赤火炎'),
                single_target.id)

        if res and must_acceleration and data[a('鼓励')] and data[a('倍增')]:
            return use_acceleration(data, True)

        if aoe_cnt > 2 and data.me.level >= 18:
            return UseAbility(
                a('赤烈风') if
                data.gauge.white_mana < data.gauge.black_mana and
                data.me.level >= 22
                else a('赤震雷'), aoe_target.id)
        return UseAbility(a('摇荡'), single_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:

        if not data.valid_enemies: return

        if data.target and data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('摇荡')))
            if not single_target or data.actor_distance_effective(single_target) > 25: return

        if not res_lv(data): return

        if not data[a('鼓励')] and not data[a('倍增')]:
            return UseAbility(a('鼓励'), data.me.id)
        if (
                not data[a('倍增')] and data[a('鼓励')] > 100 and
                max(data.gauge.white_mana, data.gauge.black_mana) <= 50 and
                data.combo_id not in combo_should_not_break(data.me.level)
        ):
            return UseAbility(a('倍增'), data.me.id)

        if not data[a('飞刺')]:
            return UseAbility(a('飞刺'), single_target.id)

        if not data[a('六分反击')]:
            contre_sixte_target, contre_sixte_cnt = cnt_enemy(data, contre_sixte)
            if contre_sixte_cnt > len(data.valid_enemies) // 2:
                return UseAbility(a('六分反击'), contre_sixte_target.id)

        acceleration_cd = data[a('促进')]
        if acceleration_cd - 55 <= 0 if data.me.level <= 88 else acceleration_cd <= 10:
            effects = data.me.effects.get_set()
            if s('促进') not in effects and not speed_swing.intersection(effects):
                return use_acceleration(data)

        if data[a('交剑')] < 5 and data.actor_distance_effective(single_target) <= 3:
            return UseAbility(a('交剑'), single_target.id)

        if data[a('短兵相接')] < 5 and data.actor_distance_effective(single_target) <= data.config['jmp_distance']:
            return UseAbility(a('短兵相接'), single_target.id)

        if data.me.current_mp < 7500:
            return UseAbility(a('醒梦'), data.me.id)
