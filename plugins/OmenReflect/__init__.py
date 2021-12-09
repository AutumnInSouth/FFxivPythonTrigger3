from ctypes import *
from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase, plugins, AddressManager, PluginNotFoundException, game_ext
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.saint_coinach import action_sheet, action_names, territory_type_names
from .reflect import reflect_data

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent

# 常用标记
# 关于月环：月环内圈为等比缩放，请根据内圈半径/外圈半径比例选择 omen
# 1：圆形
# 2：矩形
#
# 146：20扇形
# 105：30扇形
# 3：60扇形
# 4：90扇形
# 5：120扇形
# 28：150扇形
# 107：180扇形
# 128：210扇形
# 15：270扇形
#
# 14：6%月环
# 13：13%月环
# 228：23%月环
# 227：25%月环
# 12：36.8%月环
# 220：40%月环
# 108：50%月环
# 112：66%月环
# 137：46%月环
# 78：80%月环
#
# 229：纵向击退(矩形)
# 203：圆心击退(圆形)
# 114：直线两侧击退(矩形)
# 188: 十字(矩形*2)
# 139：浪柱（？）

offset = 24 if game_ext == 3 else 26

full_reflect_data = {row.key: (reflect_data.get(row.key) or row['Omen'].key) for row in action_sheet}


class OmenReflect(PluginBase):
    name = "OmenReflect"

    def __init__(self):
        super().__init__()
        self.hook = self.omen_data_hook(self, AddressManager(self.name, self.logger).scan_point(
            'omen_data_hook', 'E8 * * * * 48 8B E8 48 85 C0 74 ? 45 84 E4'
        ))
        self.log_record = set()
        self.register_makeup()

    @PluginHook.decorator(c_int64, [c_int64], True)
    def omen_data_hook(self, hook, action_id):
        ans = hook.original(action_id)
        if action_id in full_reflect_data:
            cast(ans + offset, POINTER(c_ushort))[0] = full_reflect_data[action_id]
            del full_reflect_data[action_id]
        return ans

    @event("plugin_load:XivNetwork")
    def register_makeup(self, _=None):
        try:
            plugins.XivNetwork.register_packet_fixer(self, 'zone', True, 'ActorCast', self.make_up)
        except PluginNotFoundException:
            self.logger.warning("XivNetwork is not found")

    def make_up(self, bundle_header, message_header, raw_message, struct_message):
        struct_message.display_delay = int(struct_message.display_delay / 5)
        # struct_message.unk3 = 0
        return struct_message

    @event('network/zone/server/actor_cast')
    def on_cast(self, evt: 'ServerActorCastEvent'):
        if evt.source_actor.type.value != 'player':
            zone_id = plugins.XivMemory.zone_id
            msg = evt.struct_message
            key = (zone_id, evt.source_actor.name, evt.action_id, msg.display_action_id)
            if key not in self.log_record:
                self.log_record.add(key)
                try:
                    action = action_sheet[evt.action_id]
                except KeyError:
                    return
                self.logger.debug(
                    f"{territory_type_names.get(zone_id, 'unk')}|{evt.source_actor.name}|"
                    # f"{msg.display_action_id}|{action_names.get(msg.display_action_id, 'unk')}|"
                    f"{evt.action_id}|{action['Name']}|{evt.cast_time:.2f}s|"
                    f"{action['Omen'].key}({action['CastType']}/{action['EffectRange']}/{action['XAxisModifier']})=>{reflect_data.get(evt.action_id)}|",
                    #'\n', msg
                )
