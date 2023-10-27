# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle an area where humans have a population.
# To create your own you can subclass the City or Division class.

# --- Imports --- #

from enum import IntEnum, auto
from .divisions import Division, DivisionTypes


# --- CityTypes Enum --- #

class CityTypes(IntEnum):
    LOST = auto() #This is incredibly rare
    SITE = auto()
    COMMUNITY = auto()
    CITY = auto()

    def __str__(self):
        return self.name.title()


# --- AdministrativeTypes Enum --- #

class AdministrativeTypes(IntEnum):
    NONE = auto()
    SEAT = auto()
    CAPITAL = auto()

    def __str__(self):
        if (self == AdministrativeTypes.SEAT):
            return f"County {self.name.title()}"
        return self.name.title()


# --- City Class --- #

class City(Division):
    def __init__(self, name: str, citytype: CityTypes, admintype: AdministrativeTypes, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, DivisionTypes.CITY, population, subdivisions)
        self.city_type = citytype
        self.admin_type = admintype

    def __str__(self):
        if (self.admin_type != AdministrativeTypes.NONE):
            return f"The {self.admin_type} of {self.name}"
        return f"The {self.city_type} of {self.name}"
