# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a country.

# --- Imports --- #

from typing import override, Self
from .divisions import Division
from .cities import City, AdministrativeTypes

__all__ = ("Country",)


# --- NonCityError Class --- #

class NonCityError(TypeError):
    pass


# --- NonCapitalError Class --- #

class NonCapitalError(ValueError):
    pass


# --- Country Class --- #

class Country(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Division] | Division = None,
##                 capitals: list[City] = None,
                 *,
                 population: int = None,
                 prefix: str = "",
                 **kwargs):

        super().__init__(name, subdivisions, population = population, **kwargs)

        if prefix:
            self.prefix = prefix
        
##        if capitals:
##            if any((not hasattr(city, "admin_type") for city in capitals)):
##                raise NonCityError("Capitals should have an admin type attribute.")
##            if any((AdministrativeTypes.CAPITAL not in city._admin_type for city in capitals)):
##                raise NonCapitalError("Capitals should have the admin type of CAPITAL.")
##        else:
##            capitals = list(self._find_capitals())
##
##        self._capitals = capitals
        self._capitals = list(self._find_capitals())
##        if any((AdministrativeTypes.CAPITAL not in city._admin_type for city in self._capitals)):
##            raise NonCapitalError("Capitals should have the admin type of CAPITAL.")

    @override
    def __format__(self, format_spec = ""):
        if "F" in format_spec or "O" in format_spec:
            if hasattr(self, "government"):
                if hasattr(self, "prefix"):
                    return f"The {self.prefix} {self.government.leader.policy} of {self.name}"
                return f"The {self.government.leader.policy} of {self.name}"

        return str(self)

    @property
    def capitals(self):
        """Gets the capital(s) for the country"""
        return self._capitals

    @capitals.setter
    def capitals(self, new_capital: Self):
        #This needs some work to determine whether it should turn into a
        #county seat or a regular city
        self._capitals[0].admin_type, new_capital.admin_type = \
                                       new_capital.admin_type, self.capitals[0].admin_type
        del self._capitals[0]
        self._capitals.insert(new_capital, 0)

    def add_capital(self, new_capital):
        if new_capital in self._capitals:
            return

        self._capitals.append(new_capital)

    def remove_capital(self, capital: str):
        def get_capital(iterable, capital: str):
            for city in iterable:
                if city.name != capital:
                    continue
                return city

        old_capital = get_capital(self.subdivisions, capital)
        admin_type = AdministrativeTypes.SEAT if AdministrativeTypes.SEAT in old_capital else AdministrativeTypes.CITY
        old_capital.set_admin_type(admin_type)
        self.capitals.remove(old_capital)

    def _find_capitals(self):
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
