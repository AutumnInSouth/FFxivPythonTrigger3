from ..base import ActionBase, StatusBase, physic, magic


class Actions:

        class Gobskin(ActionBase):
            """
            Creates a barrier around self and all nearby party members that absorbs damage equivalent to a heal of 100 potency. Duration: 30s Barrier strength is increased to absorb damage equivalent to a heal of 250 potency when you are under the effect of Aetherial Mimicry: Healer. Effect cannot be stacked with those of scholar's Galvanize or sage's Eukrasian Diagnosis and Eukrasian Prognosis.
        2114, Gobskin, Gobskin, Hardened flesh is absorbing damage.
            """
            id = 18304
            name = {"Gobskin", "哥布防御"}
    