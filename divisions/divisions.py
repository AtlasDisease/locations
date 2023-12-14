# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a division.

# --- Imports --- #

from dataclasses import dataclass, field, KW_ONLY
from typing import Self, Callable, override
from ..enum import IntEnum, auto
from ..subdivisions import DivisionBase
from .extensions.population import add_population
from .extensions.area import add_area
from .extensions.elevation import add_elevation

__all__ = ("DivisionTypes", "Division")


# --- DivisionTypes Enum --- #

class DivisionTypes(IntEnum):
    AREA = auto() #General Use
    CITY = auto()
    COUNTY = auto()
    STATE = auto()
    COUNTRY = auto()
    CONTINENT = auto()
    PLANET = auto()
    PLANETARY_SYSTEM = auto()
    GALAXY = auto()
    UNIVERSE = auto()


# --- Division Class --- #

class Division(DivisionBase):
    def __init__(self, name: str,
                 type_: IntEnum = DivisionTypes.AREA,
                 /,
                 subdivisions: list[Self] | Self = None,
                 *,
                 population: int = None,
                 area: int = None,
                 elevation: int = None,
                 **kwargs):

        super().__init__(name, type_, subdivisions)

        if population != None:
            add_population(self, population)

        if area != None:
            add_area(self, area)

        if elevation != None:
            add_elevation(self, elevation)

        #I do not like this as it ties districts and politics together a bit
        # Also doing this to avoid having to import the Administrator
        # and Government types from the politics package
        if "administrator" in kwargs and "government" in kwargs:
            if kwargs["administrator"] and kwargs["government"]:
                raise Exception("You cannot have both government and administrator populated")

            if kwargs["administrator"]:
                self.administrator = kwargs["administrator"]
            if kwargs["government"]:
                self.government = kwargs["government"]

        # Add available extensions or extra arguments
        self.__dict__ |= kwargs
        

    @override
    def __format__(self, format_spec: str = "") -> str:
        if "O" in format_spec or "F" in format_spec: #Stands for "Formal" or "Official"
            if self.__class__.__name__ == "Division":
                return f"The {self.type_} of {self.name}".strip()
            return f"The {self.__class__.__name__} of {self.name}".strip()
        
        if "L" in format_spec or "l" in format_spec: #Stands for "Location"
            if self.__class__.__name__ == "Division":
                return f"{self.name} {self.type_}".strip()
            return f"{self.name} {self.__class__.__name__}".strip()

        return str(self)

    @override
    def __bool__(self) -> bool:
        return self.name != "New" and self.name \
               and self.type_ != DivisionTypes.AREA
        
    def get(self, func: Callable) -> Self:
        """Gets a subdivision based of a certain function.
Ex. get largest or smallest subdivision by Population"""
        return func(self)

    def search(self, search, func: Callable):
        return func(self, search)

##    def add_subdivision(self, division: Self):
##        self._subdivisions.append(division)
##        self._subdivisions.sort()
