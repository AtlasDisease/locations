# --- Imports --- #

from dataclasses import dataclass
from .divisions.cities import City, AdministrativeTypes
from locations import Location
from .infrastructure.courthouses import Courthouse, CourthouseTypes


# --- InvalidInfrastructureError Class --- #

class CityError(ValueError):
    pass


# --- InvalidInfrastructureError Class --- #

class InvalidInfrastructureError(ValueError):
    pass


# --- AdministrativeDistrict Class --- #

@dataclass(slots = True)
class AdministrativeDistrict:
    location: Location

    @property
    def type(self):
        if self.location.city is None:
            return None
        
        return self.location.city.admin_type

    @staticmethod
    def construct_courthouse(name: str, where: City, type_: AdministrativeTypes):
        """Construct a courthouse.
'where' must be a City and 'type_' must be in 'where'.admin_type"""
        if where is None:
            raise CityError("City is none. Cannot determine whether courthouse is valid. Cancelling construction.")
            
        if type_ not in where.admin_type:
            raise InvalidInfrastructureError("Courthouse type is invalid with city's administrative type. Cancelling construction.")

        where.subdivisions.append(Courthouse(name, CourthouseTypes.DISTRICT))
    
