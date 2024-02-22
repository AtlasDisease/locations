# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an airplane.

# --- Imports --- #

from ...enum import StrEnum, auto, unique
from dataclasses import dataclass, field, KW_ONLY
from .engines import Engine

__all__ = ("Seat", "Airplane")


# --- AirplaneRole Enum --- #

@unique
class AirplaneRole(StrEnum):   
    WIDE_BODY = auto() #Default
    FREIGHT = auto()
    MILITARY = auto()


# --- AirplaneManufacturer Enum --- #

@unique
class AirplaneManufacturer(StrEnum):   
    UNKNOWN = auto()
    BOEING = auto()
    AIRBUS = auto()
    CESSNA = auto()
    OTHER = auto()


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
    role: AirplaneRole = AirplaneRole.WIDE_BODY 
    _: KW_ONLY
    capacity: int = -1
    engines: list[Engine] = field(default_factory = list)

    @property
    def engine_num(self):
        return len(self.engines)

    def __str__(self) -> str:
        if self.manufacturer == AirplaneManufacturer.UNKNOWN \
           or self.manufacturer == AirplaneManufacturer.OTHER:
            return self.type_
        
        return f"{self.manufacturer} {self.type_}"
