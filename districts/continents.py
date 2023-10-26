# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes, add_population, add_subdivisions


# --- Continent Class --- #

class Continent(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.CONTINENT)

        if (population != None):
            add_population(self, population)

        if (subdivisions != None):
            add_subdivisions(self, subdivisions)
