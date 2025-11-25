# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a County, Parish, Shire, Oblast, and Borough.

# --- Imports --- #

from typing import Callable, Self, Type, Iterable
from .divisions import Division, DivisionNameError
from .cities import City, AdministrativeTypes

__all__ = ("County", "Parish", "Shire", "Oblast", "Borough")


# --- SeatError --- #

class SeatError(ValueError):
    pass


# --- County Class --- #

class County(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Type[Division]] = None,
                 max_seat_num: int = 1,
                 *,
                 population: Type[int] = None,
                 **kwargs):

##        if subdivisions:
##            subdivisions.sort(key=lambda city: city.admin_type, reverse=True)
        
        super().__init__(name, subdivisions, **kwargs)

        self._max_seat_num = max_seat_num

        if len(self.seats) > self._max_seat_num:
            raise OverflowError("There are more seats tha the maximum number of county seats.")

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
            filter(lambda div: AdministrativeTypes.SEAT in div.admin_type,
                      self.subdivisions))

    def add_city(self, city: Division):
        """Adds a city to the county.
If city is of type City and is a county seat the function will check to make sure it does not overflow the maximum number of seats"""
        if any((div.name == city.name for div in self)):
            raise DivisionNameError(f"{city.name} is already in the county.")
        if isinstance(city, City):
            if city.admin_type == AdministrativeTypes.SEAT:
                if len(self.seats) + 1 > self._max_seat_num:
                    raise ValueError("Adding this county seat would overflow the maximum number of county seats.")

        self._subdivisions.append(city)

    def remove_city(self, city: Division):
        """Removes a city from the county"""
        if city not in self._subdivisions:
            raise ValueError("{city} is not in the county.")
        self._subdivisions.remove(city)

    def move_seat(self, old_seat: City, new_seat: City):
        """Moves a county seat from old_seat to the new_seat"""
        if old_seat not in self._subdivisions:
            raise ValueError("{old_seat} is not in the county.")
        old_idx = self._subdivisions.index(old_seat)
        
        if new_seat not in self._subdivisions:
            raise SeatError("{new_seat} must be in the county.")
        new_idx = self._subdivisions.index(new_seat)
        
        self._subdivisions[new_idx].admin_type = AdministrativeTypes.SEAT
        self._subdivisions[old_idx].admin_type = AdministrativeTypes.NONE
##        self._subdivisions.sort(key=lambda city: city.admin_type, reverse=True)


class Parish(County): #French version of a County
    pass


class Shire(County): #English (UK) version of a County
    pass


class Oblast(County): #Russian version of County
    pass


class Borough(County): #Alaskan version of County
    pass
