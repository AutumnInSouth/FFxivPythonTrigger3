from typing import TYPE_CHECKING

from FFxivPythonTrigger.saint_coinach import status_names
from ..message_processors.utils import NetworkZoneServerEvent

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor


class ActorAddEffectEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'effect_add'

    def __init__(self,
                 server_event:NetworkZoneServerEvent,
                 actor:'Actor|None',
                 actor_id:int,
                 actor_name:str,
                 effect_id:int,
                 source_actor:'Actor|None',
                 source_id:int,
                 source_name:str):
        super().__init__(server_event.bundle_header, server_event.message_header, server_event.raw_message, server_event.struct_message)
        self.raw_event = server_event
        self.actor = actor
        self.actor_id = actor_id
        self.actor_name = actor_name
        self.source_actor = source_actor
        self.source_id = source_id
        self.source_name = source_name
        self.effect_id = effect_id
        self.effect_name = status_names.get(self.effect_id, 'unk')

    def text(self):
        return f'{self.actor_name}({self.actor_id:x}) add effect {self.effect_name}({self.effect_id}) from {self.source_name}'

    def str_event(self):
        return f'network_actor_effect_add|{self.actor_name}|{self.effect_id}|{self.effect_name}|{self.source_name}'


class ActorRemoveEffectEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'effect_remove'

    def __init__(self,
                 server_event:NetworkZoneServerEvent,
                 actor:'Actor|None',
                 actor_id:int,
                 actor_name:str,
                 effect_id:int,
                 source_actor:'Actor|None',
                 source_id:int,
                 source_name:str):
        super().__init__(server_event.bundle_header, server_event.message_header, server_event.raw_message, server_event.struct_message)
        self.raw_event = server_event
        self.actor = actor
        self.actor_id = actor_id
        self.actor_name = actor_name
        self.source_actor = source_actor
        self.source_id = source_id
        self.source_name = source_name
        self.effect_id = effect_id
        self.effect_name = status_names.get(self.effect_id, 'unk')

    def text(self):
        return f'{self.actor_name}({self.actor_id:x}) remove effect {self.effect_name}({self.effect_id}) from {self.source_name}'

    def str_event(self):
        return f'network_actor_effect_remove|{self.actor_name}|{self.effect_id}|{self.effect_name}|{self.source_name}'
