from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins

from RaidHelper.utils import map_trigger, common_trigger

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control import TargetIconEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent

p2s = map_trigger(1005)


# @p2s('点名校正1', 'network/zone/server/actor_control/target_icon')
def p2s_target_icon_1(out, e: 'TargetIconEvent'):
    common_trigger(e)


# @p2s('点名校正2', 'network/zone/server/actor_cast')
def p2s_target_icon_2(out, e: 'ServerActorCastEvent'):
    common_trigger(e)
