# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a galaxy.

# --- Imports --- #

from typing import override
from dataclasses import dataclass
from .divisions import Division, DivisionTypes

__all__ = ("Galaxy",)


# --- Galaxy Class --- #

@dataclass(init = False)
class Galaxy(Division):
    def __post_init__(self):
        
        self.type_ = DivisionTypes.GALAXY

    @override
    def __format__(self, format_spec = "") -> str:

        if "L" in format_spec or "l" in format_spec:
            return str(self)

        return Division.__format__(self, format_spec)
