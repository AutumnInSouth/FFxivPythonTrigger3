from ctypes import *
from random import randint

from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *

"""
sub_140A8A410 = CFUNCTYPE(c_void_p, c_int64, c_int64, c_ubyte)(BASE_ADDR + 0x0A8A410)
current = plugins.XivMemory.targets.current
sub_140A8A410(read_ulonglong(BASE_ADDR + 0x1DF0080),addressof(current) , 0)
"""


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


"""
# cn-5.58
# NumOfElements = m.qword_141D604E8
__int64 sub_140761DF0()
__int64 __fastcall sub_1406CA6A0(_DWORD *a1, __int64 *a2)
__int64 __fastcall sub_140A9A830(__int64 a1, __int64 a2, __int64 a3, __int64 **a4, unsigned int a5, unsigned int *a6)
__int64 __fastcall sub_140A9AB60(__int64 a1, __int64 a2, __int64 a3, __int64 **a4, unsigned int a5, unsigned int *a6)
__int64 __fastcall sub_140A98460(__int64 a1)
__int64 sub_140761E10()

uint v2[4];
int64 v3[34];

sub_140761DF0();
v1 = sub_1406CA6A0((_DWORD *)actor_ptr, v3);
v2[0] = 0;
qword_141D600E0 = 0i64;
NumOfElements = 0i64;
byte_141D604F0 = 0;
sub_140A9A830(qword_141DF0080, qword_141DB17A0, actor_ptr, v3, v1, v2);
sub_140A9AB60(qword_141DF0080, qword_141DB17A0, actor_ptr, v3, v1, v2);
if ( (_DWORD)NumOfElements )
{
  qword_141D600E0 = actor_ptr;
  sub_140A98460(qword_141DF0080);
  sub_140761E10();
}
"""
sub_1406CA6A0 = CFUNCTYPE(c_int64, c_void_p, c_void_p)(BASE_ADDR + 0x06CA6A0)
sub_140A9A830 = CFUNCTYPE(c_int64, c_int64, c_int64, c_int64, c_void_p, c_uint, c_void_p)(BASE_ADDR + 0x0A9A830)
sub_140A9AB60 = CFUNCTYPE(c_int64, c_int64, c_int64, c_int64, c_void_p, c_uint, c_void_p)(BASE_ADDR + 0x0A9AB60)
sub_140A98460 = CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + 0x0A98460)
sub_140761E10 = CFUNCTYPE(c_int64)(BASE_ADDR + 0x0761E10)
sub_140A6D8E0 = CFUNCTYPE(c_int64, c_int64, c_uint, c_int64)(BASE_ADDR + 0x0A6D8E0)


argus: list[str]
eid = eval(argus[0])

actor_ptr = addressof(plugins.XivMemory.targets.current or plugins.XivMemory.actor_table.me)
m = Memory()
base = sub_140A6D8E0(m.qword_141DF0080, eid, actor_ptr)
print(f"base: {hex(base)}")
if base:
    v2 = (c_uint * 4)()
    v3 = c_int64(base)
    m.qword_141D600E0 = 0
    m.qword_141D604E8 = 0
    m.byte_141D604F0 = 0
    sub_140A9A830(m.qword_141DF0080, m.qword_141DB17A0, actor_ptr, addressof(v3), 1, v2)
    # sub_140A9AB60(m.qword_141DF0080, m.qword_141DB17A0, actor_ptr, addressof(v3), 1, v2)
    if m.qword_141D604E8:
        m.qword_141D600E0 = actor_ptr
        sub_140A98460(m.qword_141DF0080)
