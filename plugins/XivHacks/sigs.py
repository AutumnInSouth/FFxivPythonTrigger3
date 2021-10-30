from FFxivPythonTrigger.memory import BASE_ADDR, read_uint
from FFxivPythonTrigger.text_pattern import find_unique_signature_address, find_unique_signature_point


def find_ninj_stiff_addr(sig):
    a1 = find_unique_signature_point(sig) + BASE_ADDR + 0x1b
    return read_uint(a1) + a1 + 4


sigs = {
    "zoom_cam_ptr": {
        'call': find_unique_signature_point,
        'param': "48 8D 0D * * * * 45 33 C0 33 D2 C6 40 09 01",
        'add': BASE_ADDR,
    },
    "zoom_cam_collision_jmp": {
        'call': find_unique_signature_address,
        'param': "0F 84 ? ? ? ? F3 0F 10 54 24 60 F3 0F 10 44 24 64 F3 41 0F 5C D5",
        'add': BASE_ADDR,
    },
    "zoom_zoom_offset": {
        'call': find_unique_signature_address,
        'param': "F3 0F ? ? ? ? ? ? 48 8B ? ? ? ? ? 48 85 ? 74 ? F3 0F ? ? ? ? ? ? 48 83 C1",
        'add': BASE_ADDR + 4,
    },
    "zoom_fov_offset": {
        'call': find_unique_signature_address,
        'param': "F3 0F ? ? ? ? ? ? 0F 2F ? ? ? ? ? 72 ? F3 0F ? ? ? ? ? ? 48 8B",
        'add': BASE_ADDR + 4,
    },
    "zoom_angle_offset": {
        'call': find_unique_signature_address,
        'param': "F3 0F 10 B3 ? ? ? ? 48 8D ? ? ? F3 44 ? ? ? ? ? ? ? F3 44",
        'add': BASE_ADDR + 4,
    },
    "zoom_cam_distance_reset": {
        'call': find_unique_signature_address,
        'param': "F3 0F 10 05 ? ? ? ? EB ? F3 0F 10 05 ? ? ? ? F3 0F 10 94 24 B0 00 00 00",
        'add': BASE_ADDR,
    },
    "swing_sync": {
        'call': find_unique_signature_address,
        'param': "F6 05 ? ? ? ? ? 74 ? 0F 2F 05 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "swing_read": {
        'call': find_unique_signature_address,
        'param': "40 53 57 41 56 41 57 48 83 EC ? 4C 8B 35 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "action_hook": {
        'call': find_unique_signature_address,
        'param': "4C 89 44 24 ? 53 56 57 41 54 41 57",
        'add': BASE_ADDR,
    },
    "skill_animation_lock_local": {
        'call': find_unique_signature_address,
        'param': "41 C7 45 08 ? ? ? ? EB ? 41 C7 45 08",
        'add': BASE_ADDR,
    },
    "ninj_stiff": {
        'call': find_ninj_stiff_addr,
        'param': "E8 * * * * C6 83 ? ? ? ? ? EB ? 0F 57 C9",
    },
    "speed_main": {
        'call': find_unique_signature_address,
        'param': "48 83 EC ? 80 B9 04 01 00 00 ? 74",
        'add': BASE_ADDR,
    },
    "speed_fly": {
        'call': find_unique_signature_address,
        'param': "40 ? 48 83 EC ? 48 8B ? 48 8B ? FF 90 ? ? ? ? 48 85 ? 75",
        'add': BASE_ADDR,
    },
    "actor_hit_box_get": {
        'call': find_unique_signature_point,
        'param':"E8 * * * * F3 0F 58 F0 F3 0F 10 05 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "cutscene_skip":{
        'call':find_unique_signature_address,
        'param':"? 32 DB EB ? 48 8B 01",
        'add':BASE_ADDR
    }
}
