from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from XivMemory import XivMemory
    from XivNetwork import XivNetwork, ExtraNetworkMessage
    from Command import CommandPlugin
    from HttpApi import HttpApiPlugin
    from Linkross import Linkross
    from OmenReflect import OmenReflect, ExtraOmens
    from Pmb import Pmb
    from Teleporter import Teleporter
    from WanaHome import WanaHome
    from XivCombat import XivCombat
    from XivCombo import XivCombo
    from XivHacks import XivHacks
    from Move import Move
    from Gui import Gui


class Plugins:
    XivMemory: 'XivMemory'
    XivNetwork: 'XivNetwork'
    ExtraNetworkMessage: 'ExtraNetworkMessage'
    Command: 'CommandPlugin'
    HttpApi: 'HttpApiPlugin'
    Linkross: 'Linkross'
    OmenReflect: 'OmenReflect'
    ExtraOmens: 'ExtraOmens'
    Pmb: 'Pmb'
    Teleporter: 'Teleporter'
    WanaHome: 'WanaHome'
    XivCombat: 'XivCombat'
    XivCombo: 'XivCombo'
    XivHacks: 'XivHacks'
    Move: 'Move'
    Gui: 'Gui'


plugins: Plugins
