# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for connecting divisions and infrastructure packages.

# --- Imports --- #

from .enum import StrEnum, auto
from .divisions.divisions import Division
from .infrastructure.buildings import Building
from .infrastructure.rooms import Room

__all__ = ("Subdivision", "SubdivisionTypes")


#A type of Building or Room
# EX. School() which could just have rooms or can have multiple buildings
type Subdivision = Building | Room


# --- SubdivisionTypes Enum --- #

class SubdivisionTypes(StrEnum):
    NEIGHBORHOOD = auto() #General use
    SCHOOL = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()
    CEMETERY = auto()
