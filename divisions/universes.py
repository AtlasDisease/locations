# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a universe.

# --- Imports --- #

from typing import override
from .divisions import Division

__all__ = ("Universe",)


# --- Universe Class --- #

class Universe(Division):

    @override
    def __str__(self):
        return f"{self.name} {self.__class__.__name__}".strip()
