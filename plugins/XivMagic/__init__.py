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
from .sigs import sigs


class XivMagic(PluginBase):
    name = "XivMagic"

    def __init__(self):
        super().__init__()
        self.address = AddressManager(self.name, self.logger).load(sigs)
        self.do_action = DoAction(self.address['do_action'], self.address('action_manager'))
        self.do_action_location = DoActionLocation(self.address['do_action_location'], self.address('action_manager'))
        self.do_text_command = DoTextCommand(self.address['do_text_command'], self.address['text_command_ui_module'])
        self.register_http_api_route()

    @event("plugin_load:HttpApi")
    def register_http_api_route(self, _):
        try:
            plugins.HttpApi.register_post_route(self, 'command', self.text_command_handler)
            plugins.HttpApi.register_post_route(self, 'useitem', self.use_item_handler)
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
