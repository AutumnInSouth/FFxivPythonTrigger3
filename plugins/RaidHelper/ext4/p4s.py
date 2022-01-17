import math
from ctypes import byref
from typing import TYPE_CHECKING
from threading import Lock
from FFxivPythonTrigger import plugins, wait_until
from FFxivPythonTrigger.exceptions import PluginNotFoundException
from RaidHelper.utils import map_trigger, common_trigger

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control import TargetIconEvent, TetherEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent

p4s = map_trigger(1009)

current_act = 0


def add_omen(source_actor, target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier: int = 0):
    try:
        plugins.OmenReflect.add_omen(byref(source_actor), target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier)
        return True
    except PluginNotFoundException:
        return False


"""
icon
300 塔
301 aoe
302 靠近
303 分攤
"""

"""
tether
165:以太操作
172:玩家連綫
173:boss 連綫
"""

icons = {}
last_icon = 0
icon_lock = Lock()

fire_aoe_omn = 1, 2, 20
tower_aoe_omn = 90, 2, 4


@p4s('点名收集', 'network/zone/server/actor_control/target_icon')
def p4s_target_icon(output, e: 'TargetIconEvent') -> None:
    global last_icon
    if 300 <= e.icon_id <= 303:
        with icon_lock:
            if last_icon < e.bundle_header.epoch - 500:
                last_icon = e.bundle_header.epoch
                icons.clear()
            icons[e.target_id] = e.icon_id
            if current_act == 4 and len(icons) == 8:
                process_act4_icons(output)


aether_tether_lock = Lock()

tethers = []
last_tether = 0
tether_lock = Lock()

boss_tethers = []
last_boss_tether = 0
boss_tether_lock = Lock()


@p4s('連綫收集', 'network/zone/server/actor_control/tether')
def p4s_tether(output, e: 'TetherEvent') -> None:
    global last_tether, last_boss_tether
    if e.type == 165:
        with aether_tether_lock:
            if e.target_id in pinax_actor:
                del pinax_actor[e.target_id]
                if len(pinax_actor) == 1:
                    process_safe_pinax(output)
    elif e.type == 172:
        with tether_lock:
            if last_tether < e.bundle_header.epoch - 500:
                last_tether = e.bundle_header.epoch
                tethers.clear()
            tethers.append((e.target_id, e.source_id))
            if current_act == 2 and len(tethers) == 4:
                wait_until(lambda: len(icons) == 7 or None, 5)
                process_act2_tethers(output)
    elif e.type == 173:
        with boss_tether_lock:
            actor = e.target_actor
            boss_tethers.append(actor)
            boss_tethers_cnt = len(boss_tethers)
            if current_act == 1:
                add_omen(actor, (actor.pos.x, actor.pos.y, actor.pos.z), 0,
                         *(fire_aoe_omn if boss_tethers_cnt <= 2 or boss_tethers_cnt >= 11 else tower_aoe_omn))
                if boss_tethers_cnt == 2:
                    process_act1_boss_tethers(output)
            elif current_act == 2:
                add_omen(actor, (actor.pos.x, actor.pos.y, actor.pos.z), 0,
                         *(fire_aoe_omn if (actor_pos(actor)[1] + 180) % 90 > 45 else tower_aoe_omn))
                if boss_tethers_cnt == 4:
                    process_act2_boss_tethers(output)
            elif current_act == 3 and len(boss_tethers) == 1:
                process_act3_boss_tethers(output)


acts = {
    27148: 1,
    28340: 2,
    28341: 3,
    28342: 4,
    28343: 5,
    27190: 6,
}

pinax = {
    27092: '毒',
    27125: '毒',
    27129: '毒',
    27196: '毒',
    27093: '火',
    27126: '火',
    27130: '火',
    27197: '火',
    27095: '雷',
    27128: '雷',
    27132: '雷',
    27199: '雷',
    27094: '水',
    27127: '水',
    27131: '水',
    27198: '水',
}

pinax_actor = {}
safe_pinax = None


@p4s('詠唱收集', 'network/zone/server/actor_cast')
def p4s_cast(output, e: 'ServerActorCastEvent') -> None:
    global current_act
    if e.struct_message.skill_type != 1: return
    if e.action_id in acts:
        current_act = acts[e.action_id]
        boss_tethers.clear()
    elif e.action_id in pinax:
        pinax_type = pinax[e.action_id]
        pinax_actor[e.source_id] = pinax_type
        if safe_pinax == pinax_type:
            process_safe_pinax_pos(output, e.source_actor)


@p4s('p4s重置', 'network/zone/server/combat_reset')
def p4s_reset(output, e):
    global current_act
    current_act = 0
    icons.clear()
    tethers.clear()
    boss_tethers.clear()
    pinax_actor.clear()


def actor_pos(actor):
    """
    return distance and angle sep of actor by actor_id with center of 100,100
    """
    x, y = actor.pos.x, actor.pos.y
    return ((x - 100) ** 2 + (y - 100) ** 2) ** 0.5, math.degrees(math.atan2(100 - x, 100 - y))


def process_safe_pinax(output):
    global safe_pinax
    safe_pinax = list(pinax_actor.values())[0]
    output(f"安全地板：{safe_pinax}")


def process_safe_pinax_pos(output, source_actor):
    global safe_pinax
    deg = actor_pos(source_actor)[1]
    if deg < -90:
        output(f"安全地板：東南({safe_pinax})")
    elif deg < 0:
        output(f"安全地板：東北({safe_pinax})")
    elif deg < 90:
        output(f"安全地板：西北({safe_pinax})")
    else:
        output(f"安全地板：西南({safe_pinax})")
    safe_pinax = None


def process_act1_boss_tethers(output):
    if abs(boss_tethers[0].pos.x - boss_tethers[1].pos.x) < 5:
        output("一運安全點：先東西，後南北")
    else:
        output("一運安全點：先南北，後東西")


def process_act2_boss_tethers(output):
    if any(-20 < actor_pos(actor)[1] < 0 for actor in boss_tethers):
        output("二運安全點：先東西，後南北")
    else:
        output("二運安全點：先南北，後東西")


def process_act3_boss_tethers(output):
    if actor_pos(boss_tethers[0])[1] < 0:
        output("三運：先東邊踩塔，後西邊踩塔")
    else:
        output("三運：先西邊踩塔，后東邊踩塔")


def process_act2_tethers(output):
    for a1_id, a2_id in tethers:
        a1 = plugins.XivMemory.actor_table.get_actor_by_id(a1_id)
        a2 = plugins.XivMemory.actor_table.get_actor_by_id(a2_id)
        if icons.get(a1_id) == 301 or icons.get(a2_id) == 301:
            output(f"AOE: {a1.job.short_name} - {a2.job.short_name}")
        elif icons.get(a1_id) == 302 or icons.get(a2_id) == 302:
            output(f"靠近: {a1.job.short_name} - {a2.job.short_name}")
        elif icons.get(a1_id) == 303 or icons.get(a2_id) == 303:
            output(f"分攤: {a1.job.short_name} - {a2.job.short_name}")
        else:
            output(f"未知: {a1.job.short_name} - {a2.job.short_name}")


def process_act4_icons(output):
    tower = [aid for aid, icon in icons.items() if icon == 300]
    aoe = [aid for aid, icon in icons.items() if icon == 301]
    tower_names = ','.join(plugins.XivMemory.actor_table.get_actor_by_id(aid).job.short_name for aid in tower)
    aoe_names = ','.join(plugins.XivMemory.actor_table.get_actor_by_id(aid).job.short_name for aid in aoe)
    output(f"塔: {tower_names}")
    output(f"AOE: {aoe_names}")
