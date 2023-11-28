# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a room. This is the smallest possible division in my package.

# --- Imports --- #

from dataclasses import dataclass, field
from ..enum import StrEnum, auto, unique


# --- RoomType Enum --- #

@unique
class RoomTypes(StrEnum):
    LIVING_ROOM = auto()
    KITCHEN = auto()
    MASTER_BEDROOM = auto()
    BEDROOM = auto()
    DINING_ROOM = auto()


# --- Room Class --- #

@dataclass
class Room:
    name: str
    type_: RoomTypes
