# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle residential buildings.

# --- Imports --- #

import datetime as dt
from enum import IntEnum, auto
from dataclasses import dataclass
from ..divisions.places import Place, PlaceTypes
        

# --- Building Class --- #

class ResidentialBuilding(Place):
    def __init__(self, name: str, *, population: int = 0, **kwargs):
        super().__init__(name, PlaceTypes.BUILDING, population = population)


# --- Apartment Class --- #

class Apartment(ResidentialBuilding):
    pass


# --- House Class --- #

class House(ResidentialBuilding):
    pass
