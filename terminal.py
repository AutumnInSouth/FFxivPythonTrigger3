from datetime import datetime

from FFxivPythonTrigger.rpc_server import RpcClient

from FFxivPythonTrigger.logger import LOG_FORMAT, LOG_HEADER_FORMAT, TIME_FORMAT, TIME_CUTOFF, _get_level_name


def print_log(_, log_data):
    print(LOG_FORMAT.format(
        header=LOG_HEADER_FORMAT.format(
            time=datetime.fromtimestamp(log_data['timestamp']).strftime(TIME_FORMAT)[:-TIME_CUTOFF],
            module=log_data['module'],
            level=_get_level_name(log_data['level']),
        ),
        message=log_data['msg'],
    ))


client = RpcClient()
client.connect(('127.0.0.1', int(input("port<<"))))
client.serve_thread.start()
client.subscribe('fpt_log', print_log)
client.serve_thread.join()
