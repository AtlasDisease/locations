# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module is for adding politics and governmental structure
# to divisions. You should use districts.details.add_government to add
# these classes to the divisions object.

# --- Imports --- #

from dataclasses import dataclass
from .leaders import Leader, Administrator
from .economics import Economy
from .law import Law

__all__ = ("Government", "add_government", "add_administrator",)


# --- Government Class --- #

@dataclass(slots = True)
class Government:
    leader: Leader
    economy: Economy
    law: Law

    def __str__(self):
        return f"{self.leader}\r\n{self.economy}\r\n{self.law}"


# --- Extending Functionality Definitions --- #

def add_government(cls, govt: Government):
    cls.government = govt

def add_administrator(cls, admin: Administrator):
    cls.administrator = admin
