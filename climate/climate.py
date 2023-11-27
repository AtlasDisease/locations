# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a climate.
# This is based off the Koppen-Geiger Classification.

# --- Imports --- #

from ..enum import StrEnum, auto
from dataclasses import dataclass
# from .temperature import TemperatureUnit

__all__ = ("Climate", "ClimateTypes")


# --- ClimateTypes Enum --- #

class ClimateTypes(StrEnum):
    UNKNOWN = auto()
    A = "Tropical"
    AF = "Tropical Rainforest"
    AM = "Tropical Monsoon"
    AW = "Tropical Savanna, Dry Winter"
    AS = "Tropical Savanna, Dry Summer"
    B = "Arid"
    BW = "Desert"
    BWH = "Hot Desert"
    BWK = "Cold Desert"
    BS = "Steppe"
    BSH = "Hot Steppe"
    BSK = "Cold Steppe"
    C = "Temperate"
    CS = "Mediterranean"
    CSA = "Mediterranean, Hot Summer"
    CSB = "Mediterranean, Cool Summer"
    CSC = "Mediterranean, Cold Summer"
    CFA = "Humid Subtropical"
    CFB = "Oceanic"
    CFC = "Subpolar Oceanic"
    CW = "Dry Winter Subtropical"
    CWA = "Dry Winter Humid Subtropical"
    CWB = "Dry Winter Subtropical Highland"
    CWC = "Dry Winter Cold Subtropical Highland"
    D = "Continental"
    DFA = "Hot Summer Continental"
    DWA = "Hot Summer Continental"
    DSA = "Hot Summer Continental"
    DFB = "Warm Summer Continental, Hemi-boreal"
    DWB = "Warm Summer Continental, Hemi-boreal"
    DSB = "Warm Summer Continental, Hemi-boreal"
    DFC = "Subarctic, Boreal"
    DWC = "Subarctic, Boreal"
    DSC = "Subarctic, Boreal"
    DFD = "Subarctic, Boreal, Severe Winter"
    DWD = "Subarctic, Boreal, Severe Winter"
    DSD = "Subarctic, Boreal, Severe Winter"
    E = "Polar"
    ET = "Tundra"
    EF = "Ice Cap"

    def __str__(self):
        return self.value


# --- Climate Class --- #

@dataclass(slots = True)
class Climate:
    """A class to handle historical weather trends in a geographical region"""

    classification: ClimateTypes
    # temperatures: dict[str, TemperatureUnit] = field(default_factory = dict)
    # precipation: dict[str, PrecipationUnit] = field(default_factory = dict)

    def __str__(self):
        return f"{self.classification} {self.__class__.__name__}"

    # def __iter__(self):
    #     return iter(self.temperatures)

    # def __len__(self):
    #     return len(self.temperatures)

#     def get(self, func: Callable) -> Self:
#         """Gets a unit based of a certain function.
# Ex. get largest or smallest unit by Temperature"""
#         return func(self)
