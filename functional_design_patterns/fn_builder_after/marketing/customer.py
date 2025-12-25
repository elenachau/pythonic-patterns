from dataclasses import dataclass
from enum import Enum

class CustomerType(Enum):
    BRONZE = 1
    SILVER = 2
    GOLD = 3

@dataclass
class Customer:
    name: str
    email: str
    type: CustomerType = CustomerType.BRONZE