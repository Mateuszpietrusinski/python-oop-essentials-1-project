"""Bird intermediate class for the Zoo Garden system."""

from __future__ import annotations

from .animal import Animal


class Bird(Animal):
    """Abstract intermediate class for birds.

    Adds wingspan and can_fly attributes.
    """

    def __init__(
        self,
        name: str,
        species: str,
        age: int,
        wingspan: float = 1.0,
        can_fly: bool = True,
    ) -> None:
        """Initialise a Bird.

        Args:
            name: Display name.
            species: Biological species.
            age: Age in years.
            wingspan: Wing span in metres. Defaults to 1.0.
            can_fly: Whether the bird is capable of flight. Defaults to True.
        """
        super().__init__(name, species, age)
        self.wingspan: float = wingspan
        self.can_fly: bool = can_fly

    def diet(self) -> str:
        """Return bird default diet description.

        Returns:
            Diet string for generic birds.
        """
        return f"{self._name} eats fish and small insects."

    def fly(self) -> str:
        """Attempt to fly.

        Returns:
            A string describing flight or explaining inability to fly.
        """
        if self.can_fly:
            return f"{self._name} spreads its wings and soars through the sky!"
        return f"{self._name} cannot fly, but swims gracefully instead."
