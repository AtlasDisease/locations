# --- Imports --- #

from districts.divisions import Division, DivisionTypes, add_population, add_subdivisions
from districts.cities import City


# --- Main Logic --- #

if __name__ == "__main__":
    city = City("College Station", population = 100000, subdivisions = [Division("Rock Prairie", DivisionTypes.NEIGHBORHOOD)])
    
    print(city.name, city.population,
          [str(subdivision) for subdivision in city.subdivisions])
