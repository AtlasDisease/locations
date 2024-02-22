# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle cemeteries.

# --- Imports --- #

import datetime as dt
from typing import override
from dataclasses import dataclass, field, KW_ONLY
from ..subdivisions import DivisionBase

__all__ = ("Cemetery",)


# --- Grave Class --- #

@dataclass(slots = True)
class Grave:
    name: str
    born: dt.date = dt.date.min
    died: dt.date = dt.date.max
    _: KW_ONLY
    epitaph: str = field(default = "")

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "L" in format_spec:
            return f"{self.__class__.__name__} of {self.name}"
        elif "F" in format_spec or "O" in format_spec:
            if self.epitaph:
                return f"{self.name}\r\n{self.born:%b. %d, %Y} - {self.died:%b. %d, %Y}\r\n{self.epitaph}"
            return f"{self.name}\r\n{self.born:%b. %d, %Y} - {self.died:%b. %d, %Y}"

        return str(self)

    def age(self) -> int:
        if self.born != dt.date.min and self.died != dt.date.max:
            return self.died.year - self.born.year
        return -1


# --- Cemetery Class --- #

class Cemetery(DivisionBase):
    def __init__(self, name: str,
                 /,
                 graves: list[Grave] = None,
                 **kwargs):

        super().__init__(name, graves, **kwargs)

    @property
    def hasSubdivisions(self) -> bool:
        return bool(self.subdivisions)

    @property
    def graves(self):
        return self._subdivisions

    @property
    @override
    def population(self): #This overrides the possible kwarg of "population"
        return len(self)

    def __len__(self):
        return len(iter(self))

    def __bool__(self) -> bool:
        return self.name != "New" and self.name \
               and not self._subdivisions

    @override
    def __format__(self, format_spec = "") -> str:
        if any((char in format_spec for char in {"F", "O", "L"})):
            return f"{self.name} {self.__class__.__name__}"
        
        return str(self)
