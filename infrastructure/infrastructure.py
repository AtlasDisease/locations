# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle infrastructure.

# --- Imports --- #

from typing import override
from .buildings import Building

__all__ = ("CityHall", "Courthouse",
           "Port", "Bank", "Hospital")
    

# --- CityHall Class --- #

class CityHall(Building):
    
    @override
    def __format__(self, format_spec = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"The City Hall of {self.name}"
        if "L" in format_spec or "l" in format_spec:
            return f"{self.name} City Hall"

        return str(self.name)


# --- Courthouse Class --- #

class Courthouse(Building):
    pass


# --- Port Class --- #

class Port(Building):
    pass


# --- Bank Class --- #

class Bank(Building):
    pass


# --- Hospital Class --- #

class Hospital(Building):
    pass
