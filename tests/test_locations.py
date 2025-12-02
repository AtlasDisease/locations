# This is an example of how the packages would be used.
# You must remove it from the package before running.

# --- Imports --- #

import os
import datetime as dt
import locale
##import timeit

from locations.divisions import District, City, CityTypes, \
     AdministrativeTypes, County, State, Country, Continent, Planet, \
     PlanetarySystem, Galaxy, LocalGroup, Supercluster
from locations.infrastructure.schools import University
from locations.infrastructure.cemeteries import Cemetery, Grave
from locations.infrastructure.airports.engines import Engine, \
     EngineManufacturer
from locations.infrastructure.airports.airplanes import Airplane, \
     AirplaneManufacturer, Seat
from locations.infrastructure.airports.flights import FlightStatus, Flight
from locations.infrastructure.airports.airlines import Airline
from locations.infrastructure.airports import Airport, AirportTypes
from locations.infrastructure.postoffice import PostOffice
from locations.infrastructure.banks import Bank#, Money
from locations.infrastructure.courthouses import Courthouse, CourthouseTypes
from locations.locations import Location, LocationIter
from locations.zipcodes import ZipCode, ZipCodeTypes
from locations.addresses import Address
from locations.climate.naturaldisasters import Wildfire
from locations.climate.weather import Weather, WeatherTypes, \
     WeatherAlertTypes, WeatherAlerts
from locations.administrativedistricts import AdministrativeDistrict
from locations.locations import Location

locale.setlocale(locale.LC_ALL, '')


# --- Definitions --- #

def texas_main():
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
    city4 = City("Bryan",
                 CityTypes.CITY,
                 AdministrativeTypes.SEAT)
    city5 = City("College Station",
                 CityTypes.CITY)
    city6 = City("Boonville",
                 CityTypes.SITE)
    city7 = City("Millican",
                 CityTypes.COMMUNITY)
    county = County("Travis", [city])
    county2 = County("McLennan", [city2, city3])
    county3 = County("Brazos", [city4, city5, city6, city7])
    country = Country("Texas", [county, county2])
    continent = Continent("North America", [country])
    planet = Planet("Earth", [continent])
    system = PlanetarySystem("Solar", [planet])
    galaxy = Galaxy("Milky Way", [system])
    galaxy2 = Galaxy("Andromeda", [])
    localgroup = LocalGroup("Milky Way", [galaxy, galaxy2])
    supercluster = Supercluster("Virgo", [localgroup])
    location = Location(district = district,
                        city = city,
                        county = county,
                        country = country,
                        continent = continent,
                        planet = planet,
                        system = system,
                        galaxy = galaxy2,
                        localgroup = localgroup,
                        supercluster = supercluster)
    locationiter = LocationIter.fromLocation(location)
    print(f"{location:, }", locationiter, sep=os.linesep)
    print()
    
    locationiter2 = LocationIter(divisions = [grave,
                                              cemetery,
                                              city2,
                                              county2,
                                              country])
    print(locationiter2, f"{grave: O}", sep=os.linesep)
    print()

    university = University("Texas A&M")
    print(f"{university: O}")
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
    print(address,
          zipcode.national_area,
          zipcode.sectional_center,
          zipcode.delivery_area,
          zipcode.specific_delivery_area)

##    print(city > city2)
    print(*map(lambda city: str(city),
               sorted(county2, key=lambda city: city.admin_type, reverse=True)),
          sep=", ")
    print(min(county2, key=lambda city: city.admin_type))
    print(max(county2, key=lambda city: city.admin_type))

    wildfire = Wildfire("Smokehouse Creek", size = 1_058_460, containment = 89)
    print(wildfire, f"{wildfire: O}", f"{wildfire.size:,.2f}", f"{wildfire.containment:,.1f}%", sep=os.linesep)

    courthouse = Courthouse("Texas", CourthouseTypes.SUPREME)
    print(f"{courthouse: L}")

    weather = Weather(WeatherTypes.THUNDERSTORM,
                      [WeatherAlerts(WeatherAlertTypes.SEVERE_THUNDERSTORM_WARNING)],
                      [city2, city3])
    print(weather,
          f"{weather: A}",
          weather.severe,
          sep=os.linesep)
    
    weather2 = Weather(WeatherTypes.THUNDERSTORM,
                      [WeatherAlerts(WeatherAlertTypes.SEVERE_THUNDERSTORM_WATCH)],
                      [city2, city3])
    print(weather2,
          f"{weather2: A}",
          weather2.severe,
          sep=os.linesep)

    location2 = Location(city = city2,
                         county = county2,
                         country = country)
    adminDistrict = AdministrativeDistrict(location2)
    adminDistrict.construct_courthouse(f"{adminDistrict.location.county: L}",
                                       adminDistrict.location.city,
                                       AdministrativeTypes.SEAT)
    print(*map(lambda div: f"{div: L}",
              adminDistrict.location.city), sep=", ")
    print(county2.seat)
    print(*map(lambda city: f"{city: L}", country.capitals), sep=", ")


# --- Main --- #

def main():
    texas_main()
    print()

    city = City("College Station",
                 CityTypes.CITY)
    city1 = City("Dallas", CityTypes.CITY, AdministrativeTypes.SEAT)
    county = County("Brazos", [city])
    county1 = County("Dallas", [city1])
    country = Country("Texas", [county])

    location2 = LocationIter("College Station", [city, county, country])
    location3 = LocationIter("Houston", [city1, county1, country])

    seat = Seat(15, "B")
    engine = Engine("Trent 1000", EngineManufacturer.ROLLS_ROYCE)
    engine2 = Engine("Trent 1000", EngineManufacturer.ROLLS_ROYCE)
    airplane = Airplane("787 - Dreamliner",
                        AirplaneManufacturer.BOEING,
                        engines = [engine, engine2])
    flight = Flight(Airline("Delta Airlines"),
                    location2,
                    location3,
                    "12345",
                    [seat],
                    airplane,
                    dt.datetime.today(),
                    dt.datetime.today() + dt.timedelta(minutes = 45))
    airport = Airport("Dallas-Fort Worth", AirportTypes.INTERNATIONAL)
    print(f"{engine: O}", airplane, f"{airport: O}", sep=os.linesep)
    print()
    print(f"{flight: D}")
    print()

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

    localbank = Bank("Local Credit Union", cash_on_hand = 100_000)
    bigbank = Bank("Wells Fargo", cash_on_hand = 500_000_000.30)
    print(localbank, bigbank, sep="\n")

    bigbank.merge(localbank)
    print(f"{bigbank} Cash on hand: {bigbank: $,}") #This requires using locales

    city10 = City("Pretoria", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city11 = City("Cape Town", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city12 = City("Bloemfontein", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    country4 = Country("South Africa", [city10, city11, city12], max_capital_num=3)#, [city10, city11, city12])
    print(*map(lambda city: f"{city: L}", country4.capitals), sep=", ")
    print(f"{country4.capital: L}")

    city13 = City("The Hague", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city14 = City("Amsterdam", CityTypes.CITY, AdministrativeTypes.CAPITAL)
    city15 = City("Workum", CityTypes.CITY, AdministrativeTypes.NONE)
    county9 = County("Test", [city13, city14])
    county10 = County("Friesland", [city15])
    country5 = Country("Netherlands", [county9, county10], max_capital_num=2)#, [city13, city14])
    print(*map(lambda city: f"{city: L}", country5.capitals), sep=", ")
    print(f"{country5.capital: L}")


if __name__ == "__main__":
    main()
##    timeit.timeit("main()", number=5)
