# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a road.

# --- Imports --- #

from dataclasses import dataclass
from enum import IntEnum, StrEnum, auto, unique

__all__ = ("Road", "Intersection", "RoadTypes",
           "MaterialTypes", "IntersectionTypes", "Trail")


# --- RoadType Enum --- #

@unique
class RoadTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
    PRIMITIVE = auto()
    PRIVATE = auto()
    LOW_CAPACITY = auto()
    HIGH_CAPACITY = auto()


# --- MaterialTypes Enum --- #

class MaterialTypes(IntEnum):
    DIRT = auto()
    GRAVEL = auto()
    CONCRETE = auto()
    ASPHALT = auto()


# --- IntersectionType Enum --- #

@unique
class IntersectionTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
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

    def __str__(self) -> str:
        return self.name


# --- Trail Class --- #

class Trail(Road):
    def __init__(self, name: str):
        super().__init__(name, RoadTypes.PRIMITIVE, MaterialTypes.DIRT)


# --- Intersection Class --- #

@dataclass
class Intersection:
    name: str
    type_: IntersectionTypes = IntersectionTypes.INTERSECTION
    material: MaterialTypes = MaterialTypes.ASPHALT

    def __str__(self) -> str:
        return self.name


# --- Testing --- #

if __name__ == "__main__":

    road = Road(name = "Hello World", type_ = RoadTypes.HIGH_CAPACITY)
    print(repr(road), str(road.type_))
