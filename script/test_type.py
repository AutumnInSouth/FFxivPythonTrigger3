class A(object):
    n=1

class B(object):
    n=2

print(type('',(B,A),{}).n)
