# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an area where humans have a population.
# To create your own you can subclass the City or Division class.

# --- Imports --- #

from typing import Self, override
from ..enum import UpgradableEnum, auto
from .divisions import Division

__all__ = ("CityTypes", "AdministrativeTypes", "City")


# --- CityTypes Enum --- #

class CityTypes(UpgradableEnum): #Upgradable
    UNKNOWN = auto() #General use
    LOST = auto() #This is incredibly rare
    SITE = auto()
    COMMUNITY = auto()
    TOWN = auto() #No real definition but incorporated, user decision
    CITY = auto()


# --- AdministrativeTypes Enum --- #

class AdministrativeTypes(UpgradableEnum): #Upgradable
    NONE = auto()
    SEAT = auto()
    CAPITAL = auto()

    def __str__(self) -> str:
        if self == AdministrativeTypes.SEAT:
            return f"County {self.name.title()}"
        return super(self).__str__()


# --- City Class --- #

class City(Division):
    def __init__(self,
                 name: str,
                 type_: CityTypes,
                 admintype: AdministrativeTypes,
                 /,
                 subdivisions: list[Division] = None,
                 *,
                 population: int = None,
                 **kwargs) -> Self:

        super().__init__(name, subdivisions,
                         population = population, **kwargs)

        if admintype > AdministrativeTypes.NONE \
        and type_ != CityTypes.CITY: #Make sure our political importance works correctly
            raise ValueError("The type of {self.type} and administrative type of {self.admin_type} do not match up.")

        self.type = type_
        self.admin_type = admintype

    @override
    def __format__(self, format_spec = "") -> str:

        if "F" in format_spec or "O" in format_spec:
            if self.admin_type != AdministrativeTypes.NONE:
                return f"The {self.admin_type} of {self.name}"
            return f"The {self.city_type} of {self.name}"

        return str(self)

    def __eq__(self, other: Self) -> bool:
        return self.type == other.type \
               and self.admin_type == other.admin_type

    def __gt__(self, other: Self) -> bool:
        return self.type >= other.type \
               and self.admin_type > other.admin_type

    def __lt__(self, other: Self) -> bool:
        return self.type <= other.type \
               and self.admin_type < other.admin_type

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

    @property
    def importance(self) -> int:
        """Returns the importance of the city.
This is mostly for debugging if there is an issue with most_importance or least_importance functions."""
        return self.admin_type.value + self.type.value

    @staticmethod
    def most_importance(division: Division) -> Self:
        """Importance is determined by the administrative type and the city type values combined
FIXME: Good for now, but hacky (and slightly unreliable) way to do this. This one should always be correct
unlike least_importance."""
        return max(division, key = lambda x: x.importance)

    @staticmethod
    def least_importance(division: Division) -> Self:
        """Importance is determined by the administrative type and the city type values combined
FIXME: Good for now, but hacky (and slightly unreliable) way to do this"""
        return min(division, key = lambda x: x.importance)
