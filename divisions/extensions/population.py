# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Population class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from typing import Callable
from ..divisions import Division, DivisionTypes

__all__ = ("Population", "add_population")


# --- Population Class --- #

class Population(int):
    """Basically an integer but with formatting when converted to string
and some additional functions to help with comparisons"""
    
    def __init__(self, population: int = 0):

        super().__init__()

    def __str__(self) -> str:
        return f"{self: ,}"   

    @staticmethod
    def __errorcheck(func):
        def inner1(*args, **kwargs):

            division = args[0]
            if any((not hasattr(x, "population") for x in division.subdivisions)):
                raise NotImplementedError("Subdivisions are required to have a population variable in order to use this function.")
        
            if len(division.subdivisions) <= 0:
                return Division("New", DivisionTypes.AREA, population = 0)

            return func(*args, **kwargs)
        
        return inner1

    @staticmethod
    def __get(division: Division, func: Callable) -> Division:
        result = division.subdivisions[0]
    
        for subdivision in division.subdivisions:
            if func(subdivision, result):
                continue
        
            result = subdivision

        return result

    @staticmethod
    @__errorcheck
    def largest(division: Division) -> Division:
        return Population.__get(division, \
                                lambda x, y: x.population <= y.population)
    
    @staticmethod
    @__errorcheck
    def smallest(division: Division) -> Division:
        return Population.__get(division, \
                                lambda x, y: x.population >= y.population)


# --- Extending Functionality Definitions --- #

def add_population(cls, population: int) -> None:
    cls.population = population
