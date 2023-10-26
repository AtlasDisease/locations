# --- Imports --- #

from enum import IntEnum, auto
from .divisions import Division


# --- AreaTypes Enum --- #

class AreaTypes(IntEnum):
    NEIGHBORHOOD = auto()
    COLLEGE = auto()
    UNIVERSITY = auto()
    PORT = auto()

    def __str__(self):
        return self.name.title()


# --- Area Class --- #

class Area(Division):
    def __init__(self, name: str, type_: AreaTypes, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, type_, population, subdivisions)


# --- Neighborhood Class --- #

class Neighborhood(Area):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, AreaTypes.NEIGHBORHOOD, population, subdivisions)
