import requests
import json
c1="""
from pprint import pprint
from FFxivPythonTrigger import *
pprint(locals())
"""
c2="""
from FFxivPythonTrigger.text_pattern import *
from FFxivPythonTrigger.text_pattern import section_virtual_address
sig="48 8d ? * * * * e8 ? ? ? ? 48 8b ? 48 8b ? 48 8d ? ? ? ? ? e8 ? ? ? ? 48 8d ? ? ? ? ? ba ? ? ? ? e8 ? ? ? ? 89 2f"
pattern, offsets = sig_to_pattern(sig)
print(pattern,offsets)
for match in re.finditer(bytes(pattern), section_data):
    print(match.groups()[0].hex(' '))
"""
c3="""
from FFxivPythonTrigger.ffxiv_python_trigger import _clients_subscribe,_clients
print(_clients,_clients_subscribe)
"""
c4="""
#reload_module('XivMemory')
from ctypes import *
print(hex(addressof(plugins.XivMemory.mission_info)))
print(plugins.XivMemory.mission_info)
"""
c5="""
from FFxivPythonTrigger.saint_coinach import realm
for s in realm._game_data.definition.sheet_definitions:
    sheet = realm.game_data.get_sheet(s.name)
    try:
        print(sheet[100011])
    except:
        pass
"""
c6="""
from time import sleep
for i in range(40):
    plugins.XivMemory.calls.way_mark(i%8 , plugins.XivMemory.actor_table.me.pos)
    sleep(0.5)
plugins.XivMemory.calls.way_mark.clear(9)
"""
c7="""
from FFxivPythonTrigger.text_pattern import find_unique_signature_address,find_unique_signature_point
print(hex(find_unique_signature_point(("48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? "
                       "BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 48 8D 0D ? ? ? ?"))))
"""
c8="""
print(plugins.Test.num,plugins.Test.num2)
plugins.Test.num += 1
plugins.Test.num2 *= 2
print(plugins.Test.num,plugins.Test.num2)
"""
t = requests.post("http://127.0.0.1:2019/exec", c8.encode('utf-8')).text

# print(t)
d = json.loads(t)
if d['print']:
    print(d['print'])
if "traceback" in d: print(json.loads(t)['traceback'])
