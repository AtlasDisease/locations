# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Area class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from typing import Callable
from ..divisions import Division
from .extensions import errorcheck

__all__ = ("Area", "Kilometers", "Miles", \
    "kilometers", "miles", "add_area")


# --- Area Class --- #

class Area(float):
    @staticmethod
    @errorcheck
    def largest(division: Division) -> Division:
        return max(division, key = lambda x: x.area)
    
    @staticmethod
    @errorcheck
    def smallest(division: Division) -> Division:
        return min(division, key = lambda x: x.area)


# --- AreaUnit Class --- #

class AreaUnit(float):
    @staticmethod
    def convert(func: Callable):
        def inner1(first, other):
            if type(first) != type(other):
                if isinstance(other, Miles):
                    other = kilometers(other)
                else:
                    other = miles(other)

            return func(first, other)
                
        return inner1

    @convert
    def __gt__(self, other) -> bool:
        return float.__gt__(self, other)

    @convert
    def __lt__(self, other) -> bool:
        return float.__lt__(self, other)

    @convert
    def __eq__(self, other) -> bool:
        return float.__eq__(self, other)


# --- Kilometers Class --- #

class Kilometers(AreaUnit):
    def __str__(self) -> str:
        return f"{self:,.2f} km2"


# --- Miles Class --- #

class Miles(AreaUnit):  
    def __str__(self) -> str:
        return f"{self:,.2f} sq mi"


# --- Extending Functionality Definitions --- #

def add_area(cls, area: float) -> None:
    cls.area = area

def kilometers(area: Miles) -> Kilometers:
    return Kilometers(area * 1.609344) 

def miles(area: Kilometers) -> Miles:
    return Miles(area / 1.609344)
