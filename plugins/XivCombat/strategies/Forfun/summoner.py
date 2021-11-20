from .. import *
from .samurai_meta import *


class SummonerLogic(Strategy):
    name = "summoner_logic"
    fight_only = False
    job = 'Summoner'
    default_data = {}
    gcd = 0

    def global_cool_down_ability(self, data: 'LogicData'):
        pass

    def non_global_cool_down_ability(self, data: 'LogicData'):
        pass
