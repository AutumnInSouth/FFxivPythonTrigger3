from functools import cached_property, lru_cache, cache
from math import sqrt

from FFxivPythonTrigger.saint_coinach import action_sheet

from . import api, define, utils
from .strategies import UseAbility
from typing import Callable, TYPE_CHECKING
from .define import AbilityType

if TYPE_CHECKING:
    from . import XivCombat

invincible_effects = {325,
                      394,
                      529,
                      656,
                      671,
                      775,
                      776,
                      895,
                      969,
                      981,
                      1570,
                      1697,
                      1829,
                      1302,
                      # 大额减伤
                      350, }
invincible_actor = set()

test_enemy_action = 9
test_enemy_pvp_action = 8746


def is_actor_status_can_damage(actor):
    if actor.id in invincible_actor or not actor.can_select:
        return False
    for eid, _ in actor.effects.get_items():
        if eid in invincible_effects:
            return False
    return True


class LogicData(object):
    def __init__(self, config: dict, plugin: 'XivCombat'):
        self.plugin = plugin
        self.config = config
        self.ability_cnt = 0
        self.last_action: int | None = None
        self.action_history: list[tuple[float, int]] = []  # [(time, action_id)]
        self.last_count_down: float | None = None

    def refresh_cache(self, key: str):
        try:
            del self.__dict__[key]
        except KeyError:
            pass
        return getattr(self, key)

    @cached_property
    def me(self):
        return api.get_me_actor()

    @cached_property
    def job(self):
        return utils.job_name()

    @cached_property
    def target_check_action(self):
        return test_enemy_pvp_action if self.is_pvp else test_enemy_action

    @lru_cache
    def is_target_attackable(self, target_actor):
        return (is_actor_status_can_damage(target_actor) and
                api.action_type_check(self.target_check_action, target_actor) and
                target_actor.current_hp > 1)

    @cached_property
    def target(self):
        for method in self.config['target_priority']:
            t = self.get_target(method)
            if t is not None and self.is_target_attackable(t):
                return t

    # @lru_cache
    def get_target(self, method: str, valid_enemies: list['api.Actor'] = None):
        if valid_enemies is None:
            valid_enemies = self.valid_enemies
        match method:
            case define.CURRENT_SELECTED:
                return api.get_current_target()
            case define.FOCUSED:
                return api.get_focus_target()
            case define.DISTANCE_NEAREST:
                return min(valid_enemies, key=self.actor_distance_effective, default=None)
            case define.DISTANCE_FURTHEST:
                return max(valid_enemies, key=self.actor_distance_effective, default=None)
            case define.HP_HIGHEST:
                return max(valid_enemies, key=lambda x: x.current_hp, default=None)
            case define.HP_LOWEST:
                return min(valid_enemies, key=lambda x: x.current_hp, default=None)
            case define.HPP_HIGHEST:
                return max(valid_enemies, key=lambda x: x.current_hp / x.max_hp, default=None)
            case define.HPP_LOWEST:
                return min(valid_enemies, key=lambda x: x.current_hp / x.max_hp, default=None)

    @cached_property
    def valid_party(self):
        return [actor for actor in api.get_party_list() if actor.can_select] or [self.me]

    @cached_property
    def valid_alliance(self):
        return [actor for actor in api.get_party_list(True) if actor.can_select] or [self.me]

    @cached_property
    def valid_players(self):
        return [actor for actor in self.all_actors if actor.type == 1]

    @cached_property
    def all_actors(self):
        return api.get_can_select()

    @cache
    def target_action_check(self, action_id, target):
        """
        ray check if you can use the action on target (not checking actor type!)
        :param action_id: the action id check
        :param target: the target actor
        :return: if action can use
        """
        o = self.me.pos.r
        self.me.pos.r = self.me.target_radian(target)
        ans = not api.action_distance_check(action_id, self.me, target)
        self.me.pos.r = o
        return ans

    @cached_property
    def valid_enemies(self):
        """
        all actors select from enemy list, and if enable extra_enemies, also search in actor table
        :return: list of enemy actor sorted by distance
        """
        match self.config['targets']:
            case define.ONLY_SELECTED:
                current = api.get_current_target()
                all_enemy = [] if current is None or not self.is_target_attackable(current) else [current]
            case define.ENEMY_LIST:
                all_enemy = [actor for actor in api.get_enemies_list() if self.is_target_attackable(actor)]
            case define.ALL_IN_COMBAT | define.ALL_CAN_ATTACK as k:
                all_enemy = [actor for actor in api.get_can_select() if self.is_target_attackable(actor)]
                if k == define.ALL_IN_COMBAT:
                    all_enemy = [actor for actor in all_enemy if actor.is_in_combat and self.is_target_attackable(actor)]
            case k:
                raise Exception(f'invalid targets {k}')
        return sorted(all_enemy, key=self.actor_distance_effective)

    def enemy_can_attack_by(self, action_id: int):
        """
        ray check if enemy can attack by action
        :param action_id: the action id check
        :return: if action can use
        """
        return [actor for actor in self.valid_enemies if self.target_action_check(action_id, actor)]

    @cached_property
    def monitor(self):
        return self.plugin.get_monitor()

    @lru_cache
    def dps(self, actor):
        return self.monitor.dps(actor.id)

    @lru_cache
    def tdps(self, actor):
        return self.monitor.dtps(actor.id)

    @lru_cache
    def ttk(self, actor):
        dtps = self.tdps(actor)
        if dtps == 0: return 1e+99
        return actor.current_hp / dtps

    @property
    def time_to_kill_target(self):
        if self.target is None: return 1e+99
        return self.ttk(self.target)

    @cached_property
    def max_ttk(self):
        if not len(self.valid_enemies): return 1e+99
        return max(self.ttk(e) for e in self.valid_enemies)

    @cached_property
    def combo_state(self):
        return api.get_combo_state()

    @property
    def combo_id(self):
        return self.combo_state.action_id

    @property
    def combo_remain(self):
        return self.combo_state.remain

    @cached_property
    def effects(self):
        return self.me.effects.get_dict()

    @cached_property
    def effects_set(self):
        return set(self.effects.keys())

    @cache
    def effect_time(self, effect_id: int):
        if effect_id in self.effects:
            return self.effects[effect_id].timer + 0.01
        return 0

    @cached_property
    def gauge(self):
        return api.get_gauge()

    @cached_property
    def gcd_group(self):
        return api.get_global_cool_down_group()

    @property
    def gcd(self):
        return self.gcd_group.remain

    @property
    def gcd_total(self):
        return self.gcd_group.total

    @cached_property
    def item_group(self):
        return api.get_item_cool_down_group()

    @cached_property
    def item_cd(self):
        return self.item_group.remain

    def reset_cd(self, action_id: int):
        """
        reset the cd of a skill (just in client!)
        """
        api.reset_cd(action_sheet[action_id]['CooldownGroup'])

    @cache
    def skill_unlocked(self, action_id: int):
        """
        check if the skill is unlocked
        """
        return self.me.level >= action_sheet[action_id]['ClassJobLevel'] and api.is_action_unlocked(action_id)

    @cache
    def skill_cd(self, action_id: int):
        """remain time of an action cool down"""
        if not self.skill_unlocked(action_id):
            return 1e+99
        else:
            return api.get_cd_group(action_sheet[action_id]['CooldownGroup']).remain

    @cache
    def pvp_skill_cd(self, action_id: int):
        """remain time of an pvp action cool down"""

        gp = api.pvp_action_cd_group_id(action_id)
        if gp:
            return api.get_cd_group(gp).remain
        else:
            return 1e+99

    def __getitem__(self, item):
        return self.skill_cd(item)

    @lru_cache
    def item_count(self, item_id, is_hq: bool = None):
        """count items in backpack"""
        return api.get_backpack_item_count(item_id, is_hq)

    @cached_property
    def is_moving(self):
        """if user is moving"""
        match self.config['cast_move']:
            case define.ALWAYS_CASTING:
                return False
            case define.ALWAYS_MOVING:
                return True
            case _:
                return bool(api.get_movement_speed())

    @lru_cache
    def actor_distance_effective(self, target_actor):
        """effective distance between user and a target"""
        if self.config['use_builtin_effective_distance']:
            return target_actor.effective_distance_x
        else:
            t_pos = target_actor.pos
            m_pos = self.coordinate
            return max(sqrt((t_pos.x - m_pos.x) ** 2 + (t_pos.y - m_pos.y) ** 2) - self.me.hitbox_radius - target_actor.hitbox_radius, 0)

    @cached_property
    def target_distance(self):
        t = self.target
        if t is None: return 1e+99
        return self.actor_distance_effective(t)

    @cached_property
    def coordinate(self):
        return api.get_coordinate()

    @cached_property
    def is_pvp(self):
        return utils.is_pvp()

    def use_ability_to_target(self, ability_id, ability_type: AbilityType = None,
                              wait_until: Callable = None):
        return UseAbility(ability_id=ability_id,
                          target_id=(self.target.id if self.target is not None else self.me.id),
                          ability_type=ability_type,
                          wait_until=wait_until)

    @cached_property
    def pet_id(self):
        return api.get_pet_id()

    @cached_property
    def actor_belongs_to_me(self):
        return api.get_actors_belongs_to(self.me.id)

    @cache
    def recast_time(self, action_id: int):
        return api.action_recast_time(action_id)
