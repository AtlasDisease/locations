# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle infrastructure.

# --- Imports --- #

import datetime as dt
from dataclasses import dataclass
from .buildings import Building, PlaceTypes

__all__ = ("CityHall", "Courthouse",
           "Port", "Bank", "Hospital",
           "PostOffice")
        

# --- CityHall Class --- #

@dataclass(init = False)
class CityHall(Building):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.CITY_HALL


# --- Courthouse Class --- #

@dataclass(init = False)
class Courthouse(Building):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.COURTHOUSE


# --- Port Class --- #

@dataclass(init = False)
class Port(Building):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.PORT


# --- Bank Class --- #

@dataclass(init = False)
class Bank(Building):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.BANK


# --- Hospital Class --- #

@dataclass(init = False)
class Hospital(Building):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.HOSPITAL


# --- PostOffice Class --- #

@dataclass(init = False)
class PostOffice(Building):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.POST_OFFICE
