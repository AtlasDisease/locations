# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a building. In my code this is
# called a place. To create your own class, you can subclass Place
# or Building. A place is supposed to be the smallest unit therefore
# it should not have subdivisions.

# --- Imports --- #

from enum import IntEnum, auto
from .districts import District

__all__ = ("PlaceTypes", "Place")


# --- PlaceTypes Enum --- #

class PlaceTypes(IntEnum):
    BUILDING = auto() #General use
    STADIUM = auto()
    CITY_HALL = auto()
    COURTHOUSE = auto()
    PORT = auto()
    HOUSE_OF_WORSHIP = auto()
    BANK = auto()
    EMERGENCY_SERVICE = auto()
    HOSPITAL = auto()
    POST_OFFICE = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- Place Class --- #

class Place:
    def __init__(self, name: str = "",
                 type_: PlaceTypes = PlaceTypes.BUILDING,
                 *,
                 population: int = None,
                 district: District = None,
                 **kwargs):

        self.name = name
        self.type_ = type_

        if population:
            self.population = population

        if district: #Type conversion
            self.name = district.name
            self.type_ = district.type_
            

    def __str__(self) -> str:
        return self.name
    
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.type_.name == "FORT":
                return f"{self.type_} {self.name}"
            return f"{self.name} {self.type_}"

        return str(self)

    def __bool__(self) -> bool:
        return self.name != "New" and self.name != "" \
               and self.type_ != PlaceTypes.BUILDING
