# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle residential buildings.

# --- Imports --- #

import datetime as dt
from enum import IntEnum, auto
from dataclasses import dataclass
from .buildings import ResidentialBuilding


# --- Apartment Class --- #

class Apartment(ResidentialBuilding):
    pass


# --- House Class --- #

class House(ResidentialBuilding):
    pass