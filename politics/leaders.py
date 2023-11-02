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
    REPUBLIC = auto()
    OLIGARCHY = auto()
    MONARCHY = auto()
    AUTHORITARIAN = auto()

    def __str__(self) -> str:
        return self.name.title()


# --- Administrator Class --- #

class Administrator:
    """A person in charge of a division without the need for a LeaderPolicy.
This is a simplified version of the Leader class.
A good use of this class would be a Chief of Police who has very little policy control
but has an administrative function."""

    __slots__ = ("name", "title")
    
    def __init__(self, name: str = "", title: str = "", /, leader = None):

        self.name = name
        self.title = title

        if (leader != None):
            self.name = leader.name
            self.title = leader.title

    def __str__(self):
        return f"{self.title} {self.name}".strip()


# --- Leader Class --- #

@dataclass(slots = True)
class Leader(Administrator):

    name: str
    policy: LeaderPolicy
    _: KW_ONLY
    title: str = "President"

    def as_Administrator(self) -> Administrator:
        return Administrator(self.name, self.title)
