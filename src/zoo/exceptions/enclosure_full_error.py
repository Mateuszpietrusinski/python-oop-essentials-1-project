"""EnclosureFullError exception for the Zoo Garden system."""

from .zoo_error import ZooError


class EnclosureFullError(ZooError):
    """Raised when an animal is added to an enclosure that has reached its capacity.

    Args:
        message: Human-readable description of the error.
    """
