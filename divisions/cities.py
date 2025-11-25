# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an area where humans have a population.
# To create your own you can subclass the City or Division class.

# --- Imports --- #

from typing import Self, override
from enum import verify, UNIQUE#, IntFlag, CONFORM

from ..enum import UpgradableEnum, UpgradableFlag, auto
from .divisions import Division

__all__ = ("CityTypes", "AdministrativeTypes", "City")


# --- CityTypes Enum --- #

@verify(UNIQUE)
class CityTypes(UpgradableEnum): #Upgradable
    UNKNOWN = auto() #General use
    LOST = auto() #Incredibly rare; no known location, no historical info (ex. Nanhattie, Coke County, TX)
    SITE = auto() # AKA Ghost Town
    COMMUNITY = auto() #Unincorporated
    TOWN = auto() #No real definition but incorporated, user decision
    CITY = auto() #Incorporated


# --- AdministrativeTypes Enum --- #

@verify(UNIQUE)
class AdministrativeTypes(UpgradableFlag): #Upgradable
    NONE = 0
    SEAT = auto()
    CAPITAL = auto()

    def __str__(self) -> str:
        if self == AdministrativeTypes.SEAT:
            return f"County {self.name.title()}"
        return self.name.title()


# --- City Class --- #

class City(Division):
    """A city object based on a realistic city.

If the city is independent (not in a county), then this should be added to the Country object."""

##    most_importance = staticmethod(partial(Division.most_by, attribute = "importance"))
##    least_importance = staticmethod(partial(Division.least_by, attribute = "importance"))
    
    def __init__(self,
                 name: str,
                 type_: CityTypes,
                 /,
                 admintype: AdministrativeTypes = AdministrativeTypes.NONE,
                 subdivisions: list[Division] = None,
                 *,
                 population: int = None,
##                 description: str = "",
                 **kwargs) -> Self:

        super().__init__(name, subdivisions,
                         population = population, **kwargs)

        if admintype > AdministrativeTypes.NONE \
        and type_ != CityTypes.CITY: #Make sure our political importance works correctly
            raise ValueError("The type of {self.type} and administrative type of {self.admin_type} do not match up.")

        self.type = type_
        self._admin_type = admintype #DO NOT CHANGE MANUALLY
        
##        if description:
##            self._description = description

    @override
    def __format__(self, format_spec = "") -> str:

        if "F" in format_spec or "O" in format_spec:
            if self._admin_type != AdministrativeTypes.NONE:
                if '-' in format_spec:
                    return f"The {min(self.admin_type)} of {self.name}"
                return f"The {max(self.admin_type)} of {self.name}"        
            return f"The {self.type} of {self.name}"
##        elif "D" in format_spec or "d" in format_spec:
##            if not hasattr(self, "_description"):
##                return ""
##            return self._description

        return str(self)

    #Comparisons are subject to change.
    #Discourage use of them for production. -Brendan
##    def __eq__(self, other: Self) -> bool:
##        if type(self) != type(other):
##            return False
##        
##        return self.type == other.type \
##               and self._admin_type == other._admin_type
##
##    def __gt__(self, other: Self) -> bool:
##        if type(self) != type(other):
##            return False
##        
##        return self.type >= other.type \
##               and self._admin_type > other._admin_type
##
##    def __lt__(self, other: Self) -> bool:
##        if type(self) != type(other):
##            return False
##        
##        return self.type <= other.type \
##               and self._admin_type < other._admin_type
##
    @property
    def admin_type(self) -> AdministrativeTypes:
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admintype: AdministrativeTypes):
        self._admin_type = admintype

    def __eq__(self, other: Self) -> bool:
        if type(self) != type(other):
            return False
        
        return self.type == other.type

    def __gt__(self, other: Self) -> bool:
        if type(self) != type(other):
            return False
        
        return self.type >= other.type

    def __lt__(self, other: Self) -> bool:
        if type(self) != type(other):
            return False
        
        return self.type <= other.type

    @property
    def incorporated(self) -> bool:
        return self.type >= CityTypes.TOWN

    @property
    def abandoned(self)-> bool:
        return self.type < CityTypes.COMMUNITY \
               and self.type != CityTypes.UNKNOWN

    @property
    def historical(self) -> bool:
        return self.type == CityTypes.SITE

##    @property
##    def importance(self) -> int:
##        """Returns the importance of the city.
##This is mostly for debugging if there is an issue with the comparison functions."""
##        return self._admin_type.value + self.type.value
##
##    @property
##    def political_importance(self) -> int:
##        return self._admin_type.value
    
