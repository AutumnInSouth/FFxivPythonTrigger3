from FFxivPythonTrigger import *
from fpt_plugins_type import *
from FFxivPythonTrigger.saint_coinach import item_sheet
for row in plugins.XivMemory.inventory.get_item_in_containers_by_key(None,'backpack'):
    item = item_sheet[row.item_id]
    if item['ItemUICategory'].key == 58:
        print(row.container_id,row.idx,item['Name'],row.count)
