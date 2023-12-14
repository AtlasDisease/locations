# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle generic buildings.

# --- Imports --- #

import datetime as dt
from typing import override, Protocol
from ..enum import StrEnum, auto, unique
from dataclasses import dataclass, field, KW_ONLY
from .rooms import Room
from ..subdivisions import DivisionBase

__all__ = ("Building", "CommercialBuilding", "ResidentialBuilding", "BuildingTypes")


# --- BuildingTypes Enum --- #

@unique
class BuildingTypes(StrEnum):  
    COMMERICAL = auto() #General use
    RESIDENTIAL = auto()


# --- Building Class --- #

class Building(DivisionBase): #Very similar to districts.places.Place
    def __init__(self, name: str,
                 type_: BuildingTypes = BuildingTypes.COMMERICAL,
                 /,
                 subdivisions: list[Room] = None):
        super().__init__(name, type_, subdivisions)

        if type_ == BuildingTypes.COMMERICAL:
            self.__class__ = CommericalBuilding

        if type_ == BuildingTypes.RESIDENTIAL:
            self.__class__ = ResidentialBuilding
            self.population = 0

    @override
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.type_.name == "FORT":
                return f"{self.type_} {self.name}"
            return f"{self.name} {self.type_}"

        return str(self)

    @override
    def __bool__(self) -> bool:
        return self.name != "New" and self.name != "" \
               and self.type_ != BuildingTypes.COMMERICAL


# --- CommericalBuilding Class --- #

class CommericalBuilding(Building):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Room] = None):
        super().__init__(name, BuildingTypes.COMMERICAL, subdivisions)


# --- ResidentialBuilding Class --- #

class ResidentialBuilding(Building):
    def __init__(self, name: str,
                 /,
                 subdivisions: list[Room] = None,
                 *,
                 population: int = 0,
                 **kwargs):
        super().__init__(name, BuildingTypes.RESIDENTIAL, subdivisions, **kwargs)

        if population:
            self.population = population
