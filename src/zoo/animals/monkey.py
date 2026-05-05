"""Monkey concrete species class for the Zoo Garden system."""

from __future__ import annotations

from .mammal import Mammal


class Monkey(Mammal):
    """Concrete species: Common Chimpanzee (Pan troglodytes)."""

    def __init__(self, name: str, age: int) -> None:
        """Initialise a Monkey.

        Args:
            name: Display name.
            age: Age in years.
        """
        super().__init__(name, "Pan troglodytes", age, fur_color="black")

    def make_sound(self) -> str:
        """Return the monkey's chatter.

        Returns:
            Chatter string.
        """
        return f"{self._name} chatters: OOH OOH AAH AAH!"
