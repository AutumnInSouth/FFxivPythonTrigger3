from time import time, perf_counter

from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.utils.shape import circle
from XivCombat.strategies import *
from .pvp_dmg_effects import source_dmg_modify

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.extra_messages.actor_add_remove_effect import ActorRemoveEffectEvent

def temp_red_hp(target, dmg):
    def func():
        target.hp -= dmg
        return True

    return func


class UseAbility(UseAbility):
    def __init__(self, ability_id: int, target=None, *args, dmg=0, **kwargs):
        if dmg: kwargs.setdefault('wait_until', temp_red_hp(target, dmg))
        super().__init__(ability_id, target.id if target else None, *args, **kwargs)
       # if target is not None and target != api.get_me_actor(): api.set_current_target(target)


class ThunderRecord:
    def __init__(self, max_damage: float, dot_damage: float, initial_damage: float):
        self.last_time = time()
        self.taken_damage = initial_damage
        self.max_damage = max_damage
        self.dot_damage = dot_damage

    def remain(self):
        dot_time = time() - self.last_time
        if dot_time > 15: return 0
        dot_damage = dot_time // 3 * self.dot_damage
        return self.max_damage - self.taken_damage - dot_damage


def thunder_remain(target_id):
    try:
        return thunder_records[target_id].remain()
    except KeyError:
        return 0


thunder_actions = {8861: (400, 8000, 400), 8860: (2400, 8000, 400), 18935: (200, 4000, 200), 18936: (1200, 4000, 200)}
thunder_records = {}
lb_skill_ids = {3360, 3361, 4249}


@event('network/zone/server/action_effect')
def blm_pvp_record_thunder(plugin, evt: 'ActionEffectEvent'):
    if evt.action_type != 'action' or evt.source_id != api.get_me_actor().id: return
    if evt.action_id in thunder_actions:
        base_dmg, max_dmg, dot_dmg = thunder_actions[evt.action_id]
    else:
        base_dmg, max_dmg, dot_dmg = 0, 0, 0
    for target_id, effects in evt.targets.items():
        new_buff = 0
        dmg = 0
        for effect in effects:
            if 'buff' in effect.tags and (effect.param == 2075 or effect.param == 1324):
                new_buff = effect.param
            elif 'ability' in effects:
                dmg += effect.param
        if new_buff:
            adjust = dmg / base_dmg
            thunder_records[target_id] = ThunderRecord(max_dmg, int(dot_dmg * adjust), dmg)
        elif dmg and target_id in thunder_records:
            thunder_records[target_id].taken_damage += dmg
            thunder_records[target_id].last_time = time()


@event('network/zone/server/effect_remove')
def blm_pvp_effect_remove(plugin, evt: 'ActorRemoveEffectEvent'):
    if evt.effect_id != 2075 and evt.effect_id != 1324 or evt.source_id != api.get_me_actor().id:
        return
    try:
        del thunder_records[evt.actor_id]
    except KeyError:
        pass


class BlmEnemy(object):
    def __init__(self, enemy, data: 'LogicData'):
        self.enemy = enemy
        self.effects = enemy.effects.get_dict(source=data.me.id)
        self.thunder = thunder_remain(self.enemy.id)
        self.hitbox = circle(enemy.pos.x, enemy.pos.y, 0.1)
        self.dis = data.actor_distance_effective(enemy)
        self.total_aoe = 0
        self.total_aoe_thunder = 0
        self.total_aoe_non_thunder = 0

    def cal_aoe_targets(self, enemies: list['BlmEnemy'], area=5):
        aoe_area = circle(self.enemy.pos.x, self.enemy.pos.y, area)
        for enemy in enemies:
            if aoe_area.intersects(enemy.hitbox):
                if enemy.thunder:
                    self.total_aoe_thunder += 1
                else:
                    self.total_aoe_non_thunder += 1
        self.total_aoe = self.total_aoe_thunder + self.total_aoe_non_thunder
        return self.total_aoe


def get_nearby_alliance(data: 'LogicData', target):
    return sum(target.absolute_distance_xy(a_m) < 10 for a_m in data.valid_alliance)


def get_nearby_enemy(data: 'LogicData', target):
    return sum(target.absolute_distance_xy(a_m) < 30 for a_m in data.valid_enemies)


def get_nearest_enemy_distance(data: 'LogicData', target):
    d = [target.absolute_distance_xy(a_m) < 30 for a_m in data.valid_enemies]
    return min(d) if d else 500


def get_enemy_data(data: 'LogicData', area=5):
    enemies = [BlmEnemy(enemy, data) for enemy in data.valid_enemies if data.actor_distance_effective(enemy) < (26 + area)]
    enemies_25 = [enemy for enemy in enemies if data.target_action_check(8858, enemy.enemy)]
    if not enemies_25: return [], [], []
    return enemies, enemies_25, [enemy for enemy in enemies_25 if enemy.cal_aoe_targets(enemies, area) > 1]


def aoe(data: 'LogicData'):
    if (data.me.current_mp >= 4000 and data.gauge.umbral_stacks > 0) or data.me.current_mp >= 10000:
        return 8866
    return 8867


def single(data: 'LogicData'):
    if data.me.current_mp >= 2000 and data.gauge.umbral_stacks > 0:
        return 8863
    if data.me.current_mp < 10000:
        return 8864


def get_buff(data: 'LogicData'):
    b = source_dmg_modify(data.effects)
    if data.gauge.umbral_stacks > 0:
        b *= 1.2
    return b * 0.95


class BlmPvpLogic(Strategy):
    name = 'ny/blm_pvp'
    job = 'BlackMage_pvp'

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> Tuple[int, int] | None:
        if action_id == 8869:
            move_targets = [member for member in data.valid_party if member.id != data.me.id and
                            data.actor_distance_effective(member) < 26 and data.target_action_check(8869, member)]
            if move_targets:
                _move_targets = [member for member in move_targets if get_nearby_alliance(data, member) > 4]
                if _move_targets: move_targets = _move_targets
                # move_target = max(move_targets, key=lambda target: get_nearest_enemy_distance(data, target))
                move_target = min(move_targets, key=lambda target: (get_nearby_enemy(data, target), - get_nearest_enemy_distance(data, target)))
                if get_nearest_enemy_distance(data, move_target) < get_nearest_enemy_distance(data, data.me):
                    return action_id, data.me.id
                return action_id, move_target.id
        elif action_id == 17775:
            enemies, enemies_25, enemies_25_aoe = get_enemy_data(data)
            if enemies_25:
                target = max(enemies_25_aoe, key=lambda x: x.total_aoe) if enemies_25_aoe else min(enemies_25, key=lambda x: x.dis)
                return 17775, target.enemy.id
        elif action_id == 3361:
            enemies, enemies_25, enemies_25_aoe = get_enemy_data(data, 8)
            if enemies_25:
                target = max(enemies_25_aoe, key=lambda x: x.total_aoe) if enemies_25_aoe else min(enemies_25, key=lambda x: x.enemy.current_hp)
                return 3361, target.enemy.id

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if data.me.current_hp / data.me.max_hp <= 0.7 and data[18943] <= 30:
            data.me.current_hp += 3000
            return UseAbility(18943, data.me)
        enemies, enemies_25, enemies_25_aoe = get_enemy_data(data)
        if not enemies_25: return
        has_speed = 1987 in data.effects or 20 > data.pvp_skill_cd(17685) > 14
        if data.gauge.foul_count:
            kill_line = 2400 * get_buff(data)
            kill_line_targets = [enemy for enemy in enemies_25 if enemy.enemy.current_hp < kill_line and enemy.enemy.type == 'player']
            if kill_line_targets: return UseAbility(17774, max(kill_line_targets, key=lambda x: x.enemy.current_hp).enemy)
        if enemies_25_aoe and data.gauge.umbral_stacks > 0:
            if 1365 in data.effects and not has_speed:
                aoe_target = max(enemies_25_aoe, key=lambda x: (x.total_aoe, x.total_aoe_non_thunder))
                if aoe_target.total_aoe > (2 if data.effects[1365].timer > 5 else 1):
                    return UseAbility(18936, aoe_target.enemy)
            enemies_25_thunder = [enemy for enemy in enemies_25_aoe if enemy.total_aoe_thunder]
            if enemies_25_thunder:
                aoe_target = max(enemies_25_thunder, key=lambda x: x.total_aoe)
                if data.gauge.foul_count > 1:
                    return UseAbility(8865, aoe_target.enemy)
                if not data.pvp_skill_cd(17685) and data.me.current_mp >= 4000 and aoe_target.total_aoe > 2:
                    return UseAbility(17685, ability_type=AbilityType.oGCD)
                if has_speed: return UseAbility(aoe(data), aoe_target.enemy)
                if data.gauge.foul_count and aoe_target.total_aoe > 3:
                    return UseAbility(8865, aoe_target.enemy)
            aoe_target = max(enemies_25_aoe, key=lambda x: (x.total_aoe_non_thunder, x.total_aoe))
            if has_speed:
                return UseAbility(aoe(data), aoe_target.enemy)
            if aoe_target.total_aoe_non_thunder > 1 and data.gauge.umbral_ms > 3000:
                return UseAbility(18935, aoe_target.enemy)
            if not data.is_moving:
                enemies_20_aoe = [enemy for enemy in enemies if enemy.dis < 23]
                if enemies_20_aoe:
                    aoe_target = max(enemies_20_aoe, key=lambda x: (x.total_aoe_thunder, x.total_aoe))
                    return UseAbility(aoe(data), aoe_target.enemy)
        target_with_thunder = [enemy for enemy in enemies_25 if enemy.thunder > 3]
        single_target = min(target_with_thunder if target_with_thunder else enemies_25, key=lambda x: x.enemy.current_hp)
        if has_speed:
            return UseAbility((single(data) or 8864) if data.gauge.umbral_stacks else aoe(data), single_target.enemy)
        if 1365 in data.effects and data.effects[1365].timer < 5:
            return UseAbility(8861, single_target.enemy)
        if not (target_with_thunder or data.gauge.umbral_ms < 3000) and enemies_25_aoe:
            return UseAbility(18935, max(enemies_25_aoe, key=lambda x: (x.total_aoe_non_thunder, x.total_aoe)).enemy)
        if not data.is_moving and data.gauge.umbral_ms > 3000:
            t = single(data)
            if t: return UseAbility(t, single_target.enemy)
        if not data[17775]:
            for enemy in enemies_25:
                if enemy.enemy.cast_info.action_id in lb_skill_ids:
                    return UseAbility(17775, enemy.enemy, ability_type=AbilityType.oGCD)
        change_line = 6000 if enemies_25_aoe and (data.gauge.foul_count or not data.pvp_skill_cd(17685)) else 10000
        if (data.me.current_mp >= 4000 and data.gauge.umbral_stacks > 0) or data.me.current_mp >= change_line:
            return UseAbility(8858, single_target.enemy)
        return UseAbility(8859, single_target.enemy)
