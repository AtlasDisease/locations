# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a railroad.

# --- Imports --- #

from dataclasses import dataclass
from ...enum import StrEnum, UpgradableEnum, auto, unique

__all__ = ("Railroad", "GaugeTypes")


# --- RoadType Enum --- #

@unique
class GaugeTypes(UpgradableEnum):
    STANDARD = auto()
    NARROW = auto()
    WIDE = auto()


# --- Railroad Class --- #

@dataclass
class Railroad:
    name: str
    type_: GaugeTypes = GaugeTypes.STANDARD

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "A" in format_spec:
            return self.abbreviation
        return str(self)

    @property
    def abbreviation(self) -> str:
        return "".join(name[0] for name in self.name.split('-'))


# --- Testing --- #

if __name__ == "__main__":

    rail = Railroad(name = "Missouri-Kansas-Texas", type_ = GaugeTypes.NARROW)
    print(repr(rail), str(rail.type_), str(rail.abbreviation), sep="\r\n")
