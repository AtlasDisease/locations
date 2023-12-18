# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a building as a place. A place lacks the
# details (like subdivisions) that the infrastructure.buildings.Building has.
# To create your own class, you can subclass Place.
# A place is the smallest unit in the divisions package.

# --- Imports --- #

from typing import Type
from ..subdivisions import DivisionBase

__all__ = ("Place",)


# --- Place Class --- #

class Place:
    def __init__(self, name: str,
                 type_: Type[DivisionBase],
                 *,
                 population: int = None,
                 district: Type[DivisionBase] = None):

        self.name = name
        self.type = type_

        if population:
            self.population = population

        if district: #Type conversion
            self.name = district.name
            self.type = district.type_
            

    def __str__(self) -> str:
        return self.name
    
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.__class__.name == "Fort":
                return f"{self.type.__name__} {self.name}"
            return f"{self.name} {self.type.__name__}"

        return str(self)

    def __bool__(self) -> bool:
        return self.name != "New" and self.name


# --- place Functions --- #

def place(obj: object) -> Place:
##    if not isinstance(obj, District) \
##       and not isinstance(obj, Building):
##        return Place()
    return Place(district = obj)
