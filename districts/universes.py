# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a universe.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- Universe Class --- #

class Universe(Division):
    def __init__(self, name: str, /,
                 population: int = None,
                 subdivisions: list[Division] | Division = None,
                 **kwargs):

        super().__init__(name, DivisionTypes.UNIVERSE, population, subdivisions, **kwargs)
