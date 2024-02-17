# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a place of learning.

# --- Imports --- #

from typing import Optional
from dataclasses import dataclass
from ..subdivisions import DivisionBase
from ..enum import UpgradableEnum, auto
from . import Subdivision

__all__ = ("School", "College", "University", "Technical")


# --- Degree Type --- #

class DegreeTypes(UpgradableEnum): #May want a FlagEnum here
     CERTIFICATE = auto() #Cert
     MINOR = auto() #Minor
     UNDERGRADUATE = auto() #Bachelors
     GRADUATE = auto() #Masters, Doctorate


# --- Class Class --- #

@dataclass(slots=True)
class Class:
     name: str
     teacher: str


# --- Department Class --- #

@dataclass(slots=True)
class Department:
     name: str
     degreeType: DegreeTypes = DegreeTypes.UNDERGRADUATE
     head: str = ""


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
     def __init__(self, name: str,
                  /,
                  subdivisions: Optional[list[Subdivision]] = None,
                  population: int = None,
                  *,
                  departments: Optional[list[Department]] = None,
                  **kwargs):
          
          super().__init__(name, subdivisions, population)
          self.departments = departments if departments else []


# --- University Class --- #

class University(School):
     def __init__(self, name: str,
                  /,
                  subdivisions: Optional[list[Subdivision]] = None,
                  population: int = None,
                  *,
                  colleges: Optional[list[College]] = None,
                  **kwargs):
          
          super().__init__(name, subdivisions, population)
          self.colleges = colleges if colleges else []


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
