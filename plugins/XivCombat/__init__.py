import traceback
from ctypes import *
from functools import lru_cache
from importlib import import_module
from inspect import isclass
from pathlib import Path
from threading import Lock
from typing import TYPE_CHECKING

import time

from FFxivPythonTrigger import PluginBase, AddressManager, plugins, PluginNotFoundException, game_ext
from FFxivPythonTrigger.decorator import event, BindValue, EventCall, ReEventCall
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import action_names, status_sheet, territory_type_names
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from . import define, strategies, api, logic_data, utils
from .define import AbilityType
from .utils import is_area_action, use_ability
from .monitor import Monitor

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control import HotEvent, DotEvent, DeathEvent, EffectRemoveEvent
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.extra_messages.actor_add_remove_effect import ActorAddEffectEvent, ActorRemoveEffectEvent
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent
    from XivNetwork.message_processors.zone_server.map_effect import ServerMapEffectEvent

command = "@acombat"
split_time = 30
ERR_LIMIT = 20
default_common_config = {
    'enable': False,
    'debug': False,
    'period': 0.2,
    'targets': define.ENEMY_LIST,
    'target_priority': [define.CURRENT_SELECTED, define.FOCUSED, define.DISTANCE_NEAREST],
    'load_targets_distance': 50,
    'resource': define.RESOURCE_AUTO,
    'single': define.SINGLE_AUTO,
    'use_builtin_effective_distance': False,
    'cast_move': define.CAST_MOVE_AUTO,
    'auto_set_current_target': False,
}
sigs = {
    "hot_bar_process": {
        'call': find_signature_address,
        'param': "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F B6 82 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "action_type_check": {
        'call': find_signature_address,
        'param': "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B 2D ? ? ? ? 49 8B D8",
        'add': BASE_ADDR,
    },
    "action_distance_check": {
        'call': find_signature_address,
        'param': "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 89 4C 24 ?",
        'add': BASE_ADDR,
    },
    "action_data_sig": {
        'call': find_signature_point,
        'param': "E8 * * * * 48 8B F0 48 85 C0 0F 84 ? ? ? ? BA ? ? ? ? 48 8B CB E8 ? ? ? ? 48 8B 0D ? ? ? ?",
        'add': BASE_ADDR,
    },
    "action_recast_ms": {
        'call': find_signature_point,
        'param': "E8 * * * * 8B D0 45 33 C0 49 8B CE E8 ? ? ? ? F6 46 ? ?",
        'add': BASE_ADDR,
    },
}
action_type_check_interface = CFUNCTYPE(c_bool, c_int64, c_int64, c_uint64)
action_distance_check_interface = CFUNCTYPE(c_int64, c_uint, c_int64, c_int64)
action_data_interface = CFUNCTYPE(c_int64, c_int64)
action_recast_interface = CFUNCTYPE(c_int, c_int, c_int, c_int64, c_int64) if game_ext > 3 else CFUNCTYPE(c_int, c_int, c_int, c_byte)
all_strategies = {}
strategy_events = {}
for file in (Path(__file__).parent / 'strategies').iterdir():
    if file.is_dir() and (file / '__init__.py').exists() or file.is_file() and file.suffix == '.py':
        module = import_module(f'{__package__}.strategies.{file.stem}')
        for name, obj in module.__dict__.items():
            if isinstance(obj, (EventCall, ReEventCall)):
                strategy_events[f"{file.stem}|{name}"] = obj
            elif isclass(obj) and issubclass(obj, strategies.Strategy) and obj != strategies.Strategy:
                all_strategies.setdefault(obj.job, {})[obj.name] = obj()

if strategy_events:
    strategy_events['name'] = "XivCombatStrategyEvent"
    XivCombatStrategyEvent = type('XivCombatStrategyEvent', (PluginBase,), strategy_events)

status_cant_action = {status.key for status in status_sheet if status['LockActions']}


class HotbarBlock(OffsetStruct({
    'type': (c_ubyte, 199),
    'param': (c_uint, 184),
})):
    type: int
    param: int


class XivCombat(PluginBase):
    name = "XivCombat"

    layout = str(Path(__file__).parent / 'layout.js')
    history_monitor: list[Monitor]
    monitor: Monitor | None
    enable_record = BindValue(default=False, auto_save=True)

    # interface
    if 1:
        def __init__(self):
            super().__init__()
            self._address = AddressManager(self.name, self.logger).load(sigs)
            api._func_action_data = action_data_interface(self._address['action_data_sig'])
            api._func_action_type_check = action_type_check_interface(self._address['action_type_check'])
            api._func_action_distance_check = action_distance_check_interface(self._address['action_distance_check'])
            api._func_action_recast_ms = action_recast_interface(self._address['action_recast_ms'])

            self.work = False
            self.work_lock = Lock()
            self.ability_cnt = 0
            self.err_count = 0
            self.history_monitor = []
            self.monitor = None
            self.monitor_lock = Lock()
            self.record_file = None
            self.record_lock = Lock()
            self.register_command()
            self.prev_job = None
            self.layout_set_lock = Lock()

            self.common_config = default_common_config | self.common_config
            self.storage.save()
            self.hot_bar_process_hook(self, self._address['hot_bar_process'])

            self.register_event('network/zone/server/combat_reset', lambda evt: self.new_monitor())

        def start(self):
            self.work = True
            self.logger.debug("start combat thread")
            while self.work:  # 独立线程版本
                try:
                    with self.work_lock:
                        sleep_time = self.process() if self.common_config['enable'] else self.common_config['period']
                except Exception:
                    self.logger.warning('error occurred while processing:\n', traceback.format_exc())
                    self.err_count += 1
                    if self.err_count > ERR_LIMIT:
                        self.logger.error('unregister process because of to many error occurred!')
                        self.work = False
                        break
                    sleep_time = self.common_config['period']
                else:
                    self.err_count = 0
                time.sleep(sleep_time)
            self.work = False

        def onunload(self):
            self.work = False
            if self.record_file is not None:
                self.record_file.close()
            self.controller.main_mission.join(timeout=2)
            self.controller.main_mission.terminate()

    # properties
    if 1:
        @property
        def common_config(self) -> dict:
            return self.storage.data.setdefault('common_config', default_common_config)

        @common_config.setter
        def common_config(self, value):
            self.storage.data['common_config'] = value
            self.layout_config_update()

        @property
        def strategy_config(self) -> dict:
            strategy = self.current_strategy
            if strategy is None: return {}
            job_data = self.storage.data.setdefault('strategy_config', {}).setdefault(utils.job_name(), {})
            job_data[strategy.name] = strategy.default_data | job_data.get(strategy.name, {})
            return job_data[strategy.name]

        @strategy_config.setter
        def strategy_config(self, value):
            strategy = self.current_strategy
            if strategy is not None:
                self.storage.data.setdefault(
                    'strategy_config', {}
                ).setdefault(
                    utils.job_name(), {}
                )[strategy.name] = value
                self.layout_config_update()

        @property
        def current_strategy(self) -> strategies.Strategy | None:
            job_name = utils.job_name()
            if job_name != self.prev_job:
                self.prev_job = job_name
                self.layout_config_update()
            strategy_name = self.storage.data.setdefault('strategy_pairing', {}).get(job_name)
            if strategy_name is None and job_name in all_strategies:
                strategy = next(iter(all_strategies[job_name].values()))
                self.current_strategy = strategy.name
                return strategy
            if strategy_name is not None:
                strategy = all_strategies.get(job_name, {}).get(strategy_name)
                if strategy is None:
                    del self.storage.data['strategy_pairing']
                    self.logger.warning("try to load an non-existing strategy %s" % strategy_name)
                return strategy

        @current_strategy.setter
        def current_strategy(self, value):
            job_name = utils.job_name()
            if isinstance(value, str):
                self.storage.data.setdefault('strategy_pairing', {})[job_name] = value
            elif isclass(value) and issubclass(value, strategies.Strategy):
                self.storage.data.setdefault('strategy_pairing', {})[job_name] = value.name
            else:
                raise TypeError("strategy must be a string or a subclass of strategies.Strategy")
            self.layout_config_update()

        def get_logic_data(self):
            data = logic_data.LogicData(self.common_config | self.strategy_config, self)
            data.ability_cnt = self.ability_cnt
            return data

        def new_monitor(self):
            # if self.monitor is not None: self.history_monitor.append(self.monitor)
            zone_id = api.get_zone_id()
            self.monitor = Monitor(zone_id)
            self.record(int(time.time() * 1000), 0, 'monitor', f"new_monitor|zone:{territory_type_names.get(zone_id)}({zone_id})")
            return self.monitor

        def get_monitor(self):
            if self.monitor is None:
                return self.new_monitor()
            return self.monitor

        def get_monitor_with_check(self, occur_time):
            m = self.get_monitor()
            if m.last_record and occur_time - m.last_record > split_time or m.zone_id != api.get_zone_id():
                m = self.new_monitor()
            return m

    # main processing function
    if 1:
        def get_to_use(self, data: logic_data.LogicData, strategy: strategies.Strategy):
            if data.gcd < 0.2: self.ability_cnt = 0
            process_non_gcd = data.gcd > 0.8 and self.ability_cnt < (data.gcd_total // 0.65) - 1 or data.gcd == 0
            if strategy is not None and (not strategy.fight_only or data.valid_enemies):
                to_use = strategy.common_ability(data)
                if to_use is not None:
                    return to_use
                if data.gcd < 0.2:
                    to_use = strategy.global_cool_down_ability(data)
                    if to_use is not None:
                        return to_use
                if process_non_gcd:
                    predict = strategy.global_cool_down_ability(data)
                    if predict and predict.ability_type == AbilityType.oGCD:
                        return predict
                    return strategy.non_global_cool_down_ability(data)

        def process(self) -> float:
            default_period = self.common_config.setdefault('period', 0.2)

            # 判断是否执行
            me = api.get_me_actor()
            if (me is None or not me.current_hp or  # 不存在角色、角色已经死亡
                    me.casting_time - me.casting_progress > 0.2  # 正在咏唱
            ):
                return default_period
            if not api.skill_queue_is_empty():
                return max(api.get_ani_lock(), default_period / 2)  # 队列中存在技能

            strategy = self.current_strategy
            if strategy is None:
                return default_period
            data = self.get_logic_data()
            if data.effects_set.intersection(status_cant_action):  # 存在不允许使用技能的状态
                return default_period
            # 获取决策行为
            to_use = self.get_to_use(data, strategy)
            if to_use is not None:
                if to_use.target_id is None:
                    target = data.target
                    to_use.target_id = data.me.id if target is None else target.id
                if api.get_current_target() is None and self.common_config.setdefault('auto_set_current_target', False):
                    api.set_current_target(to_use.actor)
                if isinstance(to_use, strategies.UseAbility):
                    if self.common_config.setdefault('debug', False):
                        new_data = self.get_logic_data()
                        self.logger.debug(f"{action_names[to_use.ability_id]}({to_use.ability_id})\t"
                                          f"{to_use.actor.name}({to_use.actor.id:x})\t"
                                          f"type:{api.action_type_check(to_use.ability_id, to_use.actor)}\t"
                                          f"ray:{data.target_action_check(to_use.ability_id, to_use.actor)}/{new_data.target_action_check(to_use.ability_id, to_use.actor)}\t"
                                          f"distance:{data.actor_distance_effective(to_use.actor)}/{new_data.actor_distance_effective(to_use.actor)}\t")
                    utils.use_ability(to_use)
                elif isinstance(to_use, strategies.UseItem):  # 使用道具，应该只有食物或者爆发药吧？
                    utils.use_item(to_use)
                elif isinstance(to_use, strategies.UseCommon):  # 通用技能——特指疾跑
                    api.reset_ani_lock()  # 因为有动画锁就会卡掉do_action，所以需要直接清除（请注意使用频率）
                    api.use_common(to_use.ability_id, to_use.target_id)
                else:
                    pass  # 理论上来说应该，或许，不会有其他类型的吧？或者策略返回的错误类型？有空加个raise？
                return max(0.4, default_period)
            return default_period

    @PluginHook.decorator(c_ubyte, [c_int64, POINTER(HotbarBlock)], True)
    def hot_bar_process_hook(self, hook, a1, block_p):
        try:
            strategy = self.current_strategy
            if strategy is not None and self.common_config['enable']:
                block = block_p[0]
                with self.work_lock:
                    t = api.get_current_target()
                    t_id = api.get_me_actor().id if t is None else t.id
                    if block.type == 1:
                        action_id = block.param
                        data = self.get_logic_data()
                        to_use = strategy.process_ability_use(data, block.param, t_id)
                        if to_use is not None:
                            if not isinstance(to_use, strategies.UseAbility):
                                to_use = strategies.UseAbility(*to_use)
                        else:
                            to_use = strategies.UseAbility(action_id, t_id)
                        if to_use.target_id is None:
                            target = data.target
                            to_use.target_id = data.me.id if target is None else target.id
                        self.ability_cnt += 1
                        use_ability(to_use)
                        return 1
                    elif block.type == 2 or block.type == 10:
                        api.reset_ani_lock()
                        return hook.original(a1, block_p)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.format_exc())
        return hook.original(a1, block_p)

    # command control
    if 1:
        @event("plugin_load:Command")
        def register_command(self, _):
            try:
                plugins.Command.register(self, command, self.process_cmd)
            except PluginNotFoundException:
                self.logger.warning("Command is not found")

        def process_cmd(self, args):
            try:
                cmd = self._process_cmd(args)
                if cmd is not None: self.logger.info(cmd)
            except Exception as e:
                self.logger.error(str(e))
                self.logger.error(traceback.format_exc())

        def _process_cmd(self, args):
            if len(args) == 0:
                return self.logger.info(self.common_config | self.strategy_config)
            match args[0]:
                case 'set':
                    match args[1]:
                        case 'pair':
                            self.current_strategy = args[2]
                        case 'common' | 'strategy' as t:
                            config = self.common_config if t == 'common' else self.strategy_config
                            old = config.get(args[2])
                            try:
                                new = eval(' '.join(args[3:]), {}, define.__dict__)
                            except:
                                new = ' '.join(args[3:])
                            config[args[2]] = new
                            self.layout_config_update()
                            return f"{old} => {new}"
                        case unk:
                            self.logger.error(f"unknown arg: {unk}")
                case unk:
                    self.logger.error(f"unknown arg: {unk}")

    # monitor events
    if 1:
        def record(self, occur_time_ms: int, source_id: int, source_name: str, str_evt: str):
            with self.record_lock:
                if self.record_file is None:
                    self.record_file = open(self.storage.path / f'record_{int(time.time())}.log', 'w+', encoding='utf-8')
                self.record_file.write(f"{occur_time_ms}|{source_id:x}|{source_name}|{str_evt}\n")
                self.record_file.flush()

        def process_monitor(self, occur_time, func, evt):
            getattr(self.get_monitor_with_check(occur_time), func)(occur_time, evt)

        @event('network/zone/server/actor_cast')
        def actor_cast_event(self, evt: 'ServerActorCastEvent'):
            if self.enable_record:
                self.record(int(evt.bundle_header.epoch), evt.source_id, evt.source_name, evt.str_event())

        @event('network/zone/server/map_effect')
        def map_effect_event(self, evt: 'ServerMapEffectEvent'):
            if self.enable_record:
                a_id = evt.message_header.actor_id
                name = getattr(api.get_actor_by_id(a_id), 'name', 'unknown')
                self.record(int(evt.bundle_header.epoch), a_id, name, evt.str_event())

        @event("network/zone/server/effect_add")
        def effect_add_event(self, evt: 'ActorAddEffectEvent'):
            if self.enable_record:
                self.record(int(evt.bundle_header.epoch), evt.actor_id, evt.actor_name, evt.str_event())

        @event("network/zone/server/effect_remove")
        def effect_remove_event(self, evt: 'ActorRemoveEffectEvent'):
            if self.enable_record:
                self.record(int(evt.bundle_header.epoch), evt.actor_id, evt.actor_name, evt.str_event())

        @event("network/zone/server/action_effect")
        def action_effect_event(self, evt: 'ActionEffectEvent'):
            with self.monitor_lock:
                self.process_monitor(evt.bundle_header.epoch / 1000, 'on_action', evt)
            if self.enable_record:
                self.record(int(evt.bundle_header.epoch), evt.source_id, getattr(evt.source_actor, 'name', 'unk'), evt.str_event())

        @event("network/zone/server/actor_control/dot")
        def actor_control_dot_event(self, evt: 'DotEvent'):
            with self.monitor_lock:
                self.process_monitor(evt.bundle_header.epoch / 1000, 'on_dot', evt)

        @event("network/zone/server/actor_control/hot")
        def actor_control_hot_event(self, evt: 'HotEvent'):
            with self.monitor_lock:
                self.process_monitor(evt.bundle_header.epoch / 1000, 'on_hot', evt)

        @event("network/zone/server/actor_control/death")
        def actor_control_death_event(self, evt: 'DeathEvent'):
            with self.monitor_lock:
                self.get_monitor().on_death(evt.bundle_header.epoch / 1000, evt)

        def dps(self, actor_id: int):
            return self.get_monitor().dps(actor_id)

        def dpsm(self, actor_id: int):
            return self.get_monitor().dpsm(actor_id)

        def hps(self, actor_id: int):
            return self.get_monitor().hps(actor_id)

        def hpsm(self, actor_id: int):
            return self.get_monitor().hpsm(actor_id)

        def dtps(self, actor_id: int):
            return self.get_monitor().dtps(actor_id)

        def dtpsm(self, actor_id: int):
            return self.get_monitor().dtpsm(actor_id)

        def ttk(self, actor_id: int):
            dtpsm = self.dtpsm(actor_id)
            if dtpsm == 0: return -1
            return getattr(api.get_actor_by_id(actor_id), 'current_hp', 0) / dtpsm

    # layout
    if 1:
        @lru_cache(1)
        def _layout_team_dps(self, last_time: float):
            members = [member for member in api.get_party_list()]
            if not members:
                me = api.get_me_actor()
                if not me: return {'zone': 0, 'members': []}
                members = [me]
            m = self.get_monitor()
            return {
                'period': int(m.last_record - m.first_record),
                'zone': m.zone_id,
                'members': [{'name': actor.name, 'dps': int(m.dps(actor.id)), 'dpsm': int(m.dpsm(actor.id)), 'job': actor.job.value} for actor in
                            members]
            }

        def layout_team_dps(self):
            return self._layout_team_dps(self.get_monitor().last_record)

        def layout_enemies_ttk(self):
            return [{
                'name': enemy.name,
                'ttk': int(self.ttk(enemy.id))
            } for enemy in api.get_enemies_list()]

        def layout_new_monitor(self):
            return bool(self.new_monitor())

        def layout_config_update(self):
            job = utils.job_name()
            self.client_event('config_update', {
                'job': job,
                'current_strategy': getattr(self.current_strategy, 'name', None),
                'strategies': [strategy for strategy in all_strategies.get(job, {}).keys()],
                'common_config': self.common_config,
                'strategy_config': self.strategy_config,
            })
            return True

        def layout_set(self, set_type: int, set_key: str, set_value: str):
            with self.layout_set_lock:
                match set_type:
                    case 1:
                        self.current_strategy = set_value
                    case 2 | 3 as t:
                        config = self.common_config if t == 2 else self.strategy_config
                        try:
                            new = eval(set_value, {}, define.__dict__)
                        except:
                            new = set_value
                        config[set_key] = new
                        self.layout_config_update()
                    case _:
                        raise ValueError(f'unknown set_type {set_type}')
