from FFxivPythonTrigger.text_pattern import find_unique_signature_address, find_unique_signature_point

from FFxivPythonTrigger.memory import BASE_ADDR

sigs = {
    "actor_table": {
        'call': find_unique_signature_point,
        'param': "48 8d ? * * * * e8 ? ? ? ? 48 8b ? 48 8b ? 48 8d ? ? ? ? ? "
                 "e8 ? ? ? ? 48 8d ? ? ? ? ? ba ? ? ? ? e8 ? ? ? ? 89 2f",
        'add': BASE_ADDR,
    },
    "combo_state": {
        'call': find_unique_signature_point,
        'param': "F3 0F 11 05 * * * * 48 83 C2 ?",
        'add': BASE_ADDR,
    },
    "skill_queue": {
        'call': find_unique_signature_point,
        'param': "80 3d * * * * ? 0f 95 c0 48 83 c4 ?",
        'add': BASE_ADDR + 1,
    },
    "cool_down_group": {
        'call': find_unique_signature_point,
        'param': "0f b7 0d * * * * 84 c0",
        'add': BASE_ADDR + 0x76,
    },
    "enemies_base": {
        'call': find_unique_signature_point,
        'param': "48 8b 0d * * * * 4c 8b c0 33 d2",
        'add': BASE_ADDR,
    },
    "gauge": {
        'call': find_unique_signature_point,
        'param': "48 8d ? * * * * e8 ? ? ? ? 80 be 13 07 ? ?",
        'add': BASE_ADDR + 0x10,
    },
    "player_info": {
        'call': find_unique_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 0F B6 F0 0F B6 05 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "targets": {
        'call': find_unique_signature_point,
        'param': "48 8B 05 * * * * 48 8D 0D ? ? ? ? FF 50 ? 48 85 DB",
        'add': BASE_ADDR,
    },
    "zone": {
        'call': find_unique_signature_point,
        'param': "0f b7 ? * * * * 48 8d ? ? ? f3 0f ? ? 33 d2",
        'add': BASE_ADDR,
    },
    "skill_animation_lock": {
        'call': find_unique_signature_point,
        'param': "F3 0F ? ? * * * * 41 F6 47 20",
        'add': BASE_ADDR,
    },
    "movement": {
        'call': find_unique_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? 0F B6 D8",
        'add': BASE_ADDR,
    },
    "inventory": {
        'call': find_unique_signature_point,
        'param': "4C 8B 0D * * * * 8B D9",
        'add': BASE_ADDR,
    },
    "party": {
        'call': find_unique_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 48 8B 4E ? 48 8B D8",
        'add': BASE_ADDR,
    },
    "world_id_hook": {
        'call': find_unique_signature_address,
        'param': "48 89 5C 24 ? 57 48 83 EC ? 0F B6 42 ? 48 8B FA 88 81 ? ? ? ? 48 8B D9 0F B6 42 ?",
        'add': BASE_ADDR,
    },
    "mission_info": {
        'call': find_unique_signature_point,
        'param': "48 83 3D * * * * ? 49 8B F8",
        'add': BASE_ADDR + 1,
    },
    "pvp_action": {
        'call': find_unique_signature_point,
        'param': "48 8D 0D * * * * 40 0F 95 C6",
        'add': BASE_ADDR,
    },
}

enemies_shifts = [0x30, 0x58, 0x98, 0x20, 0x20]
mission_info_shifts = [0x568]
