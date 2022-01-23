from ctypes import *
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import realm
from ..utils import NetworkZoneServerEvent, BaseProcessors

fate_sheet = realm.game_data.get_sheet('Fate')


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
        self.fate = fate_sheet[self.fate_id]

    def text(self):
        return f"fate {self.fate['Name'] or self.fate_id} init with health_multiple {self.health_multiple}"

    def str_event(self):
        return f"network_actor_control_fate_init|{self.fate_id}|{self.fate['Name']}|{self.health_multiple}|{self.struct_message.param3}|" \
               f"{self.struct_message.param4}|{self.struct_message.param5}|{self.struct_message.param6}"


class FateStartEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'fate_start'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.fate_id = struct_message.param1
        self.fate = fate_sheet[self.fate_id]

    def text(self):
        return f"fate {self.fate['Name'] or self.fate_id} start"

    def str_event(self):
        return f"network_actor_control_fate_start|{self.fate_id}|{self.fate['Name']}|{self.struct_message.param2}|" \
               f"{self.struct_message.param3}|{self.struct_message.param4}|{self.struct_message.param5}|{self.struct_message.param6}"


class FateProgressEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'fate_progress'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.fate_id = struct_message.param1
        self.progress = struct_message.param2
        self.fate = fate_sheet[self.fate_id]

    def text(self):
        return f"fate {self.fate['Name'] or self.fate_id} set progress {self.progress}"

    def str_event(self):
        return f"network_actor_fate_progress|{self.fate_id}|{self.fate['Name']}|{self.progress}|{self.struct_message.param3}|" \
               f"{self.struct_message.param4}|{self.struct_message.param5}|{self.struct_message.param6}"


class FateEndEvent(ActorControlSelfEvent):
    id = ActorControlSelfEvent.id + 'fate_end'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.fate_id = struct_message.param1
        self.fate = fate_sheet[self.fate_id]

    def text(self):
        return f"fate {self.fate['Name'] or self.fate_id} end"

    def str_event(self):
        return f"network_actor_fate_end|{self.fate_id}|{self.fate['Name']}|{self.struct_message.param2}|" \
               f"{self.struct_message.param3}|{self.struct_message.param4}|{self.struct_message.param5}|{self.struct_message.param6}"


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

actor_control_self_map = {
    505: LimitBreakEvent,
    2353: FateInitiEvent,
    2357: FateStartEvent,
    2358: FateEndEvent,
    2366: FateProgressEvent,
}


class ActorControlSelf(BaseProcessors):
    opcode = "ActorControlSelf"
    struct = ServerActorControlSelf

    @staticmethod
    def event(bundle_header, message_header, raw_message, struct_message: ServerActorControlSelf):
        match struct_message.category:
            case 109:
                evt = director_update_map.get(struct_message.param2, UnknownDirectorUpdateEvent)
            case c:
                evt = actor_control_self_map.get(c, UnknownActorControlSelfEvent)
        return evt(bundle_header, message_header, raw_message, struct_message)
