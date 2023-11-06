# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a country.

# --- Imports --- #

from .divisions import Division, DivisionTypes


# --- Country Class --- #

class Country(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,
                 prefix: str = "",
                 **kwargs):

        super().__init__(name, DivisionTypes.COUNTRY, subdivisions,
                         population, **kwargs)

        if prefix != "":
            self.prefix = prefix

    def __format__(self, format_spec = ""):

        if "F" in format_spec or "O" in format_spec:
            if hasattr(self, "government"):
                if hasattr(self, "prefix"):
                    return f"The {self.prefix} {self.government.leader.policy} of {self.name}"
                return f"The {self.government.leader.policy} of {self.name}"

        return str(self)
