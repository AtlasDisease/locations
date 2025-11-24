# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a County, Parish, Shire, and Oblast.

# --- Imports --- #

from typing import Callable, Self, Type, Iterable
from .divisions import Division, DivisionNameError
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
                 max_seat_num: int = 1,
                 **kwargs):

##        if subdivisions:
##            subdivisions.sort(key=lambda city: city.admin_type, reverse=True)
        
        super().__init__(name, subdivisions, **kwargs)

        self._max_seat_num = max_seat_num

    @property
    def organized(self) -> bool:
        return bool(self.seats)

    @property
    def seat(self) -> Division | None:
        """Get the first seat, do not use this if there could be more than 1 county seat. This does not decide the most important seat."""
        return self.seats[0] if self.seats else None

    @property
    def seats(self) -> Iterable[Division]:
        """Gets all county seats.

Some places have 2 county seats, EX. Lee County, Iowa"""
        return tuple(
            filter(lambda div: AdministrativeTypes.EAT in div.admin_type,
                      self.subdivisions))

    def add_city(self, city: Division):
        if any((div.name == city.name for div in self)):
            raise DivisionNameError(f"{city.name} is already in the county.")

        self._subdivisions.append(city)

##    @seats.setter
##    def seats(self, city: Division):
##        """Gets the seat(s) for the county"""
##        if city not in self._subdivisions:
##            raise SeatError("You cannot give county seat to a city not in the county.")
##
##        idx = self._subdivisions.index(city)
##        #Swap
##        self._subdivisions[idx].admin_type, self.seat.admin_type = self.seat.admin_type, self._subdivisions[idx].admin_type
##        self._subdivisions.sort(key=lambda city: city.admin_type, reverse=True)


class Parish(County): #French version of a County
    pass


class Shire(County): #English (UK) version of a County
    pass


class Oblast(County): #Russian version of County
    pass


class Borough(County): #Alaskan version of County
    pass
