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
        print(sheet[9345])
    except:
        pass
"""
c6="""
from time import sleep
for i in range(40):
    plugins.XivMagic.way_mark(i%8 , plugins.XivMemory.actor_table.me.pos)
    sleep(0.5)
plugins.XivMagic.way_mark.clear(9)
"""
c7="""
from FFxivPythonTrigger.text_pattern import find_unique_signature_address
print(hex(find_unique_signature_address("48 89 5C 24 ?? 56 48 83 EC 50 8B F2")))
"""
t = requests.post("http://127.0.0.1:2019/exec", c7.encode('utf-8')).text

# print(t)
d = json.loads(t)
if d['print']:
    print(d['print'])
if "traceback" in d: print(json.loads(t)['traceback'])
