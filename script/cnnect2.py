from datetime import datetime
import threading

from FFxivPythonTrigger.rpc_server import RpcClient


def print_log(_, data):
    print(
        "[{level}]\t[{time}|{module}]\t{message}".format(
            time=datetime.fromtimestamp(data["timestamp"]).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
            module=data['module'],
            level=data['level'],
            message=data['msg']
        )
    )


client = RpcClient()
client.connect(('127.0.0.1', 20001))
t = threading.Thread(target=client.serve_forever)
t.start()
client.subscribe('fpt_log', print_log)
print(client.run('start'))
print(client.run('get_pid'))
t.join()
