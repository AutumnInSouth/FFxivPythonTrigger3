from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

from ..utils import NetworkZoneServerEvent, BaseProcessors
from ..common import status_effect, vector3_u16


class ServerNpcSpawn(OffsetStruct({
    'gimmick_id': c_uint,
    'u2b': c_ubyte,
    'u2ab': c_ubyte,
    'gm_rank': c_ubyte,
    'u3b': c_ubyte,
    'aggression_mode': c_ubyte,
    'online_status': c_ubyte,
    'u3c': c_ubyte,
    'pose': c_ubyte,
    'u4': c_uint,
    'target_id': c_ulonglong,
    'u6': c_uint,
    'u7': c_uint,
    'main_weapon_model': c_ulonglong,
    'sec_weapon_model': c_ulonglong,
    'craft_tool_model': c_ulonglong,
    'u14': c_uint,
    'u15': c_uint,
    'b_npc_base': c_uint,
    'b_npc_name': c_uint,
    'level_id': c_uint,
    'u19': c_uint,
    'director_id': c_uint,
    'spawner_id': c_uint,
    'parent_actor_id': c_uint,
    'hp_max': c_uint,
    'hp_current': c_uint,
    'display_flags': c_uint,
    'fate_id': c_ushort,
    'mp_current': c_ushort,
    'unknown1': c_ushort,
    'unknown2': c_ushort,
    'model_chara': c_ushort,
    'rotation': c_ushort,
    'active_minion': c_ushort,
    'spawn_index': c_ubyte,
    'state': c_ubyte,
    'persistant_emote': c_ubyte,
    'model_type': c_ubyte,
    'subtype': c_ubyte,
    'voice': c_ubyte,
    'u25c': c_ushort,
    'enemy_type': c_ubyte,
    'level': c_ubyte,
    'class_job': c_ubyte,
    'u26d': c_ubyte,
    'u27a': c_ushort,
    'current_mount': c_ubyte,
    'mount_head': c_ubyte,
    'mount_body': c_ubyte,
    'mount_feet': c_ubyte,
    'mount_color': c_ubyte,
    'scale': c_ubyte,
    'elemental_level': c_ushort,
    'element': c_ushort,
    'effect': status_effect.StatusEffect30,
    'pos': vector3_u16.Vector3U16,
    'models': c_uint * 10,
    '_name': c_char * 32,
    'look': c_ubyte * 26,
    '_fc_tag': c_char * 6,
    'unk30': c_uint,
    'unk31': c_uint,
    'b_npc_part_slot': c_ubyte,
    'unk32': c_ubyte,
    'unk33': c_ushort,
    'unk34': c_uint,

})):
    gimmick_id: int
    gm_rank: int
    aggression_mode: int
    online_status: int
    pose: int
    target_id: int
    main_weapon_model: int
    sec_weapon_model: int
    craft_tool_model: int
    b_npc_base: int
    b_npc_name: int
    level_id: int
    director_id: int
    spawner_id: int
    parent_actor_id: int
    hp_max: int
    hp_current: int
    display_flags: int
    fate_id: int
    mp_current: int
    unknown1: int
    unknown2: int
    model_chara: int
    rotation: int
    active_minion: int
    spawn_index: int
    state: int
    persistant_emote: int
    model_type: int
    subtype: int
    voice: int
    enemy_type: int
    level: int
    class_job: int
    current_mount: int
    mount_head: int
    mount_body: int
    mount_feet: int
    mount_color: int
    scale: int
    elemental_level: int
    element: int
    effect: status_effect.StatusEffect30
    pos: vector3_u16.Vector3U16
    models: int
    look: list[int]
    b_npc_part_slot: int

    @property
    def name(self):
        return self._name.decode('utf-8', 'ignore')

    @property
    def fc_tag(self):
        return self._fc_tag.decode('utf-8', 'ignore')


class ServerNpcSpawnEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'npc_spawn'
    struct_message: ServerNpcSpawn

    # def __str__(self):
    #     msg = self.struct_message
    #     return f'map_effect {self.message_header.actor_id:x} - {msg.param1:x}|{msg.param2:x}|{msg.param3:x}|{msg.param4:x}'
    #
    # def str_event(self):
    #     msg = self.struct_message
    #     return f"network_map_effect|{self.message_header.actor_id:x}|{msg.param1:x}|{msg.param2:x}|{msg.param3:x}|{msg.param4:x}"


class NpcSpawn(BaseProcessors):
    opcode = "NpcSpawn"
    struct = ServerNpcSpawn
    event = ServerNpcSpawnEvent
