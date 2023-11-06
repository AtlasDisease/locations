
# --- Imports --- #

from dataclasses import dataclass


__all__ = ("Coordinates",)

# --- Coordinates Class --- #

@dataclass
class Coordinates:
	longitude: float
	latitude: float

	def __str__(self):
                return f"{self.longitude}, {self.latitude}"
