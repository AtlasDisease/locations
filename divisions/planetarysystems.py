# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a planetary system. This was originally
# called solarsystems but I learned that the correct term is planetary
# system as solar refers to Our Sun (Sol, Solis) and is the incorrect term
# for groups of other planets that revolve around other stars.

# --- Imports --- #

from typing import override
from dataclasses import dataclass
from .divisions import Division, DivisionTypes

__all__ = ("PlanetarySystem",)


# --- PlanetarySystem Class --- #

@dataclass(init = False)
class PlanetarySystem(Division):
    def __post_init__(self):
        
        self.type_ = DivisionTypes.PLANETARY_SYSTEM

    @override
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"The Planetary System of {self.name}"

        return f"{self.name} Planetary System"
