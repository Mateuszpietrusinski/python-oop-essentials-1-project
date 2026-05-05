"""Penguin concrete species class for the Zoo Garden system."""

from __future__ import annotations

from .bird import Bird


class Penguin(Bird):
    """Concrete species: Emperor Penguin (Aptenodytes forsteri).

    Penguins cannot fly (can_fly=False) but are excellent swimmers.
    """

    def __init__(self, name: str, age: int) -> None:
        """Initialise a Penguin.

        Args:
            name: Display name.
            age: Age in years.
        """
        super().__init__(name, "Aptenodytes forsteri", age, wingspan=0.3, can_fly=False)

    def make_sound(self) -> str:
        """Return the penguin's call.

        Returns:
            Call string.
        """
        return f"{self._name} squawks: BRAP BRAP!"
