import json
import threading
import traceback
import socket
import queue
import operator
from socketserver import StreamRequestHandler, ThreadingTCPServer
from types import GeneratorType
from typing import Dict, Set, Type

from FFxivPythonTrigger.utils import Counter

SEND_OUT = 0
SEND_ERR = 1
SEND_END = 2
send_types = ['out', 'err', 'end']

ThreadingTCPServer.allow_reuse_address = True


class RpcFuncHandler(object):
    client: 'RpcHandler'
    server: 'RpcServer'

    def __init__(self, client, server):
        self.client = client
        self.server = server


class RpcHandler(StreamRequestHandler):
    server: 'RpcServer'

    def __init__(self, request, client_address, server, client_id, func_class):
        self.client_id = client_id
        self.func_object = func_class(self, server)
        super().__init__(request, client_address, server)

    def _send(self, data):
        self.wfile.write(json.dumps(data).encode('utf8') + b'\n')

    def send(self, data, rtn=-1, is_iter=False, send_type=SEND_OUT, **kwargs):
        self._send({
            'rtn': rtn,
            'iter': int(is_iter),
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
                rtn = operator.methodcaller(key, *data.get('args', []), **data.get('kwargs', {}))(self.func_object)
                if isinstance(rtn, (GeneratorType | RpcGenerator)):
                    for r in rtn: self.send(r, rtn=msg_id, is_iter=True, send_type=SEND_OUT)
                    self.send(0, rtn=msg_id, is_iter=False, send_type=SEND_END)
                else:
                    self.send(rtn, rtn=msg_id)
            case 'get':
                self.send(operator.attrgetter(key)(self.func_object), rtn=msg_id)
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
        except RpcClientException as e:
            res = e.args[0]
            self.send(res['data'], rtn=msg_id, send_type=SEND_ERR, trace=res['trace'])
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
            print("disconnect ", self.client_id, flush=True)
            for t in threads: t.join()
            del self.server.clients[self.client_id]


class RpcServer(ThreadingTCPServer):
    client_subscribe: Dict[str, Set[int]]
    clients: Dict[int, 'RpcHandler']

    def __init__(self, server_address, func_class: Type[RpcFuncHandler], **kwargs):
        super().__init__(server_address, RpcHandler, **kwargs)
        self.client_counter = Counter()
        self.client_subscribe = dict()
        self.clients = dict()
        self.func_class = func_class

    def finish_request(self, request, client_address) -> None:
        self.RequestHandlerClass(request, client_address, self, self.client_counter.get(), self.func_class)

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

    def broadcast_event_force(self, key, event):
        for client in list(self.clients.values()):
            client.send_event(key, event)


class RpcServerException(Exception): pass


class RpcClientException(Exception): pass


class RpcGenerator(object):
    def __init__(self, msg_id, wait_dict, first):
        self.msg_id = msg_id
        self.wait_dict = wait_dict
        self.first = first
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i:
            res = self.wait_dict[self.msg_id].get()
        else:
            res = self.first
        self.i += 1
        if res['type'] == 'end':
            del self.wait_dict[self.msg_id]
            raise StopIteration
        elif res['type'] == 'err':
            del self.wait_dict[self.msg_id]
            raise res['data']
        else:
            return res['data']


class RpcClient(object):
    def __init__(self, on_end=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start = False
        self.buffer_size = 1024 * 1024
        self.wait_return = {}
        self.counter = Counter()
        self.subscribe_events = {}
        self.serve_thread = threading.Thread(target=self.serve_forever)
        self.on_end = on_end

    def connect(self, address):
        self.sock.connect(address)

    def on_event(self, event_name, event_data):
        if event_name in self.subscribe_events:
            for evt in self.subscribe_events[event_name].copy():
                threading.Thread(target=evt, args=(event_name, event_data)).start()

    def subscribe(self, event_name, callback):
        if event_name not in self.subscribe_events:
            self.subscribe_events[event_name] = set()
            self.send({'msg_type': 'sub', 'key': event_name}, timeout=5)
        self.subscribe_events[event_name].add(callback)
        return True

    def unsubscribe(self, event_name, callback):
        if event_name not in self.subscribe_events: return
        try:
            self.subscribe_events[event_name].remove(callback)
        except ValueError:
            return False
        if not self.subscribe_events[event_name]:
            del self.subscribe_events[event_name]
            self.send({'msg_type': 'unsub', 'key': event_name}, timeout=5)
        return True

    def process(self, line):
        data = json.loads(line)
        if data['type'] == 'event':
            self.on_event(data['key'], data['data'])
        else:
            msg_id = data['rtn']
            if msg_id in self.wait_return:
                self.wait_return[msg_id].put(data)
            else:
                raise Exception(f"unknown return {data}")

    def send(self, data, need_rtn=True, timeout=None):
        if not self.start:
            raise Exception(f"client not started")
        msg_id = self.counter.get()
        data['msg_id'] = msg_id
        q = queue.Queue()
        if need_rtn:
            self.wait_return[msg_id] = q
        self.sock.send(json.dumps(data).encode('utf-8') + b'\n')
        if need_rtn:
            try:
                res = q.get(timeout=timeout)
            except queue.Empty:
                del self.wait_return[msg_id]
                raise
            if res['type'] == 'err':
                del self.wait_return[msg_id]
                raise RpcClientException(res)
            elif res['iter']:
                return RpcGenerator(msg_id, self.wait_return, res)
            else:
                del self.wait_return[msg_id]
                return res['data']

    def run(self, name, *args, timeout=None, **kwargs):
        return self.send({'msg_type': 'run', 'key': name, 'args': args, 'kwargs': kwargs}, timeout=timeout)

    def get(self, name, timeout=None):
        return self.send({'msg_type': 'get', 'key': name}, timeout=timeout)

    def serve_forever(self):
        if self.start:
            raise Exception("client is already started")
        self.start = True
        buffer = bytearray()
        try:
            while True:
                buffer.extend(self.sock.recv(self.buffer_size))
                while True:
                    try:
                        idx = buffer.index(10)
                    except ValueError:
                        break
                    else:
                        threading.Thread(target=self.process, args=(buffer[:idx],)).start()
                        buffer = buffer[idx + 1:]
        except Exception as e:
            if self.on_end:
                self.on_end(e)
        finally:
            self.start = False
