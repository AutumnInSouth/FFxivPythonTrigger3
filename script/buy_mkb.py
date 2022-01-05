import time

from FFxivPythonTrigger import plugins

buy_list = {
    # 33932: (30, 45000),  # 暴击10
    # 33919: (75, 40000),  # 暴击9
    # 33931: (45, 45000),  # 直击10
    33918: (50, 50000),  # 直击9
    # 33941: (30, 15000),  # 技速10
    33928: (350, 25000),  # 技速9
}


def count_back_pack(item_id):
    return sum(item.count for item in plugins.XivMemory.inventory.get_item_in_containers_by_key(item_id, 'backpack'))


def gil_cnt():
    for item in plugins.XivMemory.inventory.get_item_in_containers_by_key(1, 'currency'):
        return item.count


def group_pmb_data(item_id, max_price_per_item=None):
    data = {}
    for item in plugins.Pmb.query(item_id):
        if max_price_per_item is not None and item['price_per_unit'] > max_price_per_item:
            break
        if item['price_per_unit'] not in data:
            data[item['price_per_unit']] = []
        data[item['price_per_unit']].append(item)
    return data


def item_cost_cal(item_data, need_to_buy):
    total = item_data['total_item_count'] * item_data['price_per_unit'] + item_data['total_tax']
    if item_data['total_item_count'] > need_to_buy:
        s = need_to_buy * item_data['price_per_unit'] + (item_data['total_item_count'] - need_to_buy) * item_data['price_per_unit'] * 1.2
        return s / item_data['total_item_count'], total
    return item_data['price_per_unit'], total


def action(item_id, required_count, max_price):
    print('try', item_id, required_count, max_price)
    item_data = group_pmb_data(item_id, max_price)
    need_to_buy = required_count - count_back_pack(item_id)
    if need_to_buy > 0:
        for _item_list in item_data.values():
            item_list = [(item, *item_cost_cal(item, need_to_buy)) for item in _item_list]
            item_list.sort(key=lambda x: x[1])
            for item, price, total in item_list:
                if total <= gil_cnt() and price <= max_price:
                    plugins.Pmb.buy(item)
                    print('buy', total, price, item_id)
                    return True
    return False


def main():
    for item_id, (count, max_price) in buy_list.items():
        require = count - count_back_pack(item_id)
        print('item_id', item_id, require)
        if require > 0:
            while action(item_id, count, max_price):
                time.sleep(.5)


main()
