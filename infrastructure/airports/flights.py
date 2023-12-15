# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a flight.

# --- Imports --- #

import datetime as dt
from dataclasses import dataclass, field, KW_ONLY
from ...enum import IntEnum, auto
from ...locations import Location
from .airlines import Airline
from .airplanes import Airplane, Seat

__all__ = ("FlightStatus", "Flight")


# --- FlightStatus Enum --- #

class FlightStatus(IntEnum):
    CONFIRMED = auto()
    BOARDED = auto()
    IN_FLIGHT = auto()
    LANDED = auto()

    def __str__(self) -> str:
        return self.name.title().replace("_", " ")


# --- Flight Class --- #

@dataclass(slots = True)
class Flight:
    airline: Airline
    from_: Location
    to: Location   
    flight: int
    seats: list[Seat] = field(default_factory = list)
    equipment: Airplane = field(default_factory = Airplane)
    depart: dt.date = dt.date.min
    arrival: dt.date = dt.date.max
    status: FlightStatus = FlightStatus.CONFIRMED
    stops: int = 0
    _: KW_ONLY
    flight_time: dt.timedelta | None = None

    def __post_init__(self):
        if not self.flight_time:
            return

        if self.arrival == dt.date.max and self.flight_time:
            self.arrival = self.depart + self.flight_time

        if self.depart == dt.date.min and self.flight_time:
            self.depart = self.arrival - self.flight_time

    @property
    def duration(self) -> dt.timedelta:
        return arrival - depart

    @property
    def isNonstop(self) -> bool:
        return not bool(self.stops)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.flight}"

    def __format__(self, format_spec = "") -> str:
        if "d" in format_spec or "D" in format_spec:
            return f"""{self.airline.__class__.__name__}: {self.airline}
From: {self.from_}
To: {self.to}
Flight #: {self.flight}
Seat(s): {", ".join((str(seat) for seat in self.seats))}
Equipment: {self.equipment}
Depart:{self.depart: %D, %H:%M}
Arrival:{self.arrival: %D, %H:%M}
Status: {self.status}
Stops: {self.stops}"""

        return str(self)
