import json

ClientSubscribe = 0x1000
ClientUnsubscribe = 0x1001
ClientCall = 0x1002
ClientCallReply = 0x1003
ClientGet = 0x1004
ClientSet = 0x1005
ServerEvent = 0x2000
ServerReply = 0x2001
ServerError = 0x2099


def base_response(code: int, data):
    return json.dumps({'code': code, 'data': data}).encode('utf-8')


def server_error(e: any, reply_id: int = None, **kwargs):
    return base_response(ServerError, {'exception': str(e), 'reply': reply_id} | kwargs)


def server_reply(reply_id: int, data):
    return base_response(ServerReply, {'reply': reply_id, 'data': data})


def server_event(data):
    return base_response(ServerEvent, data)
