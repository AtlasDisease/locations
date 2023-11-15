# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module contains the Extension class that extends
# the functionality of a class in the extensions package.

# --- Imports --- #

from typing import Callable
from ..divisions import Division

### --- Errorcheck Decorator --- #
##
##def check(func: Callable):
##    def inner1(*args, **kwargs):
##
##        print(func, args)
##        division = args[0]
##        print(division)
##        attr = args[1]
##        print(attr)
##
##        if not hasattr(division, attr):
##            return None
##        
##        return func(*args, **kwargs)
##        
##    return inner1


# --- Errorcheck Decorator --- #

def errorcheck(func: Callable):
    def inner1(*args, **kwargs):

        division = args[0]

        # This is a hacky way to get the class that called this so we can make sure division has a certain attribute
        varname = "subdivisions"
        if "." in varname:
            varname = func.__qualname__.split(".")[0].lower() #Area.largest = area, Population.smallest = population

        if any(not hasattr(x, varname) for x in division.subdivisions):
            raise NotImplementedError(f"Subdivisions are required to have a {varname} attribute in order to use this function.")
        
        if len(division.subdivisions) <= 0:
            return Division("New", population = 0, area = 0, elevation = 0)

        return func(*args, **kwargs)
        
    return inner1


# --- Extension Class --- #

class Extension:
    @staticmethod
    def _get(division: Division, func: Callable) -> Division:
        result = division.subdivisions[0]
    
        for subdivision in division.subdivisions:
            if func(subdivision, result):
                continue
        
            result = subdivision

        return result
