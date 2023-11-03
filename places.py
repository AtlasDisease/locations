# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a building. In my code this is
# called a place. To create your own class, you can subclass Place.
# A place is supposed to be the smallest unit therefore it should
# not have subdivisions.

# --- Imports --- #

from enum import IntEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("PlaceTypes", "Place")


# --- PlaceTypes Enum --- #

class PlaceTypes(IntEnum):
    BUILDING = auto() #General use
    STADIUM = auto()
    CITY_HALL = auto()
    COURTHOUSE = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()
    HOUSE_OF_WORSHIP = auto()
    CEMETERY = auto()
    BANK = auto()
    EMERGENCY_SERVICE = auto()
    HOSPITAL = auto()
    POST_OFFICE = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- Place Class --- #

class Place:
    def __init__(self, name: str, type_: PlaceTypes, /,
                 population: int = None, 
                 **kwargs):

        self.name = name
        self.type_ = type_

        if (population != None):
            add_population(self, population)

    def __str__(self) -> str:
        if self.type_ == PlaceTypes.FORT:
            return f"{self.type_} {self.name}"
        return f"{self.name} {self.type_}"


# --- Building Class --- #

class Building(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.BUILDING, population, **kwargs)


# --- Stadium Class --- #

class Stadium(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.STADIUM, population, **kwargs)


# --- City_Hall Class --- #

class City_Hall(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.CITY_HALL, population, **kwargs)


# --- Courthouse Class --- #

class Courthouse(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.COURTHOUSE, population, **kwargs)


# --- Fort Class --- #

class Fort(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.FORT, population, **kwargs)


# --- Port Class --- #

class Port(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.PORT, population, **kwargs)


# --- Airport Class --- #

class Airport(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.AIRPORT, population, **kwargs)


# --- House_Of_Worship Class --- #

class House_Of_Worship(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.HOUSE_OF_WORSHIP, population, **kwargs)


# --- Cemetery Class --- #

class Cemetery(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.CEMETERY, population, **kwargs)


# --- Bank Class --- #

class Bank(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.BANK, population, **kwargs)


# --- Emergency_Service Class --- #

class Emergency_Service(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.EMERGENCY_SERVICE, population, **kwargs)


# --- Hospital Class --- #

class Hospital(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.HOSPITAL, population, **kwargs)


# --- Post_Office Class --- #

class Post_Office(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.POST_OFFICE, population, **kwargs)
