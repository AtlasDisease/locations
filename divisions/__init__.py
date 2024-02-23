# Force you to import cities.py manually as
# it contains multiple classes and things you need

# --- Imports --- #

from .divisions import *
from .districts import *
from .cities import *
from .counties import *
from .states import *
from .countries import *
from .continents import *
from .planets import *
from .planetarysystems import *
from .galaxies import *
from .localgroup import *
from .supercluster import *
from .universes import *


# --- Variables --- #

_IMPORTANCE = [Division,
               City,
               County,
               State,
               Country,
               Continent,
               Planet,
               PlanetarySystem,
               Galaxy,
               LocalGroup,
               Supercluster,
               Universe]
