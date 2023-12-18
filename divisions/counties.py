# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a County, Parish, Shire, and Oblast.

# --- Imports --- #

from .divisions import Division
from .cities import AdministrativeTypes

__all__ = ("County", "Parish", "Shire", "Oblast")
        

# --- County Class --- #

class County(Division):
    def seat(self) -> Division:
        """Gets the county seat; this is a function (instead of a property)
to imply there is a cost to this function"""

        return next(filter(lambda x: x.admin_type == AdministrativeTypes.SEAT,
                           self.subdivisions), None)


class Parish(County): #French version of a County
    pass


class Shire(County): #English (UK) version of a County
    pass


class Oblast(County): #Russian version of County
    pass
