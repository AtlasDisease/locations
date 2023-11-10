# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a County, Parish, and Shire.

# --- Imports --- #

from .divisions import Division, DivisionTypes
from .cities import AdministrativeTypes

__all__ = ("County", "Parish", "Shire")
        

# --- County Class --- #

class County(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Division] | Division = None,
                 *,
                 population: int = None,   
                 **kwargs):

        super().__init__(name, DivisionTypes.COUNTY, subdivisions,
                         population = population, **kwargs)

    def seat(self) -> Division:
        """Gets the county seat; this is a function (instead of a property)
to imply there is a cost to this function"""

        return next(filter(lambda x: x.admin_type == AdministrativeTypes.SEAT,
                           self.subdivisions), None)


class Parish(County): #French version of a County
    pass


class Shire(County): #English version of a County
    pass
