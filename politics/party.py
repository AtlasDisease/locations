# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module is for political parties.

# --- Imports --- #

from dataclasses import dataclass
from .leaders import Leader

__all__ = ("Party",)


# --- Party Class --- #

@dataclass(slots = True)
class Party:
    name: str
    chair_person: str
    candidate: Leader
    
    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"{self.name} Party"

        return str(self)
