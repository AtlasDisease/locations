# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes, add_population, add_subdivisions


# --- Universe Class --- #

class Universe(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.UNIVERSE)

        if (population != None):
            add_population(self, population)

        if (subdivisions != None):
            add_subdivisions(self, subdivisions)
