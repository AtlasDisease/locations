# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- Universe Class --- #

class Universe(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.UNIVERSE, population, subdivisions)
