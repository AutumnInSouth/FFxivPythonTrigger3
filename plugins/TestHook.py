import math
import traceback

from FFxivPythonTrigger import *
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import action_names, realm
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.text_pattern import search_from_text, find_signature_point, find_signature_address
from FFxivPythonTrigger.utils import err_catch
from FFxivPythonTrigger.game_utils.std_string import StdString
from XivMemory import se_string
from OmenReflect.utils import action_struct

map_sheet = realm.game_data.get_sheet('Map')


def web_to_map(pos):
    c = map_sheet[plugins.XivMemory.map_id]['SizeFactor'] / 100
    return (41.0 / c * ((pos * c / 1000 + 1024.0) / 2048.0)) + 1.0


def web_to_raw(pos):
    return pos * 0.0305 - 1000


def raw_to_web(pos):
    return (pos + 1000) / 0.0305


def map_to_web(pos):
    c = map_sheet[plugins.XivMemory.map_id]['SizeFactor'] / 100
    return int(((pos - 1) * c / 41 * 2048 - 1024) / c)


def find_ptr_end(ptr):
    i = 0
    while ptr[i] != 0:
        i += 1
    return i


class TestHook(PluginBase):
    name = "test_hook"

    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.d = set()
        # self.sub_1405D5A30(self, BASE_ADDR + 0x5D5A30)
        # self.omen_create(self, BASE_ADDR + 0x6FF1C0)
        # self.action_recast(self, BASE_ADDR + 0x07DE990)
        # self.sub_1416014C0(self, BASE_ADDR + 0x16014C0)
        # self.sub_140A41260(self, BASE_ADDR + 0xA41260)
        # self.set_omen_create(self, BASE_ADDR + 0x6F9C60)
        # for offset, _ in search_from_text("48 89 5C 24 ? 48 89 6C 24 ? 57 48 83 EC ? 48 63 C2 48 8B D9"):
        #     self.is_key_trigger(self, offset + BASE_ADDR)
        # self.facing_hook(self, BASE_ADDR + find_signature_point("E8 * * * * 80 3D ? ? ? ? ? 0F 28 F0"))
        # self.macro_concat(self, BASE_ADDR + find_signature_address(
        #     "40 53 55 57 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 33 C4 48 89 84 24 ? ? ? ? 49 8B D8"
        # ))
        # self.macro_parse_hook(self, BASE_ADDR + find_signature_address(
        #     "40 55 53 56 48 8B EC 48 83 EC ? 48 8B 05 ? ? ? ? 48 33 C4 48 89 45 ? 48 8B F1"
        # ))
        #
        # self.print_msg_hook(self, BASE_ADDR + find_signature_address(
        #     "40 55 53 56 41 54 41 57 48 8D AC 24 ?? ?? ?? ?? 48 81 EC 20 02 00 00 48 8B 05"
        # ))
        # self.b_channel_hook(self, BASE_ADDR + find_signature_address(
        #     "48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 40 32 F6 32 DB"
        # ))
        # self.interact_hook(self, BASE_ADDR + find_signature_address(
        #     "4C 8B DC 49 89 5B ? 49 89 6B ? 49 89 73 ? 57 41 54 41 55 41 56 41 57 48 83 EC ? 0F B6 B1 ? ? ? ?"
        # ))
        # h=self.mo_ui_entity(self, BASE_ADDR + find_signature_point("E8 * * * * 48 8B ? ? ? 48 8B ? ? ? 4C 8B ? ? ? 41 83 FC"))
        # self.logger(hex(h.address))
        self.cnt_down_hook(self, BASE_ADDR + find_signature_point(
            "E8 * * * * 48 8B CB E8 ? ? ? ? 83 7B ? ? 74 ? 48 8B 4B ? 48 8B 01 FF 90 ? ? ? ?"
        ))

    @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    def set_omen_create(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
        """E8 ? ? ? ? 41 80 7E ? ? 0F 85 ? ? ? ? F3 0F 10 1D ? ? ? ?"""
        self.logger(f"{source_actor_ptr:x} {skill_type} {action_id} {pos} {facing} {a6}")
        return hook.original(source_actor_ptr, skill_type, action_id, pos, facing, a6)

    """__int64 __fastcall sub_1406FF1C0(__int64 source_actor_ptr, unsigned __int16 *web_pos, float a3, __int64 action_data, float a5, unsigned int a6)"""

    @PluginHook.decorator(c_int64, [c_int64, POINTER(c_ushort), c_float, POINTER(action_struct), c_float, c_uint], True)
    def omen_create(self, hook, source_actor_ptr, web_pos, facing, action_data, a5, a6):
        if read_uint(source_actor_ptr + 0x74) > 0x20000000 and action_data[0].omen:
            self.logger(f"c1 {read_string(source_actor_ptr + 0x30)} {source_actor_ptr:x}"
                        f" ({web_to_raw(web_pos[0]):.2f},{web_to_raw(web_pos[2]):.2f},{web_to_raw(web_pos[1]):.2f})"
                        f" {facing:.2f} {action_data[0]}")
        return hook.original(source_actor_ptr, web_pos, facing, action_data, a5, a6)

    # _QWORD *__fastcall sub_1407DE990(int a1, __int64 a2, __int64 a3, __int64 a4)
    @PluginHook.decorator(c_int, [c_int, c_int64, c_int64, c_int64], True)
    def action_recast(self, hook, a1, a2, a3, a4):
        self.cnt += 1
        if self.cnt >= 10:
            hook.uninstall()
        ans = hook.original(a1, a2, a3, a4)
        self.logger(f"{ans} {a1} {a2:x} {a3:x} {a4:x}")
        return ans

    """char __fastcall sub_1404BC6B0(__int64 a1, int a2)"""

    @PluginHook.decorator(c_bool, [c_int64, c_uint], True)
    def is_key_trigger(self, hook, a1, a2):
        if a2 == 321:
            return True
        return hook.original(a1, a2)

    """float __fastcall sub_14115B800(__int64 a1)"""

    @PluginHook.decorator(c_float, [c_int64], True)
    def facing_hook(self, hook, a1):
        self.logger(f"{a1:x}")
        hook.uninstall()
        return hook.original(a1)

    """__int64 __fastcall sub_1406325E0(__int64 a1, __int64 a2, __int64 a3, char a4, unsigned __int16 a5)"""
    """40 53 55 57 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 33 C4 48 89 84 24 ? ? ? ? 49 8B D8"""

    @PluginHook.decorator(c_int64, [c_int64, c_int64, c_int64, c_char, c_ushort], True)
    def macro_concat(self, hook, a1, a2, a3, a4, a5):
        orig = read_string(read_ulonglong(a1 + 136))
        res = hook.original(a1, a2, a3, a4, a5)
        new = read_string(read_ulonglong(a1 + 136))
        self.logger(f"{a1:x} {a2:x} {a3:x} {a4} {a5}\n{orig}\n{new}")
        return res

    """40 55 53 56 48 8B EC 48 83 EC ? 48 8B 05 ? ? ? ? 48 33 C4 48 89 45 ? 48 8B F1"""

    @PluginHook.decorator(c_int64, [c_int64, POINTER(c_int64)], True)
    def macro_parse_hook(self, hook, a1, a2):
        raw = read_memory(c_char * 50, a2[0]).value
        res = hook.original(a1, a2)
        self.logger(raw, read_memory(c_char * 50, a2[0]).value, read_string(read_ulonglong(a1 + 136)), hex(res))
        return res

    # __int64 __fastcall print_msg_hook(__int64 manager, unsigned __int16 channel_id, __int64 p_sender, __int64 p_msg, int sender_id, char parm)
    # 40 55 53 56 41 54 41 57 48 8D AC 24 ?? ?? ?? ?? 48 81 EC 20 02 00 00 48 8B 05
    @PluginHook.decorator(c_int64, [c_int64, c_ushort, POINTER(c_char_p), POINTER(c_char_p), c_uint, c_ubyte], True)
    def print_msg_hook(self, hook, manager, channel_id, p_sender, p_msg, sender_id, parm):
        try:
            from XivMemory.se_string import ChatLog, get_message_chain, group_message_chain
            sender = group_message_chain(get_message_chain(bytearray(p_sender[0])))
            msg = group_message_chain(get_message_chain(bytearray(p_msg[0])))
            need_fix = False
            for node in msg:
                if node.Type == "Interactable/Item" and node.is_hq and node.is_collect:
                    need_fix = True
                    node._display_name = node.display_name + "(fix)"
                    node.is_collect = False
            if need_fix:
                new_msg = StdString(b''.join(m.encode_group() for m in msg))
                p_msg = cast(addressof(new_msg), POINTER(c_char_p))
            sender_str = "".join(str(n) for n in sender)
            msg_str = "".join(str(n) for n in msg)
            self.logger(f"({channel_id}/{sender_id:x}/{parm:x}){sender_str}:{msg_str}")
        except:
            self.logger.error(traceback.format_exc())
        return hook.original(manager, channel_id, p_sender, p_msg, sender_id, parm)

    """__int64 __fastcall sub_140715F30(__int64 a1, int a2, int a3)"""

    @PluginHook.decorator(c_ubyte, [c_int64, c_int, c_int], True)
    def b_channel_hook(self, hook, a1, a2, a3):
        try:
            self.logger(f"{a1:x} {a2:x} {a3:x}")
        except:
            self.logger.error(traceback.format_exc())
            hook.uninstall()
        return hook.original(a1, a2, a3)

    """
    char __fastcall sub_140ACAFB0(__int64 *a1, _QWORD *a2, unsigned __int8 a3, int a4, int a5, unsigned __int8 a6, int a7)
    """

    @PluginHook.decorator(c_ubyte, [c_int64, c_int64, c_ubyte, c_int, c_int, c_ubyte, c_int], True)
    def interact_hook(self, hook, a1, a2, a3, a4, a5, a6, a7):
        try:
            self.logger(f"{a1:x} {a2:x} {a3:x} {a4:x} {a5:x} {a6:x} {a7:x}")
        except:
            self.logger.error(traceback.format_exc())
            hook.uninstall()
        return hook.original(a1, a2, a3, a4, a5, a6, a7)

    @PluginHook.decorator(c_void_p, [c_int64, c_int64], True)
    def mo_ui_entity(self, hook, a1, a2):
        try:
            self.a1 = a1
            self.a2 = a2
        except:
            self.logger.error(traceback.format_exc())
            hook.uninstall()
        return hook.original(a1, a2)

    """
    __int64 __fastcall sub_1402A8930(__int64 a1)
    """

    @PluginHook.decorator(c_int64, [c_int64], True)
    def cnt_down_hook(self, hook, a1):
        res = hook.original(a1)
        try:
            new_update = perf_counter()
            self.logger(f"{a1:#x} {read_float(a1 + 40):.2f}")
            self.last_update = new_update
        except:
            self.logger.error(traceback.format_exc())
            hook.uninstall()
        return res
