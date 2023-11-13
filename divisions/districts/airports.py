# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an airport.

# --- Imports --- #

from enum import IntEnum, auto
from dataclasses import dataclass
from .areas import AreaTypes, District

__all__ = ("Airport", "Gate")


# --- Gate Class --- #

@dataclass
class Gate:
    name: str
    

# --- Airport Class --- #

@dataclass(init = False)
class Airport(District):
     def __post_init__(self):
         
         self.type_ = AreaTypes.AIRPORT
