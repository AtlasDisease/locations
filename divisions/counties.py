# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a County, Parish, Shire, and Oblast.

# --- Imports --- #

from typing import Callable, Self, Type
from .divisions import Division
from .cities import AdministrativeTypes

__all__ = ("County", "Parish", "Shire", "Oblast")


# --- SeatError --- #

class SeatError(IndexError):
    pass
        

# --- County Class --- #

class County(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Type[Division]] = None,
                 *,
                 population: Type[int] = None,
                 **kwargs):

        if subdivisions:
            subdivisions.sort(key=lambda city: city.admin_type, reverse=True)
        
        super().__init__(name, subdivisions, **kwargs)

    @property
    def seat(self) -> Division:
        if self._subdivisions[1]._admin_type == AdministrativeTypes.SEAT:
            return self._subdivisions[1] #Rare instance in which the county seat is not the Capital, ex. Michigan.
        return self._subdivisions[0]

    @seat.setter
    def seat(self, city: Division):
        if city not in self._subdivisions:
            raise SeatError("You cannot give county seat to a city not in the county.")

        idx = self._subdivisions.index(city)
        self._subdivisions[idx].admin_type = self.seat.admin_type
        self.seat.admin_type = AdministrativeTypes.NONE

        self._subdivisions.sort(key=lambda city: city.admin_type, reverse=True)


class Parish(County): #French version of a County
    pass


class Shire(County): #English (UK) version of a County
    pass


class Oblast(County): #Russian version of County
    pass
