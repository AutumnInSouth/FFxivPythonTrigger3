import asyncio
import traceback
from pathlib import Path

from FFxivPythonTrigger import PluginBase, plugins, wait_until
from FFxivPythonTrigger.decorator import unload_callback, event
from FFxivPythonTrigger.exceptions import PluginNotFoundException, NeedRequirementError

try:
    from aiohttp import web
except ModuleNotFoundError:
    raise NeedRequirementError('aiohttp')

default_host = "127.0.0.1"
default_port = 2019
command = "@HttpApi"


class HttpApiPlugin(PluginBase):
    name = "HttpApi"

    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super(HttpApiPlugin, self).__init__()
        self.server_config = self.storage.data.setdefault('server', {
            'start_default': False,
            'port': 2019,
            'host': '127.0.0.1'
        })
        self.app = web.Application()
        self.app.add_routes([web.post('/{uri:.*}', self.post_route)])
        self.loop = asyncio.new_event_loop()
        self.routes = dict()
        self.work = False
        self.runner = None
        self.register_command()

    @event("plugin_load:Command")
    def register_command(self, _):
        try:
            plugins.Command.register(self, command, self.process_command)
        except PluginNotFoundException:
            self.logger.warning("Command is not found")

    @unload_callback('unregister_post_route')
    def register_post_route(self, path, controller):
        if path in self.routes:
            raise Exception("%s is already registered" % path)
        self.logger.debug("[%s] is registered as a new api" % path)
        self.routes[path] = controller

    def unregister_post_route(self, path, controller):
        if path not in self.routes:
            raise Exception("%s is not registered" % path)
        self.logger.debug("[%s] is unregistered" % path)
        del self.routes[path]

    async def post_route(self, request: web.Request):
        paths = request.path.strip('/').split('/')
        if not paths or paths[0] not in self.routes:
            res = web.json_response({'msg': 'resource not found', 'code': 404}, status=404)
        else:
            try:
                res = await self.routes[paths[0]](request)
            except Exception:
                res = web.json_response({'msg': 'server error occurred', 'trace': traceback.format_exc(), 'code': 500},
                                        status=500)
        self.logger.debug("request:%s ; response: %s" % (request, res))
        return res

    async def _stop_server(self):
        await self.runner.shutdown()
        await self.runner.cleanup()
        self.logger.info("HttpApi server closed")
        self.work = False

    def stop_server(self):
        asyncio.set_event_loop(self.loop)
        self.loop.create_task(self._stop_server())
        wait_until(lambda: not self.work or None)

    def onunload(self):
        if self.work:
            self.stop_server()

    async def _start_server(self):
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        host = self.server_config.setdefault('host', default_host)
        port = self.server_config.setdefault('port', default_port)
        self.storage.save()
        await web.TCPSite(self.runner, host, port).start()
        self.logger.info("HttpApi Server started on http://%s:%s" % (host, port))
        self.work = True
        while self.work:
            await asyncio.sleep(1)

    def start_server(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._start_server())

    def start(self):
        if self.server_config.setdefault('start_default', False):
            self.start_server()

    def process_command(self, args):
        if args:
            if args[0] == 'start':
                self.server_config['start_default'] = True
                if self.work:
                    self.logger("HttpApi has been started")
                else:
                    if len(args) > 1:
                        self.server_config['port'] = int(args[1])
                    self.create_mission(self.start_server, limit_sec=0)
            elif args[0] == 'close':
                self.server_config['start_default'] = False
                if self.work:
                    self.stop_server()
                else:
                    self.logger("HttpApi haven't been started")
            else:
                self.logger("unknown args: %s" % args[0])
        else:
            self.logger("HttpApi: [%s]" % ('enable' if self.work else 'disable'))
        self.storage.save()

    # layout control
    def get_config(self):
        return {
            'config': self.server_config,
            'work': self.work,
        }

    def set_config(self, key, val):
        old = self.server_config[key]
        self.server_config[key] = val
        return old

    def layout_start_server(self):
        if self.work:
            raise Exception("HttpApi has been started")
        else:
            self.create_mission(self.start_server, limit_sec=0)
        return True

    def layout_stop_server(self):
        if self.work:
            self.stop_server()
        else:
            raise Exception("HttpApi haven't been started")
        return True
