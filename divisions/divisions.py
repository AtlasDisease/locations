# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a division.

# --- Imports --- #

from typing import Self, override, Type
##from functools import total_ordering
from ..subdivisions import DivisionBase
from .extensions.population import add_population
from .extensions.area import add_area
from .extensions.elevation import add_elevation

__all__ = ("Division",)


# --- Division Class --- #

class Division(DivisionBase):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Self] = None,
                 *,
                 population: Type[int] = None,
                 area: Type[int] = None,
                 elevation: Type[int] = None,
                 **kwargs):

        super().__init__(name, subdivisions)

        if population is not None:
            add_population(self, population)

        if area is not None:
            add_area(self, area)

        if elevation is not None:
            add_elevation(self, elevation)

        #I do not like this as it ties districts and politics together a bit
        # Also doing this to avoid having to import the Administrator
        # and Government types from the politics package
        if "administrator" in kwargs and "government" in kwargs:
            if kwargs["administrator"] and kwargs["government"]:
                raise Exception("You cannot have both government and administrator populated")

            if kwargs["administrator"]:
                self.administrator = kwargs["administrator"]
            if kwargs["government"]:
                self.government = kwargs["government"]

        # Add available extensions or extra arguments
        self.__dict__ |= kwargs

##    def add_subdivision(self, division: Self):
##        self._subdivisions.append(division)
##        self._subdivisions.sort()

##    def __lt__(self, other: Self)  -> bool:
##        return False #_IMPORTANCE.index(self.__class__) < _IMPORTANCE.index(other.__class__)
##
##    def __eq__(self, other: Self)  -> bool:
##        return False #_IMPORTANCE.index(self.__class__) == _IMPORTANCE.index(other.__class__)
##
##    def __gt__(self, other: Self) -> bool:
##        return _IMPORTANCE.index(self.__class__) < _IMPORTANCE.index(other.__class__)
