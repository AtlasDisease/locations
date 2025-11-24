# --- Imports --- #

from dataclasses import dataclass, field
from typing import Iterable
from ..enum import StrEnum, auto
from ..locations import Location


# --- WeatherTypes Enum --- #

class WeatherTypes(StrEnum):
    SUNNY = auto()
    PARTLY_CLOUDY = auto()
    CLOUDY = auto()
    RAIN = auto()
    THUNDERSTORM = auto()
    SNOW = auto()
    BLIZZARD = auto()
    WINDY = auto()


# --- WeatherAlertTypes Enum --- #

class WeatherAlertTypes(StrEnum):    
    HAZARDOUS_WEATHER_OUTLOOK = auto()
    WINTER_WEATHER_ADVISORY = auto()
    WIND_CHILL_ADVISORY = auto()
    DENSE_FOG_ADVISORY = auto()
    WIND_ADVISORY = auto()
    SMALL_CRAFT_ADVISORY = auto()
    COASTAL_FLOOD_ADVISORY = auto()
    HEAT_ADVISORY = auto()
    WINTER_STORM_WATCH = auto()
    FREEZE_WATCH = auto()
    FIRE_WEATHER_WATCH = auto()
    HIGH_WIND_WATCH = auto()
    SEVERE_THUNDERSTORM_WATCH = auto()
    TORNADO_WATCH = auto()
    COASTAL_FLOOD_WATCH = auto()
    FLOOD_WATCH = auto()
    FLASH_FLOOD_WATCH = auto()
    RIVER_FLOOD_WATCH = auto()
    EXCESSIVE_HEAT_WATCH = auto()
    TROPICAL_STORM_WATCH = auto()
    HURRICANE_WATCH = auto()
    BLIZZARD_WARNING = auto()
    WINTER_STORM_WARNING = auto()
    ICE_STORM_WARNING = auto()
    FREEZE_WARNING = auto()
    RED_FLAG_WARNING = auto()
    HIGH_WIND_WARNING = auto()
    SEVERE_THUNDERSTORM_WARNING = auto()
    TORNADO_WARNING = auto()
    EXTREME_WIND_WARNING = auto()
    GALE_WARNING = auto()
    STORM_WARNING = auto()
    HURRICANE_FORCE_WIND_WARNING = auto()
    SPECIAL_MARINE_WARNING = auto()
    COASTAL_FLOOD_WARNING = auto()
    FLASH_FLOOD_WARNING = auto()
    FLOOD_WARNING = auto()
    RIVER_FLOOD_WARNING = auto()
    EXCESSIVE_HEAT_WARNING = auto()
    TROPICAL_STORM_WARNING = auto()
    HURRICANE_WARNING = auto()


# --- WeatherAlert Class --- #

@dataclass(slots=True)
class WeatherAlerts:
    alert: WeatherAlertTypes
##    locations: list[Location] = field(default_factory=list)
    description: str = ""

    def __str__(self) -> str:
        return str(self.alert)

    def __format__(self, format_spec="") -> str:
        if "A" in format_spec:
            return f"{self.alert}: {self.description}"""
        return str(self)

    def __bool__(self) -> bool:
        return "warning" in str(self.alert).lower()
    
    
# --- Wildfire Class --- #

@dataclass(slots = True)
class Weather:
    """Weather Class"""
    #name: str
    current_weather: WeatherTypes
    alerts: Iterable[WeatherAlerts] = field(default_factory=list)
    locations: list[Location] = field(default_factory=list)
    #locations might become a list of divisions.
    #Cities and counties as the NWS uses.

    def __str__(self) -> str:
        return self.current_weather.value

    def __format__(self, format_spec = "") -> str:
        if "A" in format_spec:
            return ", ".join(map(lambda alert: str(alert), self.alerts))
        return self.current_weather.value

    def __iter__(self) -> Iterable:
        return iter(self.locations)

    @property
    def severe(self):
        return any((bool(alert) for alert in self.alerts))

    def add_location(self, location):
        self.locations.append(location)
        return self

    def remove_location(self, location):
        self.locations.remove(location)
        return self

##    def get_alerts(self) -> Iterable[WeatherAlerts]:
##        return self.alerts


if __name__ == "__main__":
    def main():
        weather = Weather(WeatherTypes.THUNDERSTORM,
                          [WeatherAlerts(WeatherAlertTypes.SEVERE_THUNDERSTORM_WARNING)])
        print(f"{weather: A}")
    
    main()
