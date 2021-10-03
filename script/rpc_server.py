import zerorpc
import time


class Server(object):
    def test(self, val):
        print(val)
        return val + 1

    @zerorpc.stream
    def con(self):
        for i in range(100):
            yield f"message {i}"
            time.sleep(1)

s = zerorpc.Server(Server())
s.bind("tcp://0.0.0.0:12345")
s.run()
