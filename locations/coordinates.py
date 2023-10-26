from dataclasses import dataclass


@dataclass
class Coordinates:
	longitude: float
	latitude: float

	def __str__(self):
		return f"{self.longitude}, {self.latitude}"
