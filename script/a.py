def a(a, b, *args, **kwargs):
    print(a, b, args, kwargs)


a(1, 2, 3, a=1, b=2, c=3)
