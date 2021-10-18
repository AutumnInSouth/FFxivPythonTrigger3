import socket
import json
import threading
from datetime import datetime


class Client(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.counter = 0
        self.counter_lock = threading.Lock()

    def send(self, data: dict):
        with self.counter_lock:
            data['msg_id'] = self.counter
            self.counter += 1
        self.sock.send(json.dumps(data).encode() + b'\n')

    def main(self):
        buffer = bytearray()
        while True:
            buffer += self.sock.recv(2048)
            while True:
                try:
                    idx = buffer.index(10)
                except ValueError:
                    break
                data = json.loads(buffer[:idx])
                if data['type'] == 'event' and data['key'] == 'fpt_log':
                    data = data['data']
                    print(
                        "[{level}]\t[{time}|{module}]\t{message}".format(
                            time=datetime.fromtimestamp(data["timestamp"]).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
                            module=data['module'],
                            level=data['level'],
                            message=data['msg']
                        )
                    )
                else:
                    print(data)
                buffer = buffer[idx + 1:]


client = Client('127.0.0.1', 20001)
main_thread = threading.Thread(target=client.main)
main_thread.start()
client.send({'msg_type': 'sub', 'key': 'fpt_log'})
client.send({'msg_type': 'run', 'key': 'start'})
client.send({'msg_type': 'run', 'key': 'log_history'})
main_thread.join()
