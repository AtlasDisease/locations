# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle generic buildings.

# --- Imports --- #

import datetime as dt
from ..enum import StrEnum, auto, unique
from dataclasses import dataclass, field, KW_ONLY
from .rooms import Room

__all__ = ("Building", "ResidentialBuilding", "BuildingTypes")


# --- BuildingTypes Enum --- #

@unique
class BuildingTypes(StrEnum):  
    COMMERICAL = auto() #General use
    RESIDENTIAL = auto()


# --- Building Class --- #

@dataclass
class Building: #Very similar to districts.places.Place
    name: str
    type_: BuildingTypes = BuildingTypes.COMMERICAL
    _: KW_ONLY
    subdivisions: list[Room] = field(default_factory = list)

    def __str__(self) -> str:
        return self.name
    
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.type_.name == "FORT":
                return f"{self.type_} {self.name}"
            return f"{self.name} {self.type_}"

        return str(self)

    def __bool__(self) -> bool:
        return self.name != "New" and self.name != "" \
               and self.type_ != BuildingTypes.BUILDING

    def __iter__(self):
        return self.subdivisions


# --- ResidentialBuilding Class --- #

class ResidentialBuilding(Building):
    def __init__(self, name: str,
                 *,
                 subdivisions: list[Room] = None,
                 population: int = 0,
                 **kwargs):
        super().__init__(name, BuildingTypes.RESIDENTIAL, subdivisions = subdivisions)

        if population:
            self.population = population

