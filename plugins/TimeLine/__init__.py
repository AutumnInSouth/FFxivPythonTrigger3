from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins, PluginBase
from FFxivPythonTrigger.decorator import event

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent
    from XivNetwork.message_processors.zone_server.actor_control import TargetableEvent, CombatStateChangeEvent
    from XivNetwork.extra_messages.combat_reset import CombatResetEvent


class TimeLine(PluginBase):
    name = "TimeLine"

    @event('network/zone/server/action_effect')
    def on_action_effect(self, evt: 'ActionEffectEvent'):
        pass

    @event('network/zone/server/actor_cast')
    def on_actor_cast(self, evt: 'ServerActorCastEvent'):
        pass

    @event('network/zone/server/actor_control/targetable')
    def on_actor_targetable(self, evt: 'TargetableEvent'):
        pass

    @event('network/zone/server/actor_control/combat_state_change')
    def on_actor_combat_state_change(self, evt: 'CombatStateChangeEvent'):
        pass

    @event('network/zone/server/combat_reset')
    def on_combat_reset(self, evt: 'CombatResetEvent'):
        pass
