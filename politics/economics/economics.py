# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds information about economics.


# --- Imports --- #

from enum import StrEnum, auto
from dataclasses import dataclass, field

__all__ = ("EconomicPolicy", "Economy")


# --- EconomicPolicy Enum --- #

class EconomicPolicy(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
    NONE = auto()
    CAPITALIST = auto()
    SOCIALIST = auto()
    COMMUNIST = auto()


# --- Economy Class --- #

@dataclass(slots = True)
class Economy:
    
    policy: EconomicPolicy

    def __str__(self):
        return str(self.policy)
