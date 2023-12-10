# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Population class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from ..divisions import Division
from .extensions import errorcheck

__all__ = ("Population", "add_population")


# --- Population Class --- #

class Population(int):
    """Basically an integer but with formatting when converted to string
and some additional functions to help with comparisons"""

    def __str__(self) -> str:
        return f"{self: ,}"   

    @staticmethod
    @errorcheck
    def largest(division: Division) -> Division:
        return max(division, key = lambda x: x.population)

    @staticmethod
    @errorcheck
    def smallest(division: Division) -> Division:
        return min(division, key = lambda x: x.population)


# --- Extending Functionality Definitions --- #

def add_population(cls, population: int) -> None:
    cls.population = population
