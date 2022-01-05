from ctypes import *

from FFxivPythonTrigger import plugins, game_ext
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import realm, item_names

evt_category = 0xb
evt_id = 0xae

if game_ext == 4:
    stone_request_opcode = 719
    stone_request_struct = OffsetStruct({
        'event_id': c_ushort,  # 0xae
        'category': c_ushort,  # 0x0b
        'unk0': c_uint,  # 0xb000000 at first, then 0xc000005
        'cnt': c_uint,
        'slots': OffsetStruct({
            'container_id': c_uint,
            'slot_id': c_ushort,
            'cnt': c_ushort,
        }) * 5
    }, 72)
    max_materia = 10
    want_materia = {
        27: 8,
        22: 8,
        45: 8,
        # 44: 8,
        # 11: 8,
        # 70: 8,
        # 71: 8,
        # 72: 8,
        # 73: 8,
        # 10: 8
    }
else:
    stone_request_opcode = 375
    stone_request_struct = OffsetStruct({
        'event_id': c_ushort,  # 0xae
        'category': c_ushort,  # 0x0b
        'unk0': c_uint,  # 0xb000000 at first, then 0xc000005
        'cnt': c_uint,
        'slots': OffsetStruct({
            'container_id': c_uint,
            'slot_id': c_ushort,
            'cnt': c_ushort,
        }) * 5
    }, 72)
    max_materia = 7
    want_materia = {
        # 27: 7,
        # 44: 7,
        # 11: 6,
        # 70: 6,
        # 71: 6,
        # 72: 6,
        # 73: 6,
        # 10: 6
    }

materia_sheet = realm.game_data.get_sheet('Materia')
materia_data = dict()
for row in materia_sheet:
    try:
        for i in range(10):
            item = row[f'Item[{i}]']
            if item.key:
                materia_data[item.key] = i, getattr(row['BaseParam'], 'key', 0)
    except:
        pass
print(materia_data)


def is_evt(evt):
    return evt.struct_message.category == evt_category and evt.struct_message.event_id == evt_id


def start():
    return plugins.XivNetwork.send_messages('zone', ("EventStart", {
        'target_id': plugins.XivMemory.actor_table.me.id,
        'event_id': evt_id,
        'category': evt_category,
    }), response=("EventPlay", is_evt))


def stone_request(stones: list[tuple[int, int, int]], is_first: bool = False):
    msg = stone_request_struct(event_id=evt_id, category=evt_category, unk0=0xb000000 if is_first else 0xc000005, cnt=len(stones))
    for i, (container_id, slot_id, cnt) in enumerate(stones):
        msg.slots[i].container_id = container_id
        msg.slots[i].slot_id = slot_id
        msg.slots[i].cnt = cnt
    return plugins.XivNetwork.send_messages('zone', (stone_request_opcode, msg), response=("EventFinish", is_evt))


while True:
    backpack_materia = list()
    for row in plugins.XivMemory.inventory.get_item_in_containers_by_key(None, 'backpack'):
        if row.item_id in materia_data:
            lv, base_param = materia_data[row.item_id]
            # if lv < max_materia and (lv < max_materia - 1 or base_param not in want_materia):
            if lv < want_materia.get(base_param, max_materia):
                backpack_materia.append((row.container_id, row.idx, row.count, row.item_id, lv, base_param))
            # else:
            #     print(item_names[row.item_id], base_param, lv, want_materia.get(base_param, max_materia))
    backpack_materia.sort(key=lambda x: x[4])
    current_lv = 0
    to_mix = []
    to_mix_cnt = 0
    for item in backpack_materia:
        if item[4] != current_lv:
            current_lv = item[4]
            to_mix_cnt = 0
            to_mix = []
        to_get = min(item[2], 5 - to_mix_cnt)
        to_mix.append((item[0], item[1], to_get))
        to_mix_cnt += to_get
        if to_mix_cnt >= 5:
            break
    if to_mix_cnt < 5:
        raise Exception('Not enough materia in backpack')

    start()
    stone_request(to_mix, True)
