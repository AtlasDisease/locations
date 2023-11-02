# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: This is for testing.

# --- Main Logic --- #

if __name__ == "__main__":
    from districts.divisions import Division, DivisionTypes
    from districts.places import Place, PlaceTypes
    from districts.areas import AreaTypes, Neighborhood
    from districts.cities import City, CityTypes, AdministrativeTypes
    from districts.counties import County, Parish
    from districts.states import State
    from districts.countries import Country
    from districts.continents import Continent
    from districts.planets import Planet
    from districts.planetarysystems import PlanetarySystem
    from districts.galaxies import Galaxy
    from districts.universes import Universe
    from districts.extensions import Population

    # Politics is a complex thing as it is tied into districts very
    # closely but a separate idea so doing something like districts.politics
    # makes it seem like they rely on each other which does not make sense
    # to me especially since the politics package could be used on its own
    # without the districts being used. Could make a protocol maybe?
    from politics.government import Government
    from politics.leaders import Leader, LeaderPolicy, Administrator
    from politics.economics import Economy, EconomicPolicy
    from politics.law import Law, LawPolicy, Bill, BillStatus, Constitution


    # --- Functions --- #

    def stringify(division: Division) -> str:
        return f"{[str(subdivision) for subdivision in division.subdivisions]}"

    def print_all(start: Division) -> None:

        print(start)
        _print_all(start)

    def _print_all(start: Division) -> None:

        for subdivision in start.subdivisions:
            print(subdivision)
            if not hasattr(subdivision, "subdivisions"):
                continue

            _print_all(subdivision)
        
    administrator = Administrator("Greg Abbott")
    leader = Leader("Daniel Miller", LeaderPolicy.REPUBLIC)
    economy = Economy(EconomicPolicy.CAPITALIST)
    bill = Bill("Bill of Rights", BillStatus.ABSOLUTE,
                """
1. Freedom of Religion, Press, Protest, etc
2. Right to Own Guns""")
    law = Law(LawPolicy.EYE_FOR_AN_EYE, bills = [bill])
    government = Government(leader, economy, law)
    
    fort = Place("Concho", PlaceTypes.FORT)
    university = Division("Texas A&M", AreaTypes.UNIVERSITY)
    neighborhood = Neighborhood("Rock Prairie",
                                subdivisions = [fort])
    city = City("College Station",
                CityTypes.CITY,
                AdministrativeTypes.NONE,
                population = Population(115_000),
                subdivisions = [neighborhood, university])
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
    parish = Parish("Acadia")
    state = State("Louisiana", subdivisions = [parish])
    country = Country("Texas",
                      population = Population(27_000_000),
                      subdivisions = [county],
                      government = government,
                      prefix = "Second")
    country2 = Country("United States of America",
                       subdivisions = [state])
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

    print_all(universe)
    print()
    print(government)
    print()
    print(Administrator(leader = leader))
    print(county.seat()) #Implying there is a cost to this
    print(list(county)) # Test for __iter__

    city3 = county.get(func = Population.largest)
    if not city3:
        print(city3, city3.population, city3.incorporated, city3.abandoned, city3.historical)

    city3 = county.get(func = Population.smallest)
    if not city3:
        print(city3, city3.population, city3.incorporated, city3.abandoned, city3.historical)

##    #This will cause an error as expected
##    universe1 = universe.get(func = Population.smallest)
##    if not universe1:
##        print(universe1, universe1.population)
    
