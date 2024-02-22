# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: A module to handle a post office.

# --- Imports --- #

from typing import Protocol, Iterable, Self, Optional, NoReturn
from dataclasses import dataclass, field
from ...enum import StrEnum, auto, unique
from ...addresses import Address
from ..buildings import Building
from .packages import Sendable

__all__ = ("PostOffice", "PostalBox", "Mailbox")


# --- SendError Class --- #

class SendError(ValueError): pass


# --- Shipping Protocol --- #

class Shipping(Protocol):
    def send(self, package: Sendable):
        ...
        
    def deliver(self):
        ...
        

# --- PostOffice Class --- #

@dataclass(init=False)
class PostOffice(Building):
    def __format__(self, format_spec = "") -> str:
        if any((char in format_spec for char in {"F", "O", "L", "l"})):
            return f"{self.name} Post Office"

        return str(self)
    
    def send(self, package: Sendable) -> NoReturn:
        if not package.from_ or not package.to:
            raise SendError(f"Cannot send a {package.__class__.__name__.lower()} without a from to to address.")
        
        print(f"Sent {package} to {package.to}")

    def deliver(self, package: Sendable) -> NoReturn:
        print(f"Delivering {package} to {package.to}")

    def send_back(self, package: Sendable) -> NoReturn:
        print(f"Returning {package} to {package.from_}")
        

# --- PostalBox Class --- #

@dataclass
class PostalBox:
    address: Address
    mail: list[Sendable] = field(default_factory = list)

    def __bool__(self) -> bool:
        return bool(self.mail)

    def __len__(self) -> int:
        return len(self.mail)

    def __iter__(self) -> Iterable[Sendable]:
        return iter(self.mail)

    def send(self, package: Sendable) -> NoReturn:
        if not package.from_ or not package.to:
            raise SendError(f"Cannot send a {package.__class__.__name__.lower()} without a from to to address.")
        
        print(f"Sending {package} to {package.to}")

    def deliver(self, package: Sendable) -> Optional[Self]:
        if self.address == package.to.address:
            self.mail.append(package)
            return self
        
        return None

    def send_back(self, package: Sendable) -> NoReturn:
        print(f"Returned {package} to {package.from_}")

    def open(self, package: Sendable) -> Iterable[Sendable]:
        return self.mail

    def returns(self) -> Iterable[Sendable]:
        return filter(lambda mail: mail.from_.address == self.address, self.mail)


# --- Mailbox Class --- #

class Mailbox(PostalBox):
    pass


type DeliveryBox = PostalBox | Mailbox


# --- Functions --- #

def get_delivered_mailbox(package: Sendable, mailboxes: list[DeliveryBox]) -> Optional[DeliveryBox]:
    return next(filter(lambda mailbox: bool(mailbox.deliver(package)), mailboxes), None)
