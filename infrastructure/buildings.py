# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle generic buildings.

# --- Imports --- #

from typing import override, Optional
from .rooms import Room
from ..subdivisions import DivisionBase

__all__ = ("Building", "CommercialBuilding", "ResidentialBuilding",)


# --- Building Class --- #

class Building(DivisionBase): #DivisionBase but different functionality
    def __init__(self, name: str,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 **kwargs):
        super().__init__(name, subdivisions, **kwargs)
        
    @override
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"{self.name} {self.__class__.__name__}"

        return str(self)


# --- CommericalBuilding Class --- #

class CommericalBuilding(Building):
    def __init__(self, name: str,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 **kwargs):
        super().__init__(name, subdivisions, **kwargs)


# --- ResidentialBuilding Class --- #

class ResidentialBuilding(Building):
    def __init__(self, name: str,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 *,
                 population: int = 0,
                 **kwargs):
        super().__init__(name, subdivisions, **kwargs)

        if population:
            self.population = population
