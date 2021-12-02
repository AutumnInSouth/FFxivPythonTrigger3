from FFxivPythonTrigger import game_language

if game_language == 'chs':
    from .machinist import MachinistLogic
    from .red_mage import RDMLogic
    from .warrior import WarriorLogic
    from .gunbreaker import GunbreakerLogic
    from .dragoon import DragoonLogic
    from .monk import MonkLogic
    from .astrologian import AstrologianLogic
