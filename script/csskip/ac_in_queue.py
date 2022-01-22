import locale
import ctypes
import re
import ctypes.wintypes
import sys
from ctypes import windll

DEFAULT_CODING = locale.getpreferredencoding()

windll.kernel32.WriteProcessMemory.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
]

windll.kernel32.ReadProcessMemory.argtypes = (
    ctypes.wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
)


class ProcessEntry32(ctypes.Structure):
    _fields_ = [
        ('dwSize', ctypes.c_ulong),
        ('cntUsage', ctypes.c_ulong),
        ('th32ProcessID', ctypes.c_ulong),
        ('th32DefaultHeapID', ctypes.POINTER(ctypes.c_ulong)),
        ('th32ModuleID', ctypes.c_ulong),
        ('cntThreads', ctypes.c_ulong),
        ('th32ParentProcessID', ctypes.c_ulong),
        ('pcPriClassBase', ctypes.c_ulong),
        ('dwFlags', ctypes.c_ulong),
        ('szExeFile', ctypes.c_char * ctypes.wintypes.MAX_PATH)
    ]

    def __init__(self, *args, **kwds):
        super(ProcessEntry32, self).__init__(*args, **kwds)
        self.dwSize = ctypes.sizeof(self)


class MODULEINFO(ctypes.Structure): _fields_ = [("lpBaseOfDll", ctypes.c_void_p), ("SizeOfImage", ctypes.c_ulong), ("EntryPoint", ctypes.c_void_p), ]


class LUID(ctypes.Structure): _fields_ = [("LowPart", ctypes.c_ulong), ("HighPart", ctypes.c_long)]


class LUID_AND_ATTRIBUTES(ctypes.Structure): _fields_ = [("Luid", LUID), ("Attributes", ctypes.c_ulong), ]


class TOKEN_PRIVILEGES(ctypes.Structure): _fields_ = [("count", ctypes.c_ulong), ("Privileges", LUID_AND_ATTRIBUTES * 1)]


PTOKEN_PRIVILEGES = ctypes.POINTER(TOKEN_PRIVILEGES)


def list_processes():
    windll.kernel32.SetLastError(0)
    hSnap = windll.kernel32.CreateToolhelp32Snapshot(0x00000002, 0)
    process_entry = ProcessEntry32()
    process_entry.dwSize = ctypes.sizeof(process_entry)
    p32 = windll.kernel32.Process32First(hSnap, ctypes.byref(process_entry))
    if p32:
        yield process_entry
    while p32:
        yield process_entry
        p32 = windll.kernel32.Process32Next(hSnap, ctypes.byref(process_entry))
    windll.kernel32.CloseHandle(hSnap)


def main():
    hProcess = ctypes.c_void_p(-1)
    if not windll.advapi32.OpenProcessToken(hProcess, 32, ctypes.byref(hProcess)):
        raise Exception("OpenProcessToken failed err code:%d" % windll.kernel32.GetLastError())
    tkp = TOKEN_PRIVILEGES()
    if not windll.advapi32.LookupPrivilegeValueW(None, "SeDebugPrivilege", ctypes.byref(tkp.Privileges[0].Luid)):
        raise Exception("LookupPrivilegeValueW failed err code:%d" % windll.kernel32.GetLastError())
    tkp.count = 1
    tkp.Privileges[0].Attributes = 2
    if not windll.advapi32.AdjustTokenPrivileges(hProcess, 0, ctypes.byref(tkp), 0, None, None):
        raise Exception("AdjustTokenPrivileges failed err code:%d" % windll.kernel32.GetLastError())
    is_patch = bool(input('输入1打补丁，不输入恢复>>'))
    for p in list_processes():
        if 'ffxiv_dx11.exe' in p.szExeFile.decode(DEFAULT_CODING).lower():
            handle = windll.kernel32.OpenProcess(0x1F0FFF, False, p.th32ProcessID)
            if not handle: raise Exception('OpenProcess failed, error code: %d' % windll.kernel32.GetLastError())
            hModules = (ctypes.c_void_p * 1)()
            if not windll.psapi.EnumProcessModulesEx(handle, ctypes.byref(hModules), 8, ctypes.byref(ctypes.c_ulong()), 0x02):
                raise Exception('EnumProcessModulesEx failed with error code %d' % windll.kernel32.GetLastError())
            module_info = MODULEINFO()
            if not windll.psapi.GetModuleInformation(handle, ctypes.c_void_p(hModules[0]), ctypes.byref(module_info), ctypes.sizeof(module_info)):
                raise Exception('GetModuleInformation failed with error code %d' % windll.kernel32.GetLastError())
            module_data = (ctypes.c_ubyte * module_info.SizeOfImage)()
            if not windll.kernel32.ReadProcessMemory(handle, module_info.lpBaseOfDll, ctypes.byref(module_data), ctypes.sizeof(module_data), None):
                raise Exception('ReadProcessMemory failed with error code %d' % windll.kernel32.GetLastError())
            match = re.search(b'\x80\x7f..\x0f\x85....\x41\x83\xfe', bytes(module_data))
            if not match: raise Exception('Cannot find target bytes in memory 1')
            offset = match.span()[0]
            print('offset: %x' % offset)
            if is_patch:
                patch_byte = b'\x90' * 6
            else:
                match = re.search(b'\x85\xF6\x74.\x81\xFE', bytes(module_data))
                if not match: raise Exception('Cannot find target bytes in memory 2')
                patch_byte = b'\x0f\x84' + (match.span()[0] - offset).to_bytes(4, 'little')
            if not windll.kernel32.WriteProcessMemory(handle, offset + module_info.lpBaseOfDll - 6, patch_byte, 6, None):
                raise Exception('WriteProcessMemory failed with error code %d' % windll.kernel32.GetLastError())
            print("修改" if is_patch else "恢复", f"pid:{p.th32ProcessID} 成功")
            windll.kernel32.CloseHandle(handle)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
    finally:
        input('Press any key to exit...')
