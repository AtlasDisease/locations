# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a state.

# A State is a complicated idea due to the different meanings
# in different areas of the world. They are most usually treated
# more like their own countries than something like a County,
# Parish, Shire.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- State Class --- #

class State(Division):
    def __init__(self, name: str, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.STATE, population, subdivisions)
