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


# --- Leader Class --- #

class Leader:
    def __init__(self, name: str, policy: LeaderPolicy, title: str = "President"):

        self.name = name
        self.title = title
        self.policy = policy

    def __str__(self):
        return f"{self.title} {self.name}"
