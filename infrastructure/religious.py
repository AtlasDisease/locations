# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a religious aspects of buildings.

# --- Imports --- #

import datetime as dt
from typing import override, Iterable, Optional
from dataclasses import dataclass, field, KW_ONLY
from ..enum import StrEnum, auto, unique
from ..subdivisions import DivisionBase
from .rooms import Room
from ..timetable import Timeable, Timetable

__all__ = ("HouseOfWorship",)


# --- ReligionTypes Enum --- #

@unique
class ReligionTypes(StrEnum):
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


type ReligionType = ReligionTypes | str


# --- WorshipStructureTypes Enum --- #

@unique
class WorshipStructureTypes(StrEnum):
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


type WorshipStructure = WorshipStructureTypes | str


# --- DenominationTypes Enum --- #

@unique
class DenominationTypes(StrEnum):
    NONE = auto() #General use
    METHODIST = auto()
    PRESBYTERIAN = auto()
    BAPTIST = auto()
    LUTHERAN = auto()
    ANGLICAN = auto()
    PENTECOSTAL = auto()
    ORTHODOX = auto()
    CATHOLIC = auto()
    COPTIC = auto()
    NONDENOMINATIONAL = auto()


type Denomination = DenominationTypes | str


# --- Religion Class --- #

@dataclass(slots = True)
class Religion:
    
    type_: ReligionType
    structure: WorshipStructure
    _: KW_ONLY
    denomination: Denomination = DenominationTypes.NONE


# --- get_service_time Function --- #


def get_service_time(hour, minute = 0, day = 0):
    current = dt.datetime.now()
    day += current.day + (6 - current.weekday())
##    print(day)
    return dt.datetime(current.year, current.month, day, hour, minute)


# --- HouseOfWorship Class --- #

class HouseOfWorship(DivisionBase):
    def __init__(self,
                 name: str,
                 religion: Religion,
                 /,
                 subdivisions: Optional[list[Room]] = None,
                 *,
                 service_time: Timeable = field(default_factory = Timetable),
                 **kwargs):

        super().__init__(name, subdivisions)

        self.religion = religion

        if service_time:
            self.service_time = service_time

    @override
    def __format__(self, format_spec = "") -> str:
        if any(i in format_spec for i in {"F", "O", "L", "l"}):
            if self.religion.type_ == ReligionTypes.CHRISTIANITY:
                return f"{self.name} {self.religion.denomination} {self.religion.structure}"
            return f"{self.name} {self.religion.structure}"

        return str(self)

    @staticmethod
    def denominations(division,
                     denomination: DenominationTypes) -> Iterable:
        return filter(lambda x: x.religion.denomination == denomination,
                      (x for x in division if hasattr(x, "religion")))
    
    @staticmethod
    def religions(division, type_: ReligionTypes) -> Iterable:
        return filter(lambda x: x.religion.type_ == type_,
                      (x for x in division if hasattr(x, "religion")))

    @staticmethod
    def structures(division, structure: WorshipStructure) -> Iterable:
        return filter(lambda x: x.religion.structure == structure,
                      (x for x in division if hasattr(x, "religion")))

    def worship(self):

        if not self.service_time:
            raise Exception("A service time has not been set for this congregation.")
            
        if  self.service_time.start < dt.datetime.now().time < self.service_time.end:
            print("Worshiping...")
        else:
            print("Not worshiping...")
