# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle banks.

# --- Imports --- #

import locale
from typing import Self, Optional, override

from .buildings import CommericalBuilding
from .rooms import Room

__all__ = ("CURRENCY_SIGNS", "Bank")


CURRENCY_SIGNS = {"$", "¢", "₡"}


# --- Bank Class --- #

class Bank(CommericalBuilding):
    def __init__(self, name: str,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 *,
                 cash_on_hand: float = 0,
                 **kwargs):
        super().__init__(name, subdivisions, **kwargs)

        self._cash_on_hand = cash_on_hand

    def __format__(self, format_spec=""):
        if not format_spec:
            return str(self)

        symbol = any((spec in CURRENCY_SIGNS for spec in format_spec))
        grouping = "," in format_spec or symbol
        international = not symbol
        return locale.currency(self._cash_on_hand, symbol=symbol, grouping=grouping, international=international)

    @property
    def cash_on_hand(self) -> float:
        return self._cash_on_hand

    def merge(self, bank: Self) -> None:
        self._cash_on_hand += bank.cash_on_hand
        
    
