from XivCombat.utils import a, s, cnt_enemy, res_lv, find_area_belongs_to_me
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Rectangle, NearCircle, circle, FarCircle
from .utils import mo_provoke_and_shirk

unleash = NearCircle(5.)
flood_of_darkness = Rectangle(10, 2)
abyssal_drain = FarCircle(20, 5)


class DarkKnightStrategy(Strategy):
    name = 'ny/dk'
    job = 'DarkKnight'

    @mo_provoke_and_shirk
    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        if action_id == a('至黑之夜') or action_id == a('Oblation'):
            mo_entity = api.get_mo_target()
            if mo_entity and api.action_type_check(action_id, mo_entity):
                return UseAbility(action_id, mo_entity.id)

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 3:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('伤残')))
            if not single_target: return
            if data.actor_distance_effective(single_target) > 5:
                return UseAbility(a('伤残'), single_target.id) if not data.gcd and data.me.level >= 15 else None

        if data.me.level >= 6:
            unleash_target, unleash_cnt = cnt_enemy(data, unleash)
        else:
            unleash_target, unleash_cnt = data.me, 0
        delirium = s('血乱') in data.effects
        if (data.gauge.blood >= 50 or delirium) and data[a('掠影示现')]:
            res = res_lv(data)
            next_gain = 20 if data.combo_id == a('吸收斩') or data.combo_id == a('释放') and data.me.level >= 72 else 0
            if s('嗜血') in data.effects and data.me.level >= 66: next_gain += 10
            if res and (delirium or res > 1 or data[a('嗜血')] > 40 or data.gauge.blood + next_gain > 100):
                if data.me.level >= 64 and unleash_cnt > 2:
                    return UseAbility(a('寂灭'), unleash_target.id)
                elif data.actor_distance_effective(single_target) <= 3:
                    return UseAbility(a('血溅'), single_target.id)

        if data.combo_id == a('释放') and data.me.level >= 72 and unleash_cnt:
            return UseAbility(a('刚魂'), data.me.id)
        if unleash_cnt > 2: return UseAbility(a('释放'), data.me.id)

        if data.actor_distance_effective(single_target) > 3: return

        if data.me.level >= 26 and data.combo_id == a('吸收斩'):
            return UseAbility(a('噬魂斩'), single_target.id)
        if data.me.level >= 2 and data.combo_id == a('重斩'):
            return UseAbility(a('吸收斩'), single_target.id)
        return UseAbility(a('重斩'), single_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 3:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST)
            if data.actor_distance_effective(single_target) > 5: return

        res = res_lv(data)
        flood_of_darkness_target, flood_of_darkness_cnt = None, -1
        if (data.gauge.dark_art or data.me.current_mp > 3000 and data.skill_unlocked(a('暗黑波动')) and
                (data.gauge.darkside_timer < 3 or res and data.me.current_mp > (6000 if data[a('至黑之夜')] < 13 else 3000))):
            flood_of_darkness_target, flood_of_darkness_cnt = cnt_enemy(data, flood_of_darkness)
            old_mp = data.me.current_mp
            if data.skill_unlocked(a('暗黑锋')) and flood_of_darkness_cnt < 3:
                if data.actor_distance_effective(single_target) <= 3:
                    return UseAbility(a('暗黑锋'), single_target.id, wait_until=lambda : data.me.current_mp < old_mp)
            else:
                return UseAbility(a('暗黑波动'), flood_of_darkness_target.id, wait_until=lambda : data.me.current_mp < old_mp)
        if not res: return
        # data.plugin.logger(data.effect_time(s('腐秽大地')))
        if data.me.level >= 86 and not data[a('Salt and Darkness')] and data.effect_time(s('腐秽大地')):
            area = find_area_belongs_to_me(data)
            if area:
                area = circle(area.pos.x, area.pos.y, 5)
                if sum(area.intersects(enemy.hitbox()) for enemy in data.valid_enemies) > int(len(data.enemy_can_attack_by(a('伤残')))) * 0.75:
                    return UseAbility(a('Salt and Darkness'), data.me.id)
        if not data[a('嗜血')]:
            return UseAbility(a('嗜血'), data.me.id)
        if not data[a('血乱')] and data[a('掠影示现')]:
            return UseAbility(a('血乱'), data.me.id)
        if not data[a('掠影示现')] and data.gauge.blood >= 50:
            return UseAbility(a('掠影示现'), data.me.id)
        if not data[a('吸血深渊')]:
            abyssal_drain_target, abyssal_drain_cnt = cnt_enemy(data, abyssal_drain)
            if data.skill_unlocked(a('精雕怒斩')) and abyssal_drain_cnt < 3:
                if data.actor_distance_effective(single_target) <= 3:
                    return UseAbility(a('精雕怒斩'), single_target.id)
            else:
                return UseAbility(a('吸血深渊'), abyssal_drain_target.id)
        if not data[a('腐秽大地')]:
            unleash_target, unleash_cnt = cnt_enemy(data, unleash)
            if unleash_cnt > int(len(data.enemy_can_attack_by(a('伤残')))) / 2:
                return UseAbility(a('腐秽大地'), data.me.id)
        if data[a('Shadowbringer')] < 60 and data.gauge.darkside_timer:
            if flood_of_darkness_cnt < 0:
                flood_of_darkness_target, flood_of_darkness_cnt = cnt_enemy(data, flood_of_darkness)
            if flood_of_darkness_cnt:
                return UseAbility(a('Shadowbringer'), flood_of_darkness_target.id)
        if data.me.level >= 78 and not data.actor_distance_effective(single_target) and data[a('跳斩')] < 5:
            return UseAbility(a('跳斩'), single_target.id)
