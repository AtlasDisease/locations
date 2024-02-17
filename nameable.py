# # --- Import --- #

# from abc import ABC, abstractmethod
# from dataclasses import dataclass


# # --- Nameable Class --- #

# @dataclass
# class Nameable(ABC):
#     name: str

#     def __str__(self) -> str:
#         return self.name

#     def __format__(self, format_spec = "") -> str:
#         return str(self)

#     @classmethod
#     def _generate_next_value_(self, cls):
#         if hasattr(cls, "__class__"):
#             return f"{cls.__class__.__name__}{cls._count}"
#         return f"{cls.__name__}{cls._count}"