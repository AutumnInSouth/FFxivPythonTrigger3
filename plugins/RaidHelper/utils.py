class RaidTrigger:
    def __init__(self, map_id, title, func, event=None, re_event=None):
        self.enabled = False
        self.map_id = map_id
        self.title = title
        self.func = func
        self.event = event
        self.re_event = re_event

    def __call__(self, *args, **kwargs):
        if self.enabled:
            return self.func(*args, **kwargs)


def raid_trigger(map_id: int, title: str, event: str = None, re_event: str = None):
    return lambda func: RaidTrigger(map_id, title, func, event, re_event)


def map_trigger(map_id: int):
    def decorator(title: str, event: str = None, re_event: str = None):
        return raid_trigger(map_id, title, event, re_event)

    return decorator


common_trigger = map_trigger(-1)
