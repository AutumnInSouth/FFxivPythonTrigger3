from typing import TYPE_CHECKING

from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.saint_coinach import action_sheet

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent


class CombatTimeline(PluginBase):
    name = "Combat Timeline"

    @event("network/zone/server/action_effect")
    def action_effect_event(self, evt: 'ActionEffectEvent'):
        if evt.action_type != 'action': return
        if evt.source_actor is None: return
        source_actor = evt.source_actor
        if source_actor.type != 'battle_npc' or source_actor.owner_id != 0xe0000000 or evt.action_name == 'attack':
            return
        self.logger(evt.str_event())

    @event("network/zone/server/actor_cast")
    def actor_cast_event(self, evt: 'ServerActorCastEvent'):
        if evt.source_actor is None: return
        source_actor = evt.source_actor
        if source_actor.type != 'battle_npc' or source_actor.owner_id != 0xe0000000:
            return
        self.logger(evt.str_event())
