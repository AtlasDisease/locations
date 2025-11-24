# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a country.

# --- Imports --- #

from typing import override, Self, Iterable, Type
from .divisions import Division
from .cities import City, AdministrativeTypes

__all__ = ("Country",)


# --- Country Class --- #

class Country(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Type[Division]] = None,
                 max_capital_num: int = 1,
                 *,
                 population: int = None,
                 prefix: str = "",
                 **kwargs):

        super().__init__(name, subdivisions, population = population, **kwargs)
        
        self._max_capital_num = max_capital_num
        if prefix:
            self.prefix = prefix

    @override
    def __format__(self, format_spec = ""):
        if "F" in format_spec or "O" in format_spec:
            if hasattr(self, "government"):
                if hasattr(self, "prefix"):
                    return f"The {self.prefix} {self.government.leader.policy} of {self.name}"
                return f"The {self.government.leader.policy} of {self.name}"

        return str(self)

    @property
    def organized(self) -> bool:
        return bool(self.capitals)

    @property
    def capital(self) -> Division:
        """Get the first capital, do not use this if there could be more than 1 capital. This does not decide the most important capital."""
        return self.capitals[0] if self.capitals else None

    @property
    def capitals(self) -> Iterable[Division]:
        """Gets the capital(s) for the country"""
        return list(self.__find_capitals())

    def add_county(county: Division):
        """Adds a county to the country."""
        if any((div.name == county.name for div in self)):
            raise DivisionNameError(f"{county.name} is already in the country.")

        self._subdivisions.append(county)

    def remove_county(self, county: Division):
        """Removes a county from the country"""
        if county not in self._subdivisions:
            raise ValueError("{county} is not in the country.")
        self._subdivisions.remove(city)

##    def move_capital(self, old_capital: City, new_capital: City):
##        """Moves a capital from old_capital to the new_capital"""
##        if old_capital not in self._subdivisions:
##            raise ValueError("{old_capital} is not in the county.")
##        old_idx = self._subdivisions.index(old_seat)
##        
##        if new_seat not in self._subdivisions:
##            raise SeatError("{new_seat} must be in the county.")
##        new_idx = self._subdivisions.index(new_seat)
##        
##        self._subdivisions[new_idx].admin_type = AdministrativeTypes.CAPITAL
##        self._subdivisions[old_idx].admin_type = AdministrativeTypes.SEAT

    def __find_capitals(self):
        """Recurses into subdivisions to find any cities with admin type of CAPITAL"""
        cities = []

        def recurse(division: Division):
            for city in division:
                if not hasattr(city, "admin_type"):
                    recurse(city)
                    continue
                
                cities.append(city)
            return cities

        return filter(
            lambda city: AdministrativeTypes.CAPITAL in city.admin_type,
            recurse(self))
