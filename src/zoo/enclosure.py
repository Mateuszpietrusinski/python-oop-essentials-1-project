"""Enclosure class for housing animals in the Zoo Garden system."""

from __future__ import annotations

from typing import Iterator

from .animals import Animal
from .exceptions import AnimalNotFoundError, EnclosureFullError


class Enclosure:
    """Represents a zoo enclosure that aggregates Animal instances.

    Animals can exist independently of the enclosure (aggregation).
    The enclosure enforces a maximum capacity and provides methods
    to manage its residents.

    Attributes:
        name: Human-readable name of the enclosure.
        capacity: Maximum number of animals allowed at once.
    """

    def __init__(self, name: str, capacity: int) -> None:
        """Initialise an Enclosure.

        Args:
            name: Display name for the enclosure.
            capacity: Maximum number of animals this enclosure can hold.
        """
        self._name: str = name
        self._capacity: int = capacity
        self._animals: list[Animal] = []

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def name(self) -> str:
        """Display name of the enclosure."""
        return self._name

    @property
    def capacity(self) -> int:
        """Maximum number of animals this enclosure can hold."""
        return self._capacity

    @property
    def animals(self) -> list[Animal]:
        """A copy of the list of animals currently in the enclosure.

        Returns a copy to prevent external mutation of the internal list.
        """
        return list(self._animals)

    # ------------------------------------------------------------------
    # Animal management
    # ------------------------------------------------------------------

    def add_animal(self, animal: Animal) -> None:
        """Add an animal to the enclosure.

        Args:
            animal: The Animal instance to add.

        Raises:
            EnclosureFullError: If the enclosure is already at capacity.
        """
        if len(self._animals) >= self._capacity:
            raise EnclosureFullError(
                f"Enclosure '{self._name}' is full (capacity={self._capacity})."
            )
        self._animals.append(animal)

    def remove_animal(self, animal: Animal) -> Animal:
        """Remove and return an animal from the enclosure.

        Args:
            animal: The Animal instance to remove.

        Returns:
            The removed Animal instance.

        Raises:
            AnimalNotFoundError: If the animal is not in this enclosure.
        """
        if animal not in self._animals:
            raise AnimalNotFoundError(
                f"Animal '{animal.name}' not found in enclosure '{self._name}'."
            )
        self._animals.remove(animal)
        return animal

    def find_animal(self, name: str) -> Animal | None:
        """Find an animal by name (case-sensitive).

        Args:
            name: The name to search for.

        Returns:
            The first Animal whose name matches, or None if not found.
        """
        for animal in self._animals:
            if animal.name == name:
                return animal
        return None

    def feed_all(self) -> list[str]:
        """Feed every animal in the enclosure.

        Returns:
            A list of strings, one per animal, confirming each was fed.
        """
        return [animal.feed() for animal in self._animals]

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """Return the current number of animals in the enclosure."""
        return len(self._animals)

    def __contains__(self, animal: object) -> bool:
        """Check whether an animal is in this enclosure.

        Args:
            animal: Object to look for.

        Returns:
            True if the animal is present, False otherwise.
        """
        return animal in self._animals

    def __iter__(self) -> Iterator[Animal]:
        """Iterate over animals in the enclosure.

        Returns:
            An iterator over Animal instances.
        """
        return iter(self._animals)

    def __repr__(self) -> str:
        """Machine-readable representation."""
        return (
            f"Enclosure(name={self._name!r}, capacity={self._capacity}, "
            f"animals={len(self._animals)})"
        )

    def __eq__(self, other: object) -> bool:
        """Compare enclosures by name.

        Args:
            other: Object to compare against.

        Returns:
            True if both are Enclosure instances with the same name.
        """
        if not isinstance(other, Enclosure):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Hash based on the enclosure name."""
        return hash(self._name)
