import io
import traceback

from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.exceptions import NeedRequirementError, PluginNotFoundException

try:
    from aiohttp import web
except ModuleNotFoundError:
    raise NeedRequirementError('aiohttp')


class DebugExecPlugin(PluginBase):
    name = "DebugExec"

    async def exec_debug(self, request: web.Request):
        data = {'msg': 'success'}
        str_out = io.StringIO()
        normal_out = sys.stdout
        sys.stdout = str_out
        local_data = locals().copy()
        try:
            exec(await request.text(), globals(), local_data)
        except Exception:
            data['msg'] = 'error occurred'
            data['traceback'] = traceback.format_exc()
        sys.stdout = normal_out
        #data['res'] = local_data.get('res', None)
        data['print'] = str_out.getvalue()
        return web.json_response(data)

    def __init__(self):
        super().__init__()
        self.data = dict()
        self.register_http_api_route()

    @event("plugin_load:HttpApi")
    def register_http_api_route(self, _):
        try:
            plugins.HttpApi.register_post_route(self, 'exec', self.exec_debug)
        except PluginNotFoundException:
            self.logger.warning("HttpApi is not found")
