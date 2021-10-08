import threading
from FFxivPythonTrigger.rpc_server import RpcClient


client = RpcClient()
client.connect(("127.0.0.1", 12300))
thread = threading.Thread(target=client.serve_forever)
thread.start()
print(1)
client.send({
    'msg_type': 'run',
    'key': 'get_game_process_g',
    'args': ['python.exe']
})

thread.join(10)
