import time
from ctypes import *
from datetime import datetime
from functools import cache
from pathlib import Path
from threading import Lock
from typing import TYPE_CHECKING
from FFxivPythonTrigger import PluginBase, plugins, NeedRequirementError, frame_inject, wait_until
from FFxivPythonTrigger.decorator import event, BindValue
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import realm

try:
    import pandas as pd
except ModuleNotFoundError:
    raise NeedRequirementError('pandas')

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ward_land_info import ServerWardLandInfoEvent

areas = [
    339,  # 海雾村
    341,  # 高脚孤丘
    340,  # 薰衣草苗园
    641,  # 白银乡
]

ward_cnt = 24
house_cnt = 60

world_sheet = realm.game_data.get_sheet('World')
territory_type_sheet = realm.game_data.get_sheet('TerritoryType')

map_name = {'海': 339, '沙': 341, '森': 340, '白': 641}


@cache
def world_name(world_id):
    return world_sheet[world_id]['Name']


@cache
def place_name(place_id):
    return territory_type_sheet[place_id]['PlaceName']['Name']


def price_lv(price: int):
    if price < 4000000:
        return 'S'
    elif price <= 20000000:
        return 'M'
    else:
        return 'L'


def get_frame():
    return pd.DataFrame(index=pd.MultiIndex.from_product([map(place_name, areas), range(ward_cnt), range(house_cnt)]),
                        columns=['price', 'owner']).sort_index()


GotoStruct = OffsetStruct({'a': c_uint, 'l': c_ushort, 'wo': c_ushort, 'h': c_ushort, 'w': c_ushort, 'm': c_uint, }, 32)


class WanaHome(PluginBase):
    name = "WanaHome"
    layout = str(Path(__file__).parent / 'layout.js')

    prev_search_time = BindValue(do_save=False, default=0)
    auto_search_period = BindValue(do_save=False, default=0)
    responses: list['ServerWardLandInfoEvent'] | None

    def __init__(self):
        super().__init__()

        # search used
        self.responses = None
        self.lock = Lock()
        self.is_searching = 0
        self._world_data = dict()
        self.current_world = ""

        # setup
        self.load_world_data()
        frame_inject.register_continue_call(self.frame_work)

    def start(self):
        self.full_search()

    @event('network/zone/server/ward_land_info')
    def ward_land_info_event(self, evt: 'ServerWardLandInfoEvent'):
        if self.responses is not None: self.responses.append(evt)

    def get_world_count_down_data(self):
        return self.storage.data.setdefault('houses', dict()).setdefault(self.current_world, dict())

    def save_world_data(self):
        for k, df in self._world_data.items():
            df.to_csv(self.storage.path / f'{k}.csv')

    def load_world_data(self):
        self._world_data.clear()
        cnt = 0
        for fp in self.storage.path.glob('*.csv'):
            self._world_data[fp.stem] = pd.read_csv(fp, index_col=[0, 1, 2]).fillna('')
            cnt += 1
        self.logger.debug(f"{cnt} data loaded")

    def list_data(self):
        now = datetime.now()
        data = self.get_world_count_down_data()
        s = f"{len(data)} house is in record:\n"
        for key, d in sorted(data.items(), key=lambda x: x[1][1]):
            timestamp, price, data = d
            secs = (now - datetime.fromtimestamp(timestamp)).total_seconds()
            s += f"{key} ({price} Gil) is on sale for {int(secs // 3600)}h {int(secs % 3600 // 60)}m {int(secs % 60)}s\n"
        return s

    def get_data(self) -> list['ServerWardLandInfoEvent']:
        self.responses = []
        plugins.XivNetwork.send_messages('zone', [('ClientTrigger', {
            'param1': 0x0453,
            'param2': area,
            'param3': ward_id,
        }) for ward_id in range(ward_cnt) for area in areas])
        wait_until(lambda: len(self.responses) >= ward_cnt * len(areas) or None)
        res = sorted(self.responses, key=lambda evt: (evt.struct_message.territory_id, evt.struct_message.ward_id))
        self.responses = None
        return res

    def _full_search(self):
        self.logger.debug("start searching")
        start = time.time()
        new_world_data = get_frame()
        current_world_id = 0
        new_data = dict()
        sync_data = dict()
        for res in self.get_data():
            msg = res.struct_message
            if not msg.world_id:
                self.logger.warning("not in a valid world, abort searching")
                return
            else:
                if not current_world_id:
                    current_world_id = msg.world_id
                elif current_world_id != msg.world_id:
                    self.logger.warning("world data is not in the same world, abort searching")
                    return
                name = place_name(msg.territory_id)
                row = new_world_data.loc[name, msg.ward_id]
                w_data = sync_data.setdefault(msg.territory_id, {}).setdefault(msg.ward_id, {})
                for i, house in enumerate(msg.houses):
                    owner = f"《{house.owner}》" if house.is_fc and house.owner else house.owner
                    w_data[i] = owner, house.price
                    row.loc[i]['price'] = house.price
                    row.loc[i]['owner'] = owner
                    if not house.owner:
                        key = f"{name} {str(msg.ward_id + 1).zfill(2)}-{str(i + 1).zfill(2)}({price_lv(house.price)})"
                        new_data[key] = datetime.now(), house.price, {
                            'world_id': current_world_id, 'territory_id': msg.territory_id, 'ward_id': msg.ward_id, 'house_id': i
                        }
        current_world = world_name(current_world_id)
        data = self.storage.data.setdefault('houses', dict()).setdefault(current_world, dict())
        need_save = False
        for key in data.copy().keys():
            if key not in new_data:
                need_save = True
                del data[key]
        for key in new_data.keys():
            if key not in data:
                need_save = True
                data[key] = [new_data[key][0].timestamp(), new_data[key][1], new_data[key][2]]
            elif new_data[key][1] != data[key][1]:
                need_save = True
                data[key][1] = new_data[key][1]
        if current_world not in self._world_data:
            self.logger.debug(f"init {current_world} world data")
            self._world_data[current_world] = new_world_data
            self._world_data[current_world].to_csv(self.storage.path / f'{current_world}.csv')
        else:
            diff = self._world_data[current_world].compare(new_world_data)
            self.logger.debug(f"{len(diff.index)} different found")
            for index, row in self._world_data[current_world].compare(new_world_data).iterrows():
                territory, ward_id, house_id = index
                price = new_world_data.loc[index]['price']
                key = f"{territory} {str(ward_id + 1).zfill(2)}-{str(house_id + 1).zfill(2)}({price_lv(price)})"
                if 'owner' in diff.columns and pd.notna(row.loc['owner', 'self']):
                    old, new = row.loc['owner']
                    if old and new:
                        self.logger.info(f"{key} owner change from [{old}] to [{new}]")
                    elif old and not new:
                        self.logger.info(f"{key} start to sale on {price} Gil (own by [{old}] before)")
                    else:
                        self.logger.info(f"{key} is bought by [{new}]")
                else:
                    old, new = row.loc['price']
                    if old > new:
                        self.logger.info(f"{key} reduced price from {old} Gil to {new} Gil")
                    else:
                        need_save = True
                        data[key][0] = datetime.now().timestamp()
                        data[key][1] = price
                        self.logger.info(f"{key} cool down refresh to {new} Gil")
            self._world_data[current_world] = new_world_data
            if len(diff.index):
                self._world_data[current_world].to_csv(self.storage.path / f'{current_world}.csv')
        self.current_world = current_world
        self.logger.debug(self.list_data())
        self.logger.debug(f"finish searching in {time.time() - start:.2f}s")
        if need_save:
            self.storage.save()
            self.update_client()

    def full_search(self):
        if self.is_searching:
            self.logger.warning("Search is already in progress, wont try to search for new one")
            return
        self.is_searching = time.time()
        try:
            self._full_search()
        finally:
            self.prev_search_time = time.time()
            self.is_searching = 0

    def frame_work(self):
        if self.auto_search_period and \
                self.prev_search_time+ self.auto_search_period <= time.time()  and \
                not self.is_searching and plugins.XivMemory.actor_table.me:
            self.create_mission(self.full_search, limit_sec=0)

    def goto(self, territory_id, ward_id, house_id, world_id=None):
        if world_id is None:
            world_id = plugins.XivMemory.world_id
        plugins.XivNetwork.send_messages('zone', ('ClientTrigger', GotoStruct(a=0xd3, l=territory_id, wo=world_id, h=house_id, w=ward_id, m=0x60)))
        return True

    def update_client(self):
        self.client_event('empty_house', [
            {
                'name': key,
                'start': d[0],
                'price': d[1],
                'data': d[2]
            }
            for key, d in sorted(self.get_world_count_down_data().items(), key=lambda x: x[1][1])
        ])
        return True
