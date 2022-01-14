from functools import lru_cache
from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins

if TYPE_CHECKING:
    from XivNetwork.message_processors.utils import NetworkZoneServerEvent
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent
    from XivNetwork.message_processors.zone_server.actor_control import TargetableEvent, CombatStateChangeEvent
    from XivNetwork.extra_messages.combat_reset import CombatResetEvent


@lru_cache(maxsize=300)
def actor_name(actor_id: int) -> str:
    if actor_id == 0 or actor_id == 0xe0000000: return "-"
    actor = plugins.XivMemory.actor_table.get_actor_by_id(actor_id)
    if actor is None: return f"unk_{actor_id:x}"
    return actor.name or f"{actor.type.value}_{actor_id:x}"


class TimeLineEvent:
    evt_id = ''

    def __init__(self, idx: int, evt: 'NetworkZoneServerEvent'):
        self.idx = idx
        self.evt = evt
        self.epoch = evt.bundle_header.epoch
        self.actor = actor_name(evt.message_header.actor_id)

    def to_dict(self) -> dict:
        return {
            'epoch': self.epoch,
            'actor': self.actor,
            'evt': self.evt_id
        }


class TimeLineActionEffectEvent(TimeLineEvent):
    evt_id = 'action_effect'

    def __init__(self, idx: int, evt: ActionEffectEvent):
        super().__init__(idx, evt)
        self.action = evt.action_id

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            'action': self.action,
        }


class TimeLineActorCastEvent(TimeLineEvent):
    evt_id = 'actor_cast'

    def __init__(self, idx: int, evt: ServerActorCastEvent):
        super().__init__(idx, evt)
        self.action = evt.action_id

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            'action': self.action,
        }
