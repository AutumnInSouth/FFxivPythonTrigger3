from XivCombat.strategies import *
from XivCombat.multi_enemy_selector import FarCircle, NearCircle, select
from .pvp_dmg_effects import source_dmg_modify, target_dmg_modify


class UseAbility(UseAbility):
    def __init__(self, ability_id: int, target=None, *args, **kwargs):
        super().__init__(ability_id, target.id if target else None, *args, **kwargs)
        self._target = target
        # if target is not None and target != api.get_me_actor():
        #     api.set_current_target(target)


class GnbEnemy:
    def __init__(self, data: 'LogicData', actor: 'api.Actor'):
        self.data = data
        self.actor = actor
        self.hpp = actor.current_hp / actor.max_hp
        self.tdmg_modify = target_dmg_modify(actor)
        self.real_hp = actor.current_hp / self.tdmg_modify
        self.distance = data.actor_distance_effective(actor)
        self.is_robot = actor.effects.has(1420)


gnb_aoe = NearCircle(5)


class GnbPvpLogic(Strategy):
    name = 'ny/gnb_pvp'
    job = 'Gunbreaker_pvp'

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        match action_id:
            case 17716 | 17671 | 18952:
                mo_enyity = api.get_mo_target()
                if mo_enyity is not None:
                    return UseAbility(action_id, mo_enyity)
            case 17748:
                if not data[17890]:
                    enemy = max(
                        (actor for actor in data.valid_enemies
                         if actor.type == 'player' and
                         data.target_action_check(17890, actor)),
                        key=lambda actor: (actor.job.is_range, -actor.current_hp / actor.max_hp),
                        default=None
                    )
                    if enemy is not None:
                        return UseAbility(17890, enemy)
            case 17717:
                target = min(
                    (GnbEnemy(data, actor)
                     for actor in data.valid_enemies
                     if data.target_action_check(17717, actor)),
                    key=lambda x: (not x.is_robot, x.real_hp), default=None)
                if target is not None:
                    return UseAbility(17717, target.actor)

    def common_ability(self, data: 'LogicData') -> AnyUse:
        if data.me.current_hp / data.me.max_hp <= 0.7:
            if data[18943] <= 5:
                data.me.current_hp += 3000
                return UseAbility(18943, data.me)
            elif not data[17891]:
                data.me.current_hp += 3000
                return UseAbility(17891, data.me)
            elif data[18943] <= 30:
                data.me.current_hp += 3000
                return UseAbility(18943, data.me)
        enemies = [GnbEnemy(data, actor)
                   for actor in data.valid_enemies
                   if data.target_action_check(17717, actor)]
        if not enemies: return None
        enemies_in_five = [enemy for enemy in enemies if enemy.distance <= 5]
        _, aoe_cnt = select(data, [enemy.actor for enemy in enemies_in_five], gnb_aoe)
        single_enemy = min(enemies_in_five, key=lambda x: (not x.is_robot, x.real_hp), default=None)
        far_enemy = min(enemies, key=lambda x: (not x.is_robot, x.real_hp))
        if 2002 in data.effects or 2003 in data.effects or 2004 in data.effects:
            if single_enemy is not None:
                return UseAbility(17711, single_enemy.actor)
        elif data.gcd < 0.4:
            if single_enemy is not None:
                if data.gauge.cartridges:
                    if not data[17706] and aoe_cnt < 4:
                        return UseAbility(17706, single_enemy.actor)
                    # elif 2392 not in data.effects:
                    #     return UseAbility(17717, far_enemy.actor)
                    elif aoe_cnt > 2:
                        return UseAbility(17710)
                    else:
                        return UseAbility(17709, single_enemy.actor)
                match data.combo_id:
                    case 17703:
                        return UseAbility(17704, single_enemy.actor)
                    case 17704:
                        return UseAbility(17705, single_enemy.actor)
                    case 17706:
                        return UseAbility(17707, single_enemy.actor)
                    case 17707:
                        return UseAbility(17708, far_enemy.actor)
                    case 18910:
                        return UseAbility(18911)
                if aoe_cnt > 2:
                    return UseAbility(18910)
                else:
                    return UseAbility(17703, single_enemy.actor)
            else:
                return UseAbility(17717, far_enemy.actor)
