from functools import cached_property, lru_cache, cache
from math import sqrt
from typing import TYPE_CHECKING

from FFxivPythonTrigger.saint_coinach import action_sheet,territory_type_sheet

from . import api

if TYPE_CHECKING:
    from . import Config

invincible_effects = {325, 394, 529, 656, 671, 775, 776, 895, 969, 981, 1570, 1697, 1829, 1302, }
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


@cache
def zone_is_pvp(zone_id):
    if not zone_id: return False
    return territory_type_sheet[zone_id]["IsPvpZone"]


class LogicData(object):
    def __init__(self, config: 'Config.CombatConfig'):
        self.config = config

    @cached_property
    def me(self):
        """
        :return: current control actor
        """
        return api.get_me_actor()

    @cached_property
    def job(self):
        """
        :return: current job (add pvp when current zone is pvp zone)
        """
        if self.is_pvp:
            return f"{api.get_current_job()}_pvp"
        else:
            return str(api.get_current_job())

    @cached_property
    def target(self):
        """
        :return: auto choose target actor (if exist)
        """
        for method in self.config.target:
            t = self.get_target(method)
            if t is not None and is_actor_status_can_damage(t): return t

    @lru_cache
    def get_target(self, method: str):
        """
        different method to get target
        """
        if method == "current":
            return self.current_target
        if method == "focus":
            return self.focus_target
        if method == "list_distance":
            return self.list_dis_target
        if method == "list_hp":
            return self.list_hp_target
        if method == "list_hpp":
            return self.list_hpp_target

    @cached_property
    def current_target(self):
        """
        :return: current selected actor
        """
        return api.get_current_target()

    @cached_property
    def focus_target(self):
        """
        :return: current focused target
        """
        return api.get_focus_target()

    @cached_property
    def list_dis_target(self):
        """
        :return: nearest enemy from valid_enemies (default sorted by distance)
        """
        if not self.valid_enemies: return
        return self.valid_enemies[0]

    @cached_property
    def list_hp_target(self):
        """
        :return: lowest hp enemy from valid_enemies
        """
        if not self.valid_enemies: return
        return min(self.valid_enemies, key=lambda x: x.currentHP)

    @cached_property
    def list_hpp_target(self):
        """
        :return:lowest hp percent enemy from valid_enemies
        """
        if not self.valid_enemies: return
        return min(self.valid_enemies, key=lambda x: x.currentHP / x.maxHp)

    @cached_property
    def valid_party(self):
        """
        :return: list of actors in party if member can be selected
        """
        ids = (member.id for member in api.get_party_list() if member.id and member.id != 0xe0000000)
        return [actor for actor in api.get_actors_by_id(*ids) if actor.can_select]

    @cached_property
    def valid_alliance(self):
        """
        :return: list of actors in alliance if member can be selected
        """
        ids = (member.id for member in api.get_party_list(alliance_all=True) if member.id and member.id != 0xe0000000)
        return [actor for actor in api.get_actors_by_id(*ids) if actor.can_select]

    @cached_property
    def valid_players(self):
        """
        :return: list of actors which is player actor
        """
        return [player for player in api.get_players() if player.can_select]

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
        enemies = api.get_actors_by_id(*{enemy.id for enemy in Utils.query(api.get_enemies_iter(), key=lambda x: x.can_select)})
        enemies = [enemy for enemy in enemies if is_actor_status_can_damage(enemy)]
        if self.config.enable_extra_enemies:
            enemy_id = {enemy.id for enemy in api.get_enemies_iter()}
            extra_enemies = list()
            for enemy in api.get_can_select():
                if enemy.id not in enemy_id and self.valid_extra_enemies(enemy):
                    extra_enemies.append(enemy)
            enemies += extra_enemies
        return sorted(enemies, key=lambda enemy: enemy.effectiveDistanceX)

    @lru_cache
    def valid_extra_enemies(self, enemy):
        if not is_actor_status_can_damage(enemy): return False
        if enemy.effectiveDistanceY > self.config.extra_enemies_distance: return False
        if enemy.currentHP < 3: return False
        if self.config.extra_enemies_combat_only and not enemy.is_in_combat: return False
        if not api.can_use_action_to(test_enemy_pvp_action if self.is_pvp else test_enemy_action, enemy): return False
        return True

    @lru_cache
    def dps(self, actor_id):
        """
        get dps of an actor
        """
        return api.get_actor_dps(actor_id)

    @lru_cache
    def tdps(self, actor_id):
        """
        get tdps of an actor
        """
        return api.get_actor_tdps(actor_id)

    @lru_cache
    def ttk(self, actor_id):
        """
        get time to kill of an actor
        """
        t = api.get_actor_by_id(actor_id)
        if t is None:
            return -1
        else:
            tdps = self.tdps(actor_id)
            return (t.currentHP / tdps) if tdps else 1e+99

    @cached_property
    def combo_state(self):
        """
        current combo state
        """
        return api.get_combo_state()

    @property
    def combo_id(self):
        """
        current combo action id (last used combo action)
        """
        return self.combo_state.action_id

    @property
    def combo_remain(self):
        """
        current combo remain time
        """
        return self.combo_state.remain

    @cached_property
    def effects(self):
        """
        an dict of effect on user ( key:effect id , value:effect object )
        """
        return self.me.effects.get_dict()

    @cached_property
    def gauge(self):
        """
        get current gauge
        """
        return api.get_gauge()

    @cached_property
    def gcd_group(self):
        return api.get_gcd_group()

    @property
    def gcd(self):
        """
        remain gcd time
        """
        return self.gcd_group.remain

    @property
    def gcd_total(self):
        """
        the total gcd time (if is counting gcd)
        """
        return self.gcd_group.total

    @property
    def time_to_kill_target(self):
        """
        the time to kill of chosen target
        """
        if self.target is None: return 1e+99
        return self.ttk(self.target.id)

    @cached_property
    def max_ttk(self):
        """
        the largest time to kill in valid enemies
        """
        if not len(self.valid_enemies): return 1e+99
        return max(self.ttk(e.id) for e in self.valid_enemies)

    def reset_cd(self, action_id: int):
        """
        reset the cd of a skill (just in client!)
        """
        api.reset_cd(action_sheet[action_id]['CooldownGroup'])

    @cache
    def skill_cd(self, action_id: int):
        """remain time of an action cool down"""

        row = action_sheet[action_id]
        if self.me.level < row['ClassJobLevel'] or action_id in self.config.skill_disable:
            return 1e+99
        else:
            return api.get_cd_group(row['CooldownGroup']).remain

    @cache
    def pvp_skill_cd(self, action_id: int):
        """remain time of an pvp action cool down"""

        gp = api.pvp_action_cd_group_id(action_id)
        if gp:
            return api.get_cd_group(gp).remain
        else:
            return None

    def lv_skill(self, base_id, *statements):
        """(unused) lower level skill select"""
        me_lv = self.me.level
        for statement in statements:
            if me_lv >= statement[0]:
                break
            else:
                base_id = statement[1]
        return base_id

    def __getitem__(self, item):
        return self.skill_cd(item)

    @lru_cache
    def item_count(self, item_id, is_hq: bool = None):
        """count items in backpack"""
        return api.get_backpack_item_count(item_id, is_hq)

    @cached_property
    def is_moving(self):
        """if user is moving"""
        return self.config.custom_settings.setdefault('keep_moving', 'false') == 'true' or bool(api.get_movement_speed())

    @lru_cache
    def actor_distance_effective(self, target_actor):
        """effective distance between user and a target"""
        if self.config.custom_settings.setdefault('use_builtin_effective_distance', 'false') == 'true':
            return target_actor.effectiveDistanceX
        else:
            t_pos = target_actor.pos
            m_pos = self.coordinate
            return sqrt((t_pos.x - m_pos.x) ** 2 + (t_pos.y - m_pos.y) ** 2) - self.me.HitboxRadius - target_actor.HitboxRadius

    @cached_property
    def target_distance(self):
        """effective distance between user and selected target"""
        t = self.target
        if t is None: return 1e+99
        return self.actor_distance_effective(t)

    @cached_property
    def coordinate(self):
        """coordinate of the user"""
        return api.get_coordinate()

    @cached_property
    def is_pvp(self):
        """is current zone pvp zone"""
        return zone_is_pvp(api.get_zone_id())
