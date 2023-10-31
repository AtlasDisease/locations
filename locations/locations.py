## Created By: Brendan (@AtlasDisease)
## Description: This module holds the Location type.
## These are for describing a location.
## This is similar to an address, but should be used for
## describing unknown depth of detail.
## Location().divisions[0] = smallest area (most detailed)
## Location().divisions[-1] = largest known area (least detailed)

# --- Imports --- #

from dataclasses import dataclass, field

__all__ = ("Location",)


# --- Location Class --- #

@dataclass
class Location:
	name: str
	divisions: list = field(default_factory=list)

	def __str__(self):
		return ", ".join((f"{division}" for division in self.divisions))
