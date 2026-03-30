"""Custom exception hierarchy for the Zoo Garden system."""


class ZooError(Exception):
    """Base exception for all Zoo Garden errors.

    All application-specific exceptions inherit from this class,
    allowing callers to catch any zoo-related error with a single except clause.
    """


class EnclosureFullError(ZooError):
    """Raised when an animal is added to an enclosure that has reached its capacity.

    Args:
        message: Human-readable description of the error.
    """


class AnimalNotFoundError(ZooError):
    """Raised when an operation references an animal that is not present in the enclosure.

    Args:
        message: Human-readable description of the error.
    """


class InvalidAnimalDataError(ZooError):
    """Raised when animal data fails validation (e.g., empty name).

    Args:
        message: Human-readable description of the error.
    """
