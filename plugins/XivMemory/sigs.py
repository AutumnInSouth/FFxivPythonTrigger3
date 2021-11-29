from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.text_pattern import find_signature_address, find_signature_point

sigs = {
    "actor_table": {
        'call': find_signature_point,
        'param': "48 8d ? * * * * e8 ? ? ? ? 48 8b ? 48 8b ? 48 8d ? ? ? ? ? "
                 "e8 ? ? ? ? 48 8d ? ? ? ? ? ba ? ? ? ? e8 ? ? ? ? 89 2f",
        'add': BASE_ADDR,
    },
    "combo_state": {
        'call': find_signature_point,
        'param': "F3 0F 11 05 * * * * 48 83 C2 ?",
        'add': BASE_ADDR,
    },
    "skill_queue": {
        'call': find_signature_point,
        'param': "F3 0F 11 05 * * * * 48 83 C2 ?",
        'add': BASE_ADDR + 8,
    },
    "cool_down_group": {
        'call': find_signature_point,
        'param': "0f b7 0d * * * * 84 c0",
        'add': BASE_ADDR + 0x76,
    },
    "enemies_base": {
        'call': find_signature_point,
        'param': "48 8b 0d * * * * 4c 8b c0 33 d2",
        'add': BASE_ADDR,
    },
    "gauge": {
        'call': find_signature_point,
        'param': "48 8d ? * * * * e8 ? ? ? ? 80 be 13 07 ? ?",
        'add': BASE_ADDR + 0x10,
    },
    "player_info": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 0F B6 F0 0F B6 05 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "targets": {
        'call': find_signature_point,
        'param': "48 8B 05 * * * * 48 8D 0D ? ? ? ? FF 50 ? 48 85 DB",
        'add': BASE_ADDR,
    },
    "zone": {
        'call': find_signature_point,
        'param': "0f b7 ? * * * * 48 8d ? ? ? f3 0f ? ? 33 d2",
        'add': BASE_ADDR,
    },
    "skill_animation_lock": {
        'call': find_signature_point,
        'param': "F3 0F ? ? * * * * 41 F6 47 20",
        'add': BASE_ADDR,
    },
    "movement": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? 0F B6 D8",
        'add': BASE_ADDR,
    },
    "inventory": {
        'call': find_signature_point,
        'param': "4C 8B 0D * * * * 8B D9",
        'add': BASE_ADDR,
    },
    "party": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 48 8B 4E ? 48 8B D8",
        'add': BASE_ADDR,
    },
    "world_id_hook": {
        'call': find_signature_address,
        'param': "48 89 5C 24 ? 57 48 83 EC ? 0F B6 42 ? 48 8B FA 88 81 ? ? ? ? 48 8B D9 0F B6 42 ?",
        'add': BASE_ADDR,
    },
    "mission_info": {
        'call': find_signature_point,
        'param': "48 83 3D * * * * ? 49 8B F8",
        'add': BASE_ADDR + 1,
    },
    "pvp_action": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * 40 0F 95 C6",
        'add': BASE_ADDR,
    },
    "markings": {
        'call': find_signature_point,
        'param': "48 8D ? * * * * 41 B0 ? E8 ? ? ? ? 85 C0",
        'add': BASE_ADDR,
    },
    "mo_ui_entity_hook": {
        'call': find_signature_point,
        'param': "E8 * * * * 48 8B ? ? ? 48 8B ? ? ? 4C 8B ? ? ? 41 83 FC",
        'add': BASE_ADDR,
    },
    "do_text_command": {
        'call': find_signature_address,
        'param': "48 89 5C 24 ? 57 48 83 EC 20 48 8B FA 48 8B D9 45 84 C9",
        'add': BASE_ADDR,
    },
    "text_command_ui_module": {
        'call': find_signature_point,
        'param': "48 8B 05 * * * * 48 8B D9 8B 40 14 85 C0",
        'add': BASE_ADDR,
    },
    "do_action": {
        'call': find_signature_address,
        'param': "40 53 55 57 41 54 41 57 48 83 EC ? 83 BC 24 ? ? ? ? ?",
        'add': BASE_ADDR,
    },
    "do_action_location": {
        'call': find_signature_address,
        'param': "44 89 44 24 ? 89 54 24 ? 55 53 57",
        'add': BASE_ADDR,
    },
    "action_manager": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 8B F8 8B CF",
        'add': BASE_ADDR,
    },
    "head_mark": {
        'call': find_signature_address,
        'param': "48 89 5C 24 ? 48 89 6C 24 ? 57 48 83 EC ? 8D 42",
        'add': BASE_ADDR,
    },
    "way_mark_set": {
        'call': find_signature_address,
        'param': "48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 8B F2 49 8B E8",
        'add': BASE_ADDR,
    },
    "way_mark_clear": {
        'call': find_signature_address,
        'param': "48 89 74 24 ? 57 48 83 EC ? 8B F2 48 8B F9 83 FA ? 72 ?",
        'add': BASE_ADDR,
    },
    "way_mark_clear_all": {
        'call': find_signature_address,
        'param': "41 55 48 83 EC ? 4C 8B E9 E8 ? ? ? ? 84 C0",
        'add': BASE_ADDR,
    },
    "marking_controller": {
        'call': find_signature_point,
        'param': "48 8D ? * * * * 41 B0 ? E8 ? ? ? ? 85 C0",
        'add': BASE_ADDR,
    },
    "chat_log_hook": {
        'call': find_signature_address,
        'param': "48 89 ? ? ? 48 89 ? ? ? 48 89 ? ? ? 57 41 ? 41 ? 48 83 EC ? 48 8B ? ? 48 8B ? 48 2B ? ? 4C 8B",
        'add': BASE_ADDR,
    },
    "coordinate_main_pointer": {
        'call': find_signature_point,
        'param': "f3 0f ? ? * * * * eb ? 48 8b ? ? ? ? ? e8 ? ? ? ? 48 85",
        'add': BASE_ADDR + 0x14,
    },
    "coordinate_fly": {
        'call': find_signature_point,
        'param': "48 8d ? * * * * 84 c0 75 ? 48 8d ? ? ? ? ? 80 79 66 ? 74 ? e8 ? ? ? ? c6 87 f4 03 ? ?",
        'add': BASE_ADDR + 0x10,
    },
    "buddy_list": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 45 84 E4 75 1A F6 45 12 04",
        'add': BASE_ADDR,
    },
    "quest_manager": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 84 C0 0F 84 ? ? ? ? 83 7C 24 ? ?",
        'add': BASE_ADDR,
    },
    "is_quest_finished": {
        'call': find_signature_address,
        'param': "40 53 48 83 EC ? 8B DA 48 8B D1 81 FB ? ? ? ?",
        'add': BASE_ADDR,
    },
    'get_camera_matrix': {
        'call': find_signature_point,
        'param': 'E8 * * * * 48 8D 4C 24 ? 48 89 4c 24 ? 4C 8D 4D ? 4C 8D 44 24 ?',
        'add': BASE_ADDR,
    },
    'screen_to_world': {
        'call': find_signature_address,
        'param': '48 83 EC 48 48 8B 05 ? ? ? ? 4D 8B D1',
        'add': BASE_ADDR,
        'kwargs': {
            'unique': False,
        }
    }
}

enemies_shifts = [0x30, 0x58, 0x98, 0x20, 0x20]
mission_info_shifts = [0x568]
main_coordinate_shifts = [0xa0]
