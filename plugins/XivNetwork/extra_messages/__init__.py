from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import event

from ..message_processors.zone_server.status_effect_list import ServerStatusEffectListEvent
from ..message_processors.zone_server.effect_result import ServerEffectResultsEvent
from ..message_processors.zone_server.actor_control_self import FadeInEvent, BarrierUpEvent, UnknownDirectorUpdateEvent
from .actor_add_remove_effect import ActorAddEffectEvent, ActorRemoveEffectEvent
from .combat_reset import CombatResetEvent


class ExtraNetworkMessage(PluginBase):
    name = "ExtraNetworkMessage"

    def __init__(self):
        super().__init__()
        self.register_event(FadeInEvent.id, lambda evt: process_event(CombatResetEvent(evt)))
        self.register_event(BarrierUpEvent.id, lambda evt: process_event(CombatResetEvent(evt)))
        self.register_event(UnknownDirectorUpdateEvent.id,
                            lambda evt: process_event(CombatResetEvent(evt)) if evt.struct_message.param2 == 0x40000016 else None)

    @event(ServerStatusEffectListEvent.id)
    def zone_server_status_effect_list(self, evt: ServerStatusEffectListEvent):
        for add_effect in evt.add_effects:
            source_actor = plugins.XivMemory.actor_table.get_actor_by_id(add_effect.actor_id)
            process_event(ActorAddEffectEvent(
                evt,
                evt.target_actor,
                evt.target_id,
                evt.target_name,
                add_effect.effect_id,
                source_actor,
                add_effect.actor_id,
                getattr(source_actor, 'name', 'unk')
            ))
        for remove_effect in evt.remove_effects:
            source_actor = plugins.XivMemory.actor_table.get_actor_by_id(remove_effect.actor_id)
            process_event(ActorRemoveEffectEvent(
                evt,
                evt.target_actor,
                evt.target_id,
                evt.target_name,
                remove_effect.effect_id,
                source_actor,
                remove_effect.actor_id,
                getattr(source_actor, 'name', 'unk')
            ))

    @event(ServerEffectResultsEvent.id)
    def zone_server_effect_results(self, evt: ServerEffectResultsEvent):
        for result in evt.results:
            for effect in result.effects:
                source_actor = plugins.XivMemory.actor_table.get_actor_by_id(effect.source_actor_id)
                process_event(ActorAddEffectEvent(
                    evt,
                    evt.actor,
                    evt.actor_id,
                    evt.actor_name,
                    effect.effect_id,
                    source_actor,
                    effect.source_actor_id,
                    getattr(source_actor, 'name', 'unk')
                ))
