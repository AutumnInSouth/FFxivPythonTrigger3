from typing import TYPE_CHECKING
from threading import Lock
from FFxivPythonTrigger import plugins, wait_until
from RaidHelper.utils import map_trigger

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control import TargetIconEvent, TetherEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent

p4s = map_trigger(1009)

current_act = 0

"""
icon
301 aoe
302 靠近
303 分攤
"""

"""
tether
172:玩家連綫
173:boss 連綫
"""

icons = {}
last_icon = 0
icon_lock = Lock()


@p4s('点名收集', 'network/zone/server/actor_control/target_icon')
def p3s_target_icon(output, e: 'TargetIconEvent') -> None:
    global last_icon
    if 301 <= e.icon_id <= 303:
        with icon_lock:
            if last_icon < e.bundle_header.epoch - 1000:
                last_icon = e.bundle_header.epoch
                icons.clear()
            icons[e.target_id] = e.icon_id


tethers = []
last_tether = 0
tether_lock = Lock()


@p4s('連綫收集', 'network/zone/server/actor_control/tether')
def p3s_tether(output, e: 'TetherEvent') -> None:
    global last_tether
    if e.type == 172:
        with tether_lock:
            if last_tether < e.bundle_header.epoch - 1000:
                last_tether = e.bundle_header.epoch
                tethers.clear()
            tethers.append((e.target_id, e.source_id))
            if current_act == 2 and len(tethers) == 4:
                wait_until(lambda: len(icons) == 7 or None, 5)
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


@p4s('詠唱收集', 'network/zone/server/actor_cast')
def p3s_cast(output, e: 'ServerActorCastEvent') -> None:
    global current_act
    if e.struct_message.skill_type != 1: return
    match e.action_id:
        case 27148:
            current_act = 1
        case 28340:
            current_act = 2
        case 28341:
            current_act = 3
        case 28342:
            current_act = 4
        case 27187:
            current_act = 5
