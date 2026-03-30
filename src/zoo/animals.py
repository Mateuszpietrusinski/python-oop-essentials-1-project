"""Animal class hierarchy for the Zoo Garden system.

Hierarchy:
    Animal (ABC)
    ├── Mammal  → Lion, Elephant, Monkey
    ├── Bird    → Eagle, Penguin
    └── Reptile → Crocodile
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .exceptions import InvalidAnimalDataError


class Animal(ABC):
    """Abstract base class for all animals in the zoo.

    Attributes:
        _next_id: Class-level counter shared across all Animal subclasses.
    """

    _next_id: int = 1

    def __init__(self, name: str, species: str, age: int) -> None:
        """Initialise a new Animal instance.

        Args:
            name: The animal's display name. Must be non-empty.
            species: The biological species name.
            age: Age in years (non-negative).

        Raises:
            InvalidAnimalDataError: If name is empty or whitespace-only.
        """
        self._id: int = Animal._next_id
        Animal._next_id += 1
        self._species: str = species
        self._age: int = age
        self._health: int = 100
        # Use the property setter for validation
        self.name = name

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def id(self) -> int:
        """Unique auto-incremented identifier."""
        return self._id

    @property
    def name(self) -> str:
        """The animal's display name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the animal's name with validation.

        Args:
            value: New name string.

        Raises:
            InvalidAnimalDataError: If value is empty or whitespace-only.
        """
        if not value or not value.strip():
            raise InvalidAnimalDataError("Animal name must not be empty.")
        self._name = value

    @property
    def species(self) -> str:
        """The biological species name."""
        return self._species

    @property
    def age(self) -> int:
        """Age in years."""
        return self._age

    @property
    def health(self) -> int:
        """Health level clamped to [0, 100]."""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set health, clamping to [0, 100].

        Args:
            value: Desired health value. Values outside [0, 100] are silently clamped.
        """
        self._health = max(0, min(100, value))

    # ------------------------------------------------------------------
    # Abstract methods
    # ------------------------------------------------------------------

    @abstractmethod
    def make_sound(self) -> str:
        """Return the sound this animal makes.

        Returns:
            A species-specific sound string.
        """

    @abstractmethod
    def diet(self) -> str:
        """Return a description of this animal's diet.

        Returns:
            A string describing what the animal eats.
        """

    # ------------------------------------------------------------------
    # Concrete methods
    # ------------------------------------------------------------------

    def feed(self) -> str:
        """Feed the animal.

        Returns:
            A confirmation string containing the animal's name.
        """
        return f"{self._name} has been fed."

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        """Machine-readable representation."""
        return f"{self.__class__.__name__}(id={self._id}, name={self._name!r}, age={self._age})"

    def __str__(self) -> str:
        """Human-readable representation."""
        return f"{self._name} ({self._species}), age {self._age}, health {self._health}%"

    def __eq__(self, other: object) -> bool:
        """Compare animals by their unique ID.

        Args:
            other: Object to compare against.

        Returns:
            True if both objects are Animal instances with the same ID.
        """
        if not isinstance(other, Animal):
            return NotImplemented
        return self._id == other._id

    def __hash__(self) -> int:
        """Hash based on unique ID."""
        return hash(self._id)

    def __lt__(self, other: object) -> bool:
        """Compare animals by name (enables sorted()).

        Args:
            other: Animal to compare against.

        Returns:
            True if this animal's name is lexicographically less than other's.
        """
        if not isinstance(other, Animal):
            return NotImplemented
        return self._name < other._name


# ---------------------------------------------------------------------------
# Intermediate classes
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Concrete species
# ---------------------------------------------------------------------------


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
