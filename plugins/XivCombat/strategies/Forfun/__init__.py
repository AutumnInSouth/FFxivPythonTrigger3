from FFxivPythonTrigger import game_ext

if game_ext == 3:
    from .samurai import SamuraiLogic
    from .summoner import SummonerLogic
