# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a group of buildings that are
# collectively named. These are called Areas in my code.
# To create your own you can subclass the Area class.

# --- Imports --- #

from enum import IntEnum, auto
from .divisions import Division


# --- AreaTypes Enum --- #

class AreaTypes(IntEnum):
    NEIGHBORHOOD = auto() #General use
    COLLEGE = auto()
    UNIVERSITY = auto()
    PORT = auto()

    def __str__(self):
        return self.name.title()


# --- Area Class --- #

class Area(Division):
    def __init__(self, name: str, type_: AreaTypes, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, type_, population, subdivisions)

    def __str__(self):
        return f"The {self.type_} of {self.name}"


# --- Neighborhood Class --- #

class Neighborhood(Area):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, AreaTypes.NEIGHBORHOOD, population, subdivisions)


# --- College Class --- #

class College(Area):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, AreaTypes.COLLEGE, population, subdivisions)


# --- University Class --- #

class University(Area):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, AreaTypes.UNIVERSITY, population, subdivisions)


# --- Fort Class --- #

class Port(Area):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, AreaTypes.Port, population, subdivisions)
