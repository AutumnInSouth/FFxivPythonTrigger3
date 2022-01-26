from ctypes import *
from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import realm

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

adv_sheet = realm.game_data.get_sheet("Adventure")

opcode = 222
s_id = 2162898
sight_struct = OffsetStruct({
    'a_id': c_uint,
    'unk': c_uint,
    's_id': c_uint,
    'emote': c_uint,
})
emote = adv_sheet[s_id]["Emote"].key
me_id = plugins.XivMemory.player_info.id
sight_msg=sight_struct(a_id=me_id, s_id=s_id, emote=emote)
print(sight_msg)
plugins.XivNetwork.send_messages('zone', [
    ("ClientTrigger", {'param1': 0x1fb, 'param6': 0x7c}),
    ("ClientTrigger", {'param1': 0x1f4, 'param2': emote, 'param7': 0xe0000000}),
    (opcode, sight_msg),
    ("ClientTrigger", {'param1': 3, 'param2': me_id, 'param6': 0x1f7}),
    # ("ClientTrigger", {'param1': 3, 'param2': 0xe0000000}),
])
