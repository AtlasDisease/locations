# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds information about the leader.

# --- Imports --- #

from enum import StrEnum, auto


# --- LeaderPolicy Enum --- #

class LeaderPolicy(StrEnum):
    NONE = auto()
    ANARCHY = auto()
    DEMOCRACY = auto()
    OLIGARCHY = auto()
    MONARCHY = auto()
    AUTHORITARIAN = auto()


# --- Administrator Class --- #

class Administrator:
    """A person in charge of a division without the need for a LeaderPolicy.
This is a simplified version of the Leader class.
A good use of this class would be a Chief of Police who has very little policy control
but has an administrative function."""
    
    def __init__(self, name: str, title: str = ""):

        self.name = name
        self.title = title

    def __str__(self):
        return f"{self.title} {self.name}".strip()


# --- Leader Class --- #

class Leader(Administrator):
    def __init__(self, name: str, policy: LeaderPolicy, title: str = "President"):

        super().__init__(name, title)
        self.policy = policy
