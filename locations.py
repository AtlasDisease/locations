## Created By: Brendan (@AtlasDisease)
## Description: This module holds the Location type.
## These are for describing a location.
## This is similar to an address, but should be used for
## describing unknown depth of detail.
## Location().divisions[0] = smallest area (most detailed)
## Location().divisions[-1] = largest known area (least detailed)

# --- Imports --- #

from dataclasses import dataclass, field, KW_ONLY
from typing import Iterable, Self
from .divisions import Division, District, Neighborhood, City, County, State, \
     Country, Continent, Planet, PlanetarySystem, Galaxy, LocalGroup, \
     Supercluster, Universe

__all__ = ("Location",)


# --- Location Class --- #

@dataclass(slots = True)
class Location:
    """A standard location. This has values that can be set that are useful
in a majority of situations. If you have custom divisions use LocationIter."""
    name: str = ""
    _: KW_ONLY
    district: District | str = field(default="")
    neighborhood: Neighborhood | str = field(default="")
    city: City | str = field(default="")
    county: County | str = field(default="")
    state: State | str = field(default="")
    country: Country | str = field(default="")
    continent: Continent | str = field(default="")
    planet: Planet | str = field(default="")
    system: PlanetarySystem | str = field(default="")
    galaxy: Galaxy | str = field(default="")
    localgroup: LocalGroup | str = field(default="")
    supercluster: Supercluster | str = field(default="")
    universe: Universe | str = field(default="")

    def __post_init__(self):

        if self.name:
            return

        self.name = str(self.city)

    def __str__(self) -> str:
        return self.name

    def __format__(self, fmt: str = "") -> str:
        if fmt == ", ":
            fstring = fmt.join(
                    map(lambda loc: loc if isinstance(loc, str) else f"{loc: L}",
                    filter(lambda loc: str(loc), iter(self))))
            if self.city.name != self.name:
                return f"{self.name}{fmt}{fstring}"
            return fstring

        return str(self)

    def __iter__(self) -> Iterable[Division]:
        yield self.district
        yield self.neighborhood
        yield self.city
        yield self.county
        yield self.state
        yield self.country
        yield self.continent
        yield self.planet
        yield self.system
        yield self.galaxy
        yield self.localgroup
        yield self.supercluster
        yield self.universe


# --- LocationIter Class --- #

@dataclass(slots = True)
class LocationIter(Location):
    """A customizable location. The layout in self.divisions should be
in ascending order."""
    name: str = ""
    divisions: list[Division] = field(default_factory = list)

    def __post_init__(self):

        if not self.divisions:
            return
        
        self.divisions = list(filter(lambda loc: str(loc), self.divisions))
        #print(self.divisions)
        #self.divisions.sort()

        if self.name:
            return

        self.name = self.divisions[0].name

    def __str__(self) -> str:
        return ", ".join(map(lambda division: f"{division: L}".strip(),
                             self.divisions))

    def __iter__(self) -> Iterable:
        return self.divisions

    @staticmethod
    def fromLocation(location: Location) -> Self:
        return LocationIter(location.name, divisions=list(location))
