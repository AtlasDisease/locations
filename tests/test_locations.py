# This is an example of how the packages would be used.
# You must remove it from the package before running.

# --- Imports --- #

import datetime as dt
import timeit

from locations.divisions import District, City, CityTypes, \
     AdministrativeTypes, County, State, Country, Continent, Planet, \
     PlanetarySystem, Galaxy, LocalGroup, Supercluster
from locations.infrastructure.schools import University
from locations.infrastructure.cemeteries import Cemetery, Grave
from locations.infrastructure.airports.engines import Engine, \
     EngineManufacturer
from locations.infrastructure.airports.airplanes import Airplane, \
     AirplaneManufacturer
from locations.infrastructure.airports import Airport, AirportTypes
from locations.infrastructure.postoffice import PostOffice
from locations.infrastructure.banks import Bank, Money
from locations.infrastructure.courthouses import Courthouse, CourthouseTypes
from locations.locations import Location, LocationIter
from locations.zipcodes import ZipCode, ZipCodeTypes
from locations.addresses import Address
from locations.climate.naturaldisasters import Wildfire
from locations.climate.weather import Weather, WeatherTypes, \
     WeatherAlertTypes, WeatherAlerts
from locations.administrativedistricts import AdministrativeDistrict
from locations.locations import Location


# --- Examples --- #

def main():
    district = District("Downtown Austin")
    city = City("Austin",
                CityTypes.CITY,
                AdministrativeTypes.CAPITAL | AdministrativeTypes.SEAT,
                [district])
    grave = Grave("Lawrence Sullivan Ross",
                  dt.date(1838, 9, 27),
                  dt.date(1898, 1, 3))
    cemetery = Cemetery("Oakwood", [grave])
    city2 = City("Waco",
                 CityTypes.CITY,
                 AdministrativeTypes.SEAT,
                 [cemetery])
    city3 = City("Riesel",
                 CityTypes.CITY,
                 AdministrativeTypes.NONE)
    county = County("Travis", [city])
    county2 = County("McLennan", [city2, city3])
    country = Country("Texas", [county, county2])
    continent = Continent("North America", [country])
    planet = Planet("Earth", [continent])
    system = PlanetarySystem("Solar", [planet])
    galaxy = Galaxy("Milky Way", [system])
    localgroup = LocalGroup("Milky Way", [galaxy])
    supercluster = Supercluster("Virgo", [localgroup])
    location = Location(district = district,
                        city = city,
                        county = county,
                        country = country,
                        continent = continent,
                        planet = planet,
                        system = system,
                        galaxy = galaxy,
                        localgroup = localgroup,
                        supercluster = supercluster)
    print(f"{location:, }")
    locationiter = LocationIter.fromLocation(location)
    print(locationiter)
    print()
    
    locationiter2 = LocationIter(divisions = [grave,
                                              cemetery,
                                              city2,
                                              county2,
                                              country])
    print(locationiter2)
    print(f"{grave: O}")
    print()

    university = University("Texas A&M")
    print(f"{university: O}")
    print()

    engine = Engine("Trent 1000", EngineManufacturer.ROLLS_ROYCE)
    engine2 = Engine("Trent 1000", EngineManufacturer.ROLLS_ROYCE)
    airplane = Airplane("787 - Dreamliner",
                        AirplaneManufacturer.BOEING,
                        engines = [engine, engine2])
    print(f"{engine: O}")
    print(airplane)
    print()

    airport = Airport("Easterwood", AirportTypes.REGIONAL)
    print(f"{airport: L}")

    post_office = PostOffice("Austin")
    print(f"{post_office: L}")

    zipcode = ZipCode("78701-0001", ZipCodeTypes.AMERICA)
    address = Address("123 Main St.",
                      city,
                      county,
                      country,
                      zipcode)
    print(address)
    print(zipcode.national_area,
          zipcode.sectional_center,
          zipcode.delivery_area,
          zipcode.specific_delivery_area)

##    print(city > city2)
    print(*map(lambda city: str(city),
               sorted(county2, key=lambda city: city.admin_type, reverse=True)),
          sep=", ")
    print(min(county2, key=lambda city: city.admin_type))
    print(max(county2, key=lambda city: city.admin_type))

    city4 = City("Lansing", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city5 = City("Mason", CityTypes.CITY, AdministrativeTypes.SEAT)
    county4 = County("Ingham", [city4, city5])
    state = State("Michigan", [county4])#, [city4])

    print(max(county4, key=lambda city: city.admin_type))
    print(*map(lambda city: f"{city: L}", county4.seats), sep=", ")
    print(*map(lambda city: f"{city: L}", state.capitals), sep=", ")

    city6 = City("Richmond",
                            CityTypes.CITY,
                            AdministrativeTypes.CAPITAL)
    county5 = County("Some random county")
    county6 = County("Some other random county")
    state2 = State("Virginia", [county6, city6, county5])#, [city6])
##    print(max(state2))
    print(f"{city6:F}")
    print(*map(lambda city: f"{city: L}", state2.capitals), sep=", ")

    city7 = City("Washington",
                 CityTypes.CITY,
                 AdministrativeTypes.CAPITAL)
    state3 = State("District of Columbia", [city7])
    city8 = City("Fort Madison", CityTypes.CITY, AdministrativeTypes.SEAT)
    city9 = City("Keokuk", CityTypes.CITY, AdministrativeTypes.SEAT)
    city10 = City("Des Moines", CityTypes.CITY, AdministrativeTypes.SEAT | AdministrativeTypes.CAPITAL) #Also a Seat
    county7 = County("Lee", [city8, city9], max_seat_num=2)
    county8 = County("Polk", [city10])
    state4 = State("Iowa", [county7, county8])
    country2 = Country("USA", [state4, state3, state2, state])#, [city7])
    print(*map(lambda city: f"{city: L}", country2.capitals), sep=", ")
    print(*map(lambda city: f"{city: L}", county7.seats), sep=", ")
    print(county2.seat)

    localbank = Bank("Local Credit Union", cash_on_hand = Money(100_000))
    print(localbank)
    bigbank = Bank("Wells Fargo", cash_on_hand = Money(500_000_000.30))
    print(bigbank)

    bigbank.merge(localbank)
    print(f"{bigbank} Cash on hand: {bigbank.cash_on_hand:,.2f}")

    wildfire = Wildfire("Smokehouse Creek", size = 1_058_460, containment = 89)
    print(wildfire)
    print(f"{wildfire: O}")
    print(f"{wildfire.size:,.2f}")
    print(f"{wildfire.containment:,.1f}%")

    courthouse = Courthouse("Texas", CourthouseTypes.SUPREME)
    print(f"{courthouse: L}")

    city10 = City("Pretoria", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city11 = City("Cape Town", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city12 = City("Bloemfontein", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    country4 = Country("South Africa", [city10, city11, city12], max_capital_num=3)#, [city10, city11, city12])
    print(*map(lambda city: f"{city: L}", country4.capitals), sep=", ")
    print(*map(lambda city: f"{city: L}", country.capitals), sep=", ")
    print(f"{country4.capital: L}")

    city13 = City("The Hague", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city14 = City("Amsterdam", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city15 = City("Workum", CityTypes.CITY, AdministrativeTypes.NONE)
    county9 = County("Test", [city13, city14])
    county10 = County("Friesland", [city15])
    country5 = Country("Netherlands", [county9, county10], max_capital_num=2)#, [city13, city14])
    print(*map(lambda city: f"{city: L}", country5.capitals), sep=", ")
    print(f"{country5.capital: L}")

    weather = Weather(WeatherTypes.THUNDERSTORM,
                      [WeatherAlerts(WeatherAlertTypes.SEVERE_THUNDERSTORM_WARNING)],
                      [city2, city3])
    print(weather)
    print(f"{weather: A}")
    print(weather.severe)
    
    weather2 = Weather(WeatherTypes.THUNDERSTORM,
                      [WeatherAlerts(WeatherAlertTypes.SEVERE_THUNDERSTORM_WATCH)],
                      [city2, city3])
    print(weather2)
    print(f"{weather2: A}")
    print(weather2.severe)

    location2 = Location(city = city2,
                         county = county2,
                         country = country)
    adminDistrict = AdministrativeDistrict(location2)
    adminDistrict.construct_courthouse(f"{adminDistrict.location.county: L}",
                                       adminDistrict.location.city,
                                       AdministrativeTypes.SEAT)
    print(*map(lambda div: f"{div: L}",
              adminDistrict.location.city.subdivisions), sep=", ")


if __name__ == "__main__":
    main()
##    timeit.timeit("main()", number=5)
