# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds information about economics.


# --- Imports --- #

from enum import StrEnum, auto


# --- EconomicPolicy Enum --- #

class EconomicPolicy(StrEnum):
    NONE = auto()
    CAPITALIST = auto()
    SOCIALIST = auto()
    COMMUNIST = auto()


# --- Economy Class --- #

class Economy:
    def __init__(self, policy: EconomicPolicy):

        self.policy = policy

    def __str__(self):
        return self.policy.value.title()
