# --- Imports --- #

import datetime as dt
from typing import Protocol
from dataclasses import dataclass, field, KW_ONLY
from functools import cached_property


# --- Timetable Class --- #

@dataclass(slots = True, frozen=True)
class Timetable:
    start: dt.datetime = dt.datetime.min
    end: dt.datetime = dt.datetime.max
    _: KW_ONLY
    _duration: dt.timedelta = field(default_factory = dt.timedelta)

    def __post_init__(self):

        if self._duration:
            self.end = self.start + self._duration

    @cached_property
    def duration(self) -> dt.datetime:
        return self.end - self.start


# --- Timeable Protocol --- #

class Timeable(Protocol):
    @cached_property
    def duration(self) -> dt.datetime:
        return self.end - self.start
