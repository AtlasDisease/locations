# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an airport.

# --- Imports --- #

from typing import Self
from enum import IntEnum, auto
from dataclasses import dataclass
from ..buildings import Building
from ..rooms import Room

__all__ = ("Airport", "Gate", "AirportTypes")


# --- AirportType Enum --- #

class AirportTypes(IntEnum): #Upgradable
    UNKNOWN = auto()
    MUNICIPALITY = auto()
    REGIONAL = auto()
    INTERNATIONAL = auto()

    def __str__(self) -> str:
        return self.name.title()

    def __add__(self, other) -> Self:
        if isinstance(other, int):
            other %= len(AirportTypes)
            if other == 0:
                other = 3
            other = AirportTypes(other)

        other = self.value + other.value
        if other > len(AirportTypes):
            other %= len(AirportTypes)
            if other == 0:
                other = 3
            
        return AirportTypes(other)

    def __iadd__(self, other) -> Self:
        self = self + other
        return self


# --- Gate Class --- #

@dataclass
class Gate:
    terminal: chr
    gate: str

    def __str__(self) -> str:
        return f"{self.terminal}{self.gate}"
    

# --- Airport Class --- #

class Airport(Building):
    def __init__(self, name: str, type_: AirportTypes,
                 *,
                 subdivisions: list[Room] = None,
                 **kwargs):

        super().__init__(name, type_, subdivisions = subdivisions)

    def __format__(self, format_spec = "") -> str:
        if any(letter in format_spec for letter in {"F", "O", "L", "l"}):
            if self.type_ != AirportTypes.UNKNOWN:
                return f"{self.name} {self.type_} {self.__class__.__name__}"
            return f"{self.name} {self.__class__.__name__}"
        
        return str(self)
