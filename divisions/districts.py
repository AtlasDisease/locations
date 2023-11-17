# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a group of buildings that are
# collectively named and used for a similar purpose. To create
# your own you can subclass the Division class and create a
# Types enum for the type of area.

# --- Imports --- #

from enum import StrEnum, auto
from dataclasses import dataclass
from .divisions import Division

__all__ = ("AreaTypes", "District", "Neighborhood")


# --- AreaTypes Enum --- #

class AreaTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
    NEIGHBORHOOD = auto() #General use
    SCHOOL = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()
    CEMETERY = auto()


# --- District Class --- #

class District(Division): #A type that can have subdivisions or not
    def __init__(self, name: str, type_: StrEnum = AreaTypes.NEIGHBORHOOD,
                 /,
                 subdivisions: list = None,
                 *,
                 population: int = None,
                 **kwargs):
        super().__init__(name, type_, subdivisions, population = population)
        # Do not give super() the kwargs as the only valid extensions for a
        # district are listed as keyword arguments above

        if kwargs:
            self.__dict__ |= kwargs

    def __format__(self, format_spec = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.type_.name == "FORT":
                return f"{self.type_} {self.name}"
            return f"{self.name} {self.type_}"
        
        return str(self)

    @property
    def hasSubdivisions(self) -> bool:
        return bool(self.subdivisions)


# --- Neighborhood Class --- #

@dataclass(init = False)
class Neighborhood(District):
    def __post_init__(self):

        self.type_ = AreaTypes.NEIGHBORHOOD
