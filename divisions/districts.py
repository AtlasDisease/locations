# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a group of buildings that are
# collectively named and used for a similar purpose. To create
# your own you can subclass the Division class and create a
# Types enum for the type of area.

# --- Imports --- #

from .divisions import Division

__all__ = ("Neighborhood", "District")


# --- Neighborhood Class --- #

class Neighborhood(Division):
    pass


# --- District Class --- #

class District(Division):
    pass
