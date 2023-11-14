# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an airplane.

# --- Imports --- #

from enum import StrEnum, auto
from dataclasses import dataclass

__all__ = ("Seat", "Airplane")


# --- AirplaneManufacturer Enum --- #

class AirplaneManufacturer(StrEnum):
    UNKNOWN = auto()
    BOEING = auto()
    AIRBUS = auto()
    OTHER = auto()

    def __str__(self) -> str:
        return self.value.title()


# --- Seat Class --- #

@dataclass
class Seat:
    aisle: int
    seat: chr

    def __str__(self) -> str:
        return f"{self.aisle}{self.seat}"


# --- Airplane Class --- #

@dataclass
class Airplane:
    type_: str
    manufacturer: AirplaneManufacturer = AirplaneManufacturer.UNKNOWN
    capacity: int = -1

    def __str__(self) -> str:
        if self.manufacturer == AirplaneManufacturer.UNKNOWN \
           or self.manufacturer == AirplaneManufacturer.OTHER:
            return self.type_
        
        return f"{self.manufacturer} {self.type_}"
