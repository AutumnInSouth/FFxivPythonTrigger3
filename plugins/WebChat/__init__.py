import asyncio
import json
import time
from typing import TYPE_CHECKING
from pathlib import Path

from FFxivPythonTrigger import PluginBase, plugins, wait_until
from FFxivPythonTrigger.decorator import unload_callback, event
from FFxivPythonTrigger.exceptions import PluginNotFoundException, NeedRequirementError

if TYPE_CHECKING:
    from XivMemory.hook.chat_log import ChatLogEvent

try:
    from aiohttp import web, WSMsgType
except ModuleNotFoundError:
    raise NeedRequirementError('aiohttp')

default_host = "0.0.0.0"
default_port = 3215
command = "@WebChat"
dir = Path(__file__).parent


async def root_handler(request):
    return web.HTTPFound('/index.html')


class WebChat(PluginBase):
    name = "WebChat"

    layout = str(dir / 'layout.js')

    def __init__(self):
        super(WebChat, self).__init__()
        self.server_config = self.storage.data.setdefault('server', {
            'start_default': False,
            'port': default_port,
            'host': default_host
        })
        self.app = web.Application()
        self.app.router.add_route('GET', '/', root_handler)
        self.app.router.add_route('GET', '/ws', self.ws_handler)
        self.app.router.add_static('/', path=dir / 'res')
        self.loop = asyncio.new_event_loop()
        self.routes = dict()
        self.work = False
        self.runner = None

        self.clients = dict()
        self.client_count = 0

    async def ws_handler(self, request):
        ws = web.WebSocketResponse()
        cid = self.client_count
        self.client_count += 1
        self.clients[cid] = ws
        await ws.prepare(request)
        try:
            async for msg in ws:
                if msg.type == WSMsgType.TEXT:
                    try:
                        plugins.XivMemory.calls.do_text_command(msg.data)
                    except Exception as e:
                        await ws.send_json({
                            'epoch': time.time(),
                            'sender': 'error',
                            'text': str(e),
                            'channel': -1,
                        })
                elif msg.type == WSMsgType.ERROR:
                    pass
        except asyncio.CancelledError:
            pass
        del self.clients[cid]
        return ws

    @event("log_event")
    def deal_chat_log(self, evt: 'ChatLogEvent'):
        asyncio.set_event_loop(self.loop)
        data = {
            'epoch': evt.chat_log.timestamp,
            'sender': (evt.player or '-') if evt.player != plugins.XivMemory.actor_table.me.name else None,
            'msg': evt.message,
            'channel': evt.channel_id,
        }
        for cid, ws in self.clients.items():
            asyncio.run(ws.send_json(data))

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
        self.logger.info("WebChat Server started on http://%s:%s" % (host, port))
        self.work = True
        while self.work:
            await asyncio.sleep(1)

    def start_server(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._start_server())

    def start(self):
        if self.server_config.setdefault('start_default', False):
            self.start_server()

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
            raise Exception("WebChat has been started")
        else:
            self.create_mission(self.start_server, limit_sec=0)
        return True

    def layout_stop_server(self):
        if self.work:
            self.stop_server()
        else:
            raise Exception("WebChat haven't been started")
        return True
