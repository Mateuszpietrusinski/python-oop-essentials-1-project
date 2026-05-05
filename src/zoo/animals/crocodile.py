"""Crocodile concrete species class for the Zoo Garden system."""

from __future__ import annotations

from .reptile import Reptile


class Crocodile(Reptile):
    """Concrete species: Nile Crocodile (Crocodylus niloticus).

    Attributes:
        length: Body length in metres.
    """

    def __init__(self, name: str, age: int, length: float = 3.0) -> None:
        """Initialise a Crocodile.

        Args:
            name: Display name.
            age: Age in years.
            length: Body length in metres. Defaults to 3.0.
        """
        super().__init__(name, "Crocodylus niloticus", age, is_venomous=False)
        self.length: float = length

    def make_sound(self) -> str:
        """Return the crocodile's hiss.

        Returns:
            Hiss string.
        """
        return f"{self._name} hisses menacingly: HSSSSSS!"
