from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.saint_coinach import status_names
from FFxivPythonTrigger.decorator import BindValue, re_event, event
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class DebugPlugin(PluginBase):
    name = "DebugPlugin"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        # plugins.XivNetwork.register_packet_fixer(self, 'zone', True, 'ActorCast', self.make_up)
        # plugins.XivNetwork.register_packet_fixer(self, 'zone', False, 'UpdatePositionHandler', self.makeup_moving_handler)

    def make_up(self, bundle_header, message_header, raw_message, struct_message):
        struct_message.unk0 = 0
        return struct_message

    def makeup_moving_handler(self, bundle_header, message_header, raw_message, struct_message):
        return None

    # @re_event(r"^network/")
    def discover_event(self, evt, match: re.Match):
        if evt.id in [
            # "network/zone/client/update_position_handler",
            "network/unknown/zone/client/567",
            "network/undefined/zone/server/ActorMove",
            # "network/zone/server/actor_update_hp_mp_tp",
            # "network/zone/server/actor_control_self/unk_143",
            "network/unknown/zone/server/541",
            "network/unknown/zone/server/728",
            # "network/zone/server/status_effect_list",
        ]: return
        # if any(s in evt.id for s in ["undefined", "unknown", "unk"]): return
        self.logger(evt.id, evt, len(evt.raw_message),
                    '\n', evt.str_event())

    # @event('network/unknown/zone/client/399')
    def craft_action(self, evt):
        """
        normal action _uint_0x0:a0001|_uint_0x4:4000000|_uint_0x8:9|_uint_0xc:action_id|_uint_0x10:0|_uint_0x14:0
        craft action _uint_0x0:a0001|_uint_0x4:4000000|_uint_0x8:a|_uint_0xc:action_id|_uint_0x10:0|_uint_0x14:0
        finish craft _uint_0x0:a0001|_uint_0x4:4000000|_uint_0x8:b|_uint_0xc:0|_uint_0x10:0|_uint_0x14:0

        next craft _uint_0x0:a0001|_uint_0x4:4000000|_uint_0x8:4|_uint_0xc:recipe_id|_uint_0x10:0|_uint_0x14:0

        end craft1 _uint_0x0:a0001|_uint_0x4:4000000|_uint_0x8:7|_uint_0xc:0 if in craft else 1|_uint_0x10:0|_uint_0x14:0
        end craft2 _uint_0x0:a0001|_uint_0x4:4000000|_uint_0x8:8|_uint_0xc:0|_uint_0x10:0|_uint_0x14:0

        """
        struct = OffsetStruct({

        }, 24)
        self.logger('|'.join(f"{k}:{v:x}" for k, v in struct.from_buffer(evt.raw_message).get_data(True).items()))

    # @re_event(r"^network/")
    def discover_event2(self, evt, match: re.Match):
        if evt.id in [
            "network/zone/server/actor_update_hp_mp_tp",
        ]: return
        self.logger.debug(evt.id, evt, len(evt.raw_message))

    # @event("network/zone/server/actor_control_self/unk_143")
    def status_effect(self, evt):
        self.logger(evt)

    @event("network/zone/server/actor_control/dot")
    def dot_event(self, evt):
        self.logger(evt.id, evt, evt.status_id)

    # @event("network/zone/server/action_effect")
    def discover_event3(self, evt):
        #if evt.actor_id == getattr(plugins.XivMemory.targets.focus, 'id', 0):
        self.logger(evt)
        # self.logger(evt.struct_message)
        # s = []
        # for t, e in evt.targets.items():
        #     for _e in e:
        #         self.logger(t, _e.raw_entry)

    @re_event(r"network/zone/server/effect_(add|remove)")
    def network_zone_server_effect_add(self, evt, _=None):
        #if evt.actor_id == getattr(plugins.XivMemory.targets.focus, 'id', 0):
            self.logger(evt,evt.raw_event.id)
            if evt.raw_event.id =='network/zone/server/status_effect_list':
                self.logger('',','.join(str(e.effect_id) for e in evt.raw_event.new_effects),','.join(str(e.effect_id) for e in evt.raw_event.old_effects))
        # n_e = [status_names.get(e.effect_id,e.effect_id) for e in evt.struct_message.effects if e.effect_id]
        # self.logger(evt.struct_message.struct_size,len(evt.raw_message))
        # self.logger(evt.raw_message.hex(' '))
        # if n_e: self.logger(getattr(plugins.XivMemory.actor_table.get_actor_by_id(evt.message_header.actor_id),'name','?'),n_e)

    # @re_event(r"^network/")
    def discover_event_from_target(self, evt, match: re.Match):
        if evt.message_header.actor_id == getattr(plugins.XivMemory.targets.focus, 'id', 0):
            self.logger(evt.id, evt, len(evt.raw_message))

    # @event('network/zone/server/status_effect_list')
    def discover_event_from_target2(self, evt):
        t = plugins.XivMemory.targets.focus
        if evt.message_header.actor_id == getattr(t, 'id', 0):
            self.logger(
                "add:", ','.join(str(e.effect_id) for e in evt.add_effects),
                "remove:", ','.join(str(e.effect_id) for e in evt.remove_effects),
            )

    # @event(r"network/zone/server/market_board_purchase_handler")
    # def market_board_purchase_handler(self, evt):
    #     self.logger(evt.id, evt, '\n', evt.struct_message, '\n', evt.raw_message.hex(' '))
    #
    # @event(r"network/zone/server/market_board_item_listing")
    # def market_board_item_listing(self, evt):
    #     self.logger(evt.id, evt, '\n', '\n\t'.join(str(item) for item in evt.struct_message.items))
    #
    # @event(r"network/zone/server/market_board_item_listing_count")
    # def market_board_item_listing_count(self, evt):
    #     self.logger(evt.id, evt, '\n', evt.struct_message.get_data(True))
    #
    # @event(r"network/unknown/zone/server/265")
    # def unk_265(self, evt):
    #     self.logger(evt.id, evt, '\n', hex(int.from_bytes(evt.raw_message,byteorder='little')))
