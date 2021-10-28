from .struct import *
from ...utils import NetworkZoneServerEvent

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
                if effect_entry.param5 == 64:
                    self.param += effect_entry.param4 * 65535
                if self.tags.intersection(TYPE_HAVE_CRITICAL_DIRECT):
                    if effect_entry.param1 & 1: self.tags.add('critical')
                    if effect_entry.param1 & 2: self.tags.add('direct')
                if 'ability' in self.tags:
                    main_type = effect_entry.param2 & 0xf
                    self.tags |= ABILITY_TYPE[main_type] if main_type in ABILITY_TYPE else {f"unk_main_type_{effect_entry.param3}"}
                    sub_type = effect_entry.param2 >> 4
                    self.tags |= ABILITY_SUB_TYPE[sub_type] if sub_type in ABILITY_TYPE else {f"unk_sub_type_{effect_entry.param3}"}
        else:
            self.tags.add(f"UnkType_{effect_entry.type}")
            # self.tags.add(hex(self.raw_flag)[2:].zfill(8)+"-"+hex(self.raw_amount)[2:].zfill(8))

    def __str__(self):
        return f"{self.param}{self.tags}" + str(self.raw_entry.get_data())


class ActionEffectEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'action_effect'
    struct_message: MsgStructs

    def __init__(self, bundle_header, message_header, raw_message, struct_message:MsgStructs):
        super().__init__(bundle_header, message_header, raw_message, struct_message)

        self.source_id = message_header.actor_id
        effect_header = struct_message.header
        if effect_header.effect_display_type == ServerActionEffectDisplayType.MountName:
            self.action_type = "mount"
        elif effect_header.effect_display_type == ServerActionEffectDisplayType.ShowItemName:
            self.action_type = "item"
        elif effect_header.effect_display_type == ServerActionEffectDisplayType.ShowActionName or effect_header.effect_display_type == ServerActionEffectDisplayType.HideActionName:
            self.action_type = "action"
        else:
            self.action_type = "unknown_%s" % effect_header.effect_display_type
        self.action_id = effect_header.action_animation_id if self.action_type == "action" else effect_header.action_id
        effect_count = min(effect_header.effect_count, max_count)
        self.targets = dict()
        for i in range(effect_count):
            effects = list()
            for j in range(8):
                if not raw_msg.effects[i][j].type: break
                effects.append(ActionEffect(raw_msg.effects[i][j]))
            self.targets[raw_msg.target_id[i]] = effects