# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a fort rooms/buildings.
# This module does not differentiate between a room or a building
# as in a lot of (especially old) forts a building was used for
# one purpose. 

# --- Imports --- #

from typing import override
from ..enum import IntEnum, StrEnum, auto, unique
from ..subdivisions import DivisionBase
from . import Subdivision

__all__ = ("Fort",)


# --- FortTypes Enum --- #

class FortTypes(IntEnum):
    FORT = auto()


# --- FortAreaTypes Enum --- #

@unique
class FortAreaTypes(StrEnum): #Can be used as a Building type or a Room Type
    UNDEFINED = auto()
    PARADE = auto()
    OFFICER_QUARTERS = auto()
    BARRACKS = auto()
    POST_OFFICE = auto()
    WATCHTOWER = auto()
    HOSPITAL  = auto()


# --- Fort Class --- #

class Fort(DivisionBase):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Subdivision] = None,
                 *,
                 population: int = None,
                 **kwargs):
        
        super().__init__(name, FortTypes.FORT, subdivisions)

        if population:
            self.population = population

    @override
    def __format__(self, format_spec = ""):
        if "F" in format_spec or "O" in format_spec:
            return f"The {self.__class__.__name__} of {self.name}"
        return f"{self.__class__.__name__} {self.name}"
