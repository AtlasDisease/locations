# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle generic buildings.

# --- Imports --- #

import datetime as dt
from enum import IntEnum, auto
from dataclasses import dataclass
from ..divisions.places import PlaceTypes
from .rooms import Room


# --- BuildingTypes Enum --- #

class BuildingTypes(IntEnum):
    COMMERICAL = auto() #General use
    RESIDENTIAL = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- Building Class --- #

class Building: #Very similar to districts.places.Place
    def __init__(self, name: str,
                 type_: BuildingTypes = BuildingTypes.COMMERICAL,
                 *,
                 subdivisions: list[Room] = None,
                 **kwargs):

        self.name = name
        self.type_ = type_

        if subdivisions:
            self.subdivisions = subdivisions

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
               and self.type_ != PlaceTypes.BUILDING


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
