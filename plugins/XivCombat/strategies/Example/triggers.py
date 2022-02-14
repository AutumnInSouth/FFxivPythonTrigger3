from FFxivPythonTrigger.decorator import event
from XivCombat import api

last_use = 0


@event('network/zone/server/action_effect')
def last_use_record(plugin, evt):
    if evt.action_type == 'action' and evt.source_id == api.get_me_actor().id:
        global last_use
        last_use = evt.action_id
