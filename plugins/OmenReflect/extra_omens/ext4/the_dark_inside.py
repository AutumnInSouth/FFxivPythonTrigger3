import math
from threading import Lock
from typing import TYPE_CHECKING
from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.utils import wait_until
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

python_left = ((85, 121, 0), math.pi), ((105, 121, 0), math.pi)
python_right = ((95, 121, 0), math.pi), ((115, 121, 0), math.pi)
python_top = ((121, 85, 0), -math.pi / 2), ((121, 105, 0), -math.pi / 2)
python_bottom = ((121, 95, 0), -math.pi / 2), ((121, 115, 0), -math.pi / 2)

fire_side = ((100, 100, 0), -math.pi / 2), ((100, 100, 0), math.pi / 2)
fire_front = ((100, 100, 0), math.pi), ((100, 100, 0), 0)

behemoth = 1, 2, 15  # 15半径钢铁
quetzalcoatl = 12, 2, 15  # 外15内5月环
python = 2, 12, 42, 11  # 42长11宽矩形
fire = 4, 2, 30  # 30半径90度扇形
select_lock = Lock()

selected = []
current = []
prev_rotate_left: list = [None]
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
        raise RuntimeError('No actor found')


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
        prev_rotate_left[0] = None
    is_left = evt.action_id in astral_flow_left
    is_right = evt.action_id in astral_flow_right
    if is_left or is_right:
        clear()
        prev_rotate_left[0] = is_left
        for i in range(len(current)):
            new = draw_rotate_map[current[i]][0 if is_left else 1]
            current[i] = new
            draw(new)


@event('network/zone/server/action_effect')
def action_effect(plugin, evt: 'ActionEffectEvent'):
    if evt.action_type == 'action' and evt.action_id in paradeigma_act:
        clear()
        prev_rotate_left[0] = None


@event('network/zone/server/map_effect')
def map_effect(plugin, evt: 'ServerMapEffectEvent'):
    if plugins.XivMemory.zone_id != map_id: return
    msg = evt.struct_message
    if msg.param2 == 0x200010 and draw(msg.param3):
        current.append(msg.param3)
    elif msg.param2 == 0x20001 and msg.param3 & 0xff == 5:
        draw_fire(False)
    elif msg.param2 == 0x400020 and msg.param3 & 0xff == 5:
        draw_fire(True)


def draw_fire(is_left: bool = False):
    for pos, facing in (fire_side if wait_until(lambda: prev_rotate_left[0], timeout=5) == is_left else fire_front):
        add_omen(get_can_use_actor(), pos, facing, *fire)


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
