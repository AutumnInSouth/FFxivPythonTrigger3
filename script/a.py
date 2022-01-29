from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *

print_chat_log_offset = find_signature_address("40 55 53 56 41 54 41 57 48 8D AC 24 ?? ?? ?? ?? 48 81 EC 20 02 00 00 48 8B 05")
do_text_command_offset = find_signature_address("48 89 5C 24 ? 57 48 83 EC 20 48 8B FA 48 8B D9 45 84 C9")
text_command_ui_module_offset = find_signature_point("48 8B 05 * * * * 48 8B D9 8B 40 14 85 C0")
player_name_addr = find_signature_point("48 8D 0D * * * * E8 ? ? ? ? 0F B6 F0 0F B6 05 ? ? ? ?") + 1 + BASE_ADDR


def player_name():
    return read_string(player_name_addr)


ui_module = read_memory(POINTER(c_int64), text_command_ui_module_offset + BASE_ADDR)
_do_text_command = CFUNCTYPE(c_int64, c_void_p, c_void_p, c_int64, c_char)(do_text_command_offset + BASE_ADDR)
TextCommandStruct = OffsetStruct({"cmd": c_void_p, "t1": c_longlong, "tLength": c_longlong, "t3": c_longlong}, full_size=400)


def do_text_command(command: str | bytes):
    if isinstance(command, str): command = command.encode('utf-8')
    cmd_size = len(command)
    cmd = OffsetStruct({"cmd": c_char * cmd_size}, full_size=cmd_size + 30)(cmd=command)
    arg = TextCommandStruct(cmd=addressof(cmd), t1=64, tLength=cmd_size + 1, t3=0)
    return _do_text_command(ui_module[0], addressof(arg), 0, 0)
print(ui_module[0])
print(plugins.XivMemory.calls.do_text_command("/e 1"))
print(plugins.XivMemory.calls.do_text_command("/s 1"))
#do_text_command("/s 1")
