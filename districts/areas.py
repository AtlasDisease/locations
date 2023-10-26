# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes, add_population, add_subdivisions


# --- AreaTypes Enum --- #

class AreaTypes(StrEnum):
    NEIGHBORHOOD = auto()
    COLLEGE = auto()
    UNIVERSITY = auto()
    PORT = auto()

    def __str__(self):
        return self.name.title()


# --- Area Class --- #

class Area(Division):
    def __init__(self, name: str, type_: AreaTypes):

        super().__init__(name, DivisionTypes.BUILDING, type_)


# --- Neighborhood Class --- #

class Neighborhood(Area):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.NEIGHBORHOOD)
