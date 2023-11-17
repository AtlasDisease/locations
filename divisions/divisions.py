# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a division.

# --- Imports --- #

from enum import StrEnum, auto
from typing import Self, Callable

__all__ = ("DivisionTypes", "Division")


# --- DivisionTypes Enum --- #

class DivisionTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
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

class Division:
    def __init__(self, name: str,
                 type_: StrEnum = DivisionTypes.AREA,
                 /,
                 subdivisions: list[Self] | Self = None,
                 *,
                 population: int = None,
                 area: int = None,
                 elevation: int = None,
                 **kwargs):

        self.name = name
        self.type_ = type_
        self.subdivisions = []

        if subdivisions and not self.subdivisions:
            add_subdivisions(self, subdivisions)

        if population != None:
            self.population = population

        if area != None:
            self.area = area

        if elevation != None:
            self.elevation = elevation

        #I do not like this as it ties districts and politics together a bit
        if "administrator" in kwargs and "government" in kwargs:
            if kwargs["administrator"] and kwargs["government"]:
                raise Exception("You cannot have both government and administrator populated")

            if kwargs["administrator"]:
                self.administrator = kwargs["administrator"]
            if kwargs["government"]:
                self.government = kwargs["government"]

        self.__dict__ |= kwargs

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec: str = "") -> str:
        if "O" in format_spec or "F" in format_spec: #Stands for "Formal" or "Official"
            if self.__class__.__name__ == "Division":
                return f"The {self.type_} of {self.name}"
            return f"The {self.__class__.__name__} of {self.name}"
        
        if "L" in format_spec or "l" in format_spec: #Stands for "Location"
            if self.__class__.__name__ == "Division":
                return f"{self.name} {self.type_}"
            return f"{self.name} {self.__class__.__name__}"

        return str(self)

    def __bool__(self) -> bool:
        return self.name != "New" and self.name \
               and self.type_ != DivisionTypes.AREA

    def __iter__(self):
        return iter(self.subdivisions)
        
    def get(self, func: Callable) -> Self:
        """Gets a subdivision based of a certain function.
Ex. get largest or smallest subdivision by Population"""
        return func(self)

##    def search(name: str) -> Location:
##        for subdivision in self.subdivisions:
##            if
        


# --- Extending Functionality Definitions --- #

def add_subdivisions(cls, subdivisions: list[Division] | Division) -> None:
    if isinstance(subdivisions, list):
        cls.subdivisions.extend(subdivisions)
        return
    
    cls.subdivisions.append(subdivisions)
