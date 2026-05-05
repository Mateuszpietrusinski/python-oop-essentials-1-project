"""AnimalNotFoundError exception for the Zoo Garden system."""

from .zoo_error import ZooError


class AnimalNotFoundError(ZooError):
    """Raised when an operation references an animal that is not present in the enclosure.

    Args:
        message: Human-readable description of the error.
    """
