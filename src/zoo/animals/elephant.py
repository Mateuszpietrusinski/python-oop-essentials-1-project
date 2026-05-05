"""Elephant concrete species class for the Zoo Garden system."""

from __future__ import annotations

from .mammal import Mammal


class Elephant(Mammal):
    """Concrete species: African Elephant (Loxodonta africana).

    Attributes:
        tusk_length: Length of tusks in metres.
    """

    def __init__(self, name: str, age: int, tusk_length: float = 0.0) -> None:
        """Initialise an Elephant.

        Args:
            name: Display name.
            age: Age in years.
            tusk_length: Tusk length in metres. Defaults to 0.0.
        """
        super().__init__(name, "Loxodonta africana", age, fur_color="grey")
        self.tusk_length: float = tusk_length

    def make_sound(self) -> str:
        """Return the elephant's trumpet.

        Returns:
            Trumpet string.
        """
        return f"{self._name} trumpets: PAWOO!"

    def diet(self) -> str:
        """Return elephant-specific diet.

        Returns:
            Diet string for elephants.
        """
        return f"{self._name} is an herbivore — eats grass, leaves and fruit."
