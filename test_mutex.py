import os
import re
from ctypes import *
from FFxivPythonTrigger.memory.res import ntdll, kernel32
from FFxivPythonTrigger.memory.process import CURRENT_PROCESS_HANDLER
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


# class SYSTEM_HANDLE(OffsetStruct({
#     'ProcessId': c_ulong,
#     'CreatorBackTraceIndex': c_ushort,
#     'ObjectTypeIndex': c_byte,
#     'HandleAttributes': c_byte,
#     'HandleValue': c_ushort,
#     'Object': c_void_p,
#     'GrantedAccess': c_ulong,
# })):
#     _pack_ = 4
#     ProcessId: int
#     CreatorBackTraceIndex: int
#     ObjectTypeIndex: int
#     HandleAttributes: int
#     HandleValue: int
#     Object: any
#     GrantedAccess: int
class SYSTEM_HANDLE(Structure):
    _fields_ = [
        ("ProcessId", c_ushort),
        ("CreatorBackTraceIndex", c_ushort),
        ("ObjectTypeIndex", c_byte),
        ("HandleAttributes", c_byte),
        ("HandleValue", c_ushort),
        ("Object", c_void_p),
        ("AccessMask", c_ulong),
    ]

def close_mutex():
    require_length = c_ulong(0)
    nt_status = ntdll.NtQuerySystemInformation(16, 0, 0, byref(require_length))
    while nt_status == 0xC0000004:
        buffer = (c_ubyte * require_length.value)()
        nt_status = ntdll.NtQuerySystemInformation(16, buffer, require_length, byref(require_length))
    if nt_status != 0:
        raise Exception("NtQuerySystemInformation failed with status code: 0x{:08X}".format(nt_status))

    handle_count = cast(buffer, POINTER(c_int64))[0]
    handles = cast(cast(buffer, c_void_p).value + 8, POINTER(SYSTEM_HANDLE * handle_count))[0]
    cnt = 0
    pids=set()
    for handle in handles:
        pids.add(handle.ProcessId)
        if handle.ProcessId != os.getpid(): continue
        duplicate_handle = c_void_p()
        if not kernel32.DuplicateHandle(
                CURRENT_PROCESS_HANDLER,
                handle.HandleValue,
                CURRENT_PROCESS_HANDLER,
                byref(duplicate_handle),
                0, False, 2
        ):
            print("DuplicateHandle failed with error code: 0x{:08X}".format(kernel32.GetLastError()))
            continue
        require_length = c_ulong(1024)
        buffer_2 = (c_ubyte * require_length.value)()
        nt_status = ntdll.NtQueryObject(duplicate_handle, 1, buffer_2, require_length, byref(require_length))
        if nt_status != 0:
            print("NtQueryObject failed with status code: 0x{:08X}".format(nt_status))
            continue
        name = bytes(buffer_2[16:]).decode('utf16', 'ignore').rstrip('\0')
        if name:
            print(name)
        if re.search(r'6AA83AB5-BAC4-4a36-9F66-A309770760CB_ffxiv_game\d+', name):
            kernel32.CloseHandle(handle.HandleValue)
            cnt += 1
        kernel32.CloseHandle(duplicate_handle)
    return cnt
