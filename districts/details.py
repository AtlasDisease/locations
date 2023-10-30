# By: Brendan Beard
# Copyright: 2023
# Description: This module contains classes that help extend functionality
# of a class in the districts package.

# --- Population Class --- #

class Population(int):
    """Basically an integer but with formatting when converted to string"""
    
    def __init__(self, population: int = 0):

        super().__init__()

    def __str__(self):
        return f"{self: ,}"
