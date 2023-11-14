# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle infrastructure.

# --- Imports --- #

import datetime as dt
from dataclasses import dataclass
from ..divisions.places import Place, PlaceTypes

__all__ = ("Building", "CityHall", "Courthouse",
           "Port", "Bank", "Hospital",
           "PostOffice")


# --- Building Class --- #

class Building(Place):
    def __init__(self, name: str, **kwargs):
        super().__init__(self, PlaceTypes.BUILDING)
        

# --- CityHall Class --- #

@dataclass(init = False)
class CityHall(Place):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.CITY_HALL


# --- Courthouse Class --- #

@dataclass(init = False)
class Courthouse(Place):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.COURTHOUSE


# --- Port Class --- #

@dataclass(init = False)
class Port(Place):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.PORT


# --- Bank Class --- #

@dataclass(init = False)
class Bank(Place):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.BANK


# --- Hospital Class --- #

@dataclass(init = False)
class Hospital(Place):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.HOSPITAL


# --- PostOffice Class --- #

@dataclass(init = False)
class PostOffice(Place):
    def __post_init__(self):
        
        self.type_ = PlaceTypes.POST_OFFICE
