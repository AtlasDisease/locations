# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds information about goods and services.


# --- Imports --- #

from dataclasses import dataclass

__all__ = ("Good", "Service", "Tradeable")


# --- Good Class --- #

@dataclass(slots = True)
class Good:
    name: str
    price: int


# --- Service Class --- #

@dataclass(slots = True)
class Service:
    name: str
    price: int


# --- Sum Type --- #

type Tradeable = Good | Service
