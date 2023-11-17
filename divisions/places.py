# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a building as a place. A place lacks the
# details (like subdivisions) that the infrastructure.buildings.Building has.
# To create your own class, you can subclass Place.
# A place is the smallest unit in the divisions package.

# --- Imports --- #

from enum import StrEnum, auto
##from .districts import District
from ..subdivisions import Subdivision

__all__ = ("PlaceTypes", "Place")


# --- PlaceTypes Enum --- #

class PlaceTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
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


# --- Place Class --- #

class Place:
    def __init__(self, name: str,
                 type_: PlaceTypes = PlaceTypes.BUILDING,
                 *,
                 population: int = None,
                 district: Subdivision = None,
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
    if not isinstance(obj, District) \
       and not isinstance(obj, Building):
        return Place()
    return Place(district = obj)
