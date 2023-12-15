# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle generic buildings.

# --- Imports --- #

import datetime as dt
from typing import override, Protocol, Optional
from dataclasses import dataclass, field, KW_ONLY
from ..enum import StrEnum, auto, unique
from .rooms import Room
from ..subdivisions import DivisionBase

__all__ = ("Building", "CommercialBuilding", "ResidentialBuilding",
           "BuildingTypes")


# --- BuildingTypes Enum --- #

@unique
class BuildingTypes(StrEnum):  
    COMMERICAL = auto() #General use
    RESIDENTIAL = auto()


# --- Building Class --- #

class Building(DivisionBase): #DivisionBase but different functionality
    def __init__(self, name: str, type_: BuildingTypes = BuildingTypes.COMMERICAL,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 **kwargs):
        super().__init__(name, type_, subdivisions, **kwargs)
        
    @override
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"{self.name} {self.type_}"

        return str(self)

    @override
    def __bool__(self) -> bool:
        return self.name != "New" and self.name \
               and self.type_ != BuildingTypes.COMMERICAL


# --- CommericalBuilding Class --- #

class CommericalBuilding(Building):
    def __init__(self, name: str,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 **kwargs):
        super().__init__(name, BuildingTypes.COMMERICAL, subdivisions, **kwargs)


# --- ResidentialBuilding Class --- #

class ResidentialBuilding(Building):
    def __init__(self, name: str,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 *,
                 population: int = 0,
                 **kwargs):
        super().__init__(name, BuildingTypes.RESIDENTIAL, subdivisions, **kwargs)

        if population:
            self.population = population
