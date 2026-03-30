"""Zoo Garden — public API.

Import all public classes from this package for convenience:

    from zoo import Zoo, Lion, Eagle, Zookeeper, Enclosure, FeedingSchedule
"""

from .exceptions import (
    ZooError,
    EnclosureFullError,
    AnimalNotFoundError,
    InvalidAnimalDataError,
)
from .animals import (
    Animal,
    Mammal,
    Bird,
    Reptile,
    Lion,
    Elephant,
    Monkey,
    Eagle,
    Penguin,
    Crocodile,
)
from .enclosure import Enclosure
from .feeding import FeedingEntry, FeedingSchedule
from .employees import Employee, Zookeeper, Veterinarian, Guide
from .zoo import Zoo

__all__ = [
    # Exceptions
    "ZooError",
    "EnclosureFullError",
    "AnimalNotFoundError",
    "InvalidAnimalDataError",
    # Animals
    "Animal",
    "Mammal",
    "Bird",
    "Reptile",
    "Lion",
    "Elephant",
    "Monkey",
    "Eagle",
    "Penguin",
    "Crocodile",
    # Enclosure
    "Enclosure",
    # Feeding
    "FeedingEntry",
    "FeedingSchedule",
    # Employees
    "Employee",
    "Zookeeper",
    "Veterinarian",
    "Guide",
    # Zoo
    "Zoo",
]
