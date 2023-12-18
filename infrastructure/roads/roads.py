# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a road.

# --- Imports --- #

import datetime as dt
from dataclasses import dataclass, field, KW_ONLY
from ...enum import StrEnum, UpgradableEnum, auto, unique

__all__ = ("Road", "Intersection", "RoadTypes",
           "MaterialTypes", "IntersectionTypes", "Trail")


# --- RoadType Enum --- #

@unique
class RoadTypes(UpgradableEnum): #Upgradable
    PRIMITIVE = auto()
    PRIVATE = auto()
    LOW_CAPACITY = auto()
    HIGH_CAPACITY = auto()


# --- MaterialTypes Enum --- #

@unique
class MaterialTypes(UpgradableEnum): #Upgradable
    DIRT = auto()
    GRAVEL = auto()
    CONCRETE = auto()
    ASPHALT = auto()


# --- IntersectionType Enum --- #

@unique
class IntersectionTypes(StrEnum):   
    INTERSECTION = auto()
    ROUNDABOUT = auto()
    CONNECTOR = auto()
    LEVEL_JUNCTION = auto()
    INTERCHANGE = auto()


# --- Road Class --- #

@dataclass
class Road:
    name: str
    type_: RoadTypes = RoadTypes.LOW_CAPACITY
    material: MaterialTypes = MaterialTypes.ASPHALT
    _: KW_ONLY
    existed: dt.date = dt.date.max

    def __str__(self) -> str:
        return self.name


# --- Trail Class --- #

@dataclass(init = False, match_args = False)
class Trail(Road):
    def __post_init__(self):

        self.type_ = RoadTypes.PRIMITIVE
        self.material = MaterialTypes.DIRT


# --- Intersection Class --- #

@dataclass
class Intersection(Road):
    type_: IntersectionTypes = field(default = IntersectionTypes.INTERSECTION)
    _: KW_ONLY
    roads: list[Road] = field(default_factory = list)

    def __format__(self, format_spec = ""):
        return str(self)
    
    def __iter__(self):
        return iter(self.roads)


# --- Junction Class --- #
    
@dataclass
class Junction(Intersection):
    def __post_init__(self):
        self.type_ = IntersectionTypes.INTERCHANGE

    def __format__(self, format_spec = ""):
        return str(self)
    
    def __iter__(self):
        return iter(self.roads)
