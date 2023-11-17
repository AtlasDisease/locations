# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a religious aspects of buildings.

# --- Imports --- #

from enum import StrEnum, auto
from dataclasses import dataclass, KW_ONLY
from .buildings import Building

__all__ = ("HouseOfWorship",)


# --- ReligionTypes Enum --- #

class ReligionTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
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


# --- WorshipStructureTypes Enum --- #

class WorshipStructureTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
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


# --- DenominationTypes Enum --- #

class DenominationTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
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


# --- Religion Class --- #

@dataclass
class Religion:
    
    type_: ReligionTypes
    structure: WorshipStructureTypes
    _: KW_ONLY
    denomination: DenominationTypes


# --- HouseOfWorship Class --- #

class HouseOfWorship(Building):
    def __init__(self, name: str, religion: Religion,
                 **kwargs):

        super().__init__(name, **kwargs)

        self.religion = religion

    def __format__(self, format_spec = "") -> str:
        if any(i in format_spec for i in {"F", "O", "L", "l"}):
            if self.religion.type_ == ReligionTypes.CHRISTIANITY:
                return f"{self.name} {self.religion.denomination} {self.religion.structure}"
            return f"{self.name} {self.religion.structure}"

        return str(self)
        
