from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import NearCircle
from .utils import mo_provoke_and_shirk

aoe_area = NearCircle(5)

gnb_mo_action = {a('Heart of Corundum'), a('石之心'), a('极光')}
continuations = {s('撕喉预备'), s('裂膛预备'), s('穿目预备'), s('Ready To Blast')}


class GunBreakerStrategy(Strategy):
    name = 'ny/gbk_logic'
    job = 'Gunbreaker'
    default_data = {'single_shield': False}

    @mo_provoke_and_shirk
    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        if action_id in gnb_mo_action:
            mo_entity = api.get_mo_target()
            if mo_entity and api.action_type_check(action_id, mo_entity):
                return UseAbility(action_id, mo_entity.id)

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 3:
            single_target = data.target
            single_distance = data.target_distance
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('闪雷弹')))
            if not single_target: return
            single_distance = data.actor_distance_effective(single_target)

        if set(data.effects.keys()).intersection(continuations):
            return UseAbility(a('续剑'), single_target.id, ability_type=define.AbilityType.oGCD) if single_distance <= 3 else None

        max_cartridges = 2 if data.me.level < 88 else 3
        no_mercy_cd = data[a('无情')]
        in_no_mercy = no_mercy_cd > 58 or data.effect_time(s('无情'))
        if single_distance > 5:
            if single_distance > (10 if in_no_mercy else 7) and not data.gcd and data.me.level >= 15:
                return UseAbility(a('闪雷弹'), single_target.id)
            return

        res = res_lv(data)
        aoe_target, aoe_count = cnt_enemy(data, aoe_area) if data.me.level >= 10 else (single_target, 0)

        if res and in_no_mercy and data[a('Double Down')] < data.gcd and aoe_count and data.gauge.cartridges >= 2:
            return UseAbility(a('Double Down'), aoe_target.id)
        if data[a('烈牙')] < data.gcd and data.gauge.cartridges and res and (in_no_mercy or no_mercy_cd + 7 > data.recast_time(a('烈牙'))):
            return UseAbility(a('烈牙'), single_target.id)
        if res and in_no_mercy and data[a('音速破')] < data.gcd:
            return UseAbility(a('音速破'), single_target.id)
        if data.gauge.continuation_state:
            return UseAbility(a('烈牙'), single_target.id)

        if data.gauge.cartridges and res and (in_no_mercy or (data[a('血壤')] < data.gauge.cartridges * 2.5 and no_mercy_cd > 15)):
            if aoe_count >= 2 and data.me.level >= 72:
                return UseAbility(a('命运之环'), aoe_target.id)
            return UseAbility(a('爆发击'), single_target.id)

        brutal_shell = data.combo_id == a('残暴弹') and data.me.level >= 26 and not data.config['single_shield']
        if brutal_shell or data.combo_id == a('恶魔切') and data.me.level >= 40:
            gcd = data.recast_time(a('迅连斩'))
            if no_mercy_cd < data.gcd < 1.3 and data.gauge.cartridges:
                return UseAbility(a('无情'), data.me.id, ability_type=define.AbilityType.oGCD)
            if res and data.gauge.cartridges == max_cartridges and no_mercy_cd > gcd * 2:
                if no_mercy_cd < gcd: return UseAbility(a('闪雷弹'), single_target.id)
                if aoe_count >= 2 and data.me.level >= 72:
                    return UseAbility(a('命运之环'), aoe_target.id)
                elif aoe_count < 3 or brutal_shell:
                    return UseAbility(a('爆发击'), single_target.id)
            if res and data.gauge.cartridges and no_mercy_cd < gcd: return UseAbility(a('闪雷弹'), single_target.id)
            return UseAbility(a('迅连斩'), single_target.id) if brutal_shell else UseAbility(a('恶魔杀'), aoe_target.id)

        if aoe_count >= 3: return UseAbility(a('恶魔切'), aoe_target.id)

        if data.actor_distance_effective(single_target) > 3: return
        if data.combo_id == a('利刃斩') and data.me.level >= 4:
            return UseAbility(a('残暴弹'), single_target.id)
        return UseAbility(a('利刃斩'), single_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 3:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('利刃斩')))
            if not single_target: return
        if set(data.effects.keys()).intersection(continuations): return UseAbility(a('续剑'), single_target.id)
        if not res_lv(data): return
        no_mercy_cd = data[a('无情')]
        if not no_mercy_cd and data.gauge.cartridges and (data.combo_id == a('残暴弹') or data.combo_id == a('恶魔切')):
            if data.ability_cnt and data.gcd > 1.3:
                return
            elif data.gcd <= 1.3:
                return UseAbility(a('无情'), data.me.id)
        in_no_mercy = no_mercy_cd > 58 or data.effect_time(s('无情'))
        if not data[a('血壤')] and not data.gauge.cartridges and (in_no_mercy or no_mercy_cd > 20 or not no_mercy_cd):
            return UseAbility(a('血壤'), single_target.id)
        if not data[a('危险领域')] and (in_no_mercy or no_mercy_cd + 10 > data.recast_time(a('危险领域'))):
            return UseAbility(a('危险领域'), single_target.id)
        aoe_target, aoe_count = cnt_enemy(data, aoe_area) if data.me.level >= 10 else (single_target, 0)
        if not data[a('弓形冲波')] and in_no_mercy and aoe_count:
            return UseAbility(a('弓形冲波'), aoe_target.id)
        if data[a('粗分斩')] < 1 and not data.actor_distance_effective(single_target):
            return UseAbility(a('粗分斩'), single_target.id)
