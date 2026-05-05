"""Reptile intermediate class for the Zoo Garden system."""

from __future__ import annotations

from .animal import Animal


class Reptile(Animal):
    """Abstract intermediate class for reptiles.

    Adds is_venomous attribute.
    """

    def __init__(
        self,
        name: str,
        species: str,
        age: int,
        is_venomous: bool = False,
    ) -> None:
        """Initialise a Reptile.

        Args:
            name: Display name.
            species: Biological species.
            age: Age in years.
            is_venomous: Whether the reptile is venomous. Defaults to False.
        """
        super().__init__(name, species, age)
        self.is_venomous: bool = is_venomous

    def diet(self) -> str:
        """Return reptile default diet description.

        Returns:
            Diet string for generic reptiles.
        """
        return f"{self._name} is a carnivore that hunts prey."

    def bask(self) -> str:
        """Simulate basking in the sun.

        Returns:
            A string describing the basking behaviour.
        """
        return f"{self._name} is basking in the warm sunlight."
