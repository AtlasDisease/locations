# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a County, Parish, and Shire.

# --- Imports --- #

from dataclasses import dataclass
from .divisions import Division, DivisionTypes
from .cities import AdministrativeTypes

__all__ = ("County", "Parish", "Shire")
        

# --- County Class --- #

@dataclass(init = False)
class County(Division):
    def __post_init__(self):
        
        self.type_ = DivisionTypes.COUNTY

    def seat(self) -> Division:
        """Gets the county seat; this is a function (instead of a property)
to imply there is a cost to this function"""

        return next(filter(lambda x: x.admin_type == AdministrativeTypes.SEAT,
                           self.subdivisions), None)


class Parish(County): #French version of a County
    pass


class Shire(County): #English version of a County
    pass
