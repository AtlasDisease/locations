# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a building. In my code this is
# called a place. To create your own class, you can subclass Place.
# A place is supposed to be the smallest unit therefore it should
# not have subdivisions.

# --- Imports --- #

from enum import IntEnum, auto
from .divisions import Division, DivisionTypes

__all__ = ("PlaceTypes", "ReligionTypes", "WorshipTypes",
           "Place", "Building", "Stadium",
           "CityHall", "Courthouse", "Fort", "Port", "Airport",
           "HouseOfWorship", "Cemetery", "Bank",
           "EmergencyService", "Hospital", "PostOffice")


# --- PlaceTypes Enum --- #

class PlaceTypes(IntEnum):
    BUILDING = auto() #General use
    STADIUM = auto()
    CITY_HALL = auto()
    COURTHOUSE = auto()
    FORT = auto()
    PORT = auto()
    AIRPORT = auto()
    HOUSE_OF_WORSHIP = auto()
    CEMETERY = auto()
    BANK = auto()
    EMERGENCY_SERVICE = auto()
    HOSPITAL = auto()
    POST_OFFICE = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- ReligionTypes Enum --- #

class ReligionTypes(IntEnum):
    UNKNOWN = auto() #General use
    ATHEIST = auto()
    CHRISTIANITY = auto()
    JEWISH = auto()
    MUSLIM = auto()
    BUDDHIST = auto()
    HINDU = auto()
    PAGAN = auto()
    JAINISM = auto()
    SHINTO = auto()
    SIKHISM = auto()
    TAOISM = auto()
    ZOROASTRIANISM = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- WorshipTypes Enum --- #

class WorshipTypes(IntEnum): #Structure Type
    TEMPLE = auto() #General use, Hinduism, Buddhism, Ancient Religions
    CHURCH = auto() # Christianity
    CATHEDRAL = auto() # Christianity
    CHAPEL = auto() # Christianity
    HALL = auto() # Christianity
    SYNAGOGUE = auto() #Jewish
    MOSQUE = auto() #Islam
    DERASAR = auto() #Jainism
    BASADI = auto() #Same as DERASAR
    MANDI = auto() #Mandaeism
    MASHKHANNA = auto() # Same as MANDI
    BETH_MANDA = auto() # Same as MANDI
    HOF = auto() #Norse paganism
    JINJA = auto() #Shinto
    GURDWARA = auto() #Sikhism
    DAOGUAN = auto() #Taoism
    ATASH_BEHRAM = auto() #Zoroastrianism
    AGYARI = auto() #Zoroastrianism
    DADGAH = auto() #Zoroastrianism
    
    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- Place Class --- #

class Place:
    def __init__(self, name: str,
                 type_: PlaceTypes = PlaceTypes.BUILDING,
                 /,
                 population: int = None, 
                 **kwargs):

        self.name = name
        self.type_ = type_

        if (population != None):
            add_population(self, population)

    def __str__(self) -> str:
        return self.name
    
    def __format__(self, format_spec: str = "") -> str:
        if "F" in format_spec or "O" in format_spec:
            if self.type_ == PlaceTypes.FORT:
                return f"{self.type_.replace('_', ' ')} {self.name}"
            return f"{self.name} {self.type_.replace('_', ' ')}"

        return str(self)

    def __bool__(self) -> bool:
        return self.name != "New" and self.name != "" \
               and self.type_ != PlaceTypes.BUILDING
        

# --- Building Class --- #

class Building(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.BUILDING, population, **kwargs)


# --- Stadium Class --- #

class Stadium(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.STADIUM, population, **kwargs)


# --- CityHall Class --- #

class CityHall(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.CITY_HALL, population, **kwargs)


# --- Courthouse Class --- #

class Courthouse(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.COURTHOUSE, population, **kwargs)


# --- Fort Class --- #

class Fort(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.FORT, population, **kwargs)


# --- Port Class --- #

class Port(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.PORT, population, **kwargs)
        

# --- Airport Class --- #

class Airport(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.AIRPORT, population, **kwargs)


# --- HouseOfWorship Class --- #

class HouseOfWorship(Place):
    def __init__(self, name: str,
                 religion_type: ReligionTypes = ReligionTypes.UNKNOWN,
                 worship_type: WorshipTypes = WorshipTypes.TEMPLE,
                 /,
                 population: int = None,
                 **kwargs):

        super().__init__(name, PlaceTypes.HOUSE_OF_WORSHIP, population, **kwargs)

        self.religion_type = religion_type
        self.worship_type = worship_type


# --- Cemetery Class --- #

class Cemetery(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.CEMETERY, population, **kwargs)


# --- Bank Class --- #

class Bank(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.BANK, population, **kwargs)


# --- EmergencyService Class --- #

class EmergencyService(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.EMERGENCY_SERVICE, population, **kwargs)


# --- Hospital Class --- #

class Hospital(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.HOSPITAL, population, **kwargs)


# --- PostOffice Class --- #

class PostOffice(Place):
    def __init__(self, name: str, /, population: int = None, **kwargs):

        super().__init__(name, PlaceTypes.POST_OFFICE, population, **kwargs)
