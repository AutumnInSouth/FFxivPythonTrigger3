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
            single_distance = data.actor_distance_effective(single_target)
            if not single_target: return

        if set(data.effects.keys()).intersection(continuations):
            return UseAbility(a('续剑'), single_target.id, ability_type=define.AbilityType.oGCD) if single_distance <= 3 else None

        max_cartridges = 2 if data.me.level < 88 else 3

        if single_distance > 5:
            return UseAbility(a('闪雷弹'), single_target.id) if single_distance > 7 and not data.gcd and data.me.level >= 15 else None
        res = res_lv(data)
        aoe_target, aoe_count = cnt_enemy(data, aoe_area) if data.me.level >= 10 else (single_target, 0)


        brutal_shell = data.combo_id == a('残暴弹') and data.me.level >= 26 and not data.config['single_shield']
        if brutal_shell or data.combo_id == a('恶魔切') and data.me.level >= 40:
            if res and data.gauge.cartridges == max_cartridges:
                if aoe_count >= 2 and data.me.level >= 72:
                    return UseAbility(a('命运之环'), aoe_target.id)
                elif aoe_count < 3 or brutal_shell:
                    return UseAbility(a('爆发击'), single_target.id)
            return UseAbility(a('迅连斩'), single_target.id) if brutal_shell else UseAbility(a('恶魔杀'), aoe_target.id)

        if aoe_count >= 3: return UseAbility(a('恶魔切'), aoe_target.id)

        if data.actor_distance_effective(single_target) > 3: return
        if data.combo_id == a('利刃斩') and data.me.level >= 4:
            return UseAbility(a('残暴弹'), single_target.id)
        return UseAbility(a('利刃斩'), single_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        pass
