# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a group of buildings that are
# collectively named and used for a similar purpose. To create
# your own you can subclass the Division class and create a
# Types enum for the type of area.

# --- Imports --- #

from enum import IntEnum, auto
from ..divisions import Division

__all__ = ("AreaTypes", "Neighborhood", "Fort", "Port", "Airport")


# --- AreaTypes Enum --- #

class AreaTypes(IntEnum):
    NEIGHBORHOOD = auto() #General use
    SCHOOL = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()

    def __str__(self):
        return self.name.title()


# --- Neighborhood Class --- #

class Neighborhood(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None, 
                 **kwargs):

        super().__init__(name, AreaTypes.NEIGHBORHOOD, subdivisions, population = population, **kwargs)


# --- Fort Class --- #

class Fort(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,     
                 **kwargs):

        super().__init__(name, AreaTypes.FORT, subdivisions, population, **kwargs)    


# --- Port Class --- #

class Port(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,     
                 **kwargs):

        super().__init__(name, AreaTypes.PORT, subdivisions, population, **kwargs)


# --- Airport Class --- #

class Airport(Division):
     def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,     
                 **kwargs):

        super().__init__(name, AreaTypes.AIRPORT, subdivisions, population, **kwargs)
