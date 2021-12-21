from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *


def main():
    # _QWORD *__fastcall sub_1407DE990(int a1, __int64 a2, __int64 a3, __int64 a4)
    return plugins.XivNetwork.send_messages('zone', ("EventStart", {
        'target_id': plugins.XivMemory.targets.current.id,
        'event_id': 32197,
        'category': 3
    }))


main()
