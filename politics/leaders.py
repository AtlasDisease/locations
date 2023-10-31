# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds information about the leader.

# --- Imports --- #

from enum import StrEnum, auto
from dataclasses import dataclass, field, KW_ONLY

__all__ = ("LeaderPolicy", "Administrator", "Leader",)


# --- LeaderPolicy Enum --- #

class LeaderPolicy(StrEnum):
    NONE = auto()
    ANARCHY = auto()
    DEMOCRACY = auto()
    OLIGARCHY = auto()
    MONARCHY = auto()
    AUTHORITARIAN = auto()


# --- Administrator Class --- #

@dataclass(slots = True)
class Administrator:
    """A person in charge of a division without the need for a LeaderPolicy.
This is a simplified version of the Leader class.
A good use of this class would be a Chief of Police who has very little policy control
but has an administrative function."""

    name: str
    title: str = ""
    
    def __str__(self):
        return f"{self.title} {self.name}".strip()


# --- Leader Class --- #

@dataclass(slots = True)
class Leader(Administrator):

    name: str
    policy: LeaderPolicy
    _: KW_ONLY
    title: str = "President"
