# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a planet.

# --- Imports --- #

from .divisions import Division, DivisionTypes

__all__ = ("Planet",)


# --- Planet Class --- #

class Planet(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Division] | Division = None,
                 *,
                 population: int = None,     
                 **kwargs):

        super().__init__(name, DivisionTypes.PLANET, subdivisions,
                         population = population, **kwargs)

    def __format__(self, format_spec = "") -> str:

        if "L" in format_spec or "l" in format_spec:
            return str(self)

        return Division.__format__(self, format_spec)
