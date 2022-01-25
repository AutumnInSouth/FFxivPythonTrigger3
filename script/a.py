from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import realm

print(plugins.XivMemory.actor_table.me.pos)

dword_141D627B4 = read_uint(BASE_ADDR + 0x1D627B4)
dword_141DAD334 = read_uint(BASE_ADDR + 0x1DAD334)
map_id = dword_141D627B4 or dword_141DAD334
print(map_id, plugins.XivMemory.map_id)

map_sheet = realm.game_data.get_sheet('Map')

maps = [row for row in map_sheet if getattr(row['TerritoryType'], 'key', 0) == plugins.XivMemory.zone_id]

print(maps)
