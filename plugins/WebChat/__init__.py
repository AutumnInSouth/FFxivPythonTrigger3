import asyncio
import json
import time
from typing import TYPE_CHECKING
from pathlib import Path

from FFxivPythonTrigger import PluginBase, plugins, wait_until
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.exceptions import NeedRequirementError

if TYPE_CHECKING:
    from XivMemory.hook.chat_log import ChatLogEvent
    from XivMemory.se_string import ChatLog

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


def parse_msg_chain(msg_chain):
    msg = []
    for m in msg_chain:
        if m.Type == 'Icon':
            msg.append({
                'type': 'icon',
                'data': m.icon_id,
            })
        elif m.Type == 'AutoTranslateKey':
            msg.append({
                'type': 'text',
                'data': f"\ue040{m.text()}\ue041",
            })
        elif m.Type == "Text":
            t = m.text()
            if msg and msg[-1]['type'] == 'text':
                msg[-1]['data'] += t
            else:
                msg.append({
                    'type': 'text',
                    'data': t,
                })
    return msg


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
                            'sender': [{
                                'type': 'text',
                                'data': 'error',
                            }],
                            'text': [{
                                'type': 'text',
                                'data': str(e),
                            }],
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
        me = plugins.XivMemory.actor_table.me
        data = {
            'epoch': evt.chat_log.timestamp,
            'sender': parse_msg_chain(evt.chat_log.sender) if me is None or evt.player != me.name else None,
            'msg': parse_msg_chain(evt.chat_log.messages),
            'channel': evt.channel_id,
        }
        for cid, ws in self.clients.items():
            asyncio.run(ws.send_json(data))

    async def _stop_server(self):
        for cid, ws in self.clients.items():
            await ws.close()

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
