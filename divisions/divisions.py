# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a division.

# --- Imports --- #

from typing import Self, override, Type

from ..subdivisions import DivisionBase
from .extensions.population import add_population
from .extensions.area import add_area
from .extensions.elevation import add_elevation

__all__ = ("Division",)


# --- DivisionNameError ---#

class DivisionNameError(ValueError):
    pass


# --- Division Class --- #

class Division(DivisionBase):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Type[Self]] = None,
                 *,
                 population: Type[int | float] = None,
                 area: Type[int | float] = None,
                 elevation: Type[int | float] = None,
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

    @property
    def subdivisions(self) -> list[Self]:
        return self._subdivisions
