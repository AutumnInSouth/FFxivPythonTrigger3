import re
import traceback
from ctypes import *

from FFxivPythonTrigger import plugins, PluginBase, AddressManager
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import read_memory, write_string, read_ulonglong, read_int
from FFxivPythonTrigger.saint_coinach import item_sheet, item_names, realm, status_sheet

quest_sheet = realm.game_data.get_sheet("Quest")
map_sheet = realm.game_data.get_sheet("Map")

item_name_to_id = {row['Name']: row.key for row in item_sheet}
quest_name_to_id = {row['Name']: row.key for row in quest_sheet}
quest_names = {row.key: row['Name'] for row in quest_sheet}
maps = {}
for row in map_sheet: maps.setdefault(getattr(row['TerritoryType'], 'key', 0), {})[row['MapIndex']] = row.key
status_name_to_id = {}
for row in status_sheet: status_name_to_id.setdefault(row['Name'], []).append(row.key)


def parse_actor(name=None, world_id=None, actor_id=None, ):
    if name:
        return f"<fixed(200,1,{world_id or plugins.XivMemory.actor_table.me.current_world},{name})>"


def parse_item(name=None, item_id=None, hq=None, collect=None, no_tag=None, ):
    if item_id is None and name is None: return
    if item_id is None:
        item_id = item_name_to_id.get(name)
        if item_id is None: return
    else:
        item_id = int(item_id)
    if name is None:
        name = item_names.get(item_id, 'unk_item')
    if hq:
        item_id += 1000000
        if not no_tag: name += '\ue03c'
    if collect:
        item_id += 500000
        if not no_tag: name += '\ue03d'
    return f"<fixed(200,4,{item_id},1,0,0,{name})>"


def parse_quest(name=None, quest_id=None, ):
    if name is None and quest_id is None: return
    if quest_id is None:
        quest_id = quest_name_to_id.get(name)
        if quest_id is None: return
    else:
        quest_id = int(quest_id)
    if name is None:
        name = quest_names.get(quest_id, 'unk_quest')
    return f"<fixed(200,12,{quest_id - 65535},0,0,0,{name})>"


def parse_pos(map_id=None, territory_id=None, x=None, y=None, z=None, ):
    if map_id is None and territory_id is None:
        territory_id = plugins.XivMemory.zone_id
        map_id = plugins.XivMemory.map_id
    if map_id: map_id = int(map_id)
    if territory_id: territory_id = int(territory_id)
    if territory_id is None:
        territory_id = getattr(map_sheet[map_id]['TerritoryType'], 'key', 0)
    if x is None:
        x = plugins.XivMemory.coordinate.x
    if y is None:
        y = plugins.XivMemory.coordinate.y
    if z is None:
        z = plugins.XivMemory.coordinate.z
    if map_id is None: maps.get(territory_id, {}).get(0, 0)
    return f"<fixed(200,3,{territory_id},{map_id},{x * 1000:.0f},{y * 1000:.0f},{z:.0f})>"


def parse_status(status_id=None, name=None, ):
    if status_id is None and name is None: return
    if status_id is None:
        status_id = min(status_name_to_id.get(name, [0]))
    return f"<fixed(200,10,{status_id},0,0)>"


def parse_macro(marco: list[str]):
    args = {
        m[0]: m[1] if len(m) > 1 else True
        for m in (m.split('=', 1) for m in marco[1:])
    }
    match marco[0]:
        case 'actor' | 'a':
            return parse_actor(**args)
        case 'item' | 'i':
            return parse_item(**args)
        case 'quest' | 'q':
            return parse_quest(**args)
        case 'ppos' | 'p':
            return parse_pos(**args)
        case 'status' | 's':
            return parse_status(**args)


class SomeMacro(PluginBase):
    name = "SomeMacro"

    def __init__(self):
        super().__init__()
        am = AddressManager(self.name, self.logger)
        self.macro_parse_hook(self, am.scan_address(
            "macro_parse_hook", "40 55 53 56 48 8B EC 48 83 EC ? 48 8B 05 ? ? ? ? 48 33 C4 48 89 45 ? 48 8B F1",
        ))
        self.c1 = CFUNCTYPE(c_int64, c_int64, c_int64, c_int64)(am.scan_address(
            "c1", "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B D9 49 8B F8 48 81 C1 ? ? ? ?",
        ))
        self.c2 = CFUNCTYPE(c_int64, c_int64, c_int64)(am.scan_address(
            "c2", "48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B 79 ? 48 8B F2 48 8B 52 ?"
        ))
        self.c3 = CFUNCTYPE(c_int64, c_int64)(am.scan_address(
            "c3", "80 79 ? ? 75 ? 48 8B 51 ? 41 B8 ? ? ? ?"
        ))
        self.off = read_int(read_ulonglong(am.scan_point("offset", "48 8D 05 * * * * 4C 89 61 ? 4C 8B FA") + 0x30) + 3)

    @PluginHook.decorator(c_int64, [c_int64, POINTER(c_int64)], True)
    def macro_parse_hook(self, hook, a1, a2):
        try:
            cmd = read_memory(c_char * 50, a2[0]).value
            try:
                end = cmd.find(b'>')
            except ValueError:
                return hook.original(a1, a2)
            self.logger.debug(f"cmd: {cmd} end: {end}")
            ans = parse_macro(cmd[1:end].decode('utf8', 'ignore').split(' '))
            if ans:
                write_string(read_ulonglong(a1 + 136), ans)
                a2[0] += end + 1
                buffer = (c_char * 1024)()
                v = self.c1(read_ulonglong(a1 + 912) + self.off, addressof(buffer), read_ulonglong(a1 + 136))
                self.c2(a1 + 32, v)
                self.c3(addressof(buffer))
                return 0xffffffff
        except Exception as e:
            self.logger.error(traceback.format_exc())
        return hook.original(a1, a2)
