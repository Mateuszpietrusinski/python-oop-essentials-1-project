"""Lion concrete species class for the Zoo Garden system."""

from __future__ import annotations

from .mammal import Mammal


class Lion(Mammal):
    """Concrete species: Lion (Panthera leo).

    Attributes:
        mane: Whether the lion has a mane (typically males).
    """

    def __init__(self, name: str, age: int, mane: bool = True) -> None:
        """Initialise a Lion.

        Args:
            name: Display name.
            age: Age in years.
            mane: Whether the lion has a mane. Defaults to True.
        """
        super().__init__(name, "Panthera leo", age, fur_color="golden")
        self.mane: bool = mane

    def make_sound(self) -> str:
        """Return the lion's roar.

        Returns:
            Roar string.
        """
        return f"{self._name} roars loudly: ROARRR!"

    def diet(self) -> str:
        """Return lion-specific diet.

        Returns:
            Diet string for lions.
        """
        return f"{self._name} is an apex predator — eats large mammals."
