# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a continent.

# --- Imports --- #

from typing import override
from .divisions import Division

__all__ = ("Continent",)


# --- Continent Class --- #

class Continent(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Division] | Division = None,
                 *,
                 population: int = None,
                 **kwargs):

        super().__init__(name, subdivisions,
                         population = population, **kwargs)

    @override
    def __format__(self, format_spec = "") -> str:

        if "L" in format_spec or "l" in format_spec:
            return str(self)

        return super(self).__format__(format_spec)
