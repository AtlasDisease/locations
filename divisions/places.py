# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a building as a place. A place lacks the
# details (like subdivisions) that the infrastructure.buildings.Building has.
# To create your own class, you can subclass Place.
# A place is the smallest unit in the divisions package.

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
    def __init__(self, name: str,
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


# --- place Functions --- #

def place(obj: object) -> Place:
    if isinstance(obj, District) \
       or isinstance(obj, Building):
        return Place(district = obj)