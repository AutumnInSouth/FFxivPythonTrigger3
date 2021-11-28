from ctypes import *
from FFxivPythonTrigger.saint_coinach import action_sheet

is_quest_finished_interface = CFUNCTYPE(c_ubyte, c_int64, c_uint, c_ubyte)

action_unlock_quest = {row.key: row['UnlockLink'].key
                       for row in action_sheet
                       if row['UnlockLink'] and 0x20000 > row['UnlockLink'].key > 0x10000}


class IsQuestFinished:
    def __init__(self, func_address, quest_manager):
        self.original = is_quest_finished_interface(func_address)
        self.quest_manager = quest_manager

    def __call__(self, quest_id: int) -> int:
        return self.original(self.quest_manager, quest_id, 1)

    def is_action_unlocked(self, action_id: int) -> int:
        require_quest = action_unlock_quest.get(action_id)
        if require_quest: return self(require_quest)
        return 1
