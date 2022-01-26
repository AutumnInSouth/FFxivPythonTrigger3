from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import read_uint, BASE_ADDR
from FFxivPythonTrigger.saint_coinach import status_names
from FFxivPythonTrigger.decorator import BindValue, re_event, event
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class DebugPlugin(PluginBase):
    name = "DebugPlugin"

    # layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        # plugins.XivNetwork.register_packet_fixer(self, 'zone', True, "Effect", self.m_e)

    def m_e(self, bundle_header, message_header, raw_message, struct_message):
        struct_message.header.action_animation_id = 26362
        return struct_message

    def make_up(self, bundle_header, message_header, raw_message, struct_message):
        self.logger(struct_message)
        # if struct_message.category == 4:
        #     struct_message.event_id = 0x1f6
        self.logger(struct_message)
        return struct_message

    def makeup_moving_handler(self, bundle_header, message_header, raw_message, struct_message):
        return None

    #@re_event(r"^network/")
    def discover_event(self, evt, match: re.Match):
        if evt.id in [
            # "network/zone/client/update_position_handler",
            "network/undefined/zone/server/ActorMove",
            "network/zone/server/actor_update_hp_mp_tp",
            "network/zone/server/actor_control_self/unk_143",
            "network/zone/server/actor_control_self/fate_progress",
            # "network/unknown/zone/server/728",
            "network/zone/server/status_effect_list",
        ]: return
        # if any(s in evt.id for s in ["undefined", "unknown", "unk"]): return
        self.logger(evt.id, evt, len(evt.raw_message),
                    # '\n', evt.str_event()
                    )
        if "unknown" in evt.id:
            self.logger(evt.raw_message.hex(' '))

    #@re_event(r"^network/.*/client/")
    def discover_client_event(self, evt, match: re.Match):
        self.logger(evt.id, evt, len(evt.raw_message))
        if "unknown" in evt.id:
            self.logger(evt.raw_message.hex(' '))

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

    # @event('network/unknown/zone/client/375')
    def mix_stone_action(self, evt):
        struct = OffsetStruct({
            'event_id': c_ushort,
            'category': c_ushort,
            'unk0': c_uint,
            'cnt': c_uint,
            'slots': OffsetStruct({
                'container_id': c_uint,
                'slot_id': c_ushort,
                'cnt': c_ushort,
            }) * 5
        }, 72)
        # self.logger('|'.join(f"{k}:{v:x}" for k, v in struct.from_buffer(evt.raw_message).get_data(True).items()))
        self.logger(struct.from_buffer(evt.raw_message).get_data(True))

    # @re_event(r"^network/(unknown/|undefined/)?zone/")
    def discover_event2(self, evt, match: re.Match):
        if evt.id in [
            "network/zone/server/actor_update_hp_mp_tp",
            "network/undefined/zone/server/ActorMove",
        ]: return
        self.logger.debug(evt.id, evt, len(evt.raw_message))

    # @event("network/zone/server/actor_control_self/unk_143")
    def status_effect(self, evt):
        self.logger(evt)

    # @event("network/zone/server/actor_control/dot")
    def dot_event(self, evt):
        self.logger(evt.id, evt, evt.status_id)

    # @event("network/zone/server/action_effect")
    def discover_event3(self, evt):
        # if evt.actor_id == getattr(plugins.XivMemory.targets.focus, 'id', 0):
        self.logger(evt)
        # self.logger(evt.struct_message)
        # s = []
        # for t, e in evt.targets.items():
        #     for _e in e:
        #         self.logger(t, _e.raw_entry)

    # @re_event(r"network/zone/server/effect_(add|remove)")
    def network_zone_server_effect_add(self, evt, _=None):
        # if evt.actor_id == getattr(plugins.XivMemory.targets.focus, 'id', 0):
        self.logger(evt, evt.raw_event.id)
        if evt.raw_event.id == 'network/zone/server/status_effect_list':
            self.logger('', ','.join(str(e.effect_id) for e in evt.raw_event.new_effects),
                        ','.join(str(e.effect_id) for e in evt.raw_event.old_effects))

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

    # @event('network/zone/server/npc_spawn')
    def discover_npc_spawn(self, evt):
        self.logger(evt.id, evt, len(evt.raw_message), '\n', evt.struct_message, '\n', evt.raw_message.hex(' '))

    # @event('network/zone/server/actor_control/target_icon')
    def actor_control_target_icon(self, evt):
        self.logger(evt.id, evt.target_name, evt.struct_message.param1, evt.icon_id)

    #@event('network/zone/server/actor_control/tether')
    def actor_control_tether(self, evt):
        target = f"target:{evt.target_name}({evt.target_id:x}) {evt.target_actor.pos.x:.1f} {evt.target_actor.pos.y:.1f} {evt.target_actor.pos.z:.1f}"
        source = f"source:{evt.source_name}({evt.source_id:x}) {evt.source_actor.pos.x:.1f} {evt.source_actor.pos.y:.1f} {evt.source_actor.pos.z:.1f}"
        self.logger(evt.id, evt.type, target, source)

    # @event('network/zone/server/actor_control/targetable')
    def actor_control_targetable(self, evt):
        self.logger(evt.id, evt.str_event(), evt.struct_message)

    #@re_event(r"network/zone/server/actor_control_self/fate")
    def fate_event(self, evt, match):
        self.logger(evt.id, evt, evt.str_event())

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


    @event("log_event")
    def deal_chat_log(self, evt):
        for m in evt.chat_log.messages:
            if m.Type == "Interactable/MapPositionLink":
                self.logger(m.x,m.y)
