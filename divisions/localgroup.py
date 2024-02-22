# Created By: Brendan (@atlasdisease)
# Copyright: 2024
# Description: A module to handle a localgroup.

# --- Imports --- #

from typing import override
from .divisions import Division

__all__ = ("LocalGroup",)


# --- LocalGroup Class --- #

class LocalGroup(Division):
    def __format__(self, format_spec = ""):
        if "l" in format_spec or "L" in format_spec:
            return f"{self.name} Local Group"

        return str(self)
