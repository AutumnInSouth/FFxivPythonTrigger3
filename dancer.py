from ..base import ActionBase, StatusBase, physic, magic


class Actions:

        class VeilOfTheWhorl(ActionBase):
            """
            Counters enemies with water damage every time you suffer damage. Counter Potency: 50 Duration: 30s Shares a recast timer with certain blue magic spells.
        478, Veil of the Whorl, Veil of the Whorl, Reflecting damage dealt by ranged attacks.
        1724, Veil of the Whorl, Veil of the Whorl, Dealing water damage to attackers upon taking damage.
            """
            id = 11431
            name = {"Veil of the Whorl", "水神的面纱"}
    