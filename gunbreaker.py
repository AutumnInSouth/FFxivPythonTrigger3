from ..base import ActionBase, StatusBase, physic, magic


class Actions:

        class GlassDance(ActionBase):
            """
            Deals ice damage to all enemies in a wide arc to your fore and flanks with a potency of 350 for the first enemy, and 50% less for all remaining enemies. Shares a recast timer with certain blue magic spells.
            """
            id = 11430
            name = {"Glass Dance", "冰雪乱舞"}
    