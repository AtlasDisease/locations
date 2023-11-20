# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds information about trade.


# --- Imports --- #

from dataclasses import dataclass
from .tradeable import Tradeable

__all__ = ("Trade",)


# --- Trade Class --- #

@dataclass(slots = True)
class Trade:
    receiving: Tradeable
    giving: Tradeable
    receive_amount: int = 1
    giving_amount: int = 1

    def difference(self) -> int:
        return (self.receiving.price * self.receive_amount) \
               - (self.giving.price * self.giving_amount)
    
