# --- Imports --- #

from typing import Iterable
from dataclasses import dataclass
from enum import StrEnum, auto


# --- TornadoCategory Class --- #

@dataclass(slots=True)
class _TornadoCategory:
    name: str
    min_wind_speed: int
    max_wind_speed: int

    def __str__(self) -> str:
        return f"{self.value} damage"

    def __format__(self, format_spec = "") -> str:
        if format_spec == "R": #Range
            return "{self.min_wind_speed}-{self.max_wind_speed}"

        return str(self)
    

# --- EnhancedFujitaScale Enum --- #

class EnhancedFujitaScale(StrEnum):
    EFU = _TornadoCategory("No surveyable", 0, 64)
    EF0 = _TornadoCategory("Light", 65, 85)
    EF1 = _TornadoCategory("Moderate", 86, 110)
    EF2 = _TornadoCategory("Considerable", 111, 135)
    EF3 = _TornadoCategory("Severe", 136, 165)
    EF4 = _TornadoCategory("Devastating", 166, 200)
    EF5 = _TornadoCategory("Incredible", 200, 300)
    

# --- Tornado Class --- #

@dataclass
class Tornado:
    name: str
    category: EnhancedFujitaScale

    @property
    def min_wind_speed(self) -> int:
        return self.category.min_wind_speed

    @property
    def max_wind_speed(self) -> int:
        return self.category.max_wind_speed
            
