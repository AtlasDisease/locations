## Created By: Brendan (@AtlasDisease)
## Description: This module holds the ZipCode type.
## These are for creating a zip code
## (this is also known as a postal code, post code, PIN, or mailing code).
## This is being improved upon as other countries have different
## styles of doing this.

# --- Imports --- #

import re, warnings
import enum #Python's Enum module
from dataclasses import dataclass

__all__ = ("ZipCode", "ZipCodeTypes",)


# --- ZipCode4Warning Warning --- #

class ZipCode4Warning(UserWarning):
    pass


# --- ZipCodeFormatError --- #

class ZipCodeFormatError(ValueError):
    pass


# --- ZipCodeTypes Enum --- #

class ZipCodeTypes(enum.Enum):
    AMERICA = "^(\\d{5})(-?)((\\d{4})?)"


# --- ZipCode Class --- #

@dataclass(slots = True)
class ZipCode:
    zip_code: str
    type_: ZipCodeTypes

    def __post_init__(self):
        if (not re.fullmatch(self.type_.value, self.zip_code)):
            raise ZipCodeFormatError("Zip code must be in the correct format.")

        self.zip_code = self.zip_code.replace("-", "")

        if len(self.zip_code) == 9:
            warnings.warn(
                ZipCode4Warning("ZipCode+4 is not in widespread use.\r\n"))

    def __len__(self) -> int:
        return len(self.zip_code)

    def __str__(self) -> str:
        match (self.type_):
            case ZipCodeTypes.AMERICA:
                if len(self) == 9:
                    return f"{self.zip_code[:5]}-{self.zip_code[5:]}"
                
        return self.zip_code

    def __int__(self) -> int:
        return int(self.zip_code)

    def __format__(self, format_spec = "") -> str:
        if "-" in format_spec:
            return f"{self.zip_code[:5]}-{self.zip_code[5:]}"

        return str(self)

    @property
    def national_area(self) -> str:
        return self.zip_code[0]

    @property
    def sectional_center(self) -> str:
        """This will remove leading zeroes since it is a display concept not
a storage concept"""
        return self.zip_code[1:3]

    @property
    def delivery_area(self) -> str:
        """This will remove leading zeroes since it is a display concept not
a storage concept"""
        return self.zip_code[3:5]

    @property
    def specific_delivery_area(self) -> str:
        """Returns the specific delivery area (last 4 digits of 9 digit zip
code) if a 5 digit zip is given then it will return an empty string"""
        if len(self.zip_code) != 9:
            return ""

        return self.zip_code[5:]
