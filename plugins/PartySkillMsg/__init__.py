from random import choice
from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import event

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent


def is_in_party():
    return plugins.XivMemory.party.main_size > 1


class PartySkillMsg(PluginBase):
    name = "PartySkillMsg"

    action_use = BindValue(default={}, auto_save=True)

    @event("network/zone/server/action_effect",condition=is_in_party)
    def on_action_effect(self, evt: "ActionEffectEvent"):
        if evt.action_type == 'action' and evt.source_id == plugins.XivMemory.player_info.id:
            msgs = self.action_use.get(str(evt.action_id))
            if msgs:
                targets = "、".join(actor.name for actor in evt.target_actors.values())
                plugins.XivMemory.calls.do_text_command('/p '+choice(msgs).format(
                    t=targets,
                    targets = targets,
                ))

