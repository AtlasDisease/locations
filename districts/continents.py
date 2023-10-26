# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- Continent Class --- #

class Continent(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.CONTINENT, population, subdivisions)
