## Created By: Brendan (@AtlasDisease)
## Description: This module holds the Languages dictionary, Language enum, and getNameInLanguage() funcion.
## This is still being improved with different languages.

# --- Imports --- #

from enum import IntEnum, auto
from .divisions import Division


# --- Variables --- #

_LATIN_NAMES = {"Earth": "Terra"}
_NORSK_NAMES = {"Earth": "Jord"}

LANGUAGES = {"Norwegian": _NORSK_NAMES, "Latin": _LATIN_NAMES}


# --- Language Enum --- #

class Language(IntEnum):
    """A enum for the list of languages that are available"""
    ENGLISH = auto()
    LATIN = auto()
    NORWEGIAN = auto()

    def __str__(self):
        return self.name.title()


def getNameInLanguage(division: Division, language: Language):
    """Translates a division name into a language"""

    # This should never happen with the enum unless you are in a development environment
    # if str(language) not in LANGUAGES:
    #     raise Exception("Language not found in the dictionary.")
    if division.name not in LANGUAGES[str(language)]:
        raise Exception(f"Name not found in the {language} dictionary.")

    return LANGUAGES[str(language)][division.name]
