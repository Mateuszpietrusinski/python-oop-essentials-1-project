"""Abstract base Employee class for the Zoo Garden system."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract base class for all zoo employees.

    Attributes:
        _next_id: Class-level counter shared across all Employee subclasses.
    """

    _next_id: int = 1

    def __init__(self, name: str, salary: float) -> None:
        """Initialise a new Employee instance.

        Args:
            name: Employee's full name.
            salary: Monthly salary in PLN.
        """
        self._id: int = Employee._next_id
        Employee._next_id += 1
        self._name: str = name
        self._salary: float = salary

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def id(self) -> int:
        """Unique auto-incremented identifier."""
        return self._id

    @property
    def name(self) -> str:
        """Employee's full name."""
        return self._name

    @property
    def salary(self) -> float:
        """Monthly salary in PLN."""
        return self._salary

    # ------------------------------------------------------------------
    # Abstract methods
    # ------------------------------------------------------------------

    @abstractmethod
    def work(self) -> str:
        """Describe the employee's current work activity.

        Returns:
            A string describing what the employee is doing.
        """

    @abstractmethod
    def role(self) -> str:
        """Return the employee's role title and key attributes.

        Returns:
            A string describing the employee's role.
        """

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        """Machine-readable representation."""
        return f"{self.__class__.__name__}(id={self._id}, name={self._name!r})"

    def __eq__(self, other: object) -> bool:
        """Compare employees by their unique ID.

        Args:
            other: Object to compare against.

        Returns:
            True if both are Employee instances with the same ID.
        """
        if not isinstance(other, Employee):
            return NotImplemented
        return self._id == other._id

    def __hash__(self) -> int:
        """Hash based on unique ID."""
        return hash(self._id)
