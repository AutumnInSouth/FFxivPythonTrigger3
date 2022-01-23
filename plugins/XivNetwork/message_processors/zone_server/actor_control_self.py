from ctypes import *
import struct
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


class FateInitiEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'fate_init'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.fate_id = struct_message.param1
         # 应该是血量倍数, 因为fate出现时,周围人多时数值是7,人少时是2,同时怪的血量也有所变化
        self.health_multiple = struct_message.param2

    def text(self):
        return f"fate init | fate_id:{self.fate_id} | health_multiple: {self.health_multiple}"

    def str_event(self):
        return f"network_actor_fate_init|{self.fate_id}|{self.health_multiple}"


class FateStartEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'fate_start'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.fate_id = struct_message.param1

    def text(self):
        return f"fate start | fate_id:{self.fate_id}"

    def str_event(self):
        return f"network_actor_fate_start|{self.fate_id}"


class FateProgressEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'fate_progress'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.fate_id = struct_message.param1
        self.progress = struct_message.param2
        self.unk_1 = struct_message.param3
        self.unk_2 = struct_message.param4
        self.unk_3 = struct_message.param5
        self.unk_4 = struct_message.param6

    def text(self):
        return f"fate progress | fate_id:{self.fate_id} | progress:{self.progress} | unks: {self.unk_1} {self.unk_2} {self.unk_3} {self.unk_4}"

    def str_event(self):
        return f"network_actor_fate_progress|{self.fate_id}|{self.progress}"


class FateEndEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'fate_end'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.fate_id = struct_message.param1

    def text(self):
        return f"fate end | fate_id:{self.fate_id}"

    def str_event(self):
        return f"network_actor_fate_end|{self.fate_id}"


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
            case 2353:
                evt = FateInitiEvent
            case 2357:
                evt = FateStartEvent
            case 2358:
                evt = FateEndEvent
            case 2366:
                evt = FateProgressEvent
            case _:
                evt = UnknownActorControlSelfEvent
        return evt(bundle_header, message_header, raw_message, struct_message)
