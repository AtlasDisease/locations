# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a state.

# A State is a complicated idea due to the different meanings
# in different areas of the world. They are most usually treated
# more like their own countries than something like a County,
# Parish, Shire.

# --- Imports --- #

from .divisions import Division
from .cities import City
from .independentcities import IndependentCity, AdministrativeTypes

__all__ = ("State",)


# --- NonCityError Class --- #

class NonCityError(TypeError):
    pass


# --- NonCapitalError Class --- #

class NonCapitalError(ValueError):
    pass


# --- State Class --- #

class State(Division):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Division] | Division = None,
                 capitals: list[City] = None,
                 *,
                 population: int = None,
                 **kwargs):

        super().__init__(name, subdivisions, population = population, **kwargs)

        if capitals:
            if any((not hasattr(city, "admin_type") for city in capitals)):
                raise NonCityError("Capitals should have an admin type attribute.")
            if any((AdministrativeTypes.CAPITAL not in city._admin_type for city in capitals)):
                raise NonCapitalError("Capitals should have the admin type of CAPITAL.")
        else:
            capitals = list(self._find_capitals())

        self._capitals = capitals 

    @property
    def capitals(self):
        """Gets the capital(s) for the country"""
        return self._capitals

    @capitals.setter
    def capitals(self, new_capital):
        #This needs some work to determine whether it should turn into a
        #county seat or a regular city
        self._capitals[0]._admin_type, new_capital._admin_type = \
                                       new_capital._admin_type, self._capitals[0]._admin_type
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
        if AdministrativeTypes.SEAT in old_capital:    
            old_capital.set_admin_type(AdministrativeTypes.SEAT)
        else:
            old_capital.set_admin_type(AdministrativeTypes.CITY)
        self.capitals.remove(old_capital)
        
    def _find_capitals(self):
        """Recurses into subdivisions to find any cities with admin type of CAPITAL."""
        cities = []

        def recurse(division: Division):
            for city in division:
##                print(city)
                if not hasattr(city, "admin_type"):
                    return recurse(city)
                    continue
                
                cities.append(city)
            return cities

        return filter(
            lambda city: AdministrativeTypes.CAPITAL in city.admin_type,
            recurse(self))
