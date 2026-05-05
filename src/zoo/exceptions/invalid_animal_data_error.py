"""InvalidAnimalDataError exception for the Zoo Garden system."""

from .zoo_error import ZooError


class InvalidAnimalDataError(ZooError):
    """Raised when animal data fails validation (e.g., empty name).

    Args:
        message: Human-readable description of the error.
    """
