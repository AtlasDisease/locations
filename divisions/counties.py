# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a County, Parish, Shire, and Oblast.

# --- Imports --- #

from typing import Callable, Self, Type, Iterable
from .divisions import Division
from .cities import City, AdministrativeTypes

__all__ = ("County", "Parish", "Shire", "Oblast")


# --- SeatError --- #

class SeatError(ValueError):
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
    def seats(self) -> Iterable[Division]:
        #Some places have 2 county seats, EX. Lee County, Iowa
        return tuple(
            filter(lambda div: AdministrativeTypes.SEAT in div.admin_type,
                      self.subdivisions))

    @seats.setter
    def seats(self, city: Division):
        """Gets the seat(s) for the county"""
        if city not in self._subdivisions:
            raise SeatError("You cannot give county seat to a city not in the county.")

        idx = self._subdivisions.index(city)
        #Swap
        self._subdivisions[idx].admin_type, self.seat.admin_type = self.seat.admin_type, self._subdivisions[idx].admin_type
        self._subdivisions.sort(key=lambda city: city.admin_type, reverse=True)


class Parish(County): #French version of a County
    pass


class Shire(County): #English (UK) version of a County
    pass


class Oblast(County): #Russian version of County
    pass
