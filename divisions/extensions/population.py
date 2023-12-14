# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Population class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from dataclasses import dataclass
from .extensions import errorcheck
from ...subdivisions import Divisible

__all__ = ("Population", "add_population")


# --- Population Class --- #

class Population(int):
    """Basically an integer but with formatting when converted to string
and some additional functions to help with comparisons"""

    def __str__(self) -> str:
        return f"{self: ,}"   

    @staticmethod
    @errorcheck
    def largest(division: Divisible) -> Divisible:
        return max(division, key = lambda x: x._population)

    @staticmethod
    @errorcheck
    def smallest(division: Divisible) -> Divisible:
        return min(division, key = lambda x: x._population)


# --- Population Functions --- #

def _get_population(self):
    return self._population

def _set_population(self, population: int):
    self._population = population

def add_population(self, population: int) -> None:
    self._population = population
    self.__class__.population = property(_get_population, _set_population)
