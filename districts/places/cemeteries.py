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
    date_born: dt.date = dt.date.min
    date_died: dt.date = dt.date.max
    _: KW_ONLY
    description: str = field(default = "")

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.description:
                return f"{self.name}\r\n{self.date_born:%b. %d, %Y} - {self.date_died:%b. %d, %Y}\r\n{self.description}"
            return f"{self.name}\r\n{self.date_born:%b. %d, %Y} - {self.date_died:%b. %d, %Y}"

        return str(self)

    def age(self) -> int:
        if self.date_born != dt.date.min and self.date_died != dt.date.max:
            return self.date_died.year - self.date_born.year
        return -1


# --- Cemetery Class --- #

class Cemetery(Place):
    def __init__(self, name: str, /, population: int = None,
                 graves: list[Grave] = None, **kwargs):

        super().__init__(name, PlaceTypes.CEMETERY, population, **kwargs)

        if graves != None:
            self.graves = graves
