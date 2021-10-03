import json
import socket
import time
from datetime import datetime

HOST, PORT = "127.0.0.1", 3520
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            sock.connect((HOST, PORT))
            break
        except:
            time.sleep(1)
    print("connect!")
    sock.send(json.dumps({'code': 0x1000, 'name': 'fpt_log', 'msg_id': 0}).encode('utf-8') + b'\n')
    buffer = bytearray()
    while True:
        try:
            buffer += sock.recv(2048)
        except ConnectionError as e:
            print("connection failed", e)
            break
        while True:
            try:
                idx = buffer.index(10)
            except ValueError:
                break
            data = json.loads(buffer[:idx])
            if data['code'] == 0x2000:
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
    print("disconnect")

