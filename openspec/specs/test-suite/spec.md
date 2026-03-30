## ADDED Requirements

### Requirement: Exactly 15 pytest tests
The system SHALL include exactly 15 test functions in `tests/test_zoo.py`, all passing. Tests SHALL use `pytest` fixtures defined in `tests/conftest.py`. Tests SHALL use `pytest.raises` for exception scenarios.

#### Scenario: All tests pass
- **WHEN** `pytest tests/` is run
- **THEN** all 15 tests pass with exit code 0

### Requirement: Test coverage of all 15 specified scenarios
The test file SHALL cover these exact scenarios (one test function each):
1. Creating animals of different types (`Lion`, `Eagle`, `Crocodile`)
2. Checking base stats and properties (`id`, `name`, `health`, `age`)
3. Adding animals to an enclosure
4. Capacity validation — `EnclosureFullError` on full enclosure
5. Removing an animal — `AnimalNotFoundError` on missing animal
6. Feeding animals: `feed()` and `feed_all()`
7. Health clamping (above 100, below 0)
8. Object equality via `__eq__`
9. Sorting with `__lt__` via `sorted()`
10. Data validation — `InvalidAnimalDataError` on empty name
11. `__str__` and `__repr__` representations
12. Polymorphism — `make_sound()` and `diet()` on a mixed list
13. Inheritance — `isinstance()` and `issubclass()` checks
14. `FeedingSchedule` — add and remove entries
15. Zoo report — output contains expected content

#### Scenario: Test 4 uses pytest.raises
- **WHEN** test 4 runs
- **THEN** it uses `pytest.raises(EnclosureFullError)` to assert the exception

### Requirement: conftest.py fixtures
`tests/conftest.py` SHALL define reusable pytest fixtures including at minimum: a `zoo` fixture (Zoo instance with at least one enclosure) and an `enclosure` fixture (Enclosure with animals). Fixtures SHALL use `@pytest.fixture` decorator.

#### Scenario: Fixtures are reusable across tests
- **WHEN** multiple test functions declare the same fixture parameter
- **THEN** each test gets a fresh instance (function scope)
