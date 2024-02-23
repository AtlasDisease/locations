# --- Imports --- #

from .cities import City, AdministrativeTypes
from .counties import County

__all__ = ("IndependentCity",)


# --- IndependentCity Class --- #

class IndependentCity(City, County):
    """A city that is not in a county.
Ex. Baltimore, MD, US; Carson City, NV, US; Richmond, VA, US.
Implementation creates a City object then overrides with County functionality."""
    @property
    def admin_type(self) -> AdministrativeTypes:
        return self._admin_type
    
    @property
    def incorporated(self) -> bool:
        return self.type >= CityTypes.TOWN

    @property
    def abandoned(self)-> bool:
        return self.type < CityTypes.COMMUNITY \
               and self.type != CityTypes.UNKNOWN

    @property
    def historical(self) -> bool:
        return self.type == CityTypes.SITE

    @property
    def importance(self) -> int:
        """Returns the importance of the city.
This is mostly for debugging if there is an issue with the comparison functions."""
        return self._admin_type.value + self.type.value
