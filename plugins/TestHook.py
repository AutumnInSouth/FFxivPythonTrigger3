from ctypes import *

from FFxivPythonTrigger import *
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import BASE_ADDR, read_int, read_ulonglong, read_ubyte, read_string, read_memory, read_ubytes
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.utils import err_catch
from XivMemory import se_string

TextCommandStruct = OffsetStruct({
    "cmd": POINTER(c_char),
    "t1": c_longlong,
    "tLength": c_longlong,
    "t3": c_longlong,
}, full_size=400)

TextStruct = OffsetStruct({
    "text": POINTER(c_ubyte),
    "long": (c_longlong, 0x10),
})


class TestHook(PluginBase):
    name = "test_hook"

    def __init__(self):
        super().__init__()
        self.cnt = 0
        # self.cmd_catch2(self, BASE_ADDR + 0x990B0)
        # self.h1(self, BASE_ADDR + 0x7138E0)
        self.change_sht(self, BASE_ADDR + 0x6319B0)
        # self.change_sht2(self, BASE_ADDR + 0x62EF40)

    """__int64 __fastcall sub_1406319B0(__int64 a1, __int64 *a2)"""

    @PluginHook.decorator(c_int64, [c_int64, c_int64], True)
    @err_catch
    def change_sht(self, hook, a1, a2):
        self.logger(f"{a1:x} {a2:x}", read_string(read_ulonglong(a2)))
        ans = hook.original(a1, a2)
        self.logger(hex(ans), read_string(read_ulonglong(a2)))
        # if ans: ans = 43
        return ans

    """unsigned __int64 __fastcall sub_14062EF40(__int64 a1, unsigned __int64 a2, unsigned int a3)"""

    @PluginHook.decorator(c_int64, [c_int64, c_int64, c_uint], True)
    @err_catch
    def change_sht2(self, hook, a1, a2, a3):
        self.logger(f"{a1:x} {a2:x},{a3}", read_string(read_ulonglong(a2)))
        ans = hook.original(a1, a2, a3)
        data = read_memory(TextStruct, ans)
        data=bytearray(data.text[:data.long])
        self.logger(data.hex(' '))
        self.logger('/'.join(map(str,se_string.get_message_chain(data))))
        return ans

    """__int64 __fastcall sub_1407138E0(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5) all cant change"""

    @PluginHook.decorator(c_void_p, [c_int64, c_int64, c_int64, c_int64, c_int], True)
    @err_catch
    def cmd_catch(self, hook, a1, cmd_ptr, a3, a4, is_invalid):
        data = read_memory(TextCommandStruct, cmd_ptr)
        self.logger(f"{a1:x} {a3:x} {a4:x}")
        self.logger(bytes(data.cmd[:data.tLength]).decode('utf-8'), is_invalid == 0, hex(cast(cmd_ptr, c_void_p).value))
        msg = bytearray('/s hi!'.encode('utf-8') + b'\x00' * 40)
        data.cmd = (c_ubyte * len(msg)).from_buffer(msg)
        data.tLength = len(msg) - 40
        self.logger(hex(read_ulonglong(read_ulonglong(a1) + 8) - BASE_ADDR))
        hook.original(a1, cmd_ptr, a3, a4, is_invalid)

    """_BYTE *__fastcall sub_1400990B0(__int64 a1, _QWORD *a2, __int64 a3) dialog only can change"""

    @PluginHook.decorator(c_int64, [c_int64, c_int64, c_int64], True)
    @err_catch
    def cmd_catch2(self, hook, a1, cmd_ptr, a3):
        data = read_memory(TextCommandStruct, cmd_ptr)
        self.logger(f"{a1:x} {a3:x}")
        self.logger(bytes(data.cmd[:data.tLength]).decode('utf-8'), hex(cast(cmd_ptr, c_void_p).value))
        msg = bytearray('/s hi!'.encode('utf-8') + b'\x00' * 40)
        data.cmd = (c_ubyte * len(msg)).from_buffer(msg)
        data.tLength = len(msg) - 40
        self.logger(hex(read_ulonglong(read_ulonglong(a1) + 8) - BASE_ADDR))
        ans = hook.original(a1, cmd_ptr, a3)
        self.logger(hex(ans))
        return ans
