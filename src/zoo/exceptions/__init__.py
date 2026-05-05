"""Exception sub-package for the Zoo Garden system."""

from .zoo_error import ZooError
from .enclosure_full_error import EnclosureFullError
from .animal_not_found_error import AnimalNotFoundError
from .invalid_animal_data_error import InvalidAnimalDataError

__all__ = [
    "ZooError",
    "EnclosureFullError",
    "AnimalNotFoundError",
    "InvalidAnimalDataError",
]
