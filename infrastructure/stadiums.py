# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for stadiums.

# --- Imports --- #

from enum import StrEnum, auto
from .buildings import Building

__all__ = ("StadiumTypes", "Stadium")


# --- Stadium Enums --- #

class StadiumTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
    SPORTS = auto()
    CONCERT = auto()
    CONVENTION = auto() #Convention Center


# --- Stadium Class --- #

class Stadium(Building):
    def __init__(self, name: str, **kwargs):

        super().__init__(name, **kwargs)
