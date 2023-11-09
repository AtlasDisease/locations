# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for stadiums.

# --- Imports --- #

from enum import IntEnum, auto
from .places import Place, PlaceTypes

__all__ = ("StadiumTypes", "Stadium")


# --- Stadium Enums --- #

class StadiumTypes(IntEnum):
    SPORTS = auto()
    CONCERT = auto()
    CONVENTION = auto() #Convention Center


# --- Stadium Class --- #

class Stadium(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.STADIUM, population, **kwargs)
