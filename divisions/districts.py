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
from ..subdivisions import SubdivisionTypes

__all__ = ("Neighborhood",)


# --- Neighborhood Class --- #

@dataclass(init = False)
class Neighborhood(Division):
    def __post_init__(self):

        self.type_ = SubdivisionTypes.NEIGHBORHOOD


# --- District Class --- #

@dataclass(init = False)
class District(Division):
    pass
