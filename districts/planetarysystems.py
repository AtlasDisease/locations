# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a planetary system. This was originally
# called solarsystems but I learned that the correct term is planetary
# system as solar refers to Our Sun (Sol, Solis) and is the incorrect term
# for groups of other planets that revolve around other stars.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("PlanetarySystem",)


# --- PlanetarySystem Class --- #

class PlanetarySystem(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,  
                 **kwargs):

        super().__init__(name, DivisionTypes.PLANETARY_SYSTEM, subdivisions, population, **kwargs)

    def __str__(self) -> str:
        return f"The Planetary System of {self.name}"

    def __format__(self, format_spec: str = "") -> str:

        if format_spec == "%t":
            return str(self)

        return f"{self.name} Planetary System"
