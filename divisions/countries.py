# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a country.

# --- Imports --- #

from typing import override, Self, Iterable, Type
from itertools import chain

from .divisions import Division
from .cities import City, AdministrativeTypes
from .counties import County

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
        return list(self._find_capitals(self))

    def add_city(city: City, county: County) -> None:
        if county not in self:
            raise IndexError("{county.name} must be in the country.")
        if any((div.name == city.name for div in self)):
            raise DivisionNameError(f"{city.name} is already in the county.")
        if isinstance(city, City):
            if city.admin_type == AdministrativeTypes.CAPITAL:
                if len(self.seats) + 1 > self._max_capital_num:
                    raise ValueError("Adding this capital would overflow the maximum number of capitals.")

        self._subdivisions.append(city)
        
    def add_county(county: Division) -> None:
        """Adds a county to the country."""
        if any((div.name == county.name for div in self)):
            raise DivisionNameError(f"{county.name} is already in the country.")

        self._subdivisions.append(county)

    def remove_county(self, county: Division) -> None:
        """Removes a county from the country"""
        if county not in self._subdivisions:
            raise ValueError("{county} is not in the country.")
        
        self._subdivisions.remove(city)

    def _get_cities(self, subdivisions: list[Division]):
        """Get all cities from subdivisions (flattened)"""
        def get_cities(subdivision) -> list[Division]:
            if isinstance(subdivision, City):
                return [subdivision]
            elif isinstance(subdivision, County):
                return list(chain.from_iterable(get_cities(sub) for sub in subdivision.subdivisions))
            return []
        
        return chain.from_iterable(get_cities(sub) for sub in subdivisions)

    def _find_capitals(self, subdivision: list[Division]):
        """Find all capitals"""
        return filter(lambda city: AdministrativeTypes.CAPITAL in city.admin_type,
                          self._get_cities(subdivision))
    
    def _count_capitals_in_subdivision(self, subdivision: list[Division]):
        """Count capitals in a specific subdivision"""
        return len(self._find_capitals(subdivision))
