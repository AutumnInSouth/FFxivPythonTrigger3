from typing import Callable


class TimeLine(object):
    map_id = 0  # the map id of time line used
    mission_id = 0  # TODO:the mission id or any key can be used to define actual mission

    def time_line(self):
        """
        return a dictionary with timestamp key and event value
        """
        pass

    def register(self):
        """
        triggers that register at the start of the time line initialization
        """
        pass


class TimeLineEvent(object):
    type: str


class Effect(TimeLineEvent):
    key = "effect"
    action_id: list[int] | None
    source: list[str] | None
    title: str | None
    tag: list[int]

    def __init__(self, action_id: int | list[int] = None, source: str | list[str] = None,
                 title: str = None, tag: int | list[int] = None):
        """
        an action effected
        Args:
            action_id: the effect action, can be either one or a list. If None, default as "Any"
            source: the name of action source, can be either one or a list. If None, default as "Any"
            title: the title will be shown on hint and generated for event. If None, it won't be shown or generate event
            tag: tag(s) of this event (optional)
        """
        self.action_id = action_id if action_id is None or isinstance(action_id, list) else [action_id]
        self.source = source if source is None or isinstance(source, list) else [source]
        self.title = title
        self.tags = [] if tag is None else tag if isinstance(tag, list) else [tag]


class Cast(Effect):
    key = "cast"


class Jmp(TimeLineEvent):
    key = "jmp"
    condition: Effect | None
    to: int | Callable[[any], int]
