## ADDED Requirements

### Requirement: Abstract Animal base class
The system SHALL define an abstract base class `Animal` (inheriting from `ABC`) in `src/zoo/animals.py`. It SHALL have a class-level counter `_next_id: int = 1` that auto-increments for each new instance, storing the assigned integer in `self._id`. Constructor parameters: `name: str`, `species: str`, `age: int`. The class SHALL be uninstantiable directly.

#### Scenario: Direct instantiation raises TypeError
- **WHEN** code attempts `Animal("X", "X", 1)` directly
- **THEN** Python raises `TypeError` because `Animal` is abstract

#### Scenario: Auto-increment ID
- **WHEN** two animals of any species are created in sequence
- **THEN** the second animal's `id` is exactly one greater than the first

### Requirement: health property with clamping
The `Animal` class SHALL expose a `health` property (int, default 100). The setter SHALL clamp the value to the range [0, 100] using `max(0, min(100, value))` without raising exceptions.

#### Scenario: Setting health above 100 clamps to 100
- **WHEN** `animal.health = 150` is called
- **THEN** `animal.health` returns `100`

#### Scenario: Setting health below 0 clamps to 0
- **WHEN** `animal.health = -10` is called
- **THEN** `animal.health` returns `0`

### Requirement: name property with validation
The `name` property setter SHALL raise `InvalidAnimalDataError` if the value is an empty string or whitespace-only.

#### Scenario: Empty name raises InvalidAnimalDataError
- **WHEN** `animal.name = ""` is called
- **THEN** `InvalidAnimalDataError` is raised

### Requirement: Animal dunder methods
`Animal` SHALL implement: `__repr__` (machine-readable string), `__str__` (human-readable string), `__eq__` (compares by `_id`), `__hash__` (hashes `_id`), `__lt__` (compares by `name` for sorting).

#### Scenario: Equality by ID
- **WHEN** two different animal instances have different IDs even with the same name
- **THEN** `lion1 == lion2` returns `False`

#### Scenario: Sorting by name
- **WHEN** `sorted([lion_C, eagle_A, penguin_B])` is called
- **THEN** result order is `[eagle_A, penguin_B, lion_C]`

### Requirement: Abstract methods make_sound and diet
`Animal` SHALL declare `make_sound() -> str` and `diet() -> str` as `@abstractmethod`. Concrete subclasses MUST implement both.

#### Scenario: Concrete species implement make_sound
- **WHEN** `lion.make_sound()` is called on a `Lion` instance
- **THEN** it returns a non-empty string specific to lions

### Requirement: feed method
`Animal` SHALL implement `feed() -> str` returning a string confirming the animal was fed.

#### Scenario: Feeding an animal
- **WHEN** `animal.feed()` is called
- **THEN** it returns a string containing the animal's name

### Requirement: Mammal intermediate class
`Mammal(Animal)` SHALL accept additional parameter `fur_color: str = "brown"`. It SHALL implement `diet() -> str` returning a string describing mammal diet. It SHALL provide `give_birth() -> str`.

#### Scenario: Mammal diet
- **WHEN** `mammal.diet()` is called on any Mammal subclass that doesn't override it
- **THEN** it returns a string describing mammal diet

### Requirement: Bird intermediate class
`Bird(Animal)` SHALL accept `wingspan: float = 1.0` and `can_fly: bool = True`. It SHALL implement `diet() -> str` and `fly() -> str`. `fly()` SHALL handle the case where `can_fly` is `False` gracefully (return descriptive string, not raise).

#### Scenario: Penguin cannot fly
- **WHEN** `penguin.fly()` is called (Penguin has can_fly=False)
- **THEN** it returns a string indicating it cannot fly, no exception raised

### Requirement: Reptile intermediate class
`Reptile(Animal)` SHALL accept `is_venomous: bool = False`. It SHALL implement `diet() -> str` and `bask() -> str`.

#### Scenario: Bask method
- **WHEN** `crocodile.bask()` is called
- **THEN** it returns a non-empty string

### Requirement: Six concrete animal species
The system SHALL implement exactly: `Lion(Mammal)`, `Elephant(Mammal)`, `Monkey(Mammal)`, `Eagle(Bird)`, `Penguin(Bird)`, `Crocodile(Reptile)`. Each SHALL implement `make_sound() -> str` with a species-specific sound. `Lion` and `Elephant` SHALL override `diet()`. Constructors: `Lion(name, age, mane=True)`, `Elephant(name, age, tusk_length=0.0)`, `Monkey(name, age)`, `Eagle(name, age)`, `Penguin(name, age)`, `Crocodile(name, age, length=3.0)`.

#### Scenario: isinstance checks
- **WHEN** `isinstance(lion, Mammal)` and `isinstance(lion, Animal)` are called
- **THEN** both return `True`

#### Scenario: Polymorphic make_sound
- **WHEN** `make_sound()` is called on a list containing Lion, Eagle, Crocodile
- **THEN** each returns a different species-specific string without error
