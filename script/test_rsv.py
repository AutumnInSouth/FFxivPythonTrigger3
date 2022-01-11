from FFxivPythonTrigger.memory import *

qword_141E773C0 = read_ulonglong(BASE_ADDR + 0x1E773C0)
if qword_141E773C0:
    print("qword_141E773C0: 0x%016X" % qword_141E773C0)
    a0 = read_ulonglong(qword_141E773C0 + 0x218)
    print("a0: 0x%016X" % a0)
