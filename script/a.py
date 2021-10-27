class a(object):
    def __init__(self):
        self._v = 1

    def __getattr__(self, item):
        if not item.startswith('_'):
            return getattr(self, '_' + item)
        raise AttributeError


print(a().v)
