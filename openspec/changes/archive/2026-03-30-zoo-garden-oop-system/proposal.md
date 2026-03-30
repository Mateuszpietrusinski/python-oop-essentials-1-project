## Why

This project implements a Zoo Garden management system as a university semester project for Object-Oriented Programming I. The goal is to demonstrate mastery of core OOP concepts (inheritance, composition, polymorphism, abstract classes, encapsulation, operator overloading, custom exceptions) through a practical, well-structured Python application.

## What Changes

- Implement the full `Zoo Garden` system from scratch as specified in `Projekt_A_Zoo_Garden.md`
- Create a multi-module Python package (`src/zoo/`) with proper separation of concerns
- Deliver a working demo (`demo.py`) and exactly 15 pytest test cases
- Provide required documentation: `README.md`, `CHECKLIST.md`, `JUSTIFICATION.md`

Specific new modules:
- `exceptions.py` — custom exception hierarchy (`ZooError`, `EnclosureFullError`, `AnimalNotFoundError`, `InvalidAnimalDataError`)
- `animals.py` — abstract `Animal` base, intermediate types (`Mammal`, `Bird`, `Reptile`), 6 concrete species
- `employees.py` — abstract `Employee` base, `Zookeeper`, `Veterinarian`, `Guide`
- `enclosure.py` — `Enclosure` class with dunder methods and aggregation of animals
- `feeding.py` — `FeedingEntry` dataclass and `FeedingSchedule` composition
- `zoo.py` — top-level `Zoo` class with composition of enclosures and aggregation of employees
- `tests/` — `conftest.py` with fixtures and `test_zoo.py` with 15 test scenarios
- `demo.py` — demonstration script covering all 7 required scenarios

## Capabilities

### New Capabilities

- `animal-hierarchy`: Abstract `Animal` base class with `Mammal`, `Bird`, `Reptile` intermediates and 6 concrete species (Lion, Elephant, Monkey, Eagle, Penguin, Crocodile); includes health property with clamping, auto-ID, dunder methods, and polymorphic `make_sound()`/`diet()`
- `employee-system`: Abstract `Employee` base with `Zookeeper` (enclosure association), `Veterinarian` (specialization), and `Guide` (languages list); abstract `work()` and `role()` methods
- `enclosure-management`: `Enclosure` class with capacity enforcement, animal aggregation, `add_animal`/`remove_animal`/`find_animal`/`feed_all`, and dunder methods (`__len__`, `__contains__`, `__iter__`, `__eq__`, `__hash__`)
- `feeding-schedule`: `FeedingEntry` dataclass and `FeedingSchedule` composition class with `add_entry`, `remove_entry`, `get_by_enclosure`
- `zoo-core`: Top-level `Zoo` class composing enclosures and aggregating employees; `create_enclosure`, `hire_employee`, `total_animals`, `find_animal`, `report`, dunder methods
- `test-suite`: Exactly 15 pytest tests with fixtures and `pytest.raises` covering all major scenarios
- `demo-script`: `demo.py` demonstrating all 7 required scenarios end-to-end

### Modified Capabilities

## Impact

- New Python package at `src/zoo/` (no existing code to break)
- Requires Python 3.10+
- Dependencies: `pytest>=7.0.0`, optionally `pytest-cov>=4.0.0`
- New documentation files: `README.md`, `CHECKLIST.md`, `JUSTIFICATION.md`, `requirements.txt`
