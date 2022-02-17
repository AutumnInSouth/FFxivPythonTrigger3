from math import radians

from FFxivPythonTrigger.utils.shape import sector
from XivCombat.strategies import *
from XivCombat import define, logic_data

"""
2866：分裂弹
2868：独头弹
2872：热弹
2876：整备
2874：虹吸弹
2870：散射
2873：狙击弹
17209：超荷
7410：热冲击
2864：炮塔
2878：野火
2890：弹射
16497：自动弩
16498：钻头
7414：枪管加热
16499：毒菌
"""

mch_aoe_angle = radians(90)


def is_single(data: logic_data.LogicData) -> bool:
    if data.config['single'] == define.FORCE_SINGLE:
        return True
    elif data.config['single'] == define.FORCE_MULTI:
        return False
    cnt = 0
    mch_aoe = sector(data.me.pos.x, data.me.pos.y, 12, mch_aoe_angle, data.me.target_radian(data.target))
    for enemy in data.valid_enemies:
        if mch_aoe.intersects(enemy.hitbox()):
            cnt += 1
            if cnt > 2: return False
    return True


def res_lv(data: logic_data.LogicData) -> int:
    if data.config['resource'] == define.RESOURCE_SQUAND:
        return 2
    elif data.config['resource'] == define.RESOURCE_NORMAL:
        return 1
    elif data.config['resource'] == define.RESOURCE_STINGY:
        return 0
    return 1


class MachinistLogic(Strategy):
    name = "machinist_logic"
    job = "Machinist"

    def global_cool_down_ability(self, data: logic_data.LogicData) -> AnyUse:
        hsid = 2872 if data.me.level < 76 else 16500
        single = is_single(data)
        res_use = res_lv(data)
        if data.target_distance > 25:
            return
        if data[2876] or not res_use:
            if data.gcd >= data[16498]: return data.use_ability_to_target(16498 if single or data.me.level < 72 else 16498)
        if data[2876] or not res_use or data.me.level < 76:
            if data.gcd >= data[hsid]: return data.use_ability_to_target(hsid)
        if single or data.target_distance > 12 or data.me.level < 18:
            if data.gauge.overheat_ms and data.me.level >= 35:
                return data.use_ability_to_target(7410)
            elif data.combo_id == 2866 and data.me.level >= 2:
                return data.use_ability_to_target(2868)
            elif data.combo_id == 2868 and data.me.level >= 26:
                return data.use_ability_to_target(2873)
            else:
                return data.use_ability_to_target(2866)
        else:
            return data.use_ability_to_target(16497 if data.gauge.overheat_ms and data.me.level >= 52 else 2870)

    def non_global_cool_down_ability(self, data: logic_data.LogicData) -> AnyUse:
        hsid = 2872 if data.me.level < 76 else 16500
        res_use = res_lv(data)
        if data.target_distance > 25:
            return
        if min(data[2874], data[2890]) < 15:
            return data.use_ability_to_target(2874) if data[2874] <= data[2890] else data.use_ability_to_target(2890)
        if not res_use: return
        if data.gauge.battery >= 90:
            return data.use_ability_to_target(2864)

        if data.config['tincture'] and not data.item_cd and data.item_count(31894):
            cds = [2878, 16498, 7414]
            if data.me.level > 76: cds.append(16500)
            cds = [data[cd] for cd in cds]
            if min(cds) < 3 and max(cds) < 25:
                return UseItem(31894)

        if not data[2876]:
            if data[16498] < data.gcd:
                data.reset_cd(16498)
                return data.use_ability_to_target(2876)
            elif data[hsid] < data.gcd and data.me.level > 76:
                data.reset_cd(hsid)
                return data.use_ability_to_target(2876)

        can_over = not data.gauge.overheat_ms and \
                   data[16498] > 8 and data[hsid] > 8 and \
                   (data.combo_remain > 11 or data.combo_id not in {2866,2868}) and\
                   data.gauge.heat >= 50

        if can_over and not data[2878] and not data.ability_cnt:
            return data.use_ability_to_target(2878)
        if can_over and data[2878] > 8:
            if data.ability_cnt and data.gcd > 1.3:
                return
            elif data.gcd <= 1.3:
                return data.use_ability_to_target(17209)
        if data.gauge.heat < 50 and not data[7414]: return data.use_ability_to_target(7414)
        if min(data[2874], data[2890]) < 60:
            return data.use_ability_to_target(2874) if data[2874] <= data[2890] else data.use_ability_to_target(2890)
        if data.gauge.battery >= 50:
            return data.use_ability_to_target(2864)

    def global_cool_down_ability_on_count_down(self, data: 'LogicData') -> AnyUse:
        if data.last_count_down > 5 or not res_lv(data): return
        if not data[2876]: return UseAbility(2876)
        if data.last_count_down < 2 and data.config['tincture'] and not data.item_cd and data.item_count(31894):
            return UseItem(31894)
        if data.last_count_down < 1 and not data[16498]:
            target = api.get_current_target()
            if target is None or not data.is_target_attackable(target): return
            return UseAbility(16498, target.id)
        if not data[7557]: return UseAbility(7557)
