from ctypes import *
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerActorControlSelf(OffsetStruct({
    'category': c_ushort,
    'padding0': c_ushort,
    'param1': c_uint,
    'param2': c_uint,
    'param3': c_uint,
    'param4': c_uint,
    'param5': c_uint,
    'param6': c_uint,
    'padding1': c_uint,
})):
    category: int
    padding0: int
    param1: int
    param2: int
    param3: int
    param4: int
    param5: int
    param6: int
    padding1: int


class ActorControlSelfEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_control_self/'
    struct_message: ServerActorControlSelf


class UnknownActorControlSelfEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'unk_143'

    def text(self):
        return f'unknown actor control 143 category from {self.message_header.actor_id:x} {self.struct_message.category:x}|{self.struct_message.param1:x}|' \
               f'{self.struct_message.param2:x}|{self.struct_message.param3:x}|{self.struct_message.param4:x}|' \
               f'{self.struct_message.param5:x}|{self.struct_message.param6:x}'


class LimitBreakEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'limit_break'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.param = struct_message.param1 & 255

    def text(self):
        return f"limit break {self.param}/10000*3"

    def str_event(self):
        return f"network_actor_limit_break|{self.param}"


class DirectorUpdateEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'director_update/'


class UnknownDirectorUpdateEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + 'unk'


class InitialCommenceEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "initial_commence"


class RecommenceEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "recommence"


class LockoutTimeAdjustEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "lockout_time_adjust"


class ChargeBossLBEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "charge_boss_lb"


class MusicChangeEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "music_change"


class FadeOutEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "fade_out"


class FadeInEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "fade_in"


class BarrierUpEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "barrier_up"


class VictoryEvent(DirectorUpdateEvent):
    id = DirectorUpdateEvent.id + "victory"


director_update_map = {
    0x40000001: InitialCommenceEvent,
    0x40000006: RecommenceEvent,
    0x80000004: LockoutTimeAdjustEvent,
    0x8000000C: ChargeBossLBEvent,
    0x80000001: MusicChangeEvent,
    0x40000005: FadeOutEvent,
    0x40000010: FadeInEvent,
    0x40000012: BarrierUpEvent,
    0x40000003: VictoryEvent,
}


class ActorControlSelf(BaseProcessors):
    opcode = "ActorControlSelf"
    struct = ServerActorControlSelf

    @staticmethod
    def event(bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        match struct_message.category:
            case 109:
                evt = director_update_map.get(struct_message.param2, UnknownDirectorUpdateEvent)
            case 505:
                evt = LimitBreakEvent
            case _:
                evt = UnknownActorControlSelfEvent
        return evt(bundle_header, message_header, raw_message, struct_message)
