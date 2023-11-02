# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a universe.

# --- Imports --- #

from .divisions import Division, DivisionTypes

__all__ = ("Universe",)


# --- Universe Class --- #

class Universe(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,
                 **kwargs):

        super().__init__(name, DivisionTypes.UNIVERSE, subdivisions, population, **kwargs)
