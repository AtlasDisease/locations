# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a country.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- Country Class --- #

class Country(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None, 
                 **kwargs):

        super().__init__(name, DivisionTypes.COUNTRY, subdivisions, population, **kwargs)
