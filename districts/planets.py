# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a planet.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("Planet",)


# --- Planet Class --- #

class Planet(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,     
                 **kwargs):

        super().__init__(name, DivisionTypes.PLANET, subdivisions, population, **kwargs)
