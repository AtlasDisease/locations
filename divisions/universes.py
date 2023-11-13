# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a universe.

# --- Imports --- #

from dataclasses import dataclass
from .divisions import Division, DivisionTypes

__all__ = ("Universe",)


# --- Universe Class --- #

@dataclass(init = False)
class Universe(Division):
    def __post_init__(self):
        
        self.type_ = DivisionTypes.UNIVERSE

    def __str__(self):
        return f"{self.name} {self.__class__.__name__}".strip()
