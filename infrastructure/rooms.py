# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a room. This is the smallest possible division in my package.

# --- Imports --- #

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

class Room:
    def __init__(self, name: str, type_: StrEnum):

        self.name = name
        self.type_ = type_
