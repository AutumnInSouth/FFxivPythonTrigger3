from FFxivPythonTrigger.saint_coinach import action_sheet
from FFxivPythonTrigger.memory import *


def main():
    func = CFUNCTYPE(POINTER(c_ubyte), c_int64)(BASE_ADDR + 0x6764b0)
    for skill_id in [21904,]:
        print(bytes(func(skill_id)[:112]).hex(' '))

