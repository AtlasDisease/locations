# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds bill information.

# --- Imports --- #

from dataclasses import dataclass, field
from ...enum import StrEnum, auto, unique

__all__ = ("BillStatus", "Bill", "Constitution")


# --- BillStatus Enum --- #

@unique
class BillStatus(StrEnum):
    UNASSIGNED = auto()
    ASSIGNED = auto()
    VOTED = auto()
    PASSED = auto()
    ABSOLUTE = auto() #Given by God


# --- Bill Class --- #

@dataclass(slots = True)
class Bill:

    name: str
    status: BillStatus = BillStatus.UNASSIGNED
    description: str = ""

    def __str__(self):
        return f"{self.name}:\r\n{self.description}"


# --- Constitution Class --- #

@dataclass(slots = True)
class Constitution:
    """Similar to the Law class but will be bills that are considered absolute"""
    
    bills: list[Bill] = field(default_factory=list)

    def __str__(self):
        return "\r\n".join(self.bills)
