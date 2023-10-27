# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a galaxy.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- Galaxy Class --- #

class Galaxy(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.GALAXY, population, subdivisions)
