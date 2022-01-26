from ctypes import *

from FFxivPythonTrigger import frame_inject
from FFxivPythonTrigger.memory import read_memory
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, PointerStruct

TextCommandStruct = OffsetStruct({
    "cmd": c_void_p,
    "t1": c_longlong,
    "tLength": c_longlong,
    "t3": c_longlong,
}, full_size=400)

do_text_command_interface = CFUNCTYPE(c_int64, c_void_p, c_void_p, c_int64, c_char)


class DoTextCommand(object):
    def __init__(self, func_address: int, ui_module_ptr_address: int):
        self._original = do_text_command_interface(func_address)
        self.ui_module = read_memory(PointerStruct(c_void_p, 0), ui_module_ptr_address)

    def original(self, command: str | bytes) -> int:
        if isinstance(command, str):
            command = command.encode('utf-8')
        cmd_size = len(command)
        cmd = OffsetStruct({"cmd": c_char * cmd_size}, full_size=cmd_size + 30)(cmd=command)
        arg = TextCommandStruct(cmd=addressof(cmd), t1=64, tLength=cmd_size + 1, t3=0)
        return self._original(self.ui_module.value, addressof(arg), 0, 0)

    def __call__(self, command: str):
        frame_inject.register_once_call(self.original, command)
