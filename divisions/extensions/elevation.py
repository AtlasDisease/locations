# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Elevation class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from typing import Callable
from enum import IntEnum, auto
from ..divisions import Division
from .extenders import Extender, errorcheck

__all__ = ("Elevation", "Meters", "Feet", \
    "meters", "feet", "add_elevation" )


# --- Elevation Class --- #

class Elevation(Extender):
    @staticmethod
    @errorcheck
    def highest(division: Division) -> Division:
        return Elevation._get(division, lambda x, y: x.elevation <= y.elevation)
    
    @staticmethod
    @errorcheck
    def lowest(division: Division) -> Division:
        return Elevation._get(division, lambda x, y: x.elevation >= y.elevation)


# --- Meters Class --- #

class Meters(int):
    def __str__(self) -> str:
        return f"{self:,.2f} m"

    def __gt__(self, other) -> bool:
        if isinstance(other, Feet):
            other = feet(other)

        return int.__gt__(self, other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Feet):
            other = feet(other)

        return int.__lt__(self, other)

    def __eq__(self, other) -> bool:
        if isinstance(other, Feet):
            other = feet(other)

        return int.__eq__(self, other)


# --- Feet Class --- #

class Feet(int):
    def __str__(self) -> str:
        return f"{self:,.2f} ft"

    def __gt__(self, other) -> bool:
        if isinstance(other, Meters):
            other = meters(other)

        return int.__gt__(self, other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Meters):
            other = meters(other)

        return int.__lt__(self, other)

    def __eq__(self, other) -> bool:
        if isinstance(other, Meters):
            other = meters(other)

        return int.__eq__(self, other)


# --- Extending Functionality Definitions --- #

def add_elevation(cls, elevation: int) -> None:
    cls.elevation = elevation

def meters(elevation: Feet) -> Meters:
    return Meters(elevation * 0.3048)

def feet(elevation: Meters) -> Feet:
    return Feet(elevation / 0.3048)
