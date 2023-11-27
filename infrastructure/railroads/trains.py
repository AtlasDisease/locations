# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a train.

# --- Imports --- #

import sys
from typing import override
from dataclasses import dataclass, field
from ...enum import IntEnum, StrEnum, auto, unique

__all__ = ("Train", "PowerType", "UsageType",
"FreightOperators", "PassengerOperators", "Operators")


# --- PowerType Enum --- #

@unique
class PowerType(IntEnum):
    STEAM = auto()
    DIESEL = auto()
    ELECTRIC = auto()
    GAS_TURBINE = auto()
    HYDROGEN = auto()
    NATURAL_GAS = auto()

    def __str__(self):
        return self.name.replace("_", " ").title()


# --- Usage Type --- #

@unique
class UsageType(StrEnum):
    PASSENGER = auto()
    RAPID_TRANSIT = auto() #Basically, passenger but more specific
    FREIGHT = auto()
    MILITARY = auto()


# --- FreightOperators Enum --- #

@unique
class FreightOperators(StrEnum):
    OTHER = auto() #General use
    BNSF = auto()
    UNION_PACIFIC = auto()
    KANSAS_CITY_SOUTHERN = auto()
    SANTA_FE = auto()
    MILITARY = auto() #Only should be used with the Military UsageType


# --- PassengerOperators Enum --- #

@unique
class PassengerOperators(StrEnum):
    OTHER = auto() #General use
    AMTRAK = auto()


# --- Operators Type --- #

type Operators = PassengerOperators | FreightOperators | str


# --- Train Class --- #

class Train:
    def __init__(self, name: str, /, type_: UsageType = UsageType.FREIGHT, power_type: PowerType = PowerType.DIESEL, operator: Operators = ""):
        self.name = name
        self.type_ = type_
        self.power_type = power_type

        # Try to determine operator if operator is not given
        self.operator = operator
        if not self.operator and self.type_ == UsageType.FREIGHT:
            self.operator = FreightOperators.OTHER
        if not self.operator and (self.type_ == UsageType.PASSENGER or self.type_ == UsageType.RAPID_TRANSIT):
            self.operator = PassengerOperators.OTHER
        if not self.operator and self.type_ == UsageType.MILITARY:
            self.operator = FreightOperators.MILITARY

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "O" in format_spec or "F" in format_spec:
            return f"The {self.name}"

        return str(self)
