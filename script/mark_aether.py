import math
from FFxivPythonTrigger import *
from FFxivPythonTrigger.saint_coinach import realm

plugins.XivMemory.calls.do_action(1, 26988)
current_map_id = plugins.XivMemory.zone_id
coor = plugins.XivMemory.coordinate
aether_currents = {row.key for row in realm.game_data.get_sheet('AetherCurrent')}
zone_aether_currents = sorted([row for row in realm.game_data.get_sheet('Level') if
                               getattr(row['Territory'], 'key', 0) == current_map_id and
                               getattr(getattr(row['Object'], 'sheet', None), 'name', None) == 'EObj' and
                               row['Object']['Data'] in aether_currents],
                              key=lambda x: math.sqrt((coor.x - x['X']) ** 2 + (coor.y - x['Z']) ** 2 + (coor.z - x['Y']) ** 2))
for i, row in enumerate(zone_aether_currents[:8]):
    plugins.XivMemory.calls.way_mark(i, (row['X'], row['Z'], row['Y']))
