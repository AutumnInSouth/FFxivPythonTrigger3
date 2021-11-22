from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase
from FFxivPythonTrigger.decorator import event

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent


class CombatMonitor(PluginBase):
    name = 'CombatMonitor'

    def __init__(self):
        super().__init__()
        self.current=1

    @event('network/zone/server/action_effect')
    def on_action_effect(self, evt: 'ActionEffectEvent'):
        pass
