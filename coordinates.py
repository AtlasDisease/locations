
# --- Imports --- #

from dataclasses import dataclass


__all__ = ("Coordinates",)

# --- Coordinates Class --- #

@dataclass(slots = True)
class Coordinates:
    longitude: float
    latitude: float
    
    def __str__(self):
        return f"{self.longitude}, {self.latitude}"

    def __iter__(self):
        yield self.longitude
        yield self.latitude
