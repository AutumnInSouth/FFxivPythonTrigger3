from . import astrologian, bard, black_mage, blue_mage, dancer, dark_knight
from . import dragoon, gunbreaker, machinist, monk, ninja, paladin, red_mage
from . import samurai, scholar, summoner, warrior, white_mage, reaper, sage
from ..base import ActionBase, StatusBase


class Action(
    astrologian.Actions,
    bard.Actions,
    black_mage.Actions,
    blue_mage.Actions,
    dancer.Actions,
    dark_knight.Actions,
    dragoon.Actions,
    gunbreaker.Actions,
    machinist.Actions,
    monk.Actions,
    ninja.Actions,
    paladin.Actions,
    red_mage.Actions,
    samurai.Actions,
    scholar.Actions,
    summoner.Actions,
    warrior.Actions,
    white_mage.Actions,
    reaper.Actions,
    sage.Actions,
): pass


class Status(
    ##astrologian.Status,
    bard.Status,
    # black_mage.Status,
    # blue_mage.Status,
    # dancer.Status,
    dark_knight.Status,
    # dragoon.Status,
    # gunbreaker.Status,
    # machinist.Status,
    # monk.Status,
    # ninja.Status,
    paladin.Status,
    # red_mage.Status,
    # samurai.Status,
    # scholar.Status,
    # summoner.Status,
    # warrior.Status,
    # white_mage.Status,
    # reaper.Status,
    # sage.Status,
):pass



actions: dict[str, ActionBase] = {}

for k, v in Action.__dict__.items():
    if isinstance(v, ActionBase):
        for name in v.name:
            actions[name] = v
for action in actions.values():
    if isinstance(action.combo_action, str):
        action.combo_action = getattr(Action, action.combo_action).id

status: dict[str, StatusBase] = {}
for k, v in Status.__dict__.items():
    if isinstance(v, StatusBase):
        for name in v.name:
            status[name] = v
