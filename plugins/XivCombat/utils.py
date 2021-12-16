import time
from functools import cache
from time import perf_counter
from typing import TYPE_CHECKING

from FFxivPythonTrigger.meta_data import actions, status
from FFxivPythonTrigger.saint_coinach import action_sheet, territory_type_sheet
from . import define, strategies, api, multi_enemy_selector

if TYPE_CHECKING:
    from .logic_data import LogicData


def use_item(to_use: strategies.UseItem):
    api.reset_ani_lock()
    match to_use.priority:
        case define.HQ_ONLY:
            if api.get_backpack_item_count(to_use.item_id, True):
                api.use_item(to_use.item_id, True, to_use.target_id)
        case define.NQ_ONLY:
            if api.get_backpack_item_count(to_use.item_id, False):
                api.use_item(to_use.item_id, False, to_use.target_id)
        case define.HQ_FIRST:
            if api.get_backpack_item_count(to_use.item_id, True):
                api.use_item(to_use.item_id, True, to_use.target_id)
            elif api.get_backpack_item_count(to_use.item_id, False):
                api.use_item(to_use.item_id, False, to_use.target_id)
        case define.NQ_FIRST:
            if api.get_backpack_item_count(to_use.item_id, False):
                api.use_item(to_use.item_id, False, to_use.target_id)
            elif api.get_backpack_item_count(to_use.item_id, True):
                api.use_item(to_use.item_id, True, to_use.target_id)


@cache
def is_area_action(action_id: int):
    return action_sheet[action_id]['TargetArea']


def use_ability(to_use: strategies.UseAbility):
    if to_use.ability_id is None: return
    if is_area_action(to_use.ability_id):
        api.reset_ani_lock()
        if to_use.target_position: api.use_area_action(to_use.ability_id, *to_use.target_position, 0xe0000000)
        actor = api.get_actor_by_id(to_use.target_id) if to_use.target_id != 0xe0000000 else api.get_me_actor()
        if actor is not None:  api.use_area_action(to_use.ability_id, actor.pos.x, actor.pos.y, actor.pos.z, actor.id)
    else:
        api.use_action(to_use.ability_id, to_use.target_id)
        if to_use.wait_until:
            prev = perf_counter()
            while not to_use.wait_until() and perf_counter() - prev < 2:
                time.sleep(0.1)


@cache
def zone_is_pvp(zone_id):
    if not zone_id: return False
    return territory_type_sheet[zone_id]["IsPvpZone"]


def is_pvp():
    return zone_is_pvp(api.get_zone_id())


def job_name():
    if is_pvp():
        return f"{api.get_current_job()}_pvp"
    else:
        return str(api.get_current_job())


def a(action_name: str) -> int:
    return actions[action_name].id


def s(status_name: str) -> int:
    return status[status_name].id


def cnt_enemy(data: 'LogicData', ability):
    target, cnt = multi_enemy_selector.select(data, data.valid_enemies, ability)
    if not cnt: return data.target, 0
    if data.config['single'] == define.FORCE_SINGLE: return data.target, 1
    if data.config['single'] == define.FORCE_MULTI: return data.target, 3
    return target, cnt


def res_lv(data: 'LogicData', max_ttk: float = 10):
    match data.config['resource']:
        case define.RESOURCE_SQUAND:
            return 2
        case define.RESOURCE_NORMAL:
            return 1
        case define.RESOURCE_STINGY:
            return 0
        case _:
            return int(data.max_ttk > max_ttk)


def find_area_belongs_to_me(data: 'LogicData'):
    for actor in data.actor_belongs_to_me:
        if actor.type == 'area':
            return actor
