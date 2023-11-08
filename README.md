# locations - Object oriented locations
---
This package offers lots classes for dealing with locations in an object oriented way. It also includes some extended classes and functions for handling things that are usually associated with certain locations but not required.

----
## Basic Usage
---

Below shows the basic usage of the package using a real-world example.

```python
# --- Imports --- #

import datetime as dt
# Religion is a complex thing as it is tied into places very
# closely but a separate idea so doing something like districts.religions
# makes it seem like they rely on each other which does not make sense
# to me especially since the religions package could be used on its own
# without the districts being used.
from locations.districts.places import Place, PlaceTypes, HouseOfWorship, \
     Cemetery
from locations.districts.places.religious import ReligionTypes, \
     WorshipStructureTypes, DenominationTypes, Religion
from locations.districts.places.cemeteries import Grave
from locations.districts.areas import AreaTypes, Neighborhood, University
from locations.districts.areas.schools import SchoolTypes
from locations.districts import Division, DivisionTypes, City, County,\
Parish, State, Country, Continent, Planet, PlanetarySystem, Galaxy, \
Universe
from locations.districts.cities import CityTypes, AdministrativeTypes
from locations.districts.extensions import Population

# Politics is a complex thing as it is tied into districts very
# closely but a separate idea so doing something like districts.politics
# makes it seem like they rely on each other which does not make sense
# to me especially since the politics package could be used on its own
# without the districts being used.
from locations.politics.government import Government
from locations.politics.leaders import Leader, LeaderPolicy, Administrator
from locations.politics.economics import Economy, EconomicPolicy
from locations.politics.law import Law, LawPolicy, Bill, BillStatus, Constitution

from locations.positional import Address, Coordinates, Location

from locations.zipcodes import ZipCode, ZipCodeTypes


# --- Main Logic --- #

administrator = Administrator("Dan Patrick")
leader = Leader("Greg Abbott", LeaderPolicy.REPUBLIC)
economy = Economy(EconomicPolicy.CAPITALIST)
bill = Bill("Bill of Rights", BillStatus.ABSOLUTE,
            """
1. Freedom of Religion, Press, Protest, etc
2. Right to Own Guns""")
law = Law(LawPolicy.FAIR_AND_JUST, bills = [bill])
government = Government(leader, economy, law)

zipcode = ZipCode(77845, ZipCodeTypes.AMERICA)
coordinates = Coordinates(0.001545, 51.477928) #Prime Meridian
religion = Religion(ReligionTypes.CHRISTIANITY,
                    WorshipStructureTypes.CHURCH,
                    denomination = DenominationTypes.PRESBYTERIAN)
grave = Grave("Rosie Lee Moore", dt.date(1899, 6, 22), dt.date(1967, 2, 12),
              epitaph = """Rosie was \" Aunt Jemima\" for
Quaker Oats Co. for 25 years.""")
cemetery = Cemetery("Blackjack", graves = [grave])
church = HouseOfWorship("First", religion)
stadium = Place("Kyle Field", PlaceTypes.STADIUM)
university = Division("Texas A&M", AreaTypes.SCHOOL) #Can create a university-like object like this
university = Division("Texas A&M", SchoolTypes.UNIVERSITY) #Can create a university like this too which is more accurate
university = University("Texas A&M") #This is the best way
neighborhood = Neighborhood("Downtown",
                            subdivisions = [stadium])
city = City("College Station",
			CityTypes.CITY,
			AdministrativeTypes.NONE,
			population = Population(115_000),
			subdivisions = [neighborhood, church, university])
city2 = City("Bryan",
            CityTypes.CITY,
            AdministrativeTypes.SEAT,
            population = Population(200_000))
city3 = City("Boonville",
            CityTypes.SITE,
            AdministrativeTypes.NONE,
            population = Population(0))
county = County("Brazos",
                population = Population(233_849),
                subdivisions = [city, city2, city3])

# Louisiana uses Parishes instead of Counties, same concept
parish = Parish("Acadia")
louisiana = State("Louisiana", subdivisions = [parish])
texas = State("Texas",
			  population = Population(27_000_000),
			  subdivisions = [county])
country2 = Country("United States of America",
                    subdivisions = [texas, louisiana])
continent = Continent("North America",
                    subdivisions = [country, country2])
planet = Planet("Earth",
                population = Population(8_000_000_000),
                subdivisions = [continent])
solarsystem = PlanetarySystem("Solis",
							  subdivisions = [planet])
galaxy = Galaxy("Milky Way",
				subdivisions = [solarsystem])
universe = Universe("My Universe",
					population = float('inf'),
                    subdivisions = [galaxy])
location = Location("Universe", [church, neighborhood, city, county,
                                country, continent, planet, solarsystem,
                                galaxy, universe])

print(cemetery)
for grave in cemetery.graves:
	print(f"{grave}: O")
print(location)
print()
print(government)
print()

# These do the same thing, prefer the bottom one
print(leader.as_Administrator())
print(Administrator(leader = leader))

print(f"{county.seat(): O}") #Implying there is a cost to this
print(list(county)) # Test for __iter__

city3 = county.get(func = Population.largest)
if not city3:
    print(city3, city3.population, city3.incorporated, city3.abandoned, city3.historical)

city3 = county.get(func = Population.smallest)
if not city3:
    print(city3, city3.population, city3.incorporated, city3.abandoned, city3.historical)
```

----
## Districts Package
---
### Areas Package
#### areas.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument. These classes do not have additional functionality currently.

*enum* areas.**AreaTypes**
	An enum that represents the types of areas. The NEIGHBORHOOD option should be the default unless there is another option that more accurately represents your area.

#### Options
- NEIGHBORHOOD - General use
- SCHOOL
- FORT
- PORT
- AIRPORT

*class* areas.**Neighborhood**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a neighbor or a generic area of a city. 

*class* areas.**Fort**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a fort.

*class* areas.**Port**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a port.

*class* areas.**Airport**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents an airport.

#### schools.py

*enum* schools.**SchoolTypes**
	An enum that represents the types of schools. The SCHOOL option should be the default unless there is another option that more accurately represents your place of learning.

#### Options
- SCHOOL - General use
- COLLEGE
- UNIVERSITY
- TECHNICAL

*class* schools.**School**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a school.

*class* schools.**College**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a college campus.

*class* schools.**University**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a university campus.

*class* schools.**Technical**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a technical school.

### Places Package
#### cemeteries.py
*class* cemeteries.**Grave**(*name: str*, *date_born: datetime.date = datetime.date.min*, *date_died: datetime.date = datetime.date.max*, /, *description: str = ""*)\
	A class that represents a grave. This class is used when the extended *graves* keyword is used for Cemetery.

*class* cemeteries.**Cemetery**(*name: str*, /, *population: int = None*, *graves: list[Grave] = None*, *\*\*kwargs*)\
	A class that represents a cemetery.

#### emergency.py
*enum* emergency.**EmergencyServiceTypes**\
	An enum that represents the type of emergency service. The POLICE option is the default unless there is another option that more accurately represents the emergency service.

##### Options
- POLICE
- FIRE
- HEALTH

*class* emergency.**EmergencyService**(*name: str*, *service: EmergencyServiceTypes*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents an emergency service.

#### places.py

These classes can receive extended functionality by specifying the population keyword argument.

*enum* places.**PlaceTypes**\
	An enum that represents the type of place. The BUILDING option should be the default unless there is another option that more accurately represents the place.

##### Options
- BUILDING - General use.
- STADIUM
- CITY_HALL
- COURTHOUSE
- FORT
- PORT
- AIRPORT
- HOUSE_OF_WORSHIP
- CEMETERY
- BANK
- EMERGENCY_SERVICE
- HOSPITAL
- POST_OFFICE
- SCHOOL

*class* places.**Place**(*name: str*, *type_: PlaceTypes*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a place. A place is a division that cannot be subdivided anymore. This is the smallest unit in the districts package.

*class* places.**Building**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a building.

*class* places.**Stadium**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a stadium.

*class* places.**CityHall**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a city hall.

*class* places.**Courthouse**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a courthouse.

*class* places.**Fort**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a fort.

*class* places.**Port**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a port.

*class* places.**Airport**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents an airport.
	
*class* places.**Bank**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a bank.

*class* places.**Hospital**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a hospital.

*class* places.**PostOffice**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a post office.

*class* places.**School**(*name: str*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a school.

#### religious.py
*enum* religious.**ReligionTypes**
	An enum that represents the type of religion. The UNKNOWN option should be the default unless there is another option that more accurately represents the religion.

##### Options
- UNKNOWN - General use.
- ATHEIST
- CHRISTIANITY
- JEWISH
- MUSLIM
- BUDDHIST
- HINDU
- PAGAN
- JAINISM
- SHINTO
- SIKHISM
- TAOISM
- ZOROASTRIANISM

*enum* religious.**WorshipStructureTypes**\
	An enum that represents the type of worship structure. The TEMPLE option should be the default unless there is another option that more accurately represents the worship structure.

##### Options
- TEMPLE - General use.
- CHURCH
- CATHEDRAL
- CHAPEL
- HALL
- SYNAGOGUE
- MOSQUE
- DERASAR
- BASADI
- MANDI
- MASHKHANNA
- BETH_MANDA
- HOF
- JINJA
- GURDWARA
- DAOGUAN
- ATASH_BEHRAM
- AGYARI
- DADGAH

*enum* religious.**DenominationTypes**\
	An enum that represents the type of Christian denomination. The NONE option should be the default unless there is another option that more accurately represents the Christian denomination.

##### Options
- NONE - General use.
- METHODIST
- PRESBYTERIAN
- BAPTIST
- LUTHERAN
- ANGLICAN
- PENTECOSTAL
- ORTHODOX
- CATHOLIC
- COPTIC
- NONDENOMINATIONAL

*class* religious.**Religion**(*name: str*, *religion: ReligionTypes*, *worship_type: WorshipStructureTypes = WorshipStructureTypes.TEMPLE*, /, *denomination: DenominationTypes = DenominationTypes.NONE*)\
	A class that represents a religion.

*class* religious.**HouseOfWorship**(*name: str*, *religion: Religion*, /, *population: int = None*, *\*\*kwargs*)\
	A class that represents a house of worship.

### cities.py

*enum* cities.**CityTypes**\
	An enum that represents the type/status of a city. The UNKNOWN option should be the default unless there is another option that more accurately represents the city. I am picky about how you use these but I cannot enforce my standards but I will list them below.
#### Options
- UNKNOWN - General use or if you are not sure what type of city it is.
- LOST - This is incredibly rare but it is for a city whose location is unknown but has documentation that the city existed at some point in the division. Some examples are Nanhattie, Texas.
- SITE  - A city whose population is 0 or lacks a defined area. These are sometimes referred to as ghost towns. Some examples are Sanco, Texas, Nashville-on-the-Brazos, Texas.
- COMMUNITY - A city that is unincorporated and lacks social services.. An example is Fluvanna, Texas.
- TOWN - A city that is incorporated but lacks non-volunteer social services like fire department and police department.
- CITY - A city that is incorporated and has social services.

*enum* cities.**AdministrativeTypes**\
	An enum that represents the administrative importance of a city. The NONE option should be the default unless there is another option that more accurately represents the city.

#### Options
- NONE - No administrative importance
- SEAT - A county seat (the head of the county government)
- CAPITAL - A capital of a state or country

Some cities are about a county seat and a capital. An example is Austin, Texas. CAPITAL should be used in this case.


*class* cities.**City**(*name: str*, *citytype: CityTypes, admintype: AdministrativeTypes*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a city. This class subclasses divisions.Division, therefore it receives subdivision functionality by default. This class can receive extended functionality by specifying the population keyword argument.

##### Properties

City.**incorporated**\
	A property that returns whether the city is incorporated. The city type must be greater than or equal to CityTypes.TOWN to be true.

City.**abandoned**\
	A property that returns whether a city is abandoned. The city type must be less than CityTypes.COMMUNITY and not CityTypes.UNKNOWN to be true.

City.**historical**\
	A property that returns whether a city is historical. The city type must be CityTypes.SITE to be true. **This is subject to change. May make this a user decision.**

### continents.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument. These classes do not have additional functionality currently.

*class* continents.**Continent**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int =None*, *\*\*kwargs*)\
	A class that represents a continent.

### counties.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument.

*class* counties.**County**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a county.

*class* counties.**Parish**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a parish. Functionally the same as a county.
	
*class* counties.**Shire**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a shire. Functionally the same as a county.

#### Methods

County.**seat**()
	Gets the county seat from the list of subdivisions. Returns None if the seat is not found.

### countries.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument.

*class* countries.**Country**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *prefix: str = ""*, *\*\*kwargs*)\
	A class that represents a country. *Prefix* should only be specified if a key in *kwargs* is government.

### divisions.py

*enum* divisions.**DivisionTypes**\
	An enum that represents the division type of a division. The AREA option should be the default unless there is another option that more accurately represents the division.

#### Options
- AREA - General use.
- CITY
- COUNTY
- STATE
- COUNTRY
- CONTINENT
- PLANET
- PLANETARY_SYSTEM
- GALAXY
- UNIVERSE

*class* divisions.**Division**(*name: str*, *type_: IntEnum*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a division. This is a base class for a majority of class in the districts package.

#### Methods
Division.**get**(*func: Callable*)\
	Gets a subdivision based on a function. An example would be when you have the population functionality activated you can use Population.largest to get the largest subdivision by population.

divisions.**add_subdivisions**(cls, *subdivisions: list[Division] | Division*)\
	Adds subdivision functionality to *cls*. **This is still in development and could be removed entirely in the future.**

### galaxies.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument.

*class* galaxies.**Galaxy**(*name: str*, /, *subdivisions: list[Division] | Division*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a galaxy.

### planetarysystems.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument.

*class* planetarysystems.**PlanetarySystem**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a planetary system. This is known as a solar system though it is not the correct term (to my understanding) as solar refers to our Sun.

### planets.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument.

*class* planets.**Planet**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a planet.

### states.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument.

*class* states.**State**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a state.

### universes.py

All classes in this module subclass divisions.Division, therefore it receives subdivision functionality by default. These classes can receive extended functionality by specifying the population keyword argument.

*class* universes.**Universe**(*name: str*, /, *subdivisions: list[Division] | Division = None*, *population: int = None*, *\*\*kwargs*)\
	A class that represents a universe.

----
## Politics Package
---
### law

*enum* bills.**BillStatus**\
	An enum that represents the status of a bill. The BUILDING option should be the default unless there is another option that more accurately represents the place.

#### Options
- UNASSIGNED - General use.
- ASSIGNED - Assigned to a committee.
- VOTED - Bill has been voted on.
- PASSED - Bill has been passed/approved.
- ABSOLUTE - Bill that is in the Constitution or is a God Given right.

*class* bills.**Bill**(*name: str*, *status: BillStatus*, *description: str = ""*)\
	A class that represents a bill for a law.

*class* bills.**Constitution**(*bills: list[Bill]*)\
	A class that represents a Constitution.

*enum* laws.**LawPolicy**\
	An enum that represents the law policy of a government. The NONE option should be the default unless there is another option that more accurately represents the government law policy.

#### Options
- NONE - General use.
- REHABILITATION - Punishment is less than the crime through a judicial system in which criminals are innocent until proven guilty in a court of law or by a jury of peers. An example of this would be Norway.
- FAIR_AND_JUST - Punishment fits the crime through a judicial system in which criminals are innocent until proven guilty in a court of law or by a jury of their peers. An example of this would be The United States of America.
- EYE_FOR_AN_EYE - Punishment fits the crime to the closest degree through a judicial system in which criminals are innocent until proven guilty in a court of law or by a jury of their peers. Places with the death penalty tend to be in this category. An example of this would be Texas.
- LAW_AND_ORDER - Punishment is excessive or inhumane through a judicial system that is rigged or is corrupted in which criminals are considered guilty until proven innocent. An example of this would be China.

*class* laws.**Law**(*policy: LawPolicy*, /, *bills: list[Bills] = None*)\
	A class that represents the rule of law.

### economics.py

*enum* economics.**EconomicPolicy**\
	An enum that represents the economic policy. The NONE option should be the default unless there is another option that more accurately represents the economy.

#### Options
- NONE - General use.
- CAPITALIST
- SOCIALIST
- COMMUNIST

*class* economics.**Economy**(*policy: EconomicPolicy*)\
	A class that represents an economy.

### government.py

*class* government.**Government**(*leader: Leader*, *economy: Economy*, *law: Law*)\
	A class that represents a government.

government.**add_government**(*cls*, *govt: Government*)\
	A function that adds government functionality to a class. **This is still being worked on and may be removed in a future update.**

government.**add_administrator**(*cls*, *admin: Administrator*)\
	A function that adds administrator functionality to a class. **This is still being worked on and may be removed in a future update.**

### leaders.py

*enum* leaders.**LeaderPolicy**\
	An enum that represents the leader policy. The NONE option should be the default unless there is another option that more accurately represents the economy.

#### Options
- NONE - General use.
- ANARCHY
- DEMOCRACY
- REPUBLIC
- OLIGARCHY
- MONARCHY
- AUTHORITARIAN

*class* leaders.**Administrator**(*name: str = ""*, *title: str = ""*, /, *leader: Leader = None*)\
	A class that represents an administrator. This is similar to leaders.Leader but is used for an individual with very little or no policy but an administrative function. An example would be the Chief of Police.

*class* leaders.**Leader**(*name: str*, *policy: LeaderPolicy*, /, *title: str = "President"*)\
	A class that represents a leader.

#### Methods
Leader.**as_Administrator**()\
	A function that returns the Leader object as a Administrator object.

### languages.py

*enum* languages.**Languages**\
	An enum that represents a language.

#### Options
- ENGLISH
- LATIN
- NORWEGIAN

languages.**getNameInLanguage**(*division: Division*, *language: Languages*)\
	A function that returns the division name in another language. If the name is not found then an Exception is thrown.

### zipcodes.py

*enum* zipcodes.**ZipCodeTypes**\
	An enum that represents a zip code type.

#### Options
- AMERICA

*class* zipcodes.**ZipCode**(*zip_code: int*, *type_: ZipCodeTypes*)\
	A class that represents a zip code. This is also known as a postal code, post code, PIN, or mailing code in some places.

----
## Position Package
----
### addresses.py

*class* addresses.**Address**(*street: str*, *city: City*, *county: County*, *country: Country*, *zipcode: ZipCode*)\
	A class that represents an address.

### coordinates.py

*class* coordinates.**Coordinates**(*longitude: float*, *latitude: float*)\
	A class that represents a coordinate set.

### locations.py

*class* locations.**Location**(*name: str*, *divisions: list[Division] = []*)\
	A class that represents a location. The division list should be smallest to largest division.
