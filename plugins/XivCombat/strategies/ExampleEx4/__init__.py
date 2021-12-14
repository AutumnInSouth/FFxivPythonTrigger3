from FFxivPythonTrigger import game_ext

if game_ext == 4:
    from .bard import BardLogic
    from .dark_knight import DarkKnightStrategy
    from .gun_breaker import GunBreakerStrategy
