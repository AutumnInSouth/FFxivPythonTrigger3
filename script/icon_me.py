from ctypes import *
from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.text_pattern import find_signature_address

argus: list[str]
address = find_signature_address("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 8B EA 48 8B F9 BB ? ? ? ?")+BASE_ADDR
CFUNCTYPE(c_void_p, c_void_p, c_uint)(address)(byref(plugins.XivMemory.actor_table.me), int(argus[0]))
