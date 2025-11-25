# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a state.

# A State is a complicated idea due to the different meanings
# in different areas of the world. They are most usually treated
# more like their own countries than something like a County,
# Parish, Shire.

# --- Imports --- #

from typing import Type, Iterable, override
from itertools import chain

from .divisions import Division
from .cities import City, AdministrativeTypes
from .counties import County

__all__ = ("State",)


# --- State Class --- #

class State(Division): #Very similar to a Country
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Type[Division]] = None,
                 max_capital_num: int = 1,
                 *,
                 population: int = None,
                 **kwargs):

        super().__init__(name, subdivisions, population = population, **kwargs)

        self._max_capital_num = max_capital_num

    @override
    def __format__(self, format_spec = ""):
        if "F" in format_spec or "O" in format_spec:
            if hasattr(self, "government"):
                if hasattr(self, "prefix"):
                    return f"The {self.prefix} {self.government.leader.policy} of {self.name}"
                return f"The {self.government.leader.policy} of {self.name}"

        return str(self)

    @property
    def capital(self) -> Division:
        """Get the first capital, do not use this if there could be more than 1 capital. This does not decide the most important capital."""
        return self.capitals[0] if self.capitals else None

    @property
    def capitals(self) -> Iterable[Division]:
        """Gets the capital(s) for the country"""
        return list(self._find_capitals(self))

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
