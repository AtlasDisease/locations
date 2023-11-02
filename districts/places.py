# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a building. In my code this is
# called a place. To create your own class, you can subclass Place.
# A place is supposed to be the smallest unit therefore it should
# not have subdivisions.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("PlaceTypes", "Place")


# --- PlaceTypes Enum --- #

class PlaceTypes(StrEnum):
    BUILDING = auto() #General use
    CITY_HALL = auto()
    COURTHOUSE = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- Place Class --- #

class Place:
    def __init__(self, name: str, type_: PlaceTypes, /,
                 population: int = None, 
                 **kwargs):

        self.name = name
        self.type_ = type_

        if (population != None):
            add_population(self, population)

    def __str__(self) -> str:
        if self.type_ == PlaceTypes.FORT:
            return f"{self.type_} {self.name}"
        return f"{self.name} {self.type_}"
