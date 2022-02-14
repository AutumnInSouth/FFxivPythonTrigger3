from ctypes import *
from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import status_names, class_job_names, action_names, item_names
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerActorControl(OffsetStruct({
    'category': c_ushort,
    'padding0': c_ushort,
    'param1': c_uint,
    'param2': c_uint,
    'param3': c_uint,
    'param4': c_uint,
    'padding1': c_uint,
})):
    category: int
    padding0: int
    param1: int
    param2: int
    param3: int
    param4: int
    padding1: int


class ActorControlEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_control/'
    struct_message: ServerActorControl
    target_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.target_id = message_header.actor_id
        self.target_name = hex(self.target_id)

    def init(self):
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None: self.target_name = self.target_actor.name


class UnknownActorControlEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'unk_142'

    def _text(self):
        return f'unknown actor control 142 category from {self.target_name}({self.target_id:x}) {self.struct_message.category:x}|{self.struct_message.param1:x}|' \
               f'{self.struct_message.param2:x}|{self.struct_message.param3:x}|{self.struct_message.param4:x}'


class UnknownDotHotEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'unk_dot_hot'
    source_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.damage = struct_message.param3
        self.source_id = struct_message.param4
        self.status_id = struct_message.param1
        self.source_name = hex(self.source_id)

    def init(self):
        super().init()
        self.source_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.source_id)
        if self.source_actor is not None: self.source_name = self.source_actor.name

    def _text(self):
        return f"{self.target_name} gains {self.damage} effect over time({self.struct_message.param2}) from {self.source_name}({status_names.get(self.status_id)})"

    def _str_event(self):
        return f"network_unk_dot_hot|{self.target_name}|{self.damage}|{self.source_name}|{self.status_id}|{status_names.get(self.status_id)}"


class DotEvent(UnknownDotHotEvent):
    id = ActorControlEvent.id + 'dot'

    def _text(self):
        return f"{self.target_name} gains {self.damage} dot from {self.source_name}({status_names.get(self.status_id)})"

    def _str_event(self):
        return f"network_dot|{self.target_name}|{self.damage}|{self.source_name}|{self.status_id}|{status_names.get(self.status_id)}"


class HotEvent(UnknownDotHotEvent):
    id = ActorControlEvent.id + 'hot'

    def _text(self):
        return f"{self.target_name} gains {self.damage} hot from {self.source_name}({status_names.get(self.status_id)})"

    def _str_event(self):
        return f"network_hot|{self.target_name}|{self.damage}|{self.source_name}|{self.status_id}|{status_names.get(self.status_id)}"


def dot_hot_event(bundle_header, message_header, raw_message, struct_message: ServerActorControl):
    match struct_message.param2:
        case 4:
            c = HotEvent
        case 3:
            c = DotEvent
        case _:
            c = UnknownDotHotEvent
    return c(bundle_header, message_header, raw_message, struct_message)


class DeathEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'death'
    source_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.source_id = struct_message.param1
        self.source_name = hex(self.source_id)

    def init(self):
        super().init()
        self.source_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.source_id)
        if self.source_actor is not None: self.source_name = self.source_actor.name

    def _text(self):
        return f"{self.target_name} was defeated by {self.source_name}."

    def _str_event(self):
        return f"network_death|{self.target_name}|{self.source_name}"


class TargetIconEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'target_icon'

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.icon_id = struct_message.param1 + plugins.XivNetwork.fix_param

    def _text(self):
        return f'target icon {self.target_name}({self.target_id:x}) {self.icon_id:x}|' \
               f'{self.struct_message.param2:x}|{self.struct_message.param3:x}|{self.struct_message.param4:x}'

    def _str_event(self):
        return f'network_actor_mark|{self.target_name}|{self.icon_id:x}|' \
               f'{self.struct_message.param2:x}|{self.struct_message.param3:x}|{self.struct_message.param4:x}'


class JobChangeEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'job_change'

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.to_job = struct_message.param1

    def _text(self):
        return f"{self.target_name} change job to {class_job_names[self.to_job]}."

    def _str_event(self):
        return f"network_actor_job_change|{self.target_name}|{self.to_job}|{class_job_names[self.to_job]}"


class CombatStateChangeEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'combat_state_change'

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.is_combat = bool(struct_message.param1)

    def _text(self):
        return f"{self.target_name} set is combat to {self.is_combat}."

    def _str_event(self):
        return f"network_actor_is_combat|{self.target_name}|{self.struct_message.param1}"


class EffectUpdateEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'effect_update'

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.effect_id = struct_message.param2 & 0xffff
        self.effect_extra = struct_message.param3 & 0xffff

    def _text(self):
        return f"{self.target_name} 's effect {self.effect_id} with extra {self.effect_extra} was updated"

    def _str_event(self):
        return f"network_actor_effect_update|{self.target_name}|{self.effect_id}|{self.effect_extra}"


class TargetableEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'targetable'

    def _text(self):
        return f"{self.target_name} is " + ('targetable' if self.struct_message.param1 else 'untargetable')

    def _str_event(self):
        return f"network_actor_targetable|{self.target_name}|{self.struct_message.param1}"


class TetherEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'tether'
    source_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.source_id = struct_message.param3
        self.source_name = hex(self.source_id)
        self.type = struct_message.param2

    def init(self):
        super().init()
        self.source_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.source_id)
        if self.source_actor is not None: self.source_name = self.source_actor.name

    def _text(self):
        return f"{self.target_name} tether with {self.source_name} on {self.type}"

    def _str_event(self):
        return f"network_actor_tether|{self.target_name}|{self.source_name}|{self.type}|{self.struct_message.param1:x}|{self.struct_message.param2:x}|{self.struct_message.param3:x}|{self.struct_message.param4:x}"


class EffectRemoveEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'effect_remove'
    source_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.source_id = struct_message.param3
        self.source_name = hex(self.source_id)
        self.effect_id = struct_message.param1

    def init(self):
        super().init()
        self.source_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.source_id)
        if self.source_actor is not None: self.source_name = self.source_actor.name

    def _text(self):
        return f"{self.target_name} remove effect {status_names.get(self.effect_id)} from {self.source_name}"

    def _str_event(self):
        return f"network_actor_effect_remove|{self.target_name}|{self.effect_id}|{status_names.get(self.effect_id)}|{self.source_name}"


class CastCancelEvent(ActorControlEvent):
    id = ActorControlEvent.id + 'cast_cancel'

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.action_id = struct_message.param3
        self.action_type = struct_message.param2
        if self.action_type == 1:
            self.action_name = f"unk_action_{self.action_id}"
        elif self.action_type == 2:
            self.action_name = f"unk_item_{self.action_id}"
        else:
            self.action_name = f"unk_{self.action_type}_{self.action_id}"

    def init(self):
        super().init()
        if self.action_type == 1:
            self.action_name = action_names.get(self.action_id, self.action_name)
        elif self.action_type == 2:
            self.action_name = item_names.get(self.action_id, self.action_name)

    def _text(self):
        return f"{self.target_name} cancel cast {self.action_name}"

    def _str_event(self):
        return f"network_actor_cast_cancel|{self.target_name}|{self.target_id}|{self.action_id}|{self.action_name}"


category_event_map = {
    6: DeathEvent,
    22: EffectUpdateEvent,
    54: TargetableEvent,
    35: TetherEvent,
    5: JobChangeEvent,
    21: EffectRemoveEvent,
    23: dot_hot_event,
    4: CombatStateChangeEvent,
    34: TargetIconEvent,
    15: CastCancelEvent,
}


class ActorControl(BaseProcessors):
    opcode = "ActorControl"
    struct = ServerActorControl

    @staticmethod
    def event(bundle_header, message_header, raw_message, struct_message: ServerActorControl):
        return category_event_map.get(struct_message.category, UnknownActorControlEvent)(
            bundle_header, message_header, raw_message, struct_message)
