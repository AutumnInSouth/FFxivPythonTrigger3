# TODO: for each spell from level 1-60, and level 70, there is a possible situation that,
#  even though the player has reached the required level, but the player failed to learn the spell,
#  better check if a spell in player's spell set rather than only check level
class ComboBase(object):
    action_id = 0  # the action id this combo bind (each action can only bind one combo)
    combo_id = ""  # a unique key to identify combo
    title = ""  # the title shown on layout
    desc = ""  # the desc shown on layout (non used)

    @staticmethod
    def combo(me):
        """
        a staticmethod, return what action would return
        Args:
            me: an actor object get from XivMemory to own actor

        Returns:
            the action id to return
        """
        return 0


def combo_func(c_action_id, c_combo_id, c_title, c_desc=''):
    """
    decorator to make a combo
    """

    def decorator(func):
        class Combo(ComboBase):
            action_id = c_action_id
            combo_id = c_combo_id
            title = c_title
            desc = c_desc

            @staticmethod
            def combo(me):
                return func(me)

        return Combo

    return decorator
