i=0
data=bytearray(b'\x01\x12\x50')
while True:
    i=data.index(80,i+1)
    print(i)
