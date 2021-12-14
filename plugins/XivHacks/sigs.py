from FFxivPythonTrigger.memory import BASE_ADDR, read_uint
from FFxivPythonTrigger.text_pattern import find_signature_address, find_signature_point


def find_ninj_stiff_addr(sig):
    a1 = find_signature_point(sig) + BASE_ADDR + 0x1b
    return read_uint(a1) + a1 + 4


sigs = {
    "zoom_cam_ptr": {
        'call': find_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 48 83 3D ? ? ? ? ? 74 ? E8 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "zoom_cam_collision_jmp": {
        'call': find_signature_address,
        'param': "0F 84 ? ? ? ? F3 0F 10 54 24 60 F3 0F 10 44 24 64 F3 41 0F 5C D5",
        'add': BASE_ADDR,
    },
    "zoom_zoom_offset": {
        'call': find_signature_address,
        'param': "F3 0F ? ? ? ? ? ? 48 8B ? ? ? ? ? 48 85 ? 74 ? F3 0F ? ? ? ? ? ? 48 83 C1",
        'add': BASE_ADDR + 4,
    },
    "zoom_fov_offset": {
        'call': find_signature_address,
        'param': "F3 0F ? ? ? ? ? ? 0F 2F ? ? ? ? ? 72 ? F3 0F ? ? ? ? ? ? 48 8B",
        'add': BASE_ADDR + 4,
    },
    "zoom_angle_offset": {
        'call': find_signature_address,
        'param': "F3 0F 10 B3 ? ? ? ? 48 8D ? ? ? F3 44 ? ? ? ? ? ? ? F3 44",
        'add': BASE_ADDR + 4,
    },
    "zoom_cam_distance_reset": {
        'call': find_signature_address,
        'param': "F3 0F 10 05 ? ? ? ? EB ? F3 0F 10 05 ? ? ? ? F3 0F 10 94 24 B0 00 00 00",
        'add': BASE_ADDR,
    },
    "swing_sync": {
        'call': find_signature_address,
        'param': "F6 05 ? ? ? ? ? 74 ? 0F 2F 05 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "swing_read": {
        'call': find_signature_point,
        'param': "E8 * * * * 8B D0 48 8B CE E8 ? ? ? ? 49 8B D7",
        'add': BASE_ADDR,
    },
    "action_hook": {
        'call': find_signature_address,
        'param': "4C 89 44 24 ? 53 56 57 41 54 41 57",
        'add': BASE_ADDR,
    },
    "skill_animation_lock_local": {
        'call': find_signature_address,
        'param': "41 C7 45 08 ? ? ? ? EB ? 41 C7 45 08",
        'add': BASE_ADDR,
    },
    "ninj_stiff": {
        'call': find_ninj_stiff_addr,
        'param': "E8 * * * * C6 83 ? ? ? ? ? EB ? 0F 57 C9",
    },
    "speed_main": {
        'call': find_signature_point,
        'param': "E8 * * * * 44 0F 28 D8 E9 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "speed_fly": {
        'call': find_signature_address,
        'param': "40 ? 48 83 EC ? 48 8B ? 48 8B ? FF 90 ? ? ? ? 48 85 ? 75",
        'add': BASE_ADDR,
    },
    "actor_hit_box_get": {
        'call': find_signature_point,
        'param': "E8 * * * * F3 0F 58 F0 F3 0F 10 05 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "cutscene_skip": {
        'call': find_signature_address,
        'param': "? 32 DB EB ? 48 8B 01",
        'add': BASE_ADDR
    },
    "no_misdirect": {
        'call': find_signature_address,
        'param': "0F 84 ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? 0F B6 D8 E8 ? ? ? ? 84 C0 0F 84 ? ? ? ?",
        'add': BASE_ADDR
    },
    "no_forced_march": {
        'call': find_signature_address,
        'param': "? ? ? ? 83 F9 ? 0F 85 ? ? ? ? 48 8B 0E 48 81 C1 ? ? ? ?",
        'add': BASE_ADDR
    },
    "afk_timer_write": {
        'call': find_signature_address,
        'param': "75 ? 0F 28 C7 0F 28 CF",
        'add': BASE_ADDR
    },
    "afk_timer_write2": {
        'call': find_signature_address,
        'param': "F3 0F 11 51 ? 33 C9",
        'add': BASE_ADDR
    },
}
