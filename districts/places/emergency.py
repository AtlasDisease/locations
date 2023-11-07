# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an emergency service.

# --- Imports --- #

from enum import IntEnum, auto


# --- Emergency Service Enum --- #

class EmergencyServiceTypes(IntEnum):
    POLICE = auto()
    FIRE = auto()
    HEALTH = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()
