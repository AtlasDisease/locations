# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a religious aspects of buildings.

# --- Imports --- #

from typing import override, Iterable
from ..enum import StrEnum, auto, unique
from dataclasses import dataclass, KW_ONLY
from .buildings import Building, BuildingTypes

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
    denomination: Denomination


# --- HouseOfWorship Class --- #

class HouseOfWorship(Building):
    def __init__(self, name: str, religion: Religion,
                 **kwargs):

        super().__init__(name, BuildingTypes.COMMERICAL)

        self.religion = religion

    @override
    def __format__(self, format_spec = "") -> str:
        if any(i in format_spec for i in {"F", "O", "L", "l"}):
            if self.religion.type_ == ReligionTypes.CHRISTIANITY:
                return f"{self.name} {self.religion.denomination} {self.religion.structure}"
            return f"{self.name} {self.religion.structure}"

        return str(self)

    @staticmethod
    def get_denominations(division,
                     denomination: DenominationTypes) -> Iterable:
        return filter(lambda x: x.religion.denomination == denomination,
                      (x for x in division if hasattr(x, "religion")))
    
    @staticmethod
    def religion(division, type_: ReligionTypes) -> Iterable:
        return filter(lambda x: x.religion.type_ == type_,
                      (x for x in division if hasattr(x, "religion")))
