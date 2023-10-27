# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a planet.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- Planet Class --- #

class Planet(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.PLANET, population, subdivisions)
