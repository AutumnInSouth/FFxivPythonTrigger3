import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:12345")

print(c.test(1))
for i,m in enumerate(c.con()):
    print(i,m)
