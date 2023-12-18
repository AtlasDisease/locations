# --- Imports --- #

from ..enum import StrEnum, auto, unique
from .buildings import Building


# --- PowerStationTypes Class --- #

@unique
class PowerStationTypes(StrEnum):
    COAL = auto()
    GAS = auto()
    NUCLEAR = auto()
    HYDROELECTRIC = auto()
    GEOTHERMAL = auto()
    BIOMASS = auto()
    SOLAR = auto()


# --- Power Station Class --- #

class PowerStation(Building):
    def __init__(self, name: str,
                 power: PowerStationTypes = PowerStationTypes.COAL,
                 *,
                 functioning: bool = True,
                 **kwargs):

        super().__init__(name, **kwargs)

        self.power_type = power
        self.functioning = functioning

    def __format__(self, format_spec = ""):
        if "F" in format_spec or "O" in format_spec:
            return f"{self.name} {self.power_type} Power Station"

        return str(self)
        
