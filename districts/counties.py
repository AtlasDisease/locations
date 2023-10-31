# --- Imports --- #

from enum import StrEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("County", "Parish", "Shire")
        

# --- County Class --- #

class County(Division):
    def __init__(self, name: str, /,
                 subdivisions: list[Division] | Division = None,
                 population: int = None,   
                 **kwargs):

        super().__init__(name, DivisionTypes.COUNTY, subdivisions, population, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} {self.__class__.__name__}"


class Parish(County): #French version of a County
    pass


class Shire(County): #English version of a County
    pass
