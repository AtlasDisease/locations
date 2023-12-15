# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a post office.

# --- Imports --- #

from typing import Protocol
from dataclasses import dataclass, field
from ...enum import StrEnum, auto, unique
from ..buildings import Building
from .packages import Sendable

__all__ = ("PostOfficeTypes", "PostOffice")


# --- SendError Class --- #

class SendError(Exception): pass


# --- PostOfficeTypes Enum --- #

@unique
class PostOfficeTypes(StrEnum):
    POST_OFFICE = auto()


# --- Shipping Protocol --- #

class Shipping(Protocol):
    def send(self, package: Sendable):
        ...
        
    def deliver(self):
        ...
        

# --- PostOffice Class --- #

@dataclass(init=False)
class PostOffice(Building):
    def __post_init__(self):
        
        self.type_ = InfrastructureTypes.POST_OFFICE

    def send(self, package: Sendable):
        if not package.from_ or not package.to:
            raise SendError(f"Cannot send a {package.__class__.__name__.lower()} without a from to to address.")
        
        print(f"Sent {package} to {package.to}")

    def deliver(self, package: Sendable):
        print(f"Delivered {package} to {package.to}")
        
