from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger import plugins, wait_until

t = plugins.XivMemory.targets.focus

cnt = 0


def block_msg(*args):
    print('block')
    global cnt
    cnt += 1
    return


plugins.XivNetwork.register_packet_fixer(None, 'zone', True, 'EventStart', block_msg)
plugins.XivNetwork.register_packet_fixer(None, 'zone', True, 'EventPlay', block_msg)

plugins.XivNetwork.send_messages('zone', [
    ('ClientTrigger', OffsetStruct({
        'param1': c_uint,
        'param2': c_uint,
        'param3': c_uint,
    }, 32)(param1=3, param2=t.b_npc_id, param3=1)),
    ('EventStart', OffsetStruct({
        'target_id': c_uint,
        'unk0': c_uint,
        'event_id': c_ushort,
        'category': c_ushort
    }, 16)(target_id=t.b_npc_id, unk0=1, event_id=135, category=11)),
    ('EventFinish', OffsetStruct({
        'event_id': c_ushort,
        'category': c_ushort,
        'unk2': c_uint,
        'unk3': c_uint
    }, 16)(event_id=135, category=11, unk2=0x1000000, unk3=3))
])


try:
    wait_until(lambda: cnt >= 2 or None, timeout=3)
finally:
    plugins.XivNetwork.unregister_packet_fixer('zone', True, 'EventStart', block_msg)
    plugins.XivNetwork.unregister_packet_fixer('zone', True, 'EventPlay', block_msg)
