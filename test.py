# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for testing.

# --- Imports --- #

from districts.divisions import Division, DivisionTypes
from districts.places import Place, PlaceTypes
from districts.areas import Neighborhood
from districts.cities import City, CityTypes, AdministrativeTypes
from districts.counties import County, Parish
from districts.states import State
from districts.countries import Country
from districts.continents import Continent
from districts.planets import Planet
from districts.solarsystems import SolarSystem
from districts.galaxies import Galaxy
from districts.universes import Universe
from districts.details import Population

# Politics is a complex thing as it is tied into districts very
# closely but a separate idea so doing something like districts.politics
# makes it seem like they rely on each other which does not make sense
# to me especially since the politics package could be used on its own
# without the districts being used. Could make a protocol maybe?
from politics.government import Government
from politics.leaders import Leader, LeaderPolicy, Administrator
from politics.economics import Economy, EconomicPolicy
from politics.law import Law, LawPolicy, Bill, BillStatus, Constitution


# --- Main Logic --- #

if __name__ == "__main__":

    administrator = Administrator("Greg Abbott")
    leader = Leader("Daniel Miller", LeaderPolicy.DEMOCRACY)
    economy = Economy(EconomicPolicy.CAPITALIST)

    bill = Bill("Bill of Rights", BillStatus.ABSOLUTE,
                """
1. Freedom of Religion, Press, Protest, etc
2. Right to Own Guns
""")
    law = Law(LawPolicy.EYE_FOR_AN_EYE, bills = [bill])

    government = Government(leader, economy, law)
    
    fort = Place("Concho", PlaceTypes.FORT)
    neighborhood = Neighborhood("Rock Prairie")
    city = City("College Station",
                CityTypes.CITY,
                AdministrativeTypes.NONE,
                population = Population(115_000),
                subdivisions = [neighborhood])
    county = County("Brazos",
                    population = Population(233_849),
                    subdivisions = [city])
    parish = Parish("Acadia")
    state = State("Louisiana", subdivisions = [parish])
    country = Country("Texas",
                      population = Population(27_000_000),
                      subdivisions = [county],
                      government = government)

    country2 = Country("United States of America", subdivisions = [state])

    continent = Continent("North America",
                    subdivisions = [country])
    planet = Planet("Earth",
                    population = Population(8_000_000_000),
                    subdivisions = [continent])
    solarsystem = SolarSystem("My Solar System",
                              subdivisions = [planet])
    galaxy = Galaxy("Milky Way",
                    subdivisions = [solarsystem])
    universe = Universe("My Universe",
                        subdivisions = [galaxy])
    
    print(str(fort))
    print(str(neighborhood))
    print(str(city), city.population,
          [str(subdivision) for subdivision in city.subdivisions])
    print(str(county), county.population,
          [str(subdivision) for subdivision in county.subdivisions])
    print(str(country), country.population,
          [str(subdivision) for subdivision in country.subdivisions])
    print(str(continent), [str(subdivision) for subdivision in continent.subdivisions])
    print(str(planet), planet.population,
          [str(subdivision) for subdivision in planet.subdivisions])
    print(str(solarsystem), [str(subdivision) for subdivision in solarsystem.subdivisions])
    print(str(galaxy), [str(subdivision) for subdivision in galaxy.subdivisions])
    print(str(universe), [str(subdivision) for subdivision in universe.subdivisions])
    print()
    print(parish)
    print(state, [str(subdivision) for subdivision in state.subdivisions])
    print(country2, [str(subdivision) for subdivision in country2.subdivisions])

    print()

    print(government)
