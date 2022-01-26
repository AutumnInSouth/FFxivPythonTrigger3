import json
from ctypes import *

from FFxivPythonTrigger import PluginBase, plugins
from FFxivPythonTrigger.address_manager import AddressManager
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.exceptions import NeedRequirementError, PluginNotFoundException
from FFxivPythonTrigger.memory import read_memory, read_uint, read_float, write_float
from FFxivPythonTrigger.memory.struct_factory import PointerStruct, OffsetStruct

from .sigs import sigs, enemies_shifts, mission_info_shifts
from .struct.actor import ActorTable, Actor
from .struct.combat import ComboState, SkillQueue, CoolDownGroups, Enemies, MissionInfo, PvpAction
from .struct.inventory import InventoryPagePtr, InventoryPage
from .struct.job_gauge import gauges
from .struct.markings import Markings
from .struct.others import Target, Movement
from .struct.party import PartyList
from .struct.player_info import Player
from .struct.coordinate import Coordinate
from .struct.buddy import Buddy
from .struct.fate import FateManager
from .hook import ValueBindHook
from .hook.mo_ui_entity import MoUiEntityHook
from .hook.chat_log import ChatLogHook, PrintChatLogHook
from .calls.do_action import DoAction, DoActionLocation
from .calls.do_text_command import DoTextCommand
from .calls.head_mark import HeadMark
from .calls.way_mark import WayMark
from .calls.is_quest_finished import IsQuestFinished
from .calls.screen_to_world import ScreenToWorld
from .utils import Utils

try:
    from aiohttp import web
except ModuleNotFoundError:
    raise NeedRequirementError('aiohttp')


class XivMemory(PluginBase):
    name = "XivMemory"
    actor_table: ActorTable
    combo_state: ComboState
    skill_queue: SkillQueue
    cool_down_group: CoolDownGroups
    player_info: Player
    targets: Target
    movement: Movement
    inventory: InventoryPagePtr
    party: PartyList
    pvp_action: PvpAction
    world_id: int
    markings: Markings
    buddy: Buddy

    def __init__(self):
        super().__init__()

        self._address = AddressManager(self.name, self.logger).load(sigs)
        self.actor_table = read_memory(ActorTable, self._address['actor_table'])
        self.actor_table._aid_to_idx_cache = {}
        self.combo_state = read_memory(ComboState, self._address['combo_state'])
        self.skill_queue = read_memory(SkillQueue, self._address['skill_queue'])
        self.cool_down_group = read_memory(CoolDownGroups, self._address['cool_down_group'])
        self._enemies = read_memory(PointerStruct(Enemies, *enemies_shifts), self._address["enemies_base"])
        self._gauges = {k: read_memory(v, self._address['gauge']) for k, v in gauges.items()}
        self.player_info = read_memory(Player, self._address['player_info'])
        self.targets = read_memory(Target, self._address['targets'])
        self.movement = read_memory(Movement, self._address['movement'])
        self.inventory = read_memory(InventoryPagePtr, self._address['inventory'])
        self.party = read_memory(PartyList, self._address['party'])
        self._mission_info = read_memory(POINTER(MissionInfo), self._address['mission_info'])
        self.pvp_action = read_memory(PvpAction, self._address['pvp_action'])
        self.markings = read_memory(Markings, self._address['markings'])
        self.buddy = read_memory(Buddy, self._address['buddy_list'])
        self._fate = read_memory(POINTER(FateManager), self._address['fate_manager'])
        self.coordinate = Coordinate(self._address)
        self.value_bind_hooks = {
            # 'world_id': WorldIdHook(self, self._address["world_id_hook"]),
            'mo_ui_entity': MoUiEntityHook(self, self._address["mo_ui_entity_hook"]),
        }
        self.hooks = {
            # 'chat_log': ChatLogHook(self, self._address["chat_log_hook"]),
            'print_chat_log': PrintChatLogHook(self, self._address["print_chat_log_hook"]),
        }
        self.calls = type('memory_call', (object,), {
            'do_action': DoAction(self._address['do_action'], self._address['action_manager']),
            'do_action_location': DoActionLocation(self._address['do_action_location'],
                                                   self._address['action_manager']),
            'do_text_command': DoTextCommand(self._address['do_text_command'], self._address['text_command_ui_module']),
            'head_mark': HeadMark(self._address['head_mark'], self._address['marking_controller']),
            'way_mark': WayMark(self._address['way_mark_set'], self._address['way_mark_clear'],
                                self._address['way_mark_clear_all'],
                                self._address['marking_controller'], self._address['action_manager']),
            'is_quest_finished': IsQuestFinished(self._address['is_quest_finished'], self._address['quest_manager']),
            'screen_to_world': ScreenToWorld(self._address['screen_to_world'], self._address['get_camera_matrix']),
        })
        self.utils = Utils(self)
        self.register_http_api_route()

    @property
    def mission_info(self) -> MissionInfo:
        return self._mission_info[0] if self._mission_info else None

    @property
    def zone_id(self) -> int:
        return read_uint(self._address["zone"])

    @property
    def map_id(self) -> int:
        return read_uint(self._address["map"]) or read_uint(self._address["zone"] + 0x18)

    @property
    def enemies(self) -> Enemies:
        return self._enemies.value

    @property
    def fate(self) -> FateManager:
        return self._fate[0] if self._fate else None

    @property
    def gauge(self):
        return self._gauges.get(self.player_info.job.value)

    @property
    def skill_animation_lock(self) -> float:
        return read_float(self._address["skill_animation_lock"])

    @skill_animation_lock.setter
    def skill_animation_lock(self, value):
        write_float(self._address["skill_animation_lock"], float(value))

    # http-api handlers start

    @event("plugin_load:HttpApi")
    def register_http_api_route(self, _):
        try:
            plugins.HttpApi.register_post_route(self, 'command', self.text_command_handler)
            plugins.HttpApi.register_post_route(self, 'useitem', self.use_item_handler)
            plugins.HttpApi.register_post_route(self, 'mark', self.head_mark_handler)
        except PluginNotFoundException:
            self.logger.warning("HttpApi is not found")

    async def text_command_handler(self, request: web.Request):
        cmd = await request.text()
        self.do_text_command(cmd)
        self.logger.debug("text_command_handler", cmd)
        return web.json_response({'msg': 'success'})

    async def use_item_handler(self, request: web.Request):
        try:
            item_id = int(await request.text())
        except ValueError:
            return web.json_response({'msg': 'Value Error'})
        paths = request.path.strip('/').split('/')
        if len(paths) > 1 and paths[1] == 'hq':
            item_id += 1000000
        self.logger.debug("use_item_handler", item_id)
        self.do_action.use_item(item_id)
        return web.json_response({'msg': 'success'})

    async def head_mark_handler(self, request: web.Request):
        try:
            data = json.loads(await request.text())
        except json.JSONDecodeError:
            return web.json_response({'msg': 'failed', 'rtn': 'json error'})
        if not isinstance(data, dict):
            return web.json_response({'msg': 'failed', 'rtn': 'data should be dictionary'})

        if "Name" in data:
            target = list(plugins.XivMemory.actor_table.get_actors_by_name(data["Name"]))
            if not target:
                return web.json_response({'msg': 'failed', 'rtn': 'actor not found'})
            target = target[0].id
        elif "ActorId" in data:
            target = int(data["ActorId"])
        else:
            return web.json_response({'msg': 'failed', 'rtn': 'no target'})

        try:
            self.head_mark(data["MarkType"], target)
        except KeyError:
            return web.json_response({'msg': 'failed', 'rtn': 'Invalid MarkType'})
        else:
            return web.json_response({'msg': 'success'})

    # http-api handlers end

    def __getattr__(self, item):
        if item in self.value_bind_hooks:
            return self.value_bind_hooks[item].value
        raise AttributeError(f"{item} not found")
