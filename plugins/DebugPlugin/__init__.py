from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import BindValue, re_event, event
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class DebugPlugin(PluginBase):
    name = "DebugPlugin"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        #plugins.XivNetwork.register_packet_fixer(self, 'zone', True, 'ActorCast', self.make_up)

    def make_up(self, bundle_header, message_header, raw_message, struct_message):
        struct_message.unk0 = 0
        return struct_message

    #@re_event(r"^network/")
    def discover_event(self, evt, match: re.Match):
        if any(s in evt.id for s in ["undefined", "unknown", "unk"]): return
        self.logger(evt.id, evt, len(evt.raw_message), '\n', evt.str_event())

    #@event('network/unknown/zone/client/399')
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
        self.logger('|'.join(f"{k}:{v:x}" for k,v in struct.from_buffer(evt.raw_message).get_data(True).items()))

    #@re_event(r"^network/")
    def discover_event2(self, evt, match: re.Match):
        if evt.id in [
            "network/zone/server/actor_update_hp_mp_tp",
        ]:return
        self.logger.debug(evt.id, evt, len(evt.raw_message))

    #@event("network/zone/server/status_effect_list")
    def status_effect(self, evt):
        self.logger(evt.id, evt, len(evt.raw_message))

    #@event("network/zone/server/actor_control/dot")
    def dot_event(self, evt):
        self.logger(evt.id, evt, evt.status_id)

    @event("network/zone/server/action_effect")
    def discover_event3(self, evt):
        self.logger(evt.struct_message)
        s = []
        for t, e in evt.targets.items():
            for _e in e:
                self.logger(t, _e.raw_entry)

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
