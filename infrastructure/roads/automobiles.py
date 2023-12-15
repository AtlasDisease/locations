# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle an automobile, trucks, cars, etc.

# --- Imports --- #

from dataclasses import dataclass, KW_ONLY
from ...enum import StrEnum, auto, unique

__all__ = ("CarManufacturer", "TrailerTruckManufacturer",
           "AutomobilePowerType", "AutomobileManufacturer",
           "VehicleManufacturer", "Automobile", "Car",
           "Truck", "TrailerTruck")


# --- CarManufacturer Enum --- #

@unique
class CarManufacturer(StrEnum):
    UNKNOWN = auto() #General use
    BUICK = auto()
    CADILLAC = auto()
    CHEVROLET = auto()
    CHRYSLER = auto()
    DODGE = auto()
    FORD = auto()
    GM = auto()
    GMC = auto()
    HONDA = auto()
    HYUNDAI = auto()
    JEEP = auto()
    KIA = auto()
    LINCOLN = auto()
    RAM = auto()
    SUBARU = auto()
    TESLA = auto()


# --- TruckManufacturer Enum --- #

@unique
class TrailerTruckManufacturer(StrEnum):
    KENWORTH = auto()
    MACK = auto()
    PETERBILT = auto()


# --- AutomobilePowerType Enum --- #

@unique
class AutomobilePowerType(StrEnum):
    GAS = auto()
    DIESEL = auto()
    ELECTRIC = auto()


# --- AutomobileManufacturer Type --- #

type AutomobileManufacturer = CarManufacturer | TrailerTruckManufacturer | str


# --- VehicleManufacturer Type --- #

type VehicleManufacturer = AutomobileManufacturer | str
    

# --- Automobile Class --- #

@dataclass
class Automobile:
    year: int
    model: str
    make: AutomobileManufacturer = CarManufacturer.UNKNOWN
    type_: AutomobilePowerType = AutomobilePowerType.GAS
    _: KW_ONLY
    vin: str = ""
    wheels: int = 4

    def __post_init__(self):

        if len(self.vin) != 0 and len(self.vin) != 17:
            raise ValueError("Invalid length for a VIN number")

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def __format__(self, format_spec = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            return f"{str(self)} ({self.vin})"
        if "V" in format_spec:
            return self.vin
        return str(self)


# --- Car Class --- #

class Car(Automobile):
    pass


# --- Truck Class --- #

class Truck(Automobile):
    pass


# --- TrailerTruck Class --- #

class TrailerTruck(Truck):
    pass
    
