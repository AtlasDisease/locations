# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an emergency service.

# --- Imports --- #

from enum import IntEnum, auto
from .places import Place, PlaceTypes

__all__ = ("EmergencyService",)


# --- Emergency Service Enum --- #

class EmergencyServiceTypes(IntEnum):
    POLICE = auto()
    FIRE = auto()
    HEALTH = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- EmergencyService Class --- #

class EmergencyService(Place):
    def __init__(self, name: str, service: EmergencyServiceTypes, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.EMERGENCY_SERVICE, population, **kwargs)

        self.service = service
