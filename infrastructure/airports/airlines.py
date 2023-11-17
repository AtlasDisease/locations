# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an airline.

# --- Imports --- #

from dataclasses import dataclass, field, KW_ONLY
from ...positional import Location

__all__ = ("Airline",)


# --- Airline Class --- #

@dataclass
class Airline:
    name: str #I could make this an enum but I will let the user name things
    _: KW_ONLY
    callsign: str = ""
    alliance: str = ""
    IATA: str = "" #International Air Transport Association
    IACO: str = "" #International Civil Aviation Organization
    AOC: str = "" #Air Operator Certificate
    HQ: Location = field(default_factory = Location)
    hubs: list[Location] = field(default_factory = list)

    def __post_init__(self):

        self.IATA = self.IATA.upper()
        self.IACO = self.IACO.upper()
        self.callsign = self.callsign.upper()

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "C" in format_spec:
            return f"{self.name} ({self.callsign})"
        if "IATA" in format_spec:
            return f"{self.name} ({self.IATA})"
        if "IACO" in format_spec:
            return f"{self.name} ({self.IACO})"
        if "AOC" in format_spec:
            return f"{self.name} ({self.AOC})"
        if "A" in format_spec:
            return f"{self.name} ({self.alliance})"
        if "L" in format_spec:
            return f"{self.HQ}"

        return str(self)
