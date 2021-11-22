import time
import traceback
from ctypes import *
from pathlib import Path
from importlib import import_module
from inspect import isclass
from threading import Lock

from FFxivPythonTrigger import PluginBase, AddressManager, plugins, PluginNotFoundException
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import action_names
from FFxivPythonTrigger.text_pattern import find_unique_signature_point, find_unique_signature_address

from . import define, strategies, api, logic_data, utils
from .define import AbilityType
from .utils import is_area_action, use_ability

command = "@acombat"

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
        'call': find_unique_signature_address,
        'param': "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F B6 82 ? ? ? ?",
        'add': BASE_ADDR,
    },
    "action_type_check": {
        'call': find_unique_signature_address,
        'param': "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B 2D ? ? ? ? 49 8B D8",
        'add': BASE_ADDR,
    },
    "action_distance_check": {
        'call': find_unique_signature_address,
        'param': "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 89 4C 24 ?",
        'add': BASE_ADDR,
    },
    "action_data_sig": {
        'call': find_unique_signature_point,
        'param': "E8 * * * * 48 8B F0 48 85 C0 0F 84 ? ? ? ? BA ? ? ? ? 48 8B CB E8 ? ? ? ? 48 8B 0D ? ? ? ?",
        'add': BASE_ADDR,
    },
}
action_type_check_interface = CFUNCTYPE(c_bool, c_int64, c_int64, c_uint64)
action_distance_check_interface = CFUNCTYPE(c_int64, c_uint, c_int64, c_int64)
action_data_interface = CFUNCTYPE(c_int64, c_int64)
all_strategies = {}

for file in (Path(__file__).parent / 'strategies').iterdir():
    if file.is_dir() and (file / '__init__.py').exists() or file.is_file() and file.suffix == '.py':
        module = import_module(f'{__package__}.strategies.{file.stem}')
        for obj in module.__dict__.values():
            if isclass(obj) and issubclass(obj, strategies.Strategy) and obj != strategies.Strategy:
                all_strategies.setdefault(obj.job, {})[obj.name] = obj()


class HotbarBlock(OffsetStruct({
    'type': (c_ubyte, 199),
    'param': (c_uint, 184),
})):
    type: int
    param: int


class XivCombat(PluginBase):
    name = "XivCombat"

    # layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        self._address = AddressManager(self.name, self.logger).load(sigs)
        api._func_action_data = action_data_interface(self._address['action_data_sig'])
        api._func_action_type_check = action_type_check_interface(self._address['action_type_check'])
        api._func_action_distance_check = action_distance_check_interface(self._address['action_distance_check'])
        self.hot_bar_process_hook(self, self._address['hot_bar_process'])

        self.common_config = default_common_config | self.common_config
        self.storage.save()
        self.work = False
        self.work_lock = Lock()
        self.ability_cnt = 0
        self.err_count = 0

        self.register_command()

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
        self.controller.main_mission.join(timeout=2)

    @property
    def common_config(self) -> dict:
        return self.storage.data.setdefault('common_config', default_common_config)

    @common_config.setter
    def common_config(self, value):
        self.storage.data['common_config'] = value

    @property
    def strategy_config(self) -> dict:
        strategy = self.current_strategy
        if strategy is None: return {}
        return self.storage.data.setdefault(
            'strategy_config', {}
        ).setdefault(
            utils.job_name(), {}
        ).setdefault(
            strategy.name, strategy.default_data
        )

    @strategy_config.setter
    def strategy_config(self, value):
        strategy = self.current_strategy
        if strategy is not None:
            self.storage.data.setdefault(
                'strategy_config', {}
            ).setdefault(
                utils.job_name(), {}
            )[strategy.name] = value

    @property
    def current_strategy(self) -> strategies.Strategy | None:
        job_name = utils.job_name()
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
                        if to_use is not None: action_id, t_id = to_use
                        self.ability_cnt += 1
                        use_ability(strategies.UseAbility(action_id, t_id))
                        return 1
                    elif block.type == 2 or block.type == 10:
                        api.reset_ani_lock()
                        return hook.original(a1, block_p)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.format_exc())
        return hook.original(a1, block_p)

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
                    self.logger.debug(f"use {action_names[to_use.ability_id]}({to_use.ability_id}) on "
                                      f"{to_use.actor.name}({to_use.actor.id:x})")
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

    def get_logic_data(self):
        data = logic_data.LogicData(self.common_config | self.strategy_config)
        data.ability_cnt = self.ability_cnt
        return data

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
                        return f"{old} => {new}"
                    case unk:
                        self.logger.error(f"unknown arg: {unk}")
            case unk:
                self.logger.error(f"unknown arg: {unk}")
