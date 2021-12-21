from XivCombat import define
from XivCombat.multi_enemy_selector import Rectangle, select
from XivCombat.strategies import *

"""
7541,内丹,8
7863,扫腿,10
7542,浴血,12
7549,牵制,22
7548,亲疏自行,32
7546,真北,50

75,精准刺,1
78,贯通刺,4
83,龙剑,6
90,贯穿尖,15
87,开膛枪,18
84,直刺,26
85,猛枪,30
92,跳跃,30
94,回避跳跃,35
86,死天枪,40
95,破碎冲,45
88,樱花怒放,50
96,龙炎冲,50
3557,战斗连祷,52
3553,苍天龙血,54
3554,龙牙龙爪,56
3556,龙尾大回旋,58
3555,武神枪,60
7397,音速刺,62
7398,巨龙视线,66
7399,幻象冲,68
7400,死者之岸,70
16477,山境酷刑,72
16478,高跳,74
16479,龙眼雷电,76
16480,坠星冲,80
"""
"""
118,樱花怒放,体力逐渐减少
802,龙牙龙爪效果提高,可以发动龙牙龙爪
803,龙尾大回旋效果提高,可以发动龙尾大回旋
1243,幻象冲预备,可以发动幻象冲
1914,开膛枪,攻击所造成的伤害提高
1863,龙眼雷电预备,可以发动龙眼雷电
"""

a1 = Rectangle(10, 2)
a2 = Rectangle(15, 2)


def cnt_enemy(data: 'LogicData', ability):
    target, cnt = select(data, data.valid_enemies, ability)
    if not cnt: return data.target, 0
    if data.config['single'] == define.FORCE_SINGLE: return data.target, 1
    if data.config['single'] == define.FORCE_MULTI: return data.target, 3
    return target, cnt


def res_lv(data: 'LogicData'):
    match data.config['resource']:
        case define.RESOURCE_SQUAND:
            return 2
        case define.RESOURCE_NORMAL:
            return 1
        case define.RESOURCE_STINGY:
            return 0
        case _:
            return 1


combo_buff = {802, 803, 1863}
combo_lv = {75: 4, 78: 26, 87: 50}


def job_priority(data: 'LogicData', actor):
    if actor.job.is_dps:
        return 3, data.dps(actor)
    if actor.job.is_tank:
        return 2, data.dps(actor)
    if actor.job.is_healer:
        return 1, data.dps(actor)
    return 0, data.dps(actor)


class DragoonLogic(Strategy):
    name = "dragoon_logic"
    job = "Dragoon"

    default_data = {
        'jump_distance': 0,
    }

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> Tuple[int, int] | None:
        if action_id in {7398}:
            mo_target = api.get_mo_target()
            if mo_target: return action_id, mo_target.id

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        target, cnt = cnt_enemy(data, a1)
        has_next = set(data.effects.keys()).intersection(combo_buff) or data.me.level >= combo_lv.get(data.combo_id, 99)
        if data.me.level >= 40 and cnt and (cnt >= 3 or data.target_distance > 4 and not has_next):
            if data.combo_id == 7397 and data.me.level >= 72: return UseAbility(16477, target.id)
            if data.combo_id == 86 and data.me.level >= 62: return UseAbility(7397, target.id)
            return UseAbility(86, target.id)
        if data.target_distance > 4: return
        if 802 in data.effects: return UseAbility(3554)
        if 803 in data.effects: return UseAbility(3556)
        if data.combo_id == 78 and data.me.level >= 26: return UseAbility(84)
        if data.combo_id == 87 and data.me.level >= 50:
            return UseAbility(88)
        if (data.combo_id == 75 or data.combo_id == 16479) and data.me.level >= 4:
            if data.me.level >= 18:
                t = 11 if data.me.level >= 26 else 6
                if 1914 not in data.effects or data.effects[1914].timer < t:
                    return UseAbility(87)
                if data.me.level >= 50:
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if (118 not in t_effect or t_effect[118].timer < t) and data.time_to_kill_target > 15:
                        return UseAbility(87)
            return UseAbility(78)
        return UseAbility(75)

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if not res_lv(data): return
        if not (data[3553] or data.gauge.blood_or_life_ms) and data.gauge.stance != 2: return UseAbility(3553)
        if not data[83] and data.combo_id == (78 if data.me.level >= 26 else 75): return UseAbility(83)
        if not data[85] and (data.combo_id == 78 or data.combo_id == 87 or cnt_enemy(data, a1)[1] >= 3):
            return UseAbility(85)
        if not data[3557] and data[85] > 80:
            return UseAbility(3557)
        if not data[7398] and data[85]:
            members = [member for member in data.valid_party if (
                    member.current_mp and data.actor_distance_effective(member) <= 12 and member.id != data.me.id
            )]
            if not members:
                target = data.me
            else:
                target = max(members, key=lambda a: (job_priority(data, a), -data.actor_distance_effective(a)))
            return UseAbility(7398, target.id)
        jump_distance = data.config['jump_distance']
        if 1243 in data.effects: return UseAbility(7399)
        if not data[7400] and data.gauge.stance == 2: return UseAbility(7400)
        if data.target_distance <= jump_distance <= 20 and not data.ability_cnt:
            if not data[92]:
                data.ability_cnt += 1
                return UseAbility(92)
            if not data[96]:
                data.ability_cnt += 1
                return UseAbility(96)
            if not data[95]:
                data.ability_cnt += 1
                return UseAbility(95)
            if not data[16480] and data.gauge.stance == 2:
                data.ability_cnt += 1
                return UseAbility(16480)
        if not data[3555]: return UseAbility(3555)
