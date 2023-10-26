# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- SolarSystem Class --- #

class SolarSystem(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.SOLAR_SYSTEM, population, subdivisions)
