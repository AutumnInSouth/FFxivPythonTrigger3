from enum import Enum

# 目标选择范围
ONLY_SELECTED = 0  # 仅当前选择目标
ENEMY_LIST = 1  # 敌人列表（上限8）
ALL_IN_COMBAT = 2  # 所有在战斗中的敌人
ALL_CAN_ATTACK = 3  # 所有可攻击的敌人

# 选取敌人目标优先级
CURRENT_SELECTED = 0  # 当前选择目标
FOCUSED = 1  # 焦点目标
DISTANCE_NEAREST = 2  # 最近的敌人
DISTANCE_FURTHEST = 3  # 最远的敌人
HP_HIGHEST = 4  # HP最高的敌人
HP_LOWEST = 5  # HP最低的敌人
HPP_HIGHEST = 6  # HP百分比最高的敌人
HPP_LOWEST = 7  # HP百分比最低的敌人

# 资源策略
RESOURCE_STINGY = -1  # 节省资源，存资源
RESOURCE_AUTO = 0  # 根据目标预计击杀时间使用
RESOURCE_NORMAL = 1  # 正常使用资源
RESOURCE_SQUAND = 2  # 资源爆发

# 单体判断
FORCE_MULTI = -1  # 强制群体
SINGLE_AUTO = 0  # 自动判断，基于目标选择范围
FORCE_SINGLE = 1  # 强制单体

# 物品使用策略
HQ_ONLY = 1  # 只使用HQ
NQ_ONLY = 2  # 只使用NQ
HQ_FIRST = 3  # 先使用HQ
NQ_FIRST = 4  # 先使用NQ

# 移动，咏唱状态
ALWAYS_MOVING = -1  # 始终移动
ALWAYS_CASTING = 1  # 始终咏唱
CAST_MOVE_AUTO = 0  # 自动判断


class AbilityType(Enum):
    GCD = 1
    oGCD = 2
