# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds law information.

# --- Imports --- #

from ...enum import StrEnum, auto, unique
from .bills import Bill

__all__ = ("LawPolicy", "Law")


# --- LawPolicy Enum --- #

@unique
class LawPolicy(StrEnum):   
    NONE = auto()
    REHABILITATION = auto()
    FAIR_AND_JUST = auto()
    EYE_FOR_AN_EYE = auto()
    LAW_AND_ORDER = auto()
    

# --- Law Class --- #

class Law:
    def __init__(self, policy: LawPolicy, /, bills: list[Bill] = None):

        self.policy = policy
        self.bills = bills if bills else []

    def __str__(self):
        return "\r\n\r\n".join((str(bill) for bill in self.bills))
