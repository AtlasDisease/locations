# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Elevation class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from typing import Callable
from ..divisions import Division
from .extensions import errorcheck

__all__ = ("Elevation", "Meters", "Feet", \
    "meters", "feet", "add_elevation" )


# --- Elevation Class --- #

class Elevation(int):
    @staticmethod
    @errorcheck
    def highest(division: Division) -> Division:
        return max(division, key = lambda x: x.elevation)
    
    @staticmethod
    @errorcheck
    def lowest(division: Division) -> Division:
        return min(division, key = lambda x: x.elevation)


# --- ElevationUnit Class --- #

class ElevationUnit(int):
    @staticmethod
    def convert(func: Callable):
        def inner1(first, other):
            if type(first) != type(other):
                if isinstance(other, Feet):
                    other = feet(other)
                else:
                    other = meters(other)
                    
            return func(first, other)

        return inner1

    @convert
    def __gt__(self, other) -> bool:
        return int.__gt__(self, other)

    @convert
    def __lt__(self, other) -> bool:
        return int.__lt__(self, other)

    @convert
    def __eq__(self, other) -> bool:
        return int.__eq__(self, other)


# --- Meters Class --- #

class Meters(ElevationUnit):
    def __str__(self) -> str:
        return f"{self:,.2f} m"


# --- Feet Class --- #

class Feet(ElevationUnit):
    def __str__(self) -> str:
        return f"{self:,.2f} ft"


# --- Extending Functionality Definitions --- #

def add_elevation(cls, elevation: int) -> None:
    cls.elevation = elevation

def meters(elevation: Feet) -> Meters:
    return Meters(elevation * 0.3048)

def feet(elevation: Meters) -> Feet:
    return Feet(elevation / 0.3048)
