from ..base import ActionBase, StatusBase, physic, magic


class Actions:

        class AcornBomb(ActionBase):
            """
            Puts target and all enemies nearby it to sleep. Duration: 30s Cancels auto-attack upon execution.
            """
            id = 11392
            name = {"Acorn Bomb", "橡果炸弹"}
    