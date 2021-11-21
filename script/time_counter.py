from time import perf_counter


class TimeCounter:
    def __init__(self, start_now=False):
        self.time = perf_counter() if start_now else 0

    def update(self):
        self.time = perf_counter()

    def update_before(self):
        return perf_counter() - self.time


print(TimeCounter.__dict__)
