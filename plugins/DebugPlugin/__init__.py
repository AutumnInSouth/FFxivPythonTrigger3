from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import BindValue, re_event, event


class DebugPlugin(PluginBase):
    name = "DebugPlugin"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        plugins.XivNetwork.register_packet_fixer(self,'zone',True,'ActorCast',self.make_up)


    def make_up(self,bundle_header,message_header,raw_message,struct_message):
        self.logger(struct_message.__class__.x.offset ,struct_message)
        return raw_message

    #@re_event(r"^network/")
    def discover_event(self, evt, match: re.Match):
        if any(s in evt.id for s in ["undefined", "unknown", "unk"]): return
        self.logger(evt.id, evt, len(evt.raw_message), '\n', evt.str_event())

    #re_event(r"^network/")
    def discover_event2(self, evt, match: re.Match):
        self.logger.debug(evt.id, evt,len(evt.raw_message))

    #@event("network/zone/server/action_effect")
    def discover_event3(self,evt):
        if evt.action_id<10:return
        s=[]
        for t,d in evt.targets.items():
            n,e = d
            for _e in e:
                if 'ability' in _e.tags:
                    s.append(f"{n.name}:{_e.raw_entry.param3}")
                    break
        if s:
            self.logger(evt.action_name,' '.join(s))

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
