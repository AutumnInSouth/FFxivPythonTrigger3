from ctypes import *
from time import perf_counter

from FFxivPythonTrigger import plugins, wait_until
from FFxivPythonTrigger.memory import BASE_ADDR, read_ulonglong
from FFxivPythonTrigger.text_pattern import find_signature_address

# lock on
argus: list[str]
k = int(argus[0])
t = plugins.XivMemory.actor_table.me
address = find_signature_address("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 8B EA 48 8B F9 BB ? ? ? ?") + BASE_ADDR
s = 0
while read_ulonglong(addressof(t) + 0x1890 + s * 8): s += 1
CFUNCTYPE(c_void_p, c_void_p, c_uint)(address)(byref(t), k)
# start = perf_counter()
# wait_until(lambda: not read_ulonglong(addressof(t) + 0x1890 + s * 8) or None, period=.01)
# print(f"{k}: {perf_counter() - start:.3f}s")
