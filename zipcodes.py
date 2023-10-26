## Created By: Brendan (@AtlasDisease)
## Description: This module holds the ZipCode type.
## These are for creating a zip code
## (this is also known as a postal code, post code, PIN, or mailing code).
## This is being improved upon as other countries have different
## styles of doing this.

from dataclasses import dataclass
from enum import Enum
import re


class ZipCodeTypes(Enum):
	AMERICA = "^(\d{5})(-?)((\d{5})?)"


@dataclass
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
