# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a country.

# --- Imports --- #

from typing import override
from .divisions import Division, DivisionTypes

__all__ = ("Country",)


# --- Country Class --- #

class Country(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Division] | Division = None,
                 *,
                 population: int = None,
                 prefix: str = "",
                 **kwargs):

        super().__init__(name, DivisionTypes.COUNTRY, subdivisions,
                         population = population, **kwargs)

        if prefix != "":
            self.prefix = prefix

    @override
    def __format__(self, format_spec = ""):

        if "F" in format_spec or "O" in format_spec:
            if hasattr(self, "government"):
                if hasattr(self, "prefix"):
                    return f"The {self.prefix} {self.government.leader.policy} of {self.name}"
                return f"The {self.government.leader.policy} of {self.name}"

        return str(self)
