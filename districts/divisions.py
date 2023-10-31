# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a division.

# --- Imports --- #

from enum import IntEnum, auto
from typing import Self

__all__ = ("DivisionTypes", "Division", "add_population", "add_subdivisions")


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

    def __str__(self) -> str:
        return self.name.title()


# --- Division Class --- #

class Division:
    def __init__(self, name: str, type_: IntEnum,
                 /,
                 subdivisions: list[Self] | Self = None,
                 population: int = None,       
                 **kwargs):

        self.name = name
        self.type_ = type_

        if (population != None):
            add_population(self, population)

        if (subdivisions != None):
            add_subdivisions(self, subdivisions)

        #I do not like this as it ties districts and politics together
        if "administrator" in kwargs and "government" in kwargs:
            if kwargs["administrator"] != None and kwargs["government"] != None:
                raise Exception("You cannot have both government and administrator populated")

        self.__dict__ |= kwargs

    def __str__(self) -> str:
        
        if self.__class__.__name__ == "Division":
            return f"The {self.type_} of {self.name}"
        return f"The {self.__class__.__name__} of {self.name}"

    def __format__(self, format_spec: str = "") -> str:

        if format_spec == "%t":
            return str(self)

        if self.__class__.__name__ == "Division":
            return f"{self.name} {self.type_}"
        return f"{self.name} {self.__class__.__name__}"



# --- Extending Functionality Definitions --- #

def add_population(cls, population: int) -> None:
    cls.population = population

def add_subdivisions(cls, subdivisions: list[Division] | Division) -> None:
    if not hasattr(cls, "subdivisions"):
        cls.subdivisions = []
        
    if isinstance(subdivisions, list):
        cls.subdivisions.extend(subdivisions)
        return

    cls.subdivisions.append(subdivisions)

