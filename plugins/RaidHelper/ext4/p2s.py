from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins

from RaidHelper.utils import map_trigger

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control import TargetIconEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent

p2s = map_trigger(1005)


@p2s('点名', 'network/zone/server/actor_control/target_icon')
def p2s_target_icon_1(out, e: 'TargetIconEvent'):
    if e.target_id == plugins.XivMemory.player_info.id and 145 <= e.icon_id <= 152:
        if e.icon_id < 149:
            out(f'点名：紫{e.icon_id - 144}')
        else:
            out(f'点名：蓝{e.icon_id - 148}')
