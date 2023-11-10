# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Population class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from typing import Callable
from ..divisions import Division
from .extenders import Extender, errorcheck

__all__ = ("Population", "add_population")


# --- Population Class --- #

class Population(int, Extender):
    """Basically an integer but with formatting when converted to string
and some additional functions to help with comparisons"""

    def __str__(self) -> str:
        return f"{self: ,}"   

    @staticmethod
    @errorcheck
    def largest(division: Division) -> Division:
        return Population._get(division, \
                                lambda x, y: x.population <= y.population)
    
    @staticmethod
    @errorcheck
    def smallest(division: Division) -> Division:
        return Population._get(division, \
                                lambda x, y: x.population >= y.population)


# --- Extending Functionality Definitions --- #

def add_population(cls, population: int) -> None:
    cls.population = population
