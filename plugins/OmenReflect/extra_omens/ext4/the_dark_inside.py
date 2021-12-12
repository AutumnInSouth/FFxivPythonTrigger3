import math
from threading import Lock
from typing import TYPE_CHECKING
from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.decorator import event
from ..utils import add_omen, remove_omen

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent
    from XivNetwork.message_processors.zone_server.map_effect import ServerMapEffectEvent
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent

astral_flow_right = {26159, 26210, 28361}
astral_flow_left = {26160, 26211, 26565, 26591}
paradeigma = {26559, 26568}
paradeigma_act = {26566, 26567, 26593, 26594, 26595}
names = {'Zodiark'}
map_id = 993
left_bottom = 90, 110, 0
right_bottom = 110, 110, 0
left_top = 90, 90, 0
right_top = 110, 90, 0

python_left = ((85, 120, 0), math.pi), ((105, 120, 0), math.pi)
python_right = ((95, 120, 0), math.pi), ((115, 120, 0), math.pi)
python_top = ((120, 85, 0), -math.pi / 2), ((120, 105, 0), -math.pi / 2)
python_bottom = ((120, 95, 0), -math.pi / 2), ((120, 115, 0), -math.pi / 2)

behemoth = 1, 2, 15
quetzalcoatl = 12, 2, 15
python = 2, 12, 42, 11
select_lock = Lock()

selected = []
current = []
draw_rotate_map = {
    0x0F: (0x12, 0x11),
    0x0D: (0x12, 0x11),
    0x10: (0x11, 0x12),
    0x0E: (0x11, 0x12),
    0x11: (0x0F, 0x10),
    0x13: (0x0F, 0x10),
    0x12: (0x10, 0x0F),
    0x14: (0x10, 0x0F),
    0x16: (0x15, 0x18),
    0x18: (0x16, 0x17),
    0x17: (0x18, 0x15),
    0x15: (0x17, 0x16),
    0x0A: (0x09, 0x0C),
    0x0C: (0x0A, 0x0B),
    0x0B: (0x0C, 0x09),
    0x09: (0x0B, 0x0A),
}


def get_can_use_actor():
    with select_lock:
        for actor in plugins.XivMemory.actor_table:
            if actor.type != 'battle_npc': continue
            if actor.name in names and actor not in selected and not actor.can_select:
                selected.append(actor)
                return actor


def clear():
    with select_lock:
        if selected:
            for actor in selected:
                try:
                    remove_omen(actor)
                except:
                    pass
            selected.clear()


@event('network/zone/server/actor_cast')
def actor_cast(plugin, evt: 'ServerActorCastEvent'):
    if plugins.XivMemory.zone_id != map_id: return
    if evt.action_id in paradeigma:
        clear()
        current.clear()
    is_left = evt.action_id in astral_flow_left
    is_right = evt.action_id in astral_flow_right
    if is_left or is_right:
        clear()
        for i in range(len(current)):
            new = draw_rotate_map[current[i]][0 if is_left else 1]
            current[i] = new
            draw(new)


@event('network/zone/server/action_effect')
def action_effect(plugin, evt: 'ActionEffectEvent'):
    if evt.action_type == 'action' and evt.action_id in paradeigma_act:
        clear()


@event('network/zone/server/map_effect')
def map_effect(plugin, evt: 'ServerMapEffectEvent'):
    if plugins.XivMemory.zone_id != map_id: return
    msg = evt.struct_message
    if msg.param2 == 0x00200010 and draw(msg.param3):
        #plugin.logger(f'{msg.param3}')
        current.append(msg.param3)


def draw(param):
    match param:
        case 0x0F | 0x0D:  # 蛇左半场
            for pos, facing in python_left: add_omen(get_can_use_actor(), pos, facing, *python)
        case 0x10 | 0x0E:  # 蛇右半场
            for pos, facing in python_right: add_omen(get_can_use_actor(), pos, facing, *python)
        case 0x11 | 0x13:  # 蛇上半场
            for pos, facing in python_top: add_omen(get_can_use_actor(), pos, facing, *python)
        case 0x12 | 0x14:  # 蛇下半场
            for pos, facing in python_bottom: add_omen(get_can_use_actor(), pos, facing, *python)
        case 0x16:  # 右上月环
            add_omen(get_can_use_actor(), right_top, 0, *quetzalcoatl)
        case 0x18:  # 右下月环
            add_omen(get_can_use_actor(), right_bottom, 0, *quetzalcoatl)
        case 0x15:  # 左上月环
            add_omen(get_can_use_actor(), left_top, 0, *quetzalcoatl)
        case 0x17:  # 左下月环
            add_omen(get_can_use_actor(), left_bottom, 0, *quetzalcoatl)
        case 0x0A:  # 右上钢铁
            add_omen(get_can_use_actor(), right_top, 0, *behemoth)
        case 0x0C:  # 右下钢铁
            add_omen(get_can_use_actor(), right_bottom, 0, *behemoth)
        case 0x09:  # 左上钢铁
            add_omen(get_can_use_actor(), left_top, 0, *behemoth)
        case 0x0B:  # 左下钢铁
            add_omen(get_can_use_actor(), left_bottom, 0, *behemoth)
        case _:
            return False
    return True


events = {
    'actor_cast': actor_cast,
    'map_effect': map_effect,
    'action_effect': action_effect,
}
