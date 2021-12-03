from ..base import ActionBase, StatusBase, physic, magic


class Actions:

        class Bristle(ActionBase):
            """
            Increases the potency of the next spell cast by 50%. Duration: 30s Effect cannot be stacked with Harmonized.
            """
            id = 11393
            name = {"Bristle", "怒发冲冠"}
    