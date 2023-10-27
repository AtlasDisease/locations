# By: Brendan Beard
# Copyright: 2023
# Description: A module to handle a building. In my code this is
# called a place. To create your own class, you can subclass Place.
# You could allow an even smaller subdivision by adding the subdivisions
# parameter to the Place object when an instance is initialized.

# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes


# --- PlaceTypes Enum --- #

class PlaceTypes(StrEnum):
    BUILDING = auto() #General use
    CITY_HALL = auto()
    COURTHOUSE = auto()
    FORT = auto()
    AIRPORT = auto()

    def __str__(self):
        return self.name.replace("_", " ").title()


# --- Place Class --- #

class Place(Division):
    def __init__(self, name: str, type_: PlaceTypes, /, population: int = None, subdivisions: list[Division] | Division = None):

        super().__init__(name, type_, population, subdivisions)

    def __str__(self):
        if self.type_ == PlaceTypes.FORT:
            return f"{self.type_} {self.name}"
        return f"{self.name} {self.type_}"
