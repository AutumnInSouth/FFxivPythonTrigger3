from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import BASE_ADDR, read_pointer_shift, read_ulonglong


class Pmb(PluginBase):
    name = "Pmb"
    # layout = str(Path(__file__).parent / 'layout.js')
