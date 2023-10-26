# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes, add_population, add_subdivisions


# --- PlaceTypes Enum --- #

class PlaceTypes(StrEnum):
    BUILDING = auto()
    CITY_HALL = auto()
    COURTHOUSE = auto()
    FORT = auto()
    AIRPORT = auto()

    def __str__(self):
        return self.name.replace("_", " ").title()


# --- Place Class --- #

class Place(Division):
    def __init__(self, name: str, type_: PlaceTypes):

        super().__init__(name, DivisionTypes.BUILDING, type_)
