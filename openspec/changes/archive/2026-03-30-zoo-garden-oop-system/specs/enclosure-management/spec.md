## ADDED Requirements

### Requirement: Enclosure class with capacity
The system SHALL define `Enclosure` in `src/zoo/enclosure.py` with constructor `(name: str, capacity: int)`. It SHALL maintain an internal `list` of animals. The `animals` property SHALL return a copy (`list(self._animals)`).

#### Scenario: Empty enclosure has zero length
- **WHEN** a new `Enclosure("Savanna", 5)` is created
- **THEN** `len(enclosure)` returns `0`

### Requirement: add_animal enforces capacity
`add_animal(animal: Animal) -> None` SHALL append the animal to the internal list. If the list is already at capacity, it SHALL raise `EnclosureFullError`.

#### Scenario: Adding animal to full enclosure
- **WHEN** an enclosure at capacity has `add_animal` called
- **THEN** `EnclosureFullError` is raised and the animal is not added

#### Scenario: Adding animal within capacity
- **WHEN** `add_animal` is called on an enclosure below capacity
- **THEN** `len(enclosure)` increases by 1

### Requirement: remove_animal raises AnimalNotFoundError
`remove_animal(animal: Animal) -> Animal` SHALL remove and return the animal. If the animal is not present, it SHALL raise `AnimalNotFoundError`.

#### Scenario: Removing absent animal
- **WHEN** `remove_animal` is called with an animal not in the enclosure
- **THEN** `AnimalNotFoundError` is raised

### Requirement: find_animal by name
`find_animal(name: str) -> Animal | None` SHALL return the first animal whose name matches (case-sensitive), or `None` if not found.

#### Scenario: Finding existing animal
- **WHEN** `find_animal("Simba")` is called and Simba is in the enclosure
- **THEN** the Lion instance for Simba is returned

### Requirement: feed_all method
`feed_all() -> list[str]` SHALL call `feed()` on every animal in the enclosure and return the list of result strings.

#### Scenario: feed_all returns results for all animals
- **WHEN** enclosure has 3 animals and `feed_all()` is called
- **THEN** a list of 3 strings is returned

### Requirement: Enclosure dunder methods
`Enclosure` SHALL implement: `__len__` (number of animals), `__contains__` (checks if animal is in list), `__iter__` (iterates over animals), `__repr__` (machine-readable), `__eq__` (compares by `name`), `__hash__` (hashes `name`).

#### Scenario: in operator
- **WHEN** `lion in enclosure` is evaluated after adding the lion
- **THEN** it returns `True`

#### Scenario: Iteration
- **WHEN** `for animal in enclosure` is used
- **THEN** each animal in the enclosure is visited exactly once
