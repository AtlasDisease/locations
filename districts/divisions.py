# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a division. These are very similar to Areas
# but are for larger regions and have a clearly defined area.

# --- Imports --- #

from enum import IntEnum, auto
from typing import Self
    

# --- DivisionTypes Enum --- #

class DivisionTypes(IntEnum):
    CITY = auto()
    COUNTY = auto()
    STATE = auto()
    COUNTRY = auto()
    CONTINENT = auto()
    PLANET = auto()
    SOLAR_SYSTEM = auto()
    GALAXY = auto()
    UNIVERSE = auto()

    def __str__(self):
        return self.name.title()


# --- Division Class --- #

class Division:
    def __init__(self, name: str, type_: IntEnum,
                 /,
                 population: int = None,
                 subdivisions: list[Self] | Self = None,
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

    def __str__(self):
        return f"The {self.type_} of {self.name}"


# --- Extending Functionality Definitions --- #

def add_population(cls, population: int):
    cls.population = population

def add_subdivisions(cls, subdivisions: list[Division] | Division):
    if not hasattr(cls, "subdivisions"):
        cls.subdivisions = []
        
    if isinstance(subdivisions, list):
        cls.subdivisions.extend(subdivisions)
        return

    cls.subdivisions.append(subdivisions)
