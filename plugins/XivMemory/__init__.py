from ctypes import *

from FFxivPythonTrigger import PluginBase
from FFxivPythonTrigger.address_manager import AddressManager
from FFxivPythonTrigger.memory import read_memory, read_uint, read_float, write_float, read_ushort
from FFxivPythonTrigger.memory.struct_factory import PointerStruct

from .sigs import sigs, enemies_shifts
from .struct.actor import ActorTable
from .struct.combat import ComboState, SkillQueue, CoolDownGroups, Enemies
from .struct.job_gauge import gauges
from .struct.player_info import Player
from .struct.others import Target, Movement
from .struct.inventory import InventoryPageIdx
from .struct.party import PartyList


class XivMemory(PluginBase):
    name = "XivMemory"
    actor_table: ActorTable
    combo_state: ComboState
    skill_queue: SkillQueue
    cool_down_group: CoolDownGroups
    player_info: Player
    target: Target
    movement: Movement
    inventory: InventoryPageIdx
    party: PartyList
    world_id: int

    @property
    def zone_id(self) -> int:
        return read_uint(self._address["zone"])

    @property
    def enemies(self) -> Enemies:
        return self._enemies.value

    @property
    def gauge(self):
        job = self.player_info.job.value()
        if job in self._gauges:
            return self._gauges[job]

    @property
    def skill_animation_lock(self) -> float:
        return read_float(self._address["skill_animation_lock"])

    @skill_animation_lock.setter
    def skill_animation_lock(self, value):
        write_float(self._address["skill_animation_lock"], float(value))

    def __init__(self):
        super().__init__()

        self._address = AddressManager(self.name, self.logger).load(sigs)
        self.actor_table = read_memory(ActorTable, self._address['actor_table'])
        self.combo_state = read_memory(ComboState, self._address['combo_state'])
        self.skill_queue = read_memory(SkillQueue, self._address['skill_queue'])
        self.cool_down_group = read_memory(CoolDownGroups, self._address['cool_down_group'])
        self._enemies = read_memory(PointerStruct(Enemies, *enemies_shifts), self._address["enemies_base"])
        self._gauges = {k: read_memory(v, self._address['gauge']) for k, v in gauges.items()}
        self.player_info = read_memory(Player, self._address['player_info'])
        self.target = read_memory(Target, self._address['targets'])
        self.movement = read_memory(Movement, self._address['movement'])
        self.inventory = read_memory(InventoryPageIdx, self._address['inventory'])
        self.party = read_memory(PartyList, self._address['party'])
        self.world_id = 0
        
        class WorldIdHook(self.PluginHook):
            argtypes = [c_int64, c_int64]
            restype = c_int64

            def hook_function(_self, a1, a2):
                self.world_id = read_ushort(a2 + 4)
                return _self.original(a1, a2)

        self.world_id_hook = WorldIdHook(self._address["world_id_hook"],True)
