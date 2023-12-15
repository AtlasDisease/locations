# --- Imports --- #

from dataclasses import dataclass, field
from ...enum import UpgradableEnum, auto, unique
from ...addresses import Address


# --- PackageTypes Enum --- #

@unique
class ShippingTypes(UpgradableEnum):
    STANDARD = auto()
    PRIORITY = auto()
    FIRST_CLASS = auto()


# --- Label Class --- #

@dataclass(slots = True)
class Label:
    name: str
    address: Address

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        return str(self)

    def __bool__(self) -> bool:
        return bool(self.name)


# --- Letter/Package Class --- #

@dataclass(slots = True)
class Letter:
    contents: str
    from_: Label = None
    to: Label = None
    shipping_type: ShippingTypes = ShippingTypes.STANDARD

    def __str__(self):
        return self.from_.name

    def __format__(self, format_spec = ""):
        return f"{self.from_.name}'s {self.__class__.__name__}"


@dataclass(slots = True)
class Package(Letter):
    contents: list[Letter]
    from_: Label
    to: Label
    shipping_type: ShippingTypes = ShippingTypes.STANDARD


type Sendable = Letter | Package #This probably needs to be a protocol at a later date
