from functools import cache
from pathlib import Path
from importlib import import_module
from inspect import isclass
from threading import Lock

from FFxivPythonTrigger import PluginBase, plugins
from FFxivPythonTrigger.decorator import BindValue
from FFxivPythonTrigger.saint_coinach import action_sheet

from . import define, strategies, api,logic_data

default_common_config = {
    'enabled': False,
    'debug': False,
    'targets': define.ENEMY_LIST,
    'target_priority': [define.CURRENT_SELECTED, define.FOCUSED, define.DISTANCE_NEAREST],
    'load_targets_distance': 50,
    'resource': define.RESOURCE_AUTO,
    'single': define.SINGLE_AUTO,
    'use_builtin_effective_distance': False,
    'cast_move': define.CAST_MOVE_AUTO,
}
DEFAULT_PERIOD = 0.1
all_job_strategies = {}

for file in Path(__file__).parent.glob('strategies/*.py'):
    if file.name != '__init__.py':
        module = import_module(f'{__package__}.strategies.{file.stem}')
        for obj in module.__dict__.values():
            if isclass(obj) and issubclass(obj, strategies.Strategy) and obj != strategies.Strategy:
                all_job_strategies.setdefault(obj.job, {})[obj.name] = obj


def use_item(to_use: strategies.UseItem):
    api.reset_ani_lock()  # 因为有动画锁就会卡掉do_action，所以需要直接清除（请注意使用频率）
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
        actor = api.get_actor_by_id(to_use.target_id) if to_use.target_id != 0xe0000000 else api.get_me_actor()
        if actor is not None:
            api.use_area_action(to_use.ability_id, actor.pos.x, actor.pos.y, actor.pos.z, actor.id)
    else:
        api.use_action(to_use.ability_id, to_use.target_id)


class XivCombat(PluginBase):
    name = "XivCombat"
    layout = str(Path(__file__).parent / 'layout.js')

    common_config = BindValue(default=default_common_config)
    job_pairing = BindValue(default={})
    strategy_config = BindValue(default={})

    def __init__(self):
        super().__init__()

        self.current_job = None
        self.common_config = default_common_config | self.common_config
        self.storage.save()
        self.work = False
        self.work_lock = Lock()

    def onunload(self):
        self.work = False
        self.controller.main_mission.join(timeout=2)

    def get_to_use(self,data:logic_data.LogicData):
        pass


    def process(self) -> float:
        # 判断是否执行
        data = logic_data.LogicData(self.common_config|self.strategy_config)
        if data.me is None or not data.me.currentHP: return 0.5  # 不存在角色、角色已经死亡
        if data.me.CastingTime - data.me.CastingProgress > 0.2: return DEFAULT_PERIOD  # 正在咏唱
        if not api.skill_queue_is_empty(): return max(api.get_ani_lock(), DEFAULT_PERIOD)  # 队列中存在技能

        # 获取决策行为
        to_use = None
        if data.gcd < 0.2: self.config.ability_cnt = 0
        process_non_gcd = data.gcd > 0.9 and self.config.ability_cnt < int(data.gcd_total) or data.gcd == 0
        # self.logger(data.job)
        strategy = self.config.get_strategy(data.job)
        if strategy is not None and (not strategy.fight_only or data.valid_enemies):
            self.is_working = True
            to_use = strategy.common(data)
            if to_use is None:
                if data.gcd < 0.2:
                    to_use = strategy.global_cool_down_ability(data)
                if to_use is None and process_non_gcd:
                    to_use = strategy.non_global_cool_down_ability(data)
                    if to_use is not None: self.config.ability_cnt += 1
        else:
            self.is_working = False
        if to_use is None:
            if data.gcd < 0.2:
                to_use = self.config.get_query_skill()
            if to_use is None:
                if process_non_gcd:
                    to_use = self.config.get_query_ability()
                    if to_use is not None: self.config.ability_cnt += 1
                if to_use is None:
                    if self.config.auto_gcd is not None and not data.gcd and data.valid_enemies:
                        to_use = Strategy.UseAbility(self.config.auto_gcd)
                    else:
                        return DEFAULT_PERIOD

        # 处理决策行为
        if self.config.enable:
            if to_use.target_id is None:
                target = data.target
                to_use.target_id = data.me.id if target is None else target.id
            if Api.get_current_target() is None and data.config.custom_settings.setdefault('auto_set_current_target', 'true') == 'true':
                Api.set_current_target(Api.get_actor_by_id(to_use.target_id))
            if isinstance(to_use, Strategy.UseAbility) and Api.skill_queue_is_empty():
                if data.config.custom_settings.setdefault('debug_output', 'false') == 'true':
                    actor = Api.get_actor_by_id(to_use.target_id)
                    self.logger.debug(f"use:{action_sheet[to_use.ability_id]['Name']}({to_use.ability_id}) on {actor.Name}({hex(actor.id)[2:]})"
                                      f" check: {data.target_action_check(to_use.ability_id, actor)}")
                use_ability(to_use)
            elif isinstance(to_use, Strategy.UseItem):  # 使用道具，应该只有食物或者爆发药吧？
                use_item(to_use)
            elif isinstance(to_use, Strategy.UseCommon):  # 通用技能——特指疾跑
                Api.reset_ani_lock()  # 因为有动画锁就会卡掉do_action，所以需要直接清除（请注意使用频率）
                Api.use_common(to_use.ability_id, to_use.target_id)
            else:
                pass  # 理论上来说应该，或许，不会有其他类型的吧？或者策略返回的错误类型？有空加个raise？

        return DEFAULT_PERIOD
