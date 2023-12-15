# --- Imports --- #

from dataclasses import dataclass
from .divisions import cities, counties, countries
from .zipcodes import ZipCode

__all__ = ("Address",)


# --- Address Class --- #

@dataclass(slots = True)
class Address:
	street: str
	city: cities.City
	county: counties.County
	country: countries.Country
	zipcode: ZipCode

	def __str__(self) -> str:
		return f"{self.street} {self.city}, {self.county}, {self.country} {self.zipcode}"

	# @staticmethod
	# def fromStr(string: str):

	# 	street, city, county, country, zipcode = re.split("[(,), ( )]", string)
	# 	return Address(street, city, county, country, zipcode)
