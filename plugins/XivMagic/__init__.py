import json

from FFxivPythonTrigger import PluginBase, plugins
from FFxivPythonTrigger.address_manager import AddressManager
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.exceptions import NeedRequirementError, PluginNotFoundException

try:
    from aiohttp import web
except ModuleNotFoundError:
    raise NeedRequirementError('aiohttp')

from .do_action import DoAction, DoActionLocation
from .do_text_command import DoTextCommand
from .head_mark import HeadMark
from .way_mark import WayMark
from .sigs import sigs


class XivMagic(PluginBase):
    name = "XivMagic"

    def __init__(self):
        super().__init__()
        self.address = AddressManager(self.name, self.logger).load(sigs)
        self.do_action = DoAction(self.address['do_action'], self.address['action_manager'])
        self.do_action_location = DoActionLocation(self.address['do_action_location'], self.address['action_manager'])
        self.do_text_command = DoTextCommand(self.address['do_text_command'], self.address['text_command_ui_module'])
        self.head_mark = HeadMark(self.address['head_mark'], self.address['marking_controller'])
        self.way_mark = WayMark(self.address['way_mark_set'], self.address['way_mark_clear'], self.address['way_mark_clear_all'],
                                self.address['marking_controller'], self.address['action_manager'])
        self.register_http_api_route()

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
