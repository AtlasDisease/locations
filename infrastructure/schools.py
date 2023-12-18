# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a place of learning.

# --- Imports --- #

from typing import Optional
from ..subdivisions import DivisionBase
from . import Subdivision

__all__ = ("School", "College", "University", "Technical")


# --- School Class --- #

class School(DivisionBase):
     def __init__(self, name: str,
                  /,
                 subdivisions: Optional[list[Subdivision]] = None,
                 population: int = None,
                 **kwargs):

        super().__init__(name, subdivisions)
        self.population = population


# --- College Class --- #

class College(School):
    pass


# --- University Class --- #

class University(School):
    pass


# --- Technical Class --- #

class Technical(School):
    pass


# Experiment to take all classes in module and turn them into a IntEnum where the
# names in the enum are the class names in all uppercase

##import sys, inspect
##SchoolTypes = IntEnum("SchoolTypes",
##                     names = [name.upper() for name,obj in inspect.getmembers(sys.modules[__name__])
##       if inspect.isclass(obj) and obj.__module__ == __name__])
##
##SchoolTypes.__str__ = lambda self: self.name.title()
