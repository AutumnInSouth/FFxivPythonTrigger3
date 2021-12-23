from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *

argus: list[str]
eid = int(argus[0])
plugins.XivNetwork.send_messages('zone', ("EventStart", {
    'target_id': plugins.XivMemory.actor_table.me.id,
    # 'target_id': plugins.XivMemory.targets.current.b_npc_id,
    'event_id': eid & 0xffff,
    'category': eid >> 16,
}))
