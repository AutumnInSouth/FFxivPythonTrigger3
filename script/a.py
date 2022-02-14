from ctypes import *
from random import randint

from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *

argus: list[str]
eid = eval(argus[0])
plugins.XivNetwork.send_messages('zone', ("EventStart", {
    'target_id': (plugins.XivMemory.targets.current or plugins.XivMemory.actor_table.me).id,
    # 'target_id': plugins.XivMemory.targets.current.b_npc_id,
    'event_id': eid & 0xffff,
    'category': eid >> 16,
}))
