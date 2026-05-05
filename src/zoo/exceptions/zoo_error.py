"""Base exception for the Zoo Garden system."""


class ZooError(Exception):
    """Base exception for all Zoo Garden errors.

    All application-specific exceptions inherit from this class,
    allowing callers to catch any zoo-related error with a single except clause.
    """
