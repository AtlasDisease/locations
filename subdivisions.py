# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for connecting divisions and infrastructure packages.

# --- Imports --- #

from typing import Self, Callable, Iterable, Protocol, Optional, Type

__all__ = ("DivisionBase",)


# --- DivisionBase Class --- #

class DivisionBase:
    def __init__(self, name: str,
                 /,
                 _subdivisions: Optional[list[Type[Self]]] = None,
                 **kwargs):
        self.name = name
        self._subdivisions = list(_subdivisions) if _subdivisions else []

    @property
    def subdivisions(self) -> list[Self]:
        return self._subdivisions
    
    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec: str = "") -> str:
        if "O" in format_spec or "F" in format_spec: #Stands for "Formal" or "Official"
            return f"The {self.__class__.__name__} of {self.name}"
        
        if "L" in format_spec or "l" in format_spec: #Stands for "Location"
            return f"{self.name} {self.__class__.__name__}"
        return str(self)

    def __iter__(self):
        yield from self._subdivisions

    def __bool__(self) -> bool:
        return self.name != "New" and bool(self.name)

    def get(self, func: Callable) -> Self:
        """Gets a subdivision based of a certain function.
Ex. get largest or smallest subdivision by Population"""
        return func(self)

    def search(self, search, func: Callable):
        return func(self, search)

    @staticmethod
    def most_by(division: Self, attribute: str) -> Self:
        return max(division, key = lambda x: getattr(x, attribute, None))

    @staticmethod
    def least_by(division: Self, attribute: str) -> Self:
        return min(division, key = lambda x: getattr(x, attribute, None))

    @staticmethod
    def get_all_by(division: Self, attribute: str) -> Iterable[Self]:
        return filter(lambda x: getattr(x, attribute, None), division)


# --- Divisible Protocol --- #

class Divisible(Protocol):
    @property
    def subdivisions(self) -> list[Type[DivisionBase]]:
        ...

    def __iter__(self) -> Iterable[Type[DivisionBase]]:
        ...

    def get(self, func: Callable) -> Self:
        ...

    def search(self, search, func: Callable) -> Iterable[Self]:
        ...
