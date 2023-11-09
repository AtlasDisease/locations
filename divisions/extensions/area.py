# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Area class that extends
# the functionality of a class in the districts package.

# --- Imports --- #

from typing import Callable
from dataclasses import dataclass, field
from enum import IntEnum, auto
from ..divisions import Division, DivisionTypes

__all__ = ("Area", "add_area", "MeasurementTypes",
           "kilometers", "miles")


# NEED TO ADD SQ KILOMETERS, use SQ MILES currently

# --- MeasurementTypes Enum --- #

class MeasurementTypes(IntEnum):
    MILES = auto()
    KILOMETERS = auto()

    def __str__(self) -> str:
        if self == MeasurementTypes.MILES:
            return "sq mi"
        return "km2"

    def __format__(self, format_spec = ""):
        return str(self)


# --- Area Class --- #

@dataclass
class Area(float):
    """Basically an integer but with formatting when converted to string
and some additional functions to help with comparisons"""

    def __new__(self, value, *args):
        return float.__new__(self, value)

    def __init__(self, area: float = 0, measurement: MeasurementTypes = MeasurementTypes.MILES):
        
        super().__init__()
        self.measurement = measurement

    def __str__(self) -> str:
        return f"{self:,.2f} {self.measurement}"

    def __gt__(self, other) -> bool:

        if self.measurement != other.measurement:
            if self.measurement == MeasurementTypes.MILES:
                num = miles(other)
            elif self.measurement == MeasurementTypes.KILOMETERS:
                num = kilometers(other)
                
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
            if any((not hasattr(x, "area") for x in division.subdivisions)):
                raise NotImplementedError("Subdivisions are required to have a area variable in order to use this function.")
        
            if len(division.subdivisions) <= 0:
                return Division("New", DivisionTypes.AREA, area = 0)

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
        return Area.__get(division, lambda x, y: x.area <= y.area \
               and x.area.measurement == y.area.measurement)
    
    @staticmethod
    @__errorcheck
    def smallest(division: Division) -> Division:
        return Area.__get(division, lambda x, y: x.area >= y.area \
               and x.area.measurement == y.area.measurement)


# --- Extending Functionality Definitions --- #

def add_area(cls, area: float) -> None:
    cls.area = area

def kilometers(area: Area) -> Area:
    return Area(area * 1.609344, MeasurementTypes.KILOMETERS)

def miles(area: Area) -> Area:
    return Area(area / 1.609344, MeasurementTypes.MILES)
