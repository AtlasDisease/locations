# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds information about economics.


# --- Imports --- #

from enum import IntEnum, auto
from dataclasses import dataclass, field

__all__ = ("EconomicPolicy", "Economy")


# --- EconomicPolicy Enum --- #

class EconomicPolicy(IntEnum):
    NONE = auto()
    CAPITALIST = auto()
    SOCIALIST = auto()
    COMMUNIST = auto()

    def __str__(self) -> str:
        return self.name.title()


# --- Economy Class --- #

@dataclass(slots = True)
class Economy:
    
    policy: EconomicPolicy

    def __str__(self):
        return str(self.policy)
