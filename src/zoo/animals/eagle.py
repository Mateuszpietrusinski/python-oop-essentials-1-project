"""Eagle concrete species class for the Zoo Garden system."""

from __future__ import annotations

from .bird import Bird


class Eagle(Bird):
    """Concrete species: Bald Eagle (Haliaeetus leucocephalus)."""

    def __init__(self, name: str, age: int) -> None:
        """Initialise an Eagle.

        Args:
            name: Display name.
            age: Age in years.
        """
        super().__init__(name, "Haliaeetus leucocephalus", age, wingspan=2.1, can_fly=True)

    def make_sound(self) -> str:
        """Return the eagle's cry.

        Returns:
            Cry string.
        """
        return f"{self._name} screeches: KREE-EEE-AR!"
