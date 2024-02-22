# --- Imports --- #

from dataclasses import dataclass
from ...enum import StrEnum, unique, auto

__all__ = ("EngineManufacturer", "Engine")


# --- EngineManufacturer Class --- #

@unique
class EngineManufacturer(StrEnum):
    ROLLS_ROYCE = auto()
    GE = auto()


# --- Engine Class --- #

@dataclass
class Engine:
    name: str
    manufacturer: EngineManufacturer | str

    def __str__(self):
        return self.name

    def __format__(self, format_spec = ""):
        if "O" in format_spec or "F" in format_spec:
            return f"{self.manufacturer} {self.name}"

        return str(self)
