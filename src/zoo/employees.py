"""Employee class hierarchy for the Zoo Garden system.

Hierarchy:
    Employee (ABC)
    ├── Zookeeper   – manages and feeds animals in an assigned enclosure
    ├── Veterinarian – provides medical care with a specialization
    └── Guide        – leads visitor tours in multiple languages
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from .enclosure import Enclosure


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


class Zookeeper(Employee):
    """A zookeeper responsible for the day-to-day care of animals.

    Associated with a single Enclosure (association relationship).
    The enclosure can exist independently of the zookeeper.
    """

    def __init__(self, name: str, salary: float = 4500.0) -> None:
        """Initialise a Zookeeper.

        Args:
            name: Employee's full name.
            salary: Monthly salary in PLN. Defaults to 4500.0.
        """
        super().__init__(name, salary)
        self._assigned_enclosure: Optional[Enclosure] = None

    def assign_to(self, enclosure: Enclosure) -> None:
        """Assign this zookeeper to an enclosure.

        Args:
            enclosure: The Enclosure to be responsible for.
        """
        self._assigned_enclosure = enclosure

    def feed_animals(self) -> str:
        """Feed all animals in the assigned enclosure.

        Returns:
            A summary string of the feeding activity, or a message
            indicating no enclosure is assigned.
        """
        if self._assigned_enclosure is None:
            return f"{self._name} is not assigned to any enclosure."
        results = self._assigned_enclosure.feed_all()
        summary = "\n  ".join(results)
        return (
            f"{self._name} fed animals in '{self._assigned_enclosure.name}':\n  {summary}"
        )

    def work(self) -> str:
        """Describe the zookeeper's work.

        Returns:
            Work activity description.
        """
        if self._assigned_enclosure:
            return (
                f"{self._name} is cleaning and maintaining '{self._assigned_enclosure.name}'."
            )
        return f"{self._name} is waiting for an enclosure assignment."

    def role(self) -> str:
        """Return the zookeeper's role description.

        Returns:
            Role string including assigned enclosure if any.
        """
        enc = self._assigned_enclosure.name if self._assigned_enclosure else "unassigned"
        return f"Zookeeper — assigned to: {enc}"


class Veterinarian(Employee):
    """A veterinarian providing medical care to zoo animals.

    Can specialise in either general or exotic animal medicine.
    """

    def __init__(
        self,
        name: str,
        specialization: str = "general",
        salary: float = 7000.0,
    ) -> None:
        """Initialise a Veterinarian.

        Args:
            name: Employee's full name.
            specialization: Medical specialization ("general" or "exotic").
            salary: Monthly salary in PLN. Defaults to 7000.0.
        """
        super().__init__(name, salary)
        self._specialization: str = specialization

    @property
    def specialization(self) -> str:
        """Medical specialization ("general" or "exotic")."""
        return self._specialization

    def work(self) -> str:
        """Describe the veterinarian's work.

        Returns:
            Work activity description.
        """
        return f"{self._name} is conducting health checks on {self._specialization} animals."

    def role(self) -> str:
        """Return the veterinarian's role description.

        Returns:
            Role string including specialization.
        """
        return f"Veterinarian ({self._specialization} specialization)"


class Guide(Employee):
    """A tour guide leading visitors around the zoo.

    Speaks one or more languages to serve international visitors.
    """

    def __init__(
        self,
        name: str,
        languages: Optional[list[str]] = None,
        salary: float = 3500.0,
    ) -> None:
        """Initialise a Guide.

        Args:
            name: Employee's full name.
            languages: List of languages the guide speaks. Defaults to ["English"].
            salary: Monthly salary in PLN. Defaults to 3500.0.
        """
        super().__init__(name, salary)
        self._languages: list[str] = languages if languages is not None else ["English"]

    @property
    def languages(self) -> list[str]:
        """Languages the guide can use for tours."""
        return list(self._languages)

    def work(self) -> str:
        """Describe the guide's work.

        Returns:
            Work activity description.
        """
        langs = ", ".join(self._languages)
        return f"{self._name} is leading a guided tour in: {langs}."

    def role(self) -> str:
        """Return the guide's role description.

        Returns:
            Role string including spoken languages.
        """
        langs = ", ".join(self._languages)
        return f"Guide — languages: {langs}"
