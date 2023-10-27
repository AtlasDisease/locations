# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module is for adding politics and governmental structure
# to divisions. You should use districts.details.add_government to add
# these classes to the divisions object.

# --- Imports --- #

from .leaders import Leader
from .economics import Economy
from .law import Law


# --- Government Class --- #

class Government:
    def __init__(self, leader: Leader, economy: Economy, law: Law):

        self.leader = leader
        self.economy = economy
        self.law = law

    def __str__(self):
        return f"{self.leader}\r\n{self.economy}\r\n{self.law}"
