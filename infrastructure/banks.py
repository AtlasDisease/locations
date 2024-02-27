# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle banks.

# --- Imports --- #

from typing import Self, Optional, override
from .buildings import CommericalBuilding
from .rooms import Room


# --- Money Class --- #

class Money(float):
    def __init__(self, value: float):
        super().__init__()

##    def __str__(self):
##        print("Hello World!")
##        return "{self:,.2f}"
##
##    def __format__(self, format_spec = ""):
##        print("Hello World")
##        return "{self:,.2f}"


# --- Bank Class --- #

class Bank(CommericalBuilding):
    def __init__(self, name: str,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 *,
                 cash_on_hand: Money = Money(0),
                 **kwargs):
        super().__init__(name, subdivisions, **kwargs)

        self._cash_on_hand = cash_on_hand

    @property
    def cash_on_hand(self) -> Money:
        return self._cash_on_hand

    def merge(self, bank: Self) -> None:
        self._cash_on_hand += bank.cash_on_hand
        
    
