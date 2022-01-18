from XivCombat.strategies import *
from XivCombat.multi_enemy_selector import FarCircle, NearCircle, select
from .pvp_dmg_effects import source_dmg_modify, target_dmg_modify


class UseAbility(UseAbility):
    def __init__(self, ability_id: int, target=None, calc_dmg: int = 0, wait_until=None, *args, **kwargs):
        super().__init__(ability_id, target.id if target else None, *args, wait_until=wait_until or self.cb, **kwargs)
        self._target = target
        self._calc_dmg = calc_dmg
        # if target is not None and target != api.get_me_actor():
        #     api.set_current_target(target)

    def cb(self):
        if self._target:
            self._target.current_hp -= int(self._calc_dmg)
        return True



def get_static_dmg(data: 'LogicData'):
    rtn = 2000 * data.gauge.ninki_amount // 50
    if 1316 in data.effects: rtn += 1000
    rtn += 2000 if data[8816] <= 15 else 1000
    return rtn


def get_total_dmg(data: 'LogicData', target: 'api.Actor', static_dmg: int):
    rtn = 0
    c_hp = target.current_hp - static_dmg
    if not data[8814]: rtn += (1 - c_hp / target.max_hp) * 2000 + 1000
    if not data[18992]: rtn += (1 - c_hp / target.max_hp) * 2400 + 600
    return rtn


class NinjaEnemy:
    def __init__(self, data: 'LogicData', actor: 'api.Actor'):
        self.data = data
        self.actor = actor
        self.taken_damage_modify = target_dmg_modify(actor)
        self.efficient_hp = actor.current_hp / self.taken_damage_modify
        self.total_dmg = 0
        self.is_robot = actor.effects.has(1420)
        self.distance = data.actor_distance_effective(actor)

    def calc_total_dmg(self, static_dmg: int, self_dmg_modify: float):
        self.total_dmg = get_total_dmg(self.data, self.actor, static_dmg) * self_dmg_modify * self.taken_damage_modify
        return self.total_dmg


fire = FarCircle(15, 5)
circle = NearCircle(5)


class NinPvpLogic(Strategy):
    name = 'ny/nin_pvp'
    job = 'Ninja_pvp'

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int):
        if action_id == 8812:
            return UseAbility(8812, target_position=api.get_mo_location())

    def common_ability(self, data: 'LogicData') -> AnyUse:
        if data.me.current_hp / data.me.max_hp <= 0.7 and data[18943] <= 30:
            data.me.current_hp += 3000
            return UseAbility(18943, data.me)

        enemies = [NinjaEnemy(data, enemy)
                   for enemy in data.valid_enemies
                   if data.actor_distance_effective(enemy) <= 25
                   and data.target_action_check(17733, enemy)]
        if not enemies: return
        self_dmg_modify = source_dmg_modify(data.effects)
        self_static_dmg = get_static_dmg(data)
        target = min(
            (enemy for enemy in enemies if enemy.distance <= 5 and enemy.actor.type == 'player' and
             enemy.actor.current_hp < enemy.calc_total_dmg(self_static_dmg, self_dmg_modify)),
            key=lambda x: x.efficient_hp, default=None
        )
        if target is not None:
            if not data[8814]:
                ass_dmg = ((1 - target.actor.current_hp / target.actor.max_hp) * 2000 + 1000) * self_dmg_modify
                if target.efficient_hp <= ass_dmg:
                    return UseAbility(8814, target.actor, ass_dmg * target.taken_damage_modify)
            else:
                ass_dmg = 0

            if 1316 in data.effects:
                return UseAbility(17735, target.actor, 1200 * self_dmg_modify * target.taken_damage_modify)

            if not data[18992]:
                smite_dmg = ((1 - target.actor.current_hp / target.actor.max_hp) * 2400 + 600) * self_dmg_modify
                if target.efficient_hp <= smite_dmg + ass_dmg:
                    return UseAbility(18992, target.actor, smite_dmg * target.taken_damage_modify)

            if 1317 in data.effects:
                if data.gcd < .4:
                    return UseAbility(17733, target.actor, 2400 * self_dmg_modify * target.taken_damage_modify)
            elif data[8816] <= 15:
                return UseAbility(8816, wait_until=lambda: 1317 in data.refresh_cache('effects'))

            if not data[8815] and data.gauge.ninki_amount >= 50:
                return UseAbility(8815, target.actor, 1000 * self_dmg_modify * target.taken_damage_modify)
        single_target = min((enemy for enemy in enemies if enemy.distance <= 5), key=lambda x: (not x.is_robot, x.efficient_hp), default=None)
        if 1316 in data.effects or 1315 in data.effects:
            if single_target and 1316 in data.effects and data.effects[1316].timer <= 2:
                return UseAbility(17735, single_target.actor, 1200 * self_dmg_modify * single_target.taken_damage_modify)
            return

        if data.gcd < .4:
            if 1317 in data.effects:
                ice_target = min(enemies, key=lambda x: x.efficient_hp)
                ice_dmg = 2400 * self_dmg_modify
                if ice_target.efficient_hp <= ice_dmg:
                    return UseAbility(17733, ice_target.actor)

                fire_target, fire_cnt = select(data, (enemy.actor for enemy in enemies), fire)
                if fire_cnt >= 2: return UseAbility(17732, fire_target)

                return UseAbility(17733, ice_target.actor)

            enemies_in_five = [enemy for enemy in enemies if enemy.distance <= 5]
            if enemies_in_five:
                aoe_target, aoe_cnt = select(data, (enemy.actor for enemy in enemies), circle)
                if aoe_cnt>2:
                    if data.combo_id == 18921: return UseAbility(18922)
                    return UseAbility(18921)
                if data.combo_id == 8808:
                    return UseAbility(8809, single_target.actor, 1400 * self_dmg_modify * single_target.taken_damage_modify)
                if data.combo_id == 8807:
                    return UseAbility(8808, single_target.actor, 1200 * self_dmg_modify * single_target.taken_damage_modify)
                return UseAbility(8807, single_target.actor, 1000 * self_dmg_modify * single_target.taken_damage_modify)

            target = min((enemy for enemy in enemies if enemy.distance <= 15), key=lambda x: x.efficient_hp, default=None)
            if target: return UseAbility(8811, target.actor, 800 * self_dmg_modify * target.taken_damage_modify)

        if not data[8816] and 1317 not in data.effects:
            return UseAbility(8816, wait_until=lambda: 1317 in data.refresh_cache('effects'))
        if data.gauge.ninki_amount >= 50:
            fire_target, fire_cnt = select(data, (enemy.actor for enemy in enemies), fire)
            if fire_cnt >= 2: return UseAbility(17731, fire_target)
            if single_target: return UseAbility(8815, single_target.actor, 2000 * self_dmg_modify * single_target.taken_damage_modify)
