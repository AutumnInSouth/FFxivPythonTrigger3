import socket
import json
HOST, PORT = "127.0.0.1",3520
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print("connect!")
sock.send(json.dumps({
    'code': 0x1000,
    'name': 'fpt_log',
    'msg_id':1,
}).encode('utf-8')+b'\n')
while True:
    try:
        print(sock.recv(2048).decode('utf-8'))
    except Exception:
        break
print("disconnect")
