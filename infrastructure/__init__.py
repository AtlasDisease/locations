from .airports import *
##from .cemeteries import *
##from .emergency import *
##from .forts import *
##from .infrastructure import *
##from .religious import *
##from .residential import *
##from .schools import *
##from .stadiums import *

from .buildings import Building
from .rooms import Room


#A type of Building or Room
# EX. School() which could just have rooms or can have multiple buildings

type Subdivision = Building | Room
