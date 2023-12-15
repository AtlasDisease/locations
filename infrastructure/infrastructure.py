# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle infrastructure.

# --- Imports --- #

from dataclasses import dataclass
from ..enum import StrEnum, auto, unique
from .buildings import Building

__all__ = ("CityHall", "Courthouse",
           "Port", "Bank", "Hospital")


# --- InfrastructureTypes Enum --- #

@unique
class InfrastructureTypes(StrEnum):
    CITY_HALL = auto()
    COURTHOUSE = auto()
    PORT = auto()
    BANK = auto()
    HOSPITAL = auto()
    POWER_STATION = auto()
    POST_OFFICE = auto()
    

# --- CityHall Class --- #

@dataclass(init=False)
class CityHall(Building):
    def __post_init__(self):
        
        self.type_ = InfrastructureTypes.CITY_HALL


# --- Courthouse Class --- #

@dataclass(init=False)
class Courthouse(Building):
    def __post_init__(self):
        
        self.type_ = InfrastructureTypes.COURTHOUSE


# --- Port Class --- #

@dataclass(init=False)
class Port(Building):
    def __post_init__(self):
        
        self.type_ = InfrastructureTypes.PORT


# --- Bank Class --- #

@dataclass(init=False)
class Bank(Building):
    def __post_init__(self):
        
        self.type_ = InfrastructureTypes.BANK


# --- Hospital Class --- #

@dataclass(init=False)
class Hospital(Building):
    def __post_init__(self):
        
        self.type_ = InfrastructureTypes.HOSPITAL
