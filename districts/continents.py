# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a continent.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("Continent",)


# --- Continent Class --- #

class Continent(Division):
    def __init__(self, name: str, /,
                subdivisions: list[Division] | Division = None,
                 population: int = None,
                 **kwargs):

        super().__init__(name, DivisionTypes.CONTINENT, subdivisions, population, **kwargs)
