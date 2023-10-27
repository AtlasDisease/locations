# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a country.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- Country Class --- #

class Country(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.COUNTRY, population, subdivisions)
