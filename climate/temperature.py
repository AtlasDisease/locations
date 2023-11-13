# # Created By: Brendan (@atlasdisease)
# # Copyright: 2023
# # Description: A module to handle a temperature.

# # --- Imports --- #

# from typing import Callable
# # from ..divisions import Division
# # from .extenders import Extension, errorcheck

# def errorcheck(func: Callable):
#     def inner1(*args, **kwargs):

#         climate = args[0]

#         # This is a hacky way to get the class that called this so we can make sure division has a certain attribute
#         varname = func.__qualname__
#         if "." in varname:
#             varname = varname.split(".")[0].lower()

#         if any(not hasattr(x, varname) for x in climate):
#             raise NotImplementedError(f"Subdivisions are required to have a {varname} attribute in order to use this function.")
        
#         if len(climate) <= 0:
#             return Climate(ClimateTypes.UNKNOWN)

#         return func(*args, **kwargs)
        
#     return inner1


# # --- Temperate Class --- #

# class Temperature:#(Extension):

#     __slots__ = ()

#     @staticmethod
#     @errorcheck
#     def highest(climate: Climte) -> Climate:
#         return Temperature._get(climate, lambda x, y: x.temperatures <= y.temperatures)
    
#     @staticmethod
#     @errorcheck
#     def lowest(climate: Climate) -> Climate:
#         return Temperature._get(climate, lambda x, y: x.temperatures >= y.temperatures)


# # --- TemperatureUnit Class --- #

# class TemperatureUnit(float):

#     __slots__ = ()

#     @staticmethod
#     def convert(func: Callable):
#         def inner1(first, other):
#             if type(first) != type(other):
#                 if isinstance(other, Celsius):
#                     other = fahreinheit(other)
#                 else:
#                     other = celsius(other)
                    
#             return func(first, other)

#         return inner1

#     @convert
#     def __gt__(self, other) -> bool:
#         return float.__gt__(self, other)

#     @convert
#     def __lt__(self, other) -> bool:
#         return float.__lt__(self, other)

#     @convert
#     def __eq__(self, other) -> bool:
#         return float.__eq__(self, other)


# # --- Celsius Class --- #

# class Celsius(TemperatureUnit):

#     __slots__ = ()

#     def __str__(self) -> str:
#         return f"{self:,.1f} C"


# # --- Fahreinheit Class --- #

# class Fahreinheit(TemperatureUnit):

#     __slots__ = ()

#     def __str__(self) -> str:
#         return f"{self:,.1f} F"


# # --- Extending Functionality Definitions --- #

# # def add_temperate(cls, elevation: int) -> None:
# #     cls.climate.temperature = elevation

# def celsius(temperature: Fahreinheit) -> Celsius:
#     return Celsius(temperature)

# def fahreinheit(temperature: Celsius) -> Fahreinheit:
#     return Fahreinheit(temperature)
