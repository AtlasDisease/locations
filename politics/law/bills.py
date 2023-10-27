# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds bill information.

# --- Imports --- #

from enum import StrEnum, auto


# --- BillStatus Enum --- #

class BillStatus(StrEnum):
    UNASSIGNED = auto()
    ASSIGNED = auto()
    VOTED = auto()
    PASSED = auto()
    ABSOLUTE = auto() #Given by God


# --- Bill Class --- #

class Bill:
    def __init__(self, name: str, status: BillStatus = BillStatus.UNASSIGNED, description: str = ""):

        self.name = name
        self.status = status
        self.description = description

    def __str__(self):
        return f"{self.name}:\r\n{self.description}"


# --- Constitution Class --- #

class Constitution:
    """Similar to the Law class but will be bills that are considered absolute"""
    
    def __init__(self, bills: list[Bill]):

        self.bills = bills

    def __str__(self):
        return "\r\n".join(self.bills)
