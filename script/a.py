import time


def counter(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(f"run {func.__name__} in {time.perf_counter() - start:.3f}s")
        return res
    return wrapper

@counter
def a(l):
    del l[50000:]

@counter
def b(l):
    return l[-50000:]

a(list(range(1000000)))
b(list(range(1000000)))
