import math
from functools import cache

from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Sector, FarCircle

spread_shot = Sector(12, math.radians(120))  # 定义gcd aoe的范围，12为半径，math.radians(120)为角度
ricochet = FarCircle(25, 5)  # 定义弹射的aoe范围，25距离的5半径圆形


@cache
def mch_special_gcd(lv: int, cd_only: bool = True):
    """
    当cd_only为真，根据等级获取那些技能需要使用整备
    当cd_only为假，根据等级获取超荷需要等待那些技能避免重叠时间
    """
    ans = []
    if lv >= 58:
        ans.append(a('钻头'))
        if lv >= 76:
            ans.append(a('空气锚'))
            if lv >= 90:
                ans.append(a('Chain Saw'))
        elif cd_only:
            ans.append(a('热弹'))
    elif lv >= 26 and not cd_only:
        ans.append(a('狙击弹'))
    else:
        ans.append(a('热弹'))
    return ans


def special_gcd(data: 'LogicData', action_id: int, target_id: int):
    """
    处理可能需要整备的技能
    """
    # 当技能id属于”需要使用整备“的技能，以及整备有充能时
    if action_id in mch_special_gcd(data.me.level, False) and data[a('整备')] <= 55:
        # 返回使用整备而不是原技能
        return UseAbility(
            a('整备'), data.me.id,
            ability_type=define.AbilityType.oGCD,
            wait_until=lambda: s('整备') in data.refresh_cache('effects')
        )
    # 否则返回原技能
    return UseAbility(action_id, target_id)


class MachinistLogic(Strategy):
    name = 'ny/mch_logic'
    job = 'Machinist'

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        """
        这个函数返回使用的gcd技能，或者优先级更高的能力技
        """
        if data.target_distance <= 25:  # 如果预设目标在有效范围内
            single_target = data.target  # 选取该目标为单体攻击目标
        else:
            # 根据距离从所有可以被'分裂弹'攻击的敌人里面选取一个最近的目标
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('分裂弹')))
            # 如果这个目标的距离依然大于25，则返回空（不使用技能）
            if data.actor_distance_effective(single_target) > 25: return

        if data.me.level >= 18:  # 如果等级大于18
            aoe_target, aoe_cnt = cnt_enemy(data, spread_shot)  # 获取aoe攻击目标和数量
        else:
            aoe_target, aoe_cnt = single_target, 0  # 否则为 0 个可以被攻击的目标

        if res_lv(data):  # 这里是一个查询设置类函数，查询应不应该使用特殊技能（使用资源）
            if data.gcd >= data[a('钻头')]:  # 如果gcd大于钻头的冷却时间
                # 对单体目标使用钻头,或者当aoe目标数量大于3并且可以使用毒菌时，对aoe目标使用毒菌
                if aoe_cnt < 3 or data.me.level < 72:
                    return special_gcd(data, a('钻头'), single_target.id)
                else:
                    return UseAbility(a('毒菌冲击'), aoe_target.id)
            # 热弹和空气锚虽然是替代技能，但是冷却组不是同一个，得做分别处理 （fxxk se）
            hot_shot = a('热弹') if data.me.level < 76 else a('空气锚')
            if data.gcd >= data[hot_shot]:  # 如果gcd大于空气锚的冷却时间
                return special_gcd(data, hot_shot, single_target.id)  # 对单体目标使用空气锚
            if data.gcd >= data[a('Chain Saw')]:  # 如果gcd大于链锯的冷却时间
                return special_gcd(data, a('Chain Saw'), single_target.id)  # 对单体目标使用链锯

        if aoe_cnt < 3 or data.me.level < 18:  # 如果aoe目标数量少于3或者就不能打aoe（未解锁扫射）
            if data.gauge.overheat_ms and data.skill_unlocked(a('热冲击')):  # 如果人在过热（根据gauge读取） 以及热冲击已经被解锁
                return UseAbility(a('热冲击'), single_target.id)  # 对单体目标使用热冲击
            if data.combo_id == a('分裂弹') and data.me.level >= 2:  # 如果上一个combo技能是分裂弹，以及可以使用 独头弹
                return UseAbility(a('独头弹'), single_target.id)  # 对单体目标使用独头弹
            if data.combo_id == a('独头弹') and data.me.level >= 26:  # 如果上一个combo技能是独头弹，以及可以使用 狙击弹
                return special_gcd(data, a('狙击弹'), single_target.id)  # 对单体目标使用狙击弹
            return UseAbility(a('分裂弹'), single_target.id)  # 对单体目标使用分裂弹
        else:
            if data.gauge.overheat_ms and data.skill_unlocked(a('自动弩')):  # 如果人在过热（根据gauge读取） 以及自动弩已经被解锁
                return data.use_ability_to_target(a('自动弩'), aoe_target.id)  # 对aoe目标使用自动弩
            else:
                return data.use_ability_to_target(a('散射'), aoe_target.id)  # 对aoe目标使用散射

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        """
        这个函数返回使用的能力技
        """
        if not res_lv(data): return  # 如果需要存资源，就不使用任何能力技

        if data.target_distance <= 25:  # 如果预设目标在有效范围内
            single_target = data.target  # 选取该目标为单体攻击目标
        else:
            # 根据距离从所有可以被'分裂弹'攻击的敌人里面选取一个最近的目标
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('分裂弹')))
            # 如果这个目标的距离依然大于25，则返回空（不使用技能）
            if data.actor_distance_effective(single_target) > 25: return

        ricochet_cd = data[a('弹射')]  # 预存弹射的cd
        gauss_round_cd = data[a('虹吸弹')]  # 预存虹吸弹的cd
        if data.me.level < 74:  # 在储能升级未解锁前，cd从一层开始计算 （fxxk se）
            ricochet_cd -= 30
            gauss_round_cd -= 30

        if min(ricochet_cd, gauss_round_cd) < 15:  # 如果弹射或者虹吸弹快冷却好了（这里是防止过热期间溢出所以提高优先级）
            if gauss_round_cd <= ricochet_cd:  # 哪个cd短返回使用哪个
                return UseAbility(a('虹吸弹'), single_target.id)  # 对单体目标使用虹吸弹
            else:
                # 对aoe目标使用弹射 （cnt_enemy返回的第一个值就是敌人）
                return UseAbility(a('弹射'), cnt_enemy(data, ricochet)[0].id)

        if data.gauge.battery >= 90:  # 如果电量快溢出了
            return UseAbility(a('车式浮空炮塔'), single_target.id)  # 召唤炮塔、机器人

        if data.gauge.heat >= 50 and not data[a('超荷')] and (  # 如果热量大于50，并且超荷可以使用并且
                not data.skill_unlocked(a('热冲击')) or  # 热冲击没有解锁 或
                max(data[action] for action in mch_special_gcd(data.me.level, True)) > 8  # 需要等待级技能都要大于持续时间的cd
        ):
            wild_fire_cd = data[a('野火')]  # 预存野火的cd
            if not wild_fire_cd and not data.ability_cnt:  # 如果野火可以使用并且是第一个能力技
                return UseAbility(a('野火'), single_target.id)  # 对单体目标使用野火
            if wild_fire_cd > 8:  # 如果野火快好了就等好了才过热
                if data.ability_cnt and data.gcd > 1.3:  # 如果不是第一个能力技，但是gcd还没过半，先等着别开过热
                    return
                elif data.gcd <= 1.3:  # gcd过半，开冲
                    return UseAbility(a('超荷'), data.me.id)  # 使用超荷
        if data.gauge.heat < 50 and not data[a('枪管加热')]:  # 如果热量低于50并且加热好了
            return UseAbility(a('枪管加热'), data.me.id)  # 加热，请微波炉高温一分钟

        if min(ricochet_cd, gauss_round_cd) <= 60:  # 如果弹射或者虹吸弹有层数
            if gauss_round_cd <= ricochet_cd:  # 哪个cd短返回使用哪个
                return UseAbility(a('虹吸弹'), single_target.id)  # 对单体目标使用虹吸弹
            else:
                # 对aoe目标使用弹射 （cnt_enemy返回的第一个值就是敌人）
                return UseAbility(a('弹射'), cnt_enemy(data, ricochet)[0].id)

        if data.gauge.battery >= 50:  # 如果可以拉小机器人了
            return UseAbility(a('车式浮空炮塔'), single_target.id)  # 叫帮手，揍他
