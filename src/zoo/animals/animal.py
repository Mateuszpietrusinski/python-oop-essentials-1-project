"""Abstract base Animal class for the Zoo Garden system."""

from __future__ import annotations

from abc import ABC, abstractmethod

from ..exceptions import InvalidAnimalDataError


class Animal(ABC):
    """Abstract base class for all animals in the zoo.

    Attributes:
        _next_id: Class-level counter shared across all Animal subclasses.
    """

    _next_id: int = 1

    def __init__(self, name: str, species: str, age: int) -> None:
        """Initialise a new Animal instance.

        Args:
            name: The animal's display name. Must be non-empty.
            species: The biological species name.
            age: Age in years (non-negative).

        Raises:
            InvalidAnimalDataError: If name is empty or whitespace-only.
        """
        self._id: int = Animal._next_id
        Animal._next_id += 1
        self._species: str = species
        self._age: int = age
        self._health: int = 100
        # Use the property setter for validation
        self.name = name

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def id(self) -> int:
        """Unique auto-incremented identifier."""
        return self._id

    @property
    def name(self) -> str:
        """The animal's display name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the animal's name with validation.

        Args:
            value: New name string.

        Raises:
            InvalidAnimalDataError: If value is empty or whitespace-only.
        """
        if not value or not value.strip():
            raise InvalidAnimalDataError("Animal name must not be empty.")
        self._name = value

    @property
    def species(self) -> str:
        """The biological species name."""
        return self._species

    @property
    def age(self) -> int:
        """Age in years."""
        return self._age

    @property
    def health(self) -> int:
        """Health level clamped to [0, 100]."""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set health, clamping to [0, 100].

        Args:
            value: Desired health value. Values outside [0, 100] are silently clamped.
        """
        self._health = max(0, min(100, value))

    # ------------------------------------------------------------------
    # Abstract methods
    # ------------------------------------------------------------------

    @abstractmethod
    def make_sound(self) -> str:
        """Return the sound this animal makes.

        Returns:
            A species-specific sound string.
        """

    @abstractmethod
    def diet(self) -> str:
        """Return a description of this animal's diet.

        Returns:
            A string describing what the animal eats.
        """

    # ------------------------------------------------------------------
    # Concrete methods
    # ------------------------------------------------------------------

    def feed(self) -> str:
        """Feed the animal.

        Returns:
            A confirmation string containing the animal's name.
        """
        return f"{self._name} has been fed."

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        """Machine-readable representation."""
        return f"{self.__class__.__name__}(id={self._id}, name={self._name!r}, age={self._age})"

    def __str__(self) -> str:
        """Human-readable representation."""
        return f"{self._name} ({self._species}), age {self._age}, health {self._health}%"

    def __eq__(self, other: object) -> bool:
        """Compare animals by their unique ID.

        Args:
            other: Object to compare against.

        Returns:
            True if both objects are Animal instances with the same ID.
        """
        if not isinstance(other, Animal):
            return NotImplemented
        return self._id == other._id

    def __hash__(self) -> int:
        """Hash based on unique ID."""
        return hash(self._id)

    def __lt__(self, other: object) -> bool:
        """Compare animals by name (enables sorted()).

        Args:
            other: Animal to compare against.

        Returns:
            True if this animal's name is lexicographically less than other's.
        """
        if not isinstance(other, Animal):
            return NotImplemented
        return self._name < other._name
