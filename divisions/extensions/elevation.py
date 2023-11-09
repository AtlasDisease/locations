# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Elevation class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from typing import Callable
from enum import IntEnum, auto
from ..divisions import Division, DivisionTypes

__all__ = ("Elevation", "add_elevation", "meters",
           "feet", "ElevationMeasurementTypes")


# --- ElevationMeasurementTypes Enum --- #

class ElevationMeasurementTypes(IntEnum):
    METERS = auto()
    FEET = auto()

    def __str__(self) -> str:
        if self == ElevationMeasurementTypes.FEET:
            return "ft"
        return "m"

    def __format__(self, format_spec = ""):
        return str(self)



# --- Elevation Class --- #

class Elevation(int):
    """Basically an integer but with formatting when converted to string
and some additional functions to help with comparisons"""

    def __new__(self, value, *args):
        return int.__new__(self, value)
    
    def __init__(self, elevation: int = 0, measurement: ElevationMeasurementTypes = ElevationMeasurementTypes.METERS):

        super().__init__()
        self.measurement = measurement

    def __str__(self) -> str:
        return f"{self:,} {self.measurement}"

    def __gt__(self, other) -> bool:

        if self.measurement != other.measurement:
            if self.measurement == ElevationMeasurementTypes.FEET:
                num = feet(other)
            elif self.measurement == ElevationMeasurementTypes.METERS:
                num = meters(other)
                
            other = Area(num, self.measurement)
        
        return self.area > other.area \
               and self.measurement == other.measurement

    def __lt__(self, other) -> bool:
        return self < other \
               and self.measurement == other.measurement

    def __eq__(self, other) -> bool:
        return self.area == other.area \
               and self.measurement == other.measurement

    @staticmethod
    def __errorcheck(func):
        def inner1(*args, **kwargs):

            division = args[0]
            if any((not hasattr(x, "elevation") for x in division.subdivisions)):
                raise NotImplementedError("Subdivisions are required to have a elevation variable in order to use this function.")
        
            if len(division.subdivisions) <= 0:
                return Division("New", DivisionTypes.AREA, elevation = 0)

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
        return Elevation.__get(division, lambda x, y: x.elevation <= y.elevation \
               and x.elevation.measurement == y.elevation.measurement)
    
    @staticmethod
    @__errorcheck
    def smallest(division: Division) -> Division:
        return Elevation.__get(division, lambda x, y: x.elevation >= y.elevation \
               and x.elevation.measurement == y.elevation.measurement)


# --- Extending Functionality Definitions --- #

def add_elevation(cls, elevation: int) -> None:
    cls.elevation = elevation

def meters(elevation: Elevation) -> Elevation:
    return Elevation(elevation * 0.3048, ElevationMeasurementTypes.METERS)

def feet(elevation: Elevation) -> Elevation:
    return Elevation(elevation / 0.3048, ElevationMeasurementTypes.FEET)
