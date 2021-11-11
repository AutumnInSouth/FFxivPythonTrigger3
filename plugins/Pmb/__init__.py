from pathlib import Path

from FFxivPythonTrigger import PluginBase, plugins
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.utils import wait_until


def try_int(s: str):
    try:
        return int(s)
    except ValueError:
        return s


class Pmb(PluginBase):
    name = "Pmb"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        self.item_data = {}
        self.item_ready = {}

    @event('network/zone/server/market_board_item_listing')
    def collect_items(self, evt):
        key = evt.item.key
        if key in self.item_ready:
            for i in range(evt.item_count):
                item = evt.struct_message.items[i]
                self.item_data[key][i + evt.struct_message.list_index_start] = {
                    'listing_id': item.listing_id,
                    'retainer_id': item.retainer_id,
                    'price_per_unit': item.price_per_unit,
                    'total_tax': item.total_tax,
                    'total_item_count': item.total_item_count,
                    'item_id': item.item_id,
                    'unk0': item.unk0,
                    'is_hq': item.is_hq,
                    'retainer_city_id': item.retainer_city_id,
                    'retainer_name': item.retainer_name,
                    'player_name': item.player_name,
                }
            if not evt.struct_message.list_index_end:
                self.item_ready[key] = True

    def query(self, item_id):
        self.item_ready[item_id] = None
        if item_id not in self.item_data:
            self.item_data[item_id] = [None] * 100
        count = plugins.XivNetwork.send_messages(
            'zone', ("MarketBoardQueryItemCount", {
                'item_id': item_id, 'unk1': 0x902
            }), "MarketBoardItemListingCount").struct_message.item_count
        if not count:
            raise Exception(f"no item founds")
        wait_until(lambda: self.item_ready.get(item_id), 5.)
        return self.item_data[item_id][:count]

    def buy(self, item_data: dict):
        return plugins.XivNetwork.send_messages('zone', (
            'MarketBoardPurchaseHandler', {k: try_int(v) for k, v in item_data.items()}
        ))
