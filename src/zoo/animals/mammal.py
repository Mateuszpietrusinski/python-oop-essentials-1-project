"""Mammal intermediate class for the Zoo Garden system."""

from __future__ import annotations

from .animal import Animal


class Mammal(Animal):
    """Abstract intermediate class for mammals.

    Adds fur_color attribute and mammal-specific behaviours.
    """

    def __init__(
        self,
        name: str,
        species: str,
        age: int,
        fur_color: str = "brown",
    ) -> None:
        """Initialise a Mammal.

        Args:
            name: Display name.
            species: Biological species.
            age: Age in years.
            fur_color: Colour of the animal's fur. Defaults to "brown".
        """
        super().__init__(name, species, age)
        self.fur_color: str = fur_color

    def diet(self) -> str:
        """Return mammal default diet description.

        Returns:
            Diet string for generic mammals.
        """
        return f"{self._name} is an omnivore."

    def give_birth(self) -> str:
        """Simulate giving birth.

        Returns:
            A string announcing a new offspring.
        """
        return f"{self._name} has given birth to a new {self._species}!"
