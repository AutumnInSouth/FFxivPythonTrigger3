from ctypes import *
from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase, plugins
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.saint_coinach import action_sheet, territory_type_names
from .reflect import reflect_data

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent


# 常用标记
# 1：圆形
# 2：矩形
# 3：小扇形
# 4：中扇形
# 5：大扇形
# 229：纵向击退
# 203：圆心击退
# 114：直线两侧击退

class OmenReflect(PluginBase):
    name = "OmenReflect"

    def __init__(self):
        super().__init__()
        self.hook = self.omen_data_hook(self, BASE_ADDR + 0x6764B0)
        self.log_record = set()

    @PluginHook.decorator(c_int64, [c_int64], True)
    def omen_data_hook(self, hook, action_id):
        ans = hook.original(action_id)
        if action_id in reflect_data:
            ptr = cast(ans + 24, POINTER(c_ushort))
            ptr[0] = reflect_data[action_id]
        return ans

    @event('network/zone/server/actor_cast')
    def on_cast(self, evt: 'ServerActorCastEvent'):
        if evt.source_actor.type.value != 'player':
            zone_id = plugins.XivMemory.zone_id
            key = (zone_id, evt.source_actor.name, evt.action_id)
            if key not in self.log_record:
                self.log_record.add(key)
                try:
                    action = action_sheet[evt.action_id]
                except KeyError:
                    return
                self.logger.debug(f"{territory_type_names.get(zone_id, 'unk')}|{evt.source_actor.name}|{evt.action_id}|"
                                  f"{action['Name']}|{action['Omen'].key}({action['CastType']})=>{reflect_data.get(evt.action_id)}")
