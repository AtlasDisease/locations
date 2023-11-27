# Created By: Brendan (@atlasdisease)
# Copyright: None, would like credit though.
# Description: Custom enums and enum functionality.

# --- Imports --- #

from typing import Self
from enum import IntEnum as _IntEnum
from enum import StrEnum as _StrEnum
from enum import auto, unique

__all__ = ("StrEnum", "IntEnum", "UpgradableEnum",
           "OverflowUpgradableEnum", "auto", "unique")


### --- Enum Class --- #
##
##class Enum(_Enum):
##    pass


# --- StrEnum Class --- #

class StrEnum(_StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()


# --- IntEnum Class --- #

class IntEnum(_IntEnum):
    def __len__(self):
        return len(type(self))
    
    def __str__(self):
        return self.name.replace("_", " ").title()


# --- UpgradableEnum Class --- #

class UpgradableEnum(IntEnum):
    """Upgradable enum that has a limited range"""
    
    def __add__(self, other) -> Self:
        
        if isinstance(other, int):
            if other == len(self):
                return other
            
            other = type(self)(other)

        if other.value == len(self):
            return other
        
        other = self.value + other.value
        if other >= len(self):
            return type(self)(len(self))
        
        return type(self)(other)

    def __iadd__(self, other) -> Self:
        self = self + other
        return self


# --- OverflowUpgradableEnum Class --- #

class OverflowUpgradableEnum(IntEnum):
    """Upgradable enum that is allowed to overflow"""
    
    def __add__(self, other) -> Self:
        if isinstance(other, int):
            other %= len(self)
            if other == 0:
                other = len(self) - 1
            other = type(self)(other)

        other = self.value + other.value
        if other > len(self):
            other %= len(self)
            if other == 0:
                other = len(self) - 1
            
        return type(self)(other)

    def __iadd__(self, other) -> Self:
        self = self + other
        return self
