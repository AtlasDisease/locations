# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a group of buildings that are
# collectively named and used for a similar purpose. To create
# your own you can subclass the Division class and create a
# Types enum for the type of area.

# --- Imports --- #

from enum import IntEnum, auto
from .divisions import Division

__all__ = ("AreaTypes", "Neighborhood", "College", "University", "Fort")


# --- AreaTypes Enum --- #

class AreaTypes(IntEnum):
    NEIGHBORHOOD = auto() #General use
    COLLEGE = auto()
    UNIVERSITY = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()

    def __str__(self):
        return self.name.title()


# --- Area Class --- #

##class Area(Division):
##    def __init__(self, name: str, type_: AreaTypes, /,
##                 subdivisions: list[Division] | Division = None,
##                 population: int = None,          
##                 **kwargs):
##
##        super().__init__(name, type_, population, subdivisions, **kwargs)
##
##    def __str__(self):
##
##        if self.__class__.__name__ == "Area":
##            return f"The {self.type_} of {self.name}"
##        return f"The {self.__class__.__name__} of {self.name}"


# --- Neighborhood Class --- #

class Neighborhood(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None, 
                 **kwargs):

        super().__init__(name, AreaTypes.NEIGHBORHOOD, population, subdivisions, **kwargs)


# --- College Class --- #

class College(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,   
                 **kwargs):

        super().__init__(name, AreaTypes.COLLEGE, population, subdivisions, **kwargs)


# --- University Class --- #

class University(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,  
                 **kwargs):

        super().__init__(name, AreaTypes.UNIVERSITY, population, subdivisions, **kwargs)


# --- Fort Class --- #

class Port(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,     
                 **kwargs):

        super().__init__(name, AreaTypes.PORT, population, subdivisions, **kwargs)
