# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a planet.

# --- Imports --- #

from typing import override
from .divisions import Division

__all__ = ("Planet",)


# --- Planet Class --- #

class Planet(Division):

    @override
    def __format__(self, format_spec = "") -> str:

        if "L" in format_spec or "l" in format_spec:
            return str(self)

        return Division.__format__(self, format_spec)
