# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a state.

# A State is a complicated idea due to the different meanings
# in different areas of the world. They are most usually treated
# more like their own countries than something like a County,
# Parish, Shire.

# --- Imports --- #

from .divisions import Division

__all__ = ("State",)


# --- State Class --- #

class State(Division):
    pass
