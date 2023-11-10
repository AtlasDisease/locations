# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Area class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from ..divisions import Division
from .extenders import Extension, errorcheck

__all__ = ("Area", "Kilometers", "Miles", \
    "kilometers", "miles", "add_area")



# --- Area Class --- #

class Area(Extension):
    @staticmethod
    @errorcheck
    def largest(division: Division) -> Division:
        return Area._get(division, lambda x, y: x.area <= y.area)
    
    @staticmethod
    @errorcheck
    def smallest(division: Division) -> Division:
        return Area._get(division, lambda x, y: x.area >= y.area)


# --- Kilometers Class --- #

class Kilometers(float):
    def __str__(self) -> str:
        return f"{self:,.2f} km2"

    def __gt__(self, other) -> bool:
        if isinstance(other, Miles):
            other = kilometers(other)

        return float.__gt__(self, other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Miles):
            other = kilometers(other)

        return float.__lt__(self, other)

    def __eq__(self, other) -> bool:
        if isinstance(other, Miles):
            other = kilometers(other)

        return float.__eq__(self, other)


# --- Miles Class --- #

class Miles(float):
    def __str__(self) -> str:
        return f"{self:,.2f} sq mi"

    def __gt__(self, other) -> bool:
        if isinstance(other, Kilometers):
            other = miles(other)

        return float.__gt__(self, other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Kilometers):
            other = miles(other)

        return float.__lt__(self, other)

    def __eq__(self, other) -> bool:
        if isinstance(other, Kilometers):
            other = miles(other)

        return float.__eq__(self, other)


# --- Extending Functionality Definitions --- #

def add_area(cls, area: float) -> None:
    cls.area = area

def kilometers(area: Miles) -> Kilometers:
    return Kilometers(area * 1.609344) 

def miles(area: Kilometers) -> Miles:
    return Miles(area / 1.609344)
