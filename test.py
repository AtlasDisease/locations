# --- Imports --- #

from districts.divisions import Division, DivisionTypes
from districts.areas import Neighborhood
from districts.cities import City, CityTypes, AdministrativeTypes
from districts.counties import County, Parish
from districts.countries import Country
from districts.details import Population
#from districts.continents import Continent


# --- Main Logic --- #

if __name__ == "__main__":
    
    neighborhood = Neighborhood("Rock Prairie")
    city = City("College Station",
                CityTypes.CITY,
                AdministrativeTypes.NONE,
                population = Population(115_000),
                subdivisions = [neighborhood])
    county = County("Brazos",
                    population = Population(233_849),
                    subdivisions = [city])
    #parish = Parish("Acadia")
    country = Country("Texas",
                    population = Population(27_000_000),
                    subdivisions = [county])
    #continent = Continent("North America",
    #                population = 27_000_000,
    #                subdivisions = [country])
    
    print(str(city), city.population,
          [str(subdivision) for subdivision in city.subdivisions])
    print(str(county), county.population,
          [str(subdivision) for subdivision in county.subdivisions])
    print(str(country), country.population,
          [str(subdivision) for subdivision in country.subdivisions])

    #print(parish)
