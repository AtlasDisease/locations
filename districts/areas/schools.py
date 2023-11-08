# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a place of learning.

# --- Imports --- #

from enum import IntEnum, auto
from ..divisions import Division
from .areas import AreaTypes

__all__ = ("School", "College", "University", "Technical")


# --- SchoolTypes Enum --- #

class SchoolTypes(IntEnum):
    SCHOOL = auto()
    COLLEGE = auto()
    UNIVERSITY = auto()
    TECHNICAL = auto()

    def __str__(self):
        return self.name.title()


# --- School Class --- #

class School(Division):
     def __init__(self, name: str, school_type: SchoolTypes = SchoolTypes.SCHOOL,
                  /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,     
                 **kwargs):

        super().__init__(name, AreaTypes.SCHOOL, subdivisions, population, **kwargs)

        self.school_type = school_type


# --- College Class --- #

class College(School):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,   
                 **kwargs):

        super().__init__(name, SchoolTypes.COLLEGE, subdivisions, population, **kwargs)


# --- University Class --- #

class University(School):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,  
                 **kwargs):

        super().__init__(name, SchoolTypes.UNIVERSITY, subdivisions, population, **kwargs)


# --- Technical Class --- #

class Technical(School):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,  
                 **kwargs):

        super().__init__(name, SchoolTypes.TECHNICAL, subdivisions, population, **kwargs)
