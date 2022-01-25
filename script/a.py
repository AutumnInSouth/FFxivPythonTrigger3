from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point

print(read_int(read_ulonglong(find_signature_point("48 8D 05 * * * * 4C 89 61 ? 4C 8B FA")+BASE_ADDR + 0x30)+3))
