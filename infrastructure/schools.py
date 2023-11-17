# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a place of learning.

# --- Imports --- #

import sys, inspect
from enum import IntEnum, auto
from dataclasses import dataclass
from ..divisions import Division
from ..divisions.districts import AreaTypes, District

__all__ = ("School", "College", "University", "Technical")


# --- SchoolTypes Enum --- #

##class SchoolTypes(IntEnum):
##    SCHOOL = auto()
##    COLLEGE = auto()
##    UNIVERSITY = auto()
##    TECHNICAL = auto()
##
##    def __str__(self):
##        return self.name.title()


# --- School Class --- #

class School(District):
     def __init__(self, name: str, school_type: AreaTypes = AreaTypes.SCHOOL, #SchoolTypes = SchoolTypes.SCHOOL,
                  /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,
                 **kwargs):

        super().__init__(name, AreaTypes.SCHOOL, subdivisions, population = population, **kwargs)

        self.type_ = school_type


# --- College Class --- #

@dataclass(init = False)
class College(School):
    def __post_init__(self):
        
        self.type_ = SchoolTypes.COLLEGE


# --- University Class --- #

@dataclass(init = False)
class University(School):
    def __post_init__(self):
        
        self.type_ = SchoolTypes.UNIVERSITY


# --- Technical Class --- #

@dataclass(init = False)
class Technical(School):
    def __post_init__(self):
        
        self.type_ = SchoolTypes.TECHNICAL


# Experiment to take all classes in module and turn them into a IntEnum where the
# names in the enum are the class names in all uppercase
SchoolTypes = IntEnum("SchoolTypes",
                     names = [name.upper() for name,obj in inspect.getmembers(sys.modules[__name__])
       if inspect.isclass(obj) and obj.__module__ == __name__])

SchoolTypes.__str__ = lambda self: self.name.title()
