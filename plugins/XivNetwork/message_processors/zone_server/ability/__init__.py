from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import action_names, item_names
from .struct import *
from ...utils import NetworkZoneServerEvent, BaseProcessors
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor

MsgStructs = ServerActionEffect1 | ServerActionEffect8 | ServerActionEffect16 | ServerActionEffect24 | ServerActionEffect32


class ActionEffect(object):
    def __init__(self, effect_entry: ServerActionEffectEntry):
        self.raw_entry = effect_entry
        self.tags = set()
        self.param = 0

        if effect_entry.type in SWING_TYPES:
            self.tags = SWING_TYPES[effect_entry.type].copy()
            self.param = effect_entry.main_param
            if self.tags.intersection(TYPE_HAVE_AMOUNT):
                if effect_entry.param5 & 0x40:
                    self.param += effect_entry.param4 * 65535
                if 'ability' in self.tags:
                    self.tags.add('to_source' if effect_entry.param5 & 0xA0 else 'to_target')
                    if effect_entry.param1 & 1: self.tags.add('critical')
                    if effect_entry.param1 & 2: self.tags.add('direct')
                    main_type = effect_entry.param2 & 0xf
                    self.tags |= ABILITY_TYPE[main_type] if main_type in ABILITY_TYPE else {f"unk_main_type_{main_type}"}
                    sub_type = effect_entry.param2 >> 4
                    self.tags |= ABILITY_SUB_TYPE[sub_type] if sub_type in ABILITY_TYPE else {f"unk_sub_type_{sub_type}"}
                elif 'healing' in self.tags:
                    self.tags.add('to_source' if effect_entry.param1 & 1 else 'to_target')
                    if effect_entry.param2 & 1: self.tags.add('critical')
        else:
            self.tags.add(f"UnkType_{effect_entry.type}")
            # self.tags.add(hex(self.raw_flag)[2:].zfill(8)+"-"+hex(self.raw_amount)[2:].zfill(8))

    def __str__(self):
        return f"{self.param}{self.tags}"  # + str(self.raw_entry.get_data())


class ActionEffectEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'action_effect'
    struct_message: MsgStructs
    source_actor: 'Actor|None'
    targets: dict[int, list[ActionEffect]]

    def __init__(self, bundle_header, message_header, raw_message, struct_message: MsgStructs):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.source_id = message_header.actor_id
        effect_header = struct_message.header
        match effect_header.effect_display_type:
            case ServerActionEffectDisplayType.MountName:
                self.action_type = "mount"
            case ServerActionEffectDisplayType.ShowItemName:
                self.action_type = "item"
            case ServerActionEffectDisplayType.ShowActionName | ServerActionEffectDisplayType.HideActionName:
                self.action_type = "action"
            case t:
                self.action_type = "unknown_%s" % t
        self.action_id = effect_header.action_animation_id if self.action_type == "action" else effect_header.action_id
        effect_count = min(effect_header.effect_count, struct_message.max_count)
        self.targets = {}
        self.target_actors = {}
        for i in range(effect_count):
            effects = self.targets.setdefault(struct_message.target_id[i], [])
            for j in range(8):
                if not struct_message.effects[i][j].type: break
                effects.append(ActionEffect(struct_message.effects[i][j]))
        match self.action_type:
            case "item":
                if self.action_id > 1000000:
                    self.action_name = item_names.get(self.action_id - 1000000, 'unk') + 'hq'
                else:
                    self.action_name = item_names.get(self.action_id - 1000000, 'unk')
            case "action":
                self.action_name = action_names.get(self.action_id, 'unk')
            case t:
                self.action_name = f"{t}_{self.action_id}"

    def init(self):
        self.source_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.source_id)
        for a_id in self.targets.keys(): self.target_actors[a_id] = plugins.XivMemory.actor_table.get_actor_by_id(a_id)

    def text(self):
        self.controller.init()
        m = " / ".join(f"{getattr(self.target_actors[aid], 'name', hex(aid))}[{' ;'.join(map(str, data))}]" for aid, data in self.targets.items())
        return f"{self.source_actor.name if self.source_actor else hex(self.source_id)} use {self.action_name}({self.action_type}) on {len(self.targets)} target(s) : {m}"

    def str_event(self):
        self.controller.init()
        m = "|".join(
            f"{getattr(self.target_actors[aid], 'name', '')};{';'.join(f'{effect.param},' + ','.join(effect.tags) for effect in data)}" for aid, data
            in
            self.targets.items())
        return f"network_ability|{self.action_type}|{self.action_id}|{self.action_name}|{self.source_actor.name if self.source_actor else ''}|" + m


class Effect(BaseProcessors):
    opcode = "Effect"
    struct = ServerActionEffect1
    event = ActionEffectEvent


class AoeEffect8(BaseProcessors):
    opcode = "AoeEffect8"
    struct = ServerActionEffect8
    event = ActionEffectEvent


class AoeEffect16(BaseProcessors):
    opcode = "AoeEffect16"
    struct = ServerActionEffect16
    event = ActionEffectEvent


class AoeEffect24(BaseProcessors):
    opcode = "AoeEffect24"
    struct = ServerActionEffect24
    event = ActionEffectEvent


class AoeEffect32(BaseProcessors):
    opcode = "AoeEffect32"
    struct = ServerActionEffect32
    event = ActionEffectEvent
