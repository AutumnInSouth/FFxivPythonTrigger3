import requests
import json

c1 = """
from pprint import pprint
from FFxivPythonTrigger import *
pprint(locals())
"""
c2 = """
from FFxivPythonTrigger.text_pattern import *
from FFxivPythonTrigger.text_pattern import section_virtual_address
sig="48 8d ? * * * * e8 ? ? ? ? 48 8b ? 48 8b ? 48 8d ? ? ? ? ? e8 ? ? ? ? 48 8d ? ? ? ? ? ba ? ? ? ? e8 ? ? ? ? 89 2f"
pattern, offsets = sig_to_pattern(sig)
print(pattern,offsets)
for match in re.finditer(bytes(pattern), section_data):
    print(match.groups()[0].hex(' '))
"""
c3 = """
from FFxivPythonTrigger.ffxiv_python_trigger import _clients_subscribe,_clients
print(_clients,_clients_subscribe)
"""
c4 = """
#reload_module('XivMemory')
from ctypes import *
print(hex(addressof(plugins.XivMemory.mission_info)))
print(plugins.XivMemory.mission_info)
"""
c5 = """
from FFxivPythonTrigger.saint_coinach import realm
for s in realm._game_data.definition.sheet_definitions:
    sheet = realm.game_data.get_sheet(s.name)
    try:
        print(sheet[100011])
    except:
        pass
"""
c6 = """
from time import sleep
for i in range(40):
    plugins.XivMemory.calls.way_mark(i%8 , plugins.XivMemory.actor_table.me.pos)
    sleep(0.5)
plugins.XivMemory.calls.way_mark.clear(9)
"""
c7 = """
from FFxivPythonTrigger.text_pattern import find_unique_signature_address,find_unique_signature_point
print(hex(find_unique_signature_point(("48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? "
                       "BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 48 8D 0D ? ? ? ?"))))
"""
c8 = """
print(plugins.Test.num,plugins.Test.num2)
plugins.Test.num += 1
plugins.Test.num2 *= 2
print(plugins.Test.num,plugins.Test.num2)
"""
c9 = """
import time
for i in range(200):
    self.logger(time.time())
    time.sleep(0.1)
"""
c10 = """
from FFxivPythonTrigger.address_manager import _storage_data
del _storage_data['XivHacks']['cutscene_skip']
"""
c11 = """
from ctypes import *
from FFxivPythonTrigger.memory import BASE_ADDR, read_pointer_shift, read_ulonglong
print(CFUNCTYPE(c_int64)(BASE_ADDR + 0xA88C80)())
"""
c12 = """
from ctypes import *
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

ClientTriggerStruct = OffsetStruct({
    'param1': c_uint,  # 0x0453 in in WardLandInfo mode,0x0452 in HousingDetails mode, 0x451 in check can buy mode
    'param2': c_uint,  # territory_type
    'param3': c_ubyte,  # Ward ID in WardLandInfo mode,  House ID in HousingDetails mode
    'param4': c_ubyte,  # 0 in WardLandInfo mode,        Ward ID in HousingDetails mode
}, 32)
msg = ClientTriggerStruct(param1=0x0453, param2=339, param3=5)
print(plugins.XivNetwork.send_messages('zone',("ClientTrigger",msg),'WardLandInfo'))
"""

c13 = """
from ctypes import *
print(plugins.XivNetwork.send_messages('zone',("MarketBoardQueryItemCount",{'item_id':18,'unk1':0x902}),"MarketBoardItemListingCount",True))
"""

c14 = """
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import item_names
for page in plugins.XivMemory.inventory.value:
    self.logger(page.container_id)
    for item in page:
        try:
            name=item_names[item.item_id]
        except:
            name=item.item_id
        self.logger(item.item_id,name,item.count)
"""
c15 = """
for i in range(3):plugins.XivMemory.calls.do_text_command('/@fpt eval self.logger(1)')
"""
t = requests.post("http://127.0.0.1:2019/exec", c15.encode('utf-8')).text


d = json.loads(t)
if 'print' in d: print(d['print'])
if "traceback" in d: print(d['traceback'])
print(d)
