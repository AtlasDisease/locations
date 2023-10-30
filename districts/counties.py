# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes
        

# --- County Class --- #

class County(Division):
    def __init__(self, name: str, /,
                 population: int = None,
                 subdivisions: list[Division] | Division = None,
                 **kwargs):

        super().__init__(name, DivisionTypes.COUNTY, population, subdivisions, **kwargs)

    def __str__(self):
        return f"{self.name} {self.__class__.__name__}"


class Parish(County): #French version of a County
    pass


class Shire(County): #English version of a County
    pass
