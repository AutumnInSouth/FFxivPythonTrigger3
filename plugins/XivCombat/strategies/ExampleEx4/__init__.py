from FFxivPythonTrigger import game_ext

if game_ext == 4:
    from .bard import BardLogic
    from .dark_knight import DarkKnightStrategy
    from .gun_breaker import GunBreakerStrategy
    from .machinist import MachinistLogic
    from .red_mage import RDMLogic
    from .dancer import DncLogic
    from .summoner import SmnLogic
    from .sch import SchLogic
