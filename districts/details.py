# By: Brendan Beard
# Copyright: 2023
# Description: This module contains classes that help extend functionality
# of a class in the districts package.

__all__ = ("Population",)


# --- Population Class --- #

class Population(int):
    """Basically an integer but with formatting when converted to string"""
    
    def __init__(self, population: int = 0):

        super().__init__()

    def __str__(self) -> str:
        return f"{self: ,}"


### --- Subdivision Class --- #
##
##class Subdivisions(list):
##    def __init__(self, *args):
##
##        super().__init__()
##        self.extend(args)
##
##    def __str__(self):
##        return f"{[str(subdivision) for subdivision in self]}"
