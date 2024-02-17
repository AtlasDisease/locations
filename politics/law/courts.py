# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This module holds court information.

# --- Imports --- #

import datetime as dt
from dataclasses import dataclass, field, KW_ONLY


# --- Court Class --- #

@dataclass(slots=True)
class Court:
    name: str
    judge: str


# --- Sentence Class --- #

class Sentence(dt.timedelta):
    def __init__(self, years = 0, **kwargs):

        if "days" in kwargs:
            days = kwargs["days"]

        if years:
            days += years * 365
            
        super().__init__(**kwargs)


def sue(prosecutor: str, defense: str, court: Court) -> bool:
    return True
