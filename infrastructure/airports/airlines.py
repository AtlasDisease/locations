# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an airline.

# --- Imports --- #

from dataclasses import dataclass

__all__ = ("Airline",)


# --- Airline Class --- #

@dataclass
class Airline:
    name: str #I could make this an enum but I will let the user name things

    def __str__(self) -> str:
        return self.name
