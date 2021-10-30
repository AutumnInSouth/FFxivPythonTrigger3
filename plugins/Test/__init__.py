from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import BASE_ADDR, read_pointer_shift, read_ulonglong


class Test(PluginBase):
    name = "Test"
    layout = str(Path(__file__).parent / 'layout.js')

    def call(self):
        module=read_ulonglong(BASE_ADDR + 0x1DB3840)
        self.logger(read_ulonglong(module+56))
        return CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + 0x479700)(module)
