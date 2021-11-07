from ctypes import addressof
from functools import cache

from FFxivPythonTrigger import plugins

_func_action_data = lambda a: 0

_func_can_use_action_to = lambda a, b, c: False

_func_action_distance_check = lambda a, b, c: 0


def pvp_action_cd_group_id(action_id):
    pvp_actions = plugins.XivMemory.pvp_action
    if pvp_actions.action_1_id == action_id:
        return 26
    elif pvp_actions.action_2_id == action_id:
        return 27
    else:
        return 0


@cache
def _action_data(action_id):
    return _func_action_data(action_id)


def action_type_check(action_id, actor) -> bool:
    return _func_can_use_action_to(action_id, _action_data(action_id), addressof(actor))


def action_distance_check(action_id, source_actor, target_actor):
    return _func_action_distance_check(action_id, source_actor, target_actor)


def get_me_actor():
    return plugins.XivMemory.actor_table.me


def get_actor_by_id(a_id: int):
    return plugins.XivMemory.actor_table.get_actor_by_id(a_id)


def get_actors_by_ids(*a_id: int):
    return plugins.XivMemory.actor_table.get_actors_by_ids(a_id)


def get_party_list(alliance_all=False):
    return get_actors_by_ids(*[member.id for member in (plugins.XivMemory.party.alliance if alliance_all else plugins.XivMemory.party.main_party)()])


def get_can_select():
    return [actor for actor in plugins.XivMemory.actor_table.get_item() if actor.can_select]


def get_current_target():
    return plugins.XivMemory.targets.current


def get_focus_target():
    return plugins.XivMemory.targets.focus


def get_mo_target():
    return plugins.XivMemory.utils.mo_entity


def set_current_target(actor):
    plugins.XivMemory.targets.current = actor


def get_enemies_list():
    return get_actors_by_ids(*[enemy.id for enemy in plugins.XivMemory.enemies.get_item() if enemy.can_select])


def get_current_job():
    return plugins.XivMemory.player_info.job.value


def get_combo_state():
    return plugins.XivMemory.combo_state


def get_gauge():
    return plugins.XivMemory.gauge


def get_global_cool_down_group():
    return plugins.XivMemory.cool_down_group.gcd_group


def get_item_cool_down_group():
    return plugins.XivMemory.cool_down_group.item_group


# def get_actor_dps(a_id: int):
#     return api.CombatMonitor.actor_dps(a_id)
#
#
# def get_actor_tdps(a_id: int):
#     return api.CombatMonitor.actor_tdps(a_id, period_sec=600)
#

def get_cd_group(cd_group: int):
    return plugins.XivMemory.cool_down_group[cd_group]


def reset_cd(cd_group: int):
    temp = get_cd_group(cd_group)
    temp.duration = temp.total


def use_action(action_id: int, target_id: int = 0xE0000000):
    plugins.XivMemory.combat_data.skill_queue.use_action(action_id, target_id)


def use_area_action(action_id: int, x: float, y: float, z: float, target=0xE0000000):
    plugins.XivMemory.calls.do_action_location(1, action_id, x, y, z, target)


def use_area_action_to_target(action_id: int, target_actor):
    plugins.XivMemory.calls.do_action_location(1, action_id, target_actor.pos.x, target_actor.pos.y, target_actor.pos.z, target_actor.id)


def do_action(action_type: int, action_id: int, target_id: int, *args):
    plugins.XivMemory.calls.do_action(action_type, action_id, target_id, *args)


def use_item(item_id: int, is_hq=False, target_id: int = 0xE0000000):
    plugins.XivMemory.calls.do_action.use_item(item_id + 1000000 if is_hq else item_id, target_id)


def use_common(action_id: int, target_id: int = 0xE0000000):
    plugins.XivMemory.calls.do_action.common_action(action_id, target_id)


def get_ani_lock():
    return plugins.XivMemory.skill_animation_lock


def reset_ani_lock():
    plugins.XivMemory.skill_animation_lock = 0


def skill_queue_is_empty():
    return not plugins.XivMemory.skill_queue.has_skill


def get_backpack_item_count(item_id: int, is_hq: bool = None):
    cnt = 0
    for item in plugins.XivMemory.inventory.get_item_in_containers_by_key(item_id, "backpack"):
        if is_hq is None or item.is_hq == is_hq: cnt += item.count
    return cnt


def get_movement_speed():
    return plugins.XivMemory.movement.speed


def get_coordinate():
    return plugins.XivMemory.coordinate.coordinate_main


def get_zone_id():
    return plugins.XivMemory.zone_id
