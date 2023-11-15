# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an area where humans have a population.
# To create your own you can subclass the City or Division class.

# --- Imports --- #

from typing import Self
from enum import IntEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("CityTypes", "AdministrativeTypes", "City")


# --- CityTypes Enum --- #

class CityTypes(IntEnum):
    UNKNOWN = auto() #General use
    LOST = auto() #This is incredibly rare
    SITE = auto()
    COMMUNITY = auto()
    TOWN = auto() #No real definition, user decision, incorporated
    CITY = auto()

    def __str__(self) -> str:
        return self.name.title()

    def __add__(self, other) -> Self:
        if isinstance(other, int):
            other %= len(CityTypes)
            if other == 0:
                other = 3
            other = CityTypes(other)

        other = self.value + other.value
        if other > len(CityTypes):
            other %= len(CityTypes)
            if other == 0:
                other = 3
            
        return CityTypes(other)

    def __iadd__(self, other) -> Self:
        self = self + other
        return self


# --- AdministrativeTypes Enum --- #

class AdministrativeTypes(IntEnum):
    NONE = auto()
    SEAT = auto()
    CAPITAL = auto()

    def __str__(self) -> str:
        if self == AdministrativeTypes.SEAT:
            return f"County {self.name.title()}"
        return self.name.title()

    def __add__(self, other) -> Self:
        if isinstance(other, int):
            other %= len(AdministrativeTypes)
            if other == 0:
                other = 3
            other = AdministrativeTypes(other)

        other = self.value + other.value
        if other > len(AdministrativeTypes):
            other %= len(AdministrativeTypes)
            if other == 0:
                other = 3
            
        return AdministrativeTypes(other)

    def __iadd__(self, other) -> Self:
        self = self + other
        return self


# --- City Class --- #

class City(Division):
    def __init__(self, name: str, citytype: CityTypes, admintype: AdministrativeTypes,
                 /,
                 subdivisions: list[Division] | Division = None,
                 *,
                 population: int = None,
                 **kwargs):

        super().__init__(name, DivisionTypes.CITY, subdivisions,
                         population = population, **kwargs)
        self.city_type = citytype
        self.admin_type = admintype

    def __format__(self, format_spec = "") -> str:

        if "F" in format_spec or "O" in format_spec:
            if self.admin_type != AdministrativeTypes.NONE:
                return f"The {self.admin_type} of {self.name}"
            return f"The {self.city_type} of {self.name}"

        return str(self)

    @property
    def incorporated(self) -> bool:
        return self.city_type >= CityTypes.TOWN

    @property
    def abandoned(self)-> bool:
        return self.city_type < CityTypes.COMMUNITY and self.city_type != CityTypes.UNKNOWN

    @property
    def historical(self) -> bool:
        return self.city_type == CityTypes.SITE
