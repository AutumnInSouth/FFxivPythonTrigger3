from typing import TYPE_CHECKING
from threading import Lock
from FFxivPythonTrigger import plugins
from RaidHelper.utils import map_trigger

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control import TargetIconEvent

p3s = map_trigger(1007)
icon_lock = Lock()

last_rec = 0
rec_icons = []


@p3s('点名指挥', 'network/zone/server/actor_control/target_icon')
def p3s_target_icon_1(output, e: 'TargetIconEvent') -> None:
    global last_rec
    if 268 <= e.icon_id <= 276:
        with icon_lock:
            if last_rec < e.bundle_header.epoch - 1000:
                last_rec = e.bundle_header.epoch
                rec_icons.clear()
            rec_icons.append((e.target_actor.job.short_name, e.icon_id - 268, e.target_id == plugins.XivMemory.player_info.id))
            if len(rec_icons) >= 8:
                rec_icons.sort(key=lambda x: x[1])
                output(f"""
(4){rec_icons[3][0]} | {rec_icons[7][0]}    {rec_icons[0][0]} | {rec_icons[4][0]}(1)
                    BOSS
(3){rec_icons[2][0]} | {rec_icons[6][0]}    {rec_icons[1][0]} | {rec_icons[5][0]}(2)
""")


@p3s('点名瞬移', 'network/zone/server/actor_control/target_icon')
def p3s_target_icon_2(output, e: 'TargetIconEvent') -> None:
    global last_rec
    if 268 <= e.icon_id <= 276 and e.target_id == plugins.XivMemory.player_info.id:
        p = getattr(plugins.XivMemory.markings.way_mark, ['one', 'two', 'three', 'four'][e.icon_id - 268 % 4])
        plugins.XivMemory.coordinate.set(p.x, p.y, p.z)
