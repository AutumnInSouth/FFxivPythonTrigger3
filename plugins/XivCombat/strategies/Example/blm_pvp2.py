from time import time, perf_counter

from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.utils.shape import circle
from XivCombat.strategies import *
from .pvp_dmg_effects import source_dmg_modify, target_dmg_modify

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.extra_messages.actor_add_remove_effect import ActorRemoveEffectEvent

a = {
    '微型陨石': 3361, '火炎': 8858, '冰结': 8859, '闪雷': 8860, '暴雷': 8861,
    '天语': 8862, '炽炎': 8863, '冰澈': 8864, '秽浊': 8865, '核爆': 8866,
    '玄冰': 8867, '以太步': 8869, '制导': 9971, '吸取': 17683, '幻影弹': 17684,
    '即刻咏唱': 17685, '昏乱': 17686, '魔罩': 17687, '异言': 17774, '夜翼': 17775,
    '震雷': 18935, '霹雷': 18936, '疾跑': 18942, '军用恢复药': 18943, '以太爆发': 18956,
}

thunder_actions = {a['暴雷']: (400, 8000, 400), a['闪雷']: (2400, 8000, 400), a['震雷']: (200, 4000, 200), a['霹雷']: (1200, 4000, 200)}
thunder_records = {}
lb_skill_ids = {3360, 3361, 4249}


def temp_red_hp(target, dmg, cb=None):
    c = 0
    if cb is None:
        def func():
            target.hp -= dmg
            return True
    else:
        def func():
            nonlocal c
            if c:
                target.hp -= dmg
                c += 1
            return cb()
    return func


class UseAbility(UseAbility):
    def __init__(self, ability_id: int, target=None, *args, dmg=0, **kwargs):
        if dmg: kwargs['wait_until'] = temp_red_hp(target, dmg, kwargs.get('wait_until'))
        super().__init__(ability_id, target.id if target else None, *args, **kwargs)
        if target is not None and target != api.get_me_actor(): api.set_current_target(target)


class BlmEnemy(object):
    def __init__(self, enemy, data: 'LogicData'):
        self.enemy = enemy
        self.effects = enemy.effects.get_dict(source=data.me.id)
        try:
            self.thunder = thunder_records[self.enemy.id].remain()
        except KeyError:
            self.thunder = 0
        self.hitbox = circle(enemy.pos.x, enemy.pos.y, 0.1)
        self.dmg_modify = target_dmg_modify(self.enemy)
        self.effective_hp = self.enemy.current_hp/self.dmg_modify
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
