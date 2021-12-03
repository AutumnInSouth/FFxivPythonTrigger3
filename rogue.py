from ..base import ActionBase, StatusBase, physic, magic


class Actions:

        class 4TonzeWeight(ActionBase):
            """
            Drops a 4-tonze weight dealing physical damage at a designated location with a potency of 200 for the first enemy, and 50% less for all remaining enemies. Additional Effect: Heavy +40% Duration: 30s
            """
            id = 11384
            name = {"4-tonze Weight", "4星吨"}
    
        class WaterCannon(ActionBase):
            """
            Deals water damage with a potency of 200.
            """
            id = 11385
            name = {"Water Cannon", "水炮"}
    