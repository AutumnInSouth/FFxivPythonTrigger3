from typing import TYPE_CHECKING
from threading import Lock
from FFxivPythonTrigger import plugins
from RaidHelper.utils import map_trigger

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control import TargetIconEvent
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent

p3s = map_trigger(1007)
icon_lock = Lock()
target_icon_evt_id = 'network/zone/server/actor_control/target_icon'

last_rec = 0
rec_icons = []


@p3s('点名指挥', target_icon_evt_id)
def p3s_target_icon(output, e: 'TargetIconEvent') -> None:
    global last_rec
    if 268 <= e.icon_id <= 276:
        with icon_lock:
            if last_rec < e.bundle_header.epoch - 1000:
                last_rec = e.bundle_header.epoch
                rec_icons.clear()
            rec_icons.append((e.target_actor.job.short_name, e.icon_id - 268))
            if len(rec_icons) >= 8:
                rec_icons.sort(key=lambda x: x[1])
                output(f"(1) {rec_icons[0][0]} {rec_icons[4][0]}", in_game_output=2)
                output(f"(2) {rec_icons[1][0]} {rec_icons[5][0]}", in_game_output=2)
                output(f"(3) {rec_icons[2][0]} {rec_icons[6][0]}", in_game_output=2)
                output(f"(4) {rec_icons[3][0]} {rec_icons[7][0]}", in_game_output=2)


def dark_fire(points=None):
    def func(output, e: 'TargetIconEvent') -> None:
        if 268 <= e.icon_id <= 276 and e.target_id == plugins.XivMemory.player_info.id:
            i = (e.icon_id - 268) % 4
            if points:
                p = getattr(plugins.XivMemory.markings.way_mark, points[i])
                if p.is_active: plugins.XivMemory.coordinate.set(p.x, p.y, p.z)
            output(f"point {i + 1} ({e.icon_id - 267})")

    return func


p3s_target_icon_tp_num = p3s('点名瞬移(数字标点)', target_icon_evt_id)(dark_fire(['one', 'two', 'three', 'four']))
p3s_target_icon_tp_abc = p3s('点名瞬移(字母标点)', target_icon_evt_id)(dark_fire(['a', 'b', 'c', 'd']))
p3s_target_icon_tell = p3s('点名提示', target_icon_evt_id)(dark_fire())
invincible_effects = {
    325, 394, 529, 656, 671,
    775, 776, 895, 969, 981,
    1570, 1697, 1829, 1302,
    350,  # 大额减伤
}


@p3s('谁手贱暗炎打鳳凰', 'network/zone/server/action_effect')
def who_attack_phoinix(output, e: 'ActionEffectEvent') -> None:
    if e.source_actor.type == 'player' and e.action_type == 'action' and e.action_name != 'attack' and any(
            actor.current_hp and actor.can_select and not actor.effects.get_set().intersection(invincible_effects)
            for actor in plugins.XivMemory.actor_table.get_actors_by_name('Darkened Fire')
    ) and all(
        t.type == 'battle_npc' and t.name == "Phoinix" for t in e.target_actors.values()
    ):
        output(f"{e.source_actor.name} use {e.action_name} on Phoinix", in_game_output=2)
