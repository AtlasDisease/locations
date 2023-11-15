# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an emergency service.

# --- Imports --- #

from enum import IntEnum, auto
from .buildings import Building, BuildingTypes

__all__ = ("EmergencyService",)


# --- Emergency Service Enum --- #

class EmergencyServiceTypes(IntEnum):
    EMERGENCY = auto() #Generic
    POLICE = auto()
    FIRE = auto()
    HEALTH = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- EmergencyService Class --- #

class EmergencyService(Building):
    def __init__(self, name: str,
                 service: EmergencyServiceTypes = EmergencyServiceTypes.EMERGENCY,
                 **kwargs):

        super().__init__(name, BuildingTypes.COMMERICAL, **kwargs)

        self.service = service
