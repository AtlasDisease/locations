## Created By: Brendan (@AtlasDisease)
## Description: This module holds the ZipCode type.
## These are for creating a zip code
## (this is also known as a postal code, post code, PIN, or mailing code).
## This is being improved upon as other countries have different
## styles of doing this.

# --- Imports --- #

import re
import enum #Python's Enum module
from dataclasses import dataclass

__all__ = ("ZipCode", "ZipCodeTypes",)


# --- ZipCodeTypes Enum --- #

class ZipCodeTypes(enum.Enum):
    AMERICA = "^(\d{5})(-?)((\d{5})?)"


# --- ZipCode Class --- #

@dataclass(slots = True)
class ZipCode:
    zip_code: int
    type_: ZipCodeTypes

    def __post_init__(self):
        if (not re.fullmatch(self.type_.value, str(self.zip_code))):
            raise Exception("Zip code must be 5 numbers or 10 numbers.")

    def __len__(self):
        return len(str(self.zip_code))

    def __str__(self):
        match (self.type_):
            case ZipCodeTypes.AMERICA:
                if len(self) == 10:
                    return f"{str(self.zip_code)[:5]}-{str(self.zip_code)[5:]}"
                
        return str(self.zip_code)

    def __format__(self, format_spec = "") -> str:
        if "-" in format_spec:
            return f"{str(self.zip_code)[:5]}-{str(self.zip_code)[5:]}"

        return str(self)

    @property
    def national_area(self) -> int:
        return int(str(self.zip_code)[0])

    @property
    def sectional_center(self) -> int:
        """This will remove leading zeroes since it is a display concept not
a storage concept"""
        return int(str(self.zip_code)[1:3])

    @property
    def delivery_area(self) -> int:
        """This will remove leading zeroes since it is a display concept not
a storage concept"""
        return int(str(self.zip_code)[3:5])

    @property
    def specific_delivery_area(self) -> int:
        """Returns the specific delivery area (last 4 digits of 9 digit zip code)
if a 5 digit zip is given then it will return -1"""
        if len(str(self.zip_code)) != 9:
            return -1

        return int(str(self.zip_code)[5:])
