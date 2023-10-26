# --- Imports --- #

from enum import StrEnum, auto
    

# --- DivisionTypes Enum --- #

class DivisionTypes(StrEnum):
    BUILDING = auto()
    NEIGHBORHOOD = auto()
    CITY = auto()
    COUNTY = auto()
    STATE = auto()
    COUNTRY = auto()
    CONTINENT = auto()
    PLANET = auto()
    SOLAR_SYSTEM = auto()
    UNIVERSE = auto()

    def __str__(self):
        return self.name.title()


# --- Division Class --- #

class Division:
    def __init__(self, name: str, type_: DivisionTypes):

        self.name = name
        self.type_ = type_

    def __str__(self):
        return f"The {self.type_} of {self.name}"


# --- Extending Functionality Definitions --- #

def add_population(cls, population: int):
    cls.population = population

def add_subdivisions(cls, subdivisions: list[Division] | Division):
    if not hasattr(cls, "subdivisions"):
        cls.subdivisions = []
        
    if isinstance(subdivisions, list):
        cls.subdivisions.extend(subdivisions)
        return

    cls.subdivisions.append(subdivisions)
