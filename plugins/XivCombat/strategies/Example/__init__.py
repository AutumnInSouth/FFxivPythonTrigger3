from FFxivPythonTrigger import game_ext

if game_ext == 3:
    from .machinist import MachinistLogic
    from .red_mage import RDMLogic
    from .warrior import WarriorLogic
    from .gunbreaker import GunbreakerLogic
    from .dragoon import DragoonLogic
    from .monk import MonkLogic
    from .astrologian import AstrologianLogic
    from .blm_pvp import BlmPvpLogic, blm_pvp_effect_remove, blm_pvp_record_thunder
    from .nin_pvp import NinPvpLogic
    from .gnb_pvp import GnbPvpLogic
    from .paladin import PaladinLogic
    from .triggers import last_use_record
