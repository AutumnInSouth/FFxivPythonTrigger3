import math
from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase, plugins, BindValue, PluginNotFoundException
from FFxivPythonTrigger.decorator import event
from . import afix

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_client.update_position_handler import ClientUpdatePositionHandlerEvent
    from XivNetwork.message_processors.zone_client.update_position_instance import ClientUpdatePositionInstanceEvent
    from XivNetwork.message_processors.zone_client.action_send import ClientActionSend
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent

_afix = True


class NetworkHacks(PluginBase):
    name = "NetworkHacks"

    def __init__(self):
        super().__init__()
        if _afix:
            self.afix_adjust_mode = True
            self.afix_adjust_sig = 0
            self.afix_set_sig = 0x93
            self.afix_work = False
            self.register_afix()

    if _afix:
        afix_enable = BindValue(default=True, auto_save=True)
        afix_distance = BindValue(default=5, auto_save=True)

        @event('network/zone/client/update_position_instance')
        def deal_adjust(self, evt: 'ClientUpdatePositionInstanceEvent'):
            self.afix_adjust_mode = True
            self.afix_adjust_sig = evt.struct_message.unk1 & 0xf

        @event('network/zone/client/update_position_handler')
        def deal_set(self, evt: 'ClientUpdatePositionHandlerEvent'):
            self.afix_adjust_mode = False
            if not (evt.struct_message.unk0 or evt.struct_message.unk1) and 0x10000 > evt.struct_message.unk2 > 0:
                self.afix_set_sig = evt.struct_message.unk2

        def goto(self, new_x=None, new_y=None, new_r=None, stop=False):
            c = plugins.XivMemory.coordinate
            if new_r is None: new_r = c.r
            target = {
                'x': new_x if new_x is not None else c.x,
                'y': new_y if new_y is not None else c.y,
                'z': c.z
            }
            if self.afix_adjust_mode:
                msg = {
                    'old_r': c.r,
                    'new_r': new_r,
                    'old_pos': target,
                    'new_pos': target,
                    'unk0': (0x4000 if stop else 0),
                    'unk1': (0x40 if stop else 0) | self.afix_adjust_sig
                }
                code = "UpdatePositionInstance"
            else:
                msg = {'r': new_r, 'pos': target, 'unk2': self.afix_set_sig if stop else 0}
                code = "UpdatePositionHandler"
            self.logger.debug(f'goto x:{target["x"]:.2f} y:{target["y"]:.2f} z:{target["z"]:.2f} r:{new_r:.2f}')
            plugins.XivNetwork.send_messages('zone', (code, msg))

        @event('network/zone/server/action_effect')
        def coor_return(self, evt: 'ActionEffectEvent'):
            if not self.afix_work or evt.source_id != plugins.XivMemory.player_info.id or evt.action_type != 'action' or evt.action_id not in afix.afix_skills:
                return
            self.goto(stop=True)
            self.afix_work = False

        @event("plugin_load:XivNetwork")
        def register_afix(self, _=None):
            try:
                plugins.XivNetwork.register_packet_fixer(self, 'zone', False, 'ActionSend', self.makeup_action_send)
            except PluginNotFoundException:
                self.logger.warning("XivNetwork is not found")

        def makeup_action_send(self, bundle_header, message_header, raw_message, struct_message: 'ClientActionSend'):
            me = plugins.XivMemory.actor_table.me
            me_effects = me.effects.get_dict()
            msg = struct_message
            if self.afix_enable and msg.action_id in afix.afix_skills and 1250 not in me_effects and 1179 not in me_effects:
                t = plugins.XivMemory.actor_table.get_actor_by_id(msg.target_id)
                if t is not None and t.is_positional:
                    if isinstance(afix.afix_skills[msg.action_id], int):
                        pos, statement = afix.afix_skills[msg.action_id], lambda x: True
                    else:
                        pos, statement = afix.afix_skills[msg.action_id]
                    if statement(msg.action_id):
                        c = plugins.XivMemory.coordinate
                        xy = afix.get_nearest(c, t, pos)
                        self.logger(xy)
                        if xy is not None:
                            dis = afix.distance(xy, (c.x, c.y))
                            if dis >= self.afix_distance:
                                self.logger.debug(f"too far to fix: {dis}")
                            else:
                                new_r = c.r
                                new_r = new_r + (-math.pi if new_r > 0 else math.pi)
                                self.afix_work = True
                                self.goto(*xy, new_r)
            return struct_message
