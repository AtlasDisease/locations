# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle cemeteries.

# --- Imports --- #

import datetime as dt
from enum import IntEnum, auto
from dataclasses import dataclass, field, KW_ONLY
from .places import Place, PlaceTypes

__all__ = ("Cemetery",)


# --- Grave Class --- #

@dataclass
class Grave:
    name: str
    born: dt.date = dt.date.min
    died: dt.date = dt.date.max
    _: KW_ONLY
    epitaph: str = field(default = "")

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.epitaph:
                return f"{self.name}\r\n{self.born:%b. %d, %Y} - {self.died:%b. %d, %Y}\r\n{self.epitaph}"
            return f"{self.name}\r\n{self.born:%b. %d, %Y} - {self.died:%b. %d, %Y}"

        return str(self)

    def age(self) -> int:
        if self.born != dt.date.min and self.died != dt.date.max:
            return self.died.year - self.born.year
        return -1


# --- Cemetery Class --- #

class Cemetery(Place):
    def __init__(self, name: str, /, population: int = None,
                 graves: list[Grave] = None, **kwargs):

        super().__init__(name, PlaceTypes.CEMETERY, population, **kwargs)

        if graves:
            self.graves = graves
