from time import time, perf_counter

from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.utils.shape import circle
from XivCombat.strategies import *
from .pvp_dmg_effects import source_dmg_modify, target_dmg_modify

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.extra_messages.actor_add_remove_effect import ActorRemoveEffectEvent

a = {
    '微型陨石': 3361,
    '火炎': 8858,
    '冰结': 8859,
    '闪雷': 8860,
    '暴雷': 8861,
    '天语': 8862,
    '炽炎': 8863,
    '冰澈': 8864,
    '秽浊': 8865,
    '核爆': 8866,
    '玄冰': 8867,
    '以太步': 8869,
    '制导': 9971,
    '吸取': 17683,
    '幻影弹': 17684,
    '即刻咏唱': 17685,
    '昏乱': 17686,
    '魔罩': 17687,
    '异言': 17774,
    '夜翼': 17775,
    '震雷': 18935,
    '霹雷': 18936,
    '疾跑': 18942,
    '军用恢复药': 18943,
    '以太爆发': 18956,
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
