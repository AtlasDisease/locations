# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a fort rooms/buildings.
# This module does not differentiate between a room or a building
# as in a lot of (especially old) forts a building was used for
# one purpose. 

# --- Imports --- #

from enum import IntEnum, auto
from ..divisions.districts import AreaTypes, District


# --- FortAreaTypes Enum --- #

class FortAreaTypes(IntEnum): #Can be used as a Building type or a Room Type
    UNDEFINED = auto()
    PARADE = auto()
    OFFICER_QUARTERS = auto()
    BARRACKS = auto()
    POST_OFFICE = auto()
    WATCHTOWER = auto()
    HOSPITAL  = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- Fort Class --- #

class Fort(District):
    def __init__(self, name: str,
                 /,
                 subdivisions: list = None,
                 *,
                 population: int = None,
                 **kwargs):
        
        super().__init__(name, AreaTypes.FORT, subdivisions, population = population)
