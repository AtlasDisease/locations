# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a state.

# A State is a complicated idea due to the different meanings
# in different areas of the world. They are most usually treated
# more like their own countries than something like a County,
# Parish, Shire.

# --- Imports --- #

from .divisions import Division
from .independentcities import IndependentCity, AdministrativeTypes

__all__ = ("State",)


# --- State Class --- #

class State(Division):
    @property
    def capital(self):
        def recurse(division: Division):
            if hasattr(division, "admin_type"):
                if division.admin_type == AdministrativeTypes.CAPITAL:
                    return division
                return
            
            for item in division:
                if hasattr(item, "admin_type"):
                    if item.admin_type == AdministrativeTypes.CAPITAL:
                        return item
                    continue

                result = recurse(item)
                if result is not None:
                    return result

        return recurse(self)
