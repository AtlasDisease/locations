# --- Imports --- #

from dataclasses import dataclass, field
from typing import Iterable
from ...locations import Location


# --- Wildfire Class --- #

@dataclass
class Wildfire:
    """A wildfire. Size should be in acres, but this is not enforced currently."""
    name: str
    size: float = field(default=0)
    locations: list[Location] = field(default_factory=list)
    containment: int | float = field(default=0)

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if any((char in {"F", "O", "L", "l"} for char in format_spec)):
            return f"{self.name} {self.__class__.__name__}"

        return str(self)

    def __int__(self) -> int:
        return int(self.size)

    def __float__(self) -> float:
        return self.size

    def __iter__(self) -> Iterable:
        yield from self.locations

    def add_location(self, location):
        self.locations.append(location)


if __name__ == "__main__":
    def main():
        wildfire = Wildfire("Smokehouse Creek", 850_000)
        print(f"{wildfire: O}")
        print(f"{wildfire.size:,d}")
        print(f"{wildfire.size:,.2f}")
        print(list(iter(wildfire)))
    
    main()
