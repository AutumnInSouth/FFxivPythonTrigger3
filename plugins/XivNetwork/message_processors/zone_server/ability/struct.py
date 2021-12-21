from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class ServerActionEffectHeader(OffsetStruct({
    'animation_target_id': c_uint,
    'unk1': c_uint,
    'action_id': c_uint,
    'global_effect_counter': c_uint,
    'animation_lock_time': c_float,
    'some_target_id': c_uint,
    'hidden_animation': c_ushort,
    'rotation': c_ushort,
    'action_animation_id': c_ushort,
    'variantion': c_ubyte,
    'effect_display_type': c_ubyte,
    'unk2': c_ubyte,
    'effect_count': c_ubyte,
    'padding': c_ushort,
})):
    animation_target_id: int
    unk1: int
    action_id: int
    global_effect_counter: int
    animation_lock_time: float
    some_target_id: int
    hidden_animation: int
    rotation: int
    action_animation_id: int
    variantion: int
    effect_display_type: int
    unk2: int
    effect_count: int
    padding: int


class ServerActionEffectEntry(OffsetStruct({
    'type': c_ubyte,
    'param1': c_ubyte,
    'param2': c_ubyte,
    'param3': c_ubyte,
    'param4': c_ubyte,
    'param5': c_ubyte,
    'main_param': c_ushort,
})):
    type: int
    param1: int
    param2: int
    param3: int
    param4: int
    param5: int
    main_param: int


class ServerActionEffectType:
    max_count = 0
    header: ServerActionEffectHeader
    padding1: int
    padding2: int
    effects: list[list[ServerActionEffectEntry]]
    padding3: int
    padding4: int
    target_id: list[int]
    padding5: int


class ServerActionEffect1(OffsetStruct({
    'header': ServerActionEffectHeader,
    'padding1': c_uint,
    'padding2': c_ushort,
    'effects': ServerActionEffectEntry * 8 * 1,
    'padding3': c_ushort,
    'padding4': c_uint,
    'target_id': c_ulonglong * 1,
    'padding5': c_uint,
}), ServerActionEffectType):
    max_count = 1


class ServerActionEffect8(OffsetStruct({
    'header': ServerActionEffectHeader,
    'padding1': c_uint,
    'padding2': c_ushort,
    'effects': ServerActionEffectEntry * 8 * 8,
    'padding3': c_ushort,
    'padding4': c_uint,
    'target_id': c_ulonglong * 8,
    'padding5': c_uint,
}, 0x27c), ServerActionEffectType):
    max_count = 8


class ServerActionEffect16(OffsetStruct({
    'header': ServerActionEffectHeader,
    'padding1': c_uint,
    'padding2': c_ushort,
    'effects': ServerActionEffectEntry * 8 * 16,
    'padding3': c_ushort,
    'padding4': c_uint,
    'target_id': c_ulonglong * 16,
    'padding5': c_uint,
}, 0x4BC), ServerActionEffectType):
    max_count = 16


class ServerActionEffect24(OffsetStruct({
    'header': ServerActionEffectHeader,
    'padding1': c_uint,
    'padding2': c_ushort,
    'effects': ServerActionEffectEntry * 8 * 24,
    'padding3': c_ushort,
    'padding4': c_uint,
    'target_id': c_ulonglong * 24,
    'padding5': c_uint,
}), ServerActionEffectType):
    max_count = 24


class ServerActionEffect32(OffsetStruct({
    'header': ServerActionEffectHeader,
    'padding1': c_uint,
    'padding2': c_ushort,
    'effects': ServerActionEffectEntry * 8 * 32,
    'padding3': c_ushort,
    'padding4': c_uint,
    'target_id': c_ulonglong * 32,
    'padding5': c_uint,
}), ServerActionEffectType):
    max_count = 32


class ServerActionEffectDisplayType:
    HideActionName = 0
    ShowActionName = 1
    ShowItemName = 2
    MountName = 13


SWING_TYPES = {
    0x1: {'ability', 'miss'},
    0x2: {'ability'},
    0x3: {'ability'},
    0x4: {'healing'},
    0x5: {'blocked', 'ability'},
    0x6: {'parry', 'ability'},
    0x7: {'invincible'},
    0xA: {'power_drain'},
    0xB: {'power_healing'},
    0xD: {'tp_healing'},
    0xE: {'buff', 'to_target'},
    0xF: {'buff', 'to_source'},
    0x18: {'threat'},
    0x19: {'threat'},
    0x1B: {'combo'},
    0x20: {'knock_back'},
    0x21: {'absorb'},
    0x33: {'instant_death'},
    # 0x34: {'buff'},
    0x37: {'buff', 'resistance'},
    0x3D: {'gauge_add'},
}

TYPE_HAVE_AMOUNT = {'ability', 'healing', 'power_drain', 'power_healing''tp_healing'}
TYPE_HAVE_CRITICAL_DIRECT = {'ability', 'healing'}
ABILITY_TYPE = {
    1: {'physics', 'blow'},
    2: {'physics', 'slash'},
    3: {'physics', 'spur'},
    4: {'physics', 'shoot'},
    5: {'magic'},
    6: {'diablo'},
    7: {'sonic'},
    8: {'limit_break'},
}
ABILITY_SUB_TYPE = {
    1: {'fire'},
    2: {'ice'},
    3: {'wind'},
    4: {'ground'},
    5: {'thunder'},
    6: {'water'},
    7: {'unaspected'},
}
