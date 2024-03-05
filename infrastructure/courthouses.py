# --- Imports --- #

from ..enum import StrEnum, auto
from .buildings import Building


# --- CourthouseTypes Enum --- #

class CourthouseTypes(StrEnum):
    DISTRICT = auto()
    APPEALS = auto()
    SUPREME = auto()


# --- Courthouse Class --- #

class Courthouse(Building):
    def __init__(self, name: str, type_: CourthouseTypes):
        self.name = name
        self.type_ = type_

    def __format__(self, format_spec = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"The {self.type_.value} Court of {self.name}"
        elif "L" in format_spec or "l" in format_spec:
            return f"{self.type_.value} Court of {self.name}"

        return str(self)
