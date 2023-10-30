# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a solar system.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- SolarSystem Class --- #

class SolarSystem(Division):
    def __init__(self, name: str, /,
                 population: int = None,
                 subdivisions: list[Division] | Division = None,
                 **kwargs):

        super().__init__(name, DivisionTypes.SOLAR_SYSTEM, population, subdivisions, **kwargs)
