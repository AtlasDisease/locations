# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for connecting divisions and infrastructure packages.

# --- Imports --- #

import re
from typing import Self, Callable, Iterable, Protocol, Optional
from .enum import Enums, StrEnum, auto

__all__ = ("SubdivisionTypes",)


# --- SubdivisionTypes Enum --- #

class SubdivisionTypes(StrEnum):
    NEIGHBORHOOD = auto() #General use
    SCHOOL = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()
    CEMETERY = auto()
    POWER_STATION = auto()


# --- DivisionBase Class --- #

class DivisionBase:        
    def __init__(self, name: str,
                 type_: Enums,
                 /,
                 _subdivisions: Optional[list[Self]] = None,
                 **kwargs):
        self.name = name
        self.type_ = type_
        self._subdivisions = _subdivisions if _subdivisions else []
##        print(" ".join(re.findall('[A-Z][^A-Z]*', self.__class__.__name__)).upper())
##        print("DIVSIONBASE:", self.name, self.type_, self._subdivisions)

    @property
    def subdivisions(self) -> list[Self]:
        return self._subdivisions
    
    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec: str = "") -> str:
        if "O" in format_spec or "F" in format_spec: #Stands for "Formal" or "Official"
            return f"The {self.type_} of {self.name}".strip()
        
        if "L" in format_spec or "l" in format_spec: #Stands for "Location"
            return f"{self.name} {self.type_}".strip()
        return str(self)

    def __iter__(self):
        return iter(self.subdivisions)

    def __bool__(self) -> bool:
        return self.name != "New" and self.name

    def get(self, func: Callable) -> Self:
        """Gets a subdivision based of a certain function.
Ex. get largest or smallest subdivision by Population"""
        return func(self)

    def search(self, search, func: Callable):
        return func(self, search)


# --- Divisible Protocol --- #

class Divisible(Protocol):
    @property
    def subdivisions(self) -> list[DivisionBase]:
        ...

    def __iter__(self) -> Iterable[DivisionBase]:
        ...

    def get(self, func: Callable) -> Self:
        ...

    def search(self, search, func: Callable) -> Iterable[Self]:
        ...
