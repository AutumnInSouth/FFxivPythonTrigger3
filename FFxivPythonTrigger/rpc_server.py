import json
import threading
import traceback
import socket
from socketserver import StreamRequestHandler, ThreadingTCPServer
from types import GeneratorType
from typing import Dict, Set, Callable

from FFxivPythonTrigger.utils import Counter, wait_until

SEND_OUT = 0
SEND_ERR = 1
SEND_END = 2
send_types = ['out', 'err', 'end']

ThreadingTCPServer.allow_reuse_address = True


class RpcHandler(StreamRequestHandler):
    server: 'RpcServer'

    def __init__(self, request, client_address, server, client_id):
        self.client_id = client_id
        super().__init__(request, client_address, server)

    def _send(self, data):
        self.wfile.write(json.dumps(data).encode('utf8') + b'\n')

    def send(self, data, rtn=-1, has_next=False, send_type=SEND_OUT, **kwargs):
        self._send({
            'rtn': rtn,
            'next': int(has_next),
            'type': send_types[send_type],
            'data': data,
            **kwargs
        })

    def send_event(self, key, data):
        self._send({
            'type': 'event',
            'key': key,
            'data': data,
        })

    def _process(self, msg_id, msg_type, key, data):
        match msg_type:
            case 'run':
                rtn = getattr(self.server.func_object, key)(*data.get('args', []), **data.get('kwargs', {}))
                if isinstance(rtn, GeneratorType):
                    for r in rtn: self.send(r, rtn=msg_id, has_next=True, send_type=SEND_OUT)
                    self.send(0, rtn=msg_id, has_next=False, send_type=SEND_END)
                else:
                    self.send(rtn, rtn=msg_id)
            case 'sub':
                self.server.client_subscribe.setdefault(key, set()).add(self.client_id)
                self.send("success", rtn=msg_id)
            case 'unsub':
                try:
                    self.server.client_subscribe.setdefault(key, set()).remove(self.client_id)
                except ValueError:
                    pass
                self.send("success", rtn=msg_id)
            case other:
                self.send(f"invalid message type '{other}'", rtn=msg_id, send_type=SEND_ERR)

    def process(self, line):
        data = json.loads(line)
        msg_id = -1
        try:
            msg_id = data['msg_id']  # a number
            self._process(msg_id, data['msg_type'], data['key'], data)
        except Exception as e:
            self.send(str(e), rtn=msg_id, send_type=SEND_ERR, trace=traceback.format_exc())

    def handle(self):
        print("connect ", self.client_id, flush=True)
        self.server.clients[self.client_id] = self
        threads = []
        try:
            for _line in self.rfile:
                t = threading.Thread(target=self.process, args=(_line,))
                threads.append(t)
                t.start()
        except ConnectionError:
            pass
        finally:
            print("disconnect ",self.client_id,flush=True)
            [t.join() for t in threads]
            del self.server.clients[self.client_id]


class RpcServer(ThreadingTCPServer):
    client_subscribe: Dict[str, Set[int]]
    clients: Dict[int, 'RpcHandler']

    def __init__(self, server_address, func_object, **kwargs):
        super().__init__(server_address, RpcHandler, **kwargs)
        self.client_counter = Counter()
        self.client_subscribe = dict()
        self.clients = dict()
        self.func_object = func_object

    def finish_request(self, request, client_address) -> None:
        self.RequestHandlerClass(request, client_address, self, self.client_counter.get())

    def broadcast_event(self, key, event):
        if key not in self.client_subscribe: return
        for client_id in self.client_subscribe.get(key, set()).copy():
            try:
                client = self.clients[client_id]
            except KeyError:
                try:
                    self.client_subscribe.get(key, set()).remove(client_id)
                except ValueError:
                    pass
            else:
                client.send_event(key, event)


class RpcServerException(Exception): pass


class RpcGenerator: pass


class RpcClient(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start = False
        self.buffer_size = 1024 * 1024
        self.wait_return = {}
        self.wait_generator = {}
        self.locks = {}
        self.counter = Counter()

    def connect(self, address):
        self.sock.connect(address)

    def on_event(self, event_name, event_data):
        pass

    def process(self, line):
        print(line)
        data = json.loads(line)
        if data['type'] == 'event':
            self.on_event(data['key'], data['data'])
        else:
            msg_id = data['msg_id']
            with self.locks.setdefault(msg_id, threading.Lock()):
                if msg_id in self.wait_generator:
                    wait_until(lambda: (self.wait_generator.get(msg_id, 0) is None) or None)
                    self.wait_generator[msg_id] = data
                elif msg_id in self.wait_return:
                    if self.wait_return[msg_id] is not None:
                        raise Exception("Double recive")
                    if data['next']:
                        self.wait_generator[msg_id] = data
                        self.wait_return[msg_id] = RpcGenerator()
                    else:
                        self.wait_return[msg_id] = data['data']
                else:
                    raise Exception(f"unknown return {data}")

    def send(self, data):
        data['msg_id'] = self.counter.get()
        self.wait_return[data['msg_id']] = None
        to_send=json.dumps(data).encode('utf-8') + b'\n'
        print(to_send,self.sock.send(to_send))
        rtn = wait_until(lambda: self.wait_return[data['msg_id']])
        del self.wait_return[data['msg_id']]
        if isinstance(rtn, RpcGenerator):
            return rtn
        elif isinstance(rtn, RpcServerException):
            raise rtn
        else:
            return rtn["data"]

    def serve_forever(self):
        self.start = True
        buffer = bytearray()
        while True:
            buffer.extend(self.sock.recv(self.buffer_size))
            while True:
                try:
                    idx = buffer.index(b'\n') + 1
                except ValueError:
                    break
                else:
                    data = buffer[:idx]
                    buffer = buffer[idx:]
                    threading.Thread(target=self.process, args=(data,)).start()
