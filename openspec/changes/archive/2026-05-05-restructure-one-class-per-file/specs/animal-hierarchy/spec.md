## MODIFIED Requirements

### Requirement: Abstract Animal base class
The system SHALL define an abstract base class `Animal` (inheriting from `ABC`) in `src/zoo/animals/animal.py`. It SHALL have a class-level counter `_next_id: int = 1` that auto-increments for each new instance, storing the assigned integer in `self._id`. Constructor parameters: `name: str`, `species: str`, `age: int`. The class SHALL be uninstantiable directly.

#### Scenario: Direct instantiation raises TypeError
- **WHEN** code attempts `Animal("X", "X", 1)` directly
- **THEN** Python raises `TypeError` because `Animal` is abstract

#### Scenario: Auto-increment ID
- **WHEN** two animals of any species are created in sequence
- **THEN** the second animal's `id` is exactly one greater than the first

#### Scenario: Public import path is unchanged
- **WHEN** consumer code runs `from zoo import Animal`
- **THEN** the import succeeds and resolves to the class defined in `src/zoo/animals/animal.py`

### Requirement: Intermediate animal classes
The system SHALL define three intermediate abstract classes inheriting from `Animal`, each in its own module under `src/zoo/animals/`:

- `Mammal` in `src/zoo/animals/mammal.py` — adds `fur_color: str`; provides default `diet()` returning a herbivore string and a `give_birth()` method.
- `Bird` in `src/zoo/animals/bird.py` — adds `wingspan: float` and `can_fly: bool`; provides default `diet()` and a `fly()` method that returns a non-flying message when `can_fly=False`.
- `Reptile` in `src/zoo/animals/reptile.py` — adds `is_venomous: bool`; provides default `diet()` and a `bask()` method.

Each module SHALL contain exactly one top-level class.

#### Scenario: Each intermediate lives in its own module
- **WHEN** the developer inspects `src/zoo/animals/mammal.py`, `bird.py`, `reptile.py`
- **THEN** each file defines exactly one top-level `class` and imports `Animal` via `from .animal import Animal`

### Requirement: Concrete species classes
The system SHALL define six concrete species, each in its own module under `src/zoo/animals/`:

| Class      | Module                              | Inherits from |
|------------|-------------------------------------|---------------|
| `Lion`     | `src/zoo/animals/lion.py`           | `Mammal`      |
| `Elephant` | `src/zoo/animals/elephant.py`       | `Mammal`      |
| `Monkey`   | `src/zoo/animals/monkey.py`         | `Mammal`      |
| `Eagle`    | `src/zoo/animals/eagle.py`          | `Bird`        |
| `Penguin`  | `src/zoo/animals/penguin.py`        | `Bird`        |
| `Crocodile`| `src/zoo/animals/crocodile.py`      | `Reptile`     |

Each species SHALL implement `make_sound()` and (where appropriate) override `diet()`. Each module SHALL contain exactly one top-level class.

#### Scenario: One class per concrete-species module
- **WHEN** any concrete species file is inspected
- **THEN** the file contains exactly one top-level `class` definition

#### Scenario: Top-level barrel re-exports every species
- **WHEN** consumer code runs `from zoo import Lion, Elephant, Monkey, Eagle, Penguin, Crocodile`
- **THEN** all six imports succeed unchanged from the prior layout

### Requirement: animals package barrel
`src/zoo/animals/__init__.py` SHALL re-export `Animal`, `Mammal`, `Bird`, `Reptile`, `Lion`, `Elephant`, `Monkey`, `Eagle`, `Penguin`, `Crocodile` so that both `from zoo import Lion` (top-level) and `from zoo.animals import Lion` (sub-package) resolve to the same class object.

#### Scenario: Sub-package import works
- **WHEN** code runs `from zoo.animals import Lion`
- **THEN** the import succeeds and the resulting class is the same object as `zoo.Lion`
