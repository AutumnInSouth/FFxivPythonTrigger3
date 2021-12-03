from inspect import isclass
from typing import Type

from FFxivPythonTrigger import game_ext

from .base import ActionBase, StatusBase

if game_ext == 4:
    from .ex4 import *
else:
    from .ex3 import *

actions: dict[str, Type[ActionBase]] = {}

for k in dir(Action):
    v = getattr(Action, k)
    if isclass(v) and issubclass(v, ActionBase):
        for name in v.name:
            actions[name] = v
for action in actions.values():
    if isinstance(action.combo_action, str):
        action.combo_action = getattr(Action, action.combo_action).id
    elif isclass(action.combo_action) and issubclass(action.combo_action, ActionBase):
        action.combo_action = action.combo_action.id

status: dict[str, Type[StatusBase]] = {}
for k in dir(Status):
    v = getattr(Status, k)
    if isclass(v) and issubclass(v, StatusBase):
        for name in v.name:
            status[name] = v
