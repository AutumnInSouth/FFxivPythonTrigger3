from ctypes import *
from random import randint

from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *

argus: list[str]
eid = eval(argus[0])


class Memory:
    def __getattr__(self, key):
        data_type, address = key.rsplit('_', 1)
        match data_type:
            case 'qword':
                reader = read_ulonglong
            case 'dword':
                reader = read_ulong
            case 'word':
                reader = read_ushort
            case 'byte':
                reader = read_ubyte
            case 'float':
                reader = read_float
            case _:
                raise KeyError(key)
        return reader(int(address, 16) - 0x140000000 + BASE_ADDR)

    def __setattr__(self, key, value):
        data_type, address = key.rsplit('_', 1)
        match data_type:
            case 'qword':
                writer = write_ulonglong
            case 'dword':
                writer = write_ulong
            case 'word':
                writer = write_ushort
            case 'byte':
                writer = write_ubyte
            case 'float':
                writer = write_float
            case _:
                raise KeyError(key)
        writer(int(address, 16) - 0x140000000 + BASE_ADDR, value)


module_address = find_signature_point("48 83 3D * * * * ? 74 ? E8 ? ? ? ? 48 8B C8 E8 ? ? ? ? 3C ? 0F B6 CB") + 1 + BASE_ADDR
num_of_element_address = find_signature_point("83 3D * * * * ? 0F 85 ? ? ? ? 48 8B 0D ? ? ? ? 83 B9 ? ? ? ? ?") + 1 + BASE_ADDR
unk_address = find_signature_point("48 8B 05 * * * * 48 85 C0 74 ? 39 78 ? 75 ?") + BASE_ADDR
target_actor_address = find_signature_point("48 89 35 * * * * E8 ? ? ? ? E8 ? ? ? ?") + BASE_ADDR

exec_start = CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + find_signature_address(
    "4C 8B DC 41 57 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 33 C4 48 89 84 24 ? ? ? ? 48 8B 05 ? ? ? ?"
))
init_start = CFUNCTYPE(c_int64, c_int64, c_int64, c_int64, c_void_p, c_uint, c_void_p)(BASE_ADDR + find_signature_point(
    "E8 * * * * 48 8D 44 24 ? 4C 8B C6"
))
get_evt_base = CFUNCTYPE(c_int64, c_int64, c_uint, c_int64)(BASE_ADDR + find_signature_address(
    "48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 44 8B F2 4D 8B F8"
))

module = read_ulonglong(module_address)
actor_ptr = addressof(plugins.XivMemory.targets.current or plugins.XivMemory.actor_table.me)
base = get_evt_base(module, eid, actor_ptr)
if base:
    v3 = c_int64(base)
    write_ulonglong(num_of_element_address, 0)
    if init_start(module, read_ulonglong(unk_address), actor_ptr, addressof(v3), 1, (c_uint * 4)()):
        write_ulonglong(target_actor_address, actor_ptr)
        exec_start(module)
