# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for stadiums.

# --- Imports --- #

from ..enum import IntEnum, StrEnum, auto, unique
from .buildings import Building

__all__ = ("StadiumTypes", "Stadium", "SportTypes")


# --- Stadium Enums --- #

@unique
class StadiumTypes(StrEnum):
    SPORTS = auto()
    CONCERT = auto()
    CONVENTION = auto() #Convention Center


# --- SportTypes Enums --- #

class SportTypes(IntEnum):
    BASEBALL = auto()
    HOCKEY = auto()
    AMERICAN_FOOTBALL = auto()
    SOCCER = 4
    FOOTBALL = 4
    BASKETBALL = auto()
    CRICKET = auto()
    HANDBALL = auto()
    GOLF = auto()
    


# --- Stadium Class --- #

class Stadium(Building):
    def __init__(self, name: str, **kwargs):

        super().__init__(name, **kwargs)
