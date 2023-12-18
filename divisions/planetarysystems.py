# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a planetary system. This was originally
# called solarsystems but I learned that the correct term is planetary
# system as solar refers to Our Sun (Sol, Solis) and is the incorrect term
# for groups of other planets that revolve around other stars.

# --- Imports --- #

from typing import override
from .divisions import Division

__all__ = ("PlanetarySystem",)


# --- PlanetarySystem Class --- #

class PlanetarySystem(Division):

    @override
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"The Planetary System of {self.name}"

        if "L" in format_spec or "l" in format_spec:
            return f"{self.name} Planetary System"

        return str(self)
