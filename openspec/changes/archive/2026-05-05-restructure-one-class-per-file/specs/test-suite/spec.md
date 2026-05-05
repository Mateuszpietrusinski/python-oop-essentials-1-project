## MODIFIED Requirements

### Requirement: Exactly 15 pytest tests, distributed by capability
The system SHALL include **exactly 15 test functions in total** across the `tests/` directory, all passing. Tests SHALL be distributed across capability-aligned files:

| File                       | Test count | Capability area              |
|----------------------------|------------|------------------------------|
| `tests/test_animals.py`    | 8          | `animal-hierarchy`           |
| `tests/test_enclosure.py`  | 4          | `enclosure-management`       |
| `tests/test_feeding.py`    | 1          | `feeding-schedule`           |
| `tests/test_zoo.py`        | 2          | `zoo-core`                   |
| **Total**                  | **15**     |                              |

Tests SHALL use `pytest` fixtures defined in `tests/conftest.py`. Tests SHALL use `pytest.raises` for exception scenarios.

#### Scenario: All tests pass
- **WHEN** `pytest tests/` is run
- **THEN** all 15 tests pass with exit code 0

#### Scenario: Test count auditable by grep
- **WHEN** `grep -rE '^def test_' tests/` is run
- **THEN** the result contains exactly 15 lines

### Requirement: Test coverage of all 15 specified scenarios
The test suite SHALL cover these exact scenarios (one test function each, with the original function name preserved):

`tests/test_animals.py`:
1. `test_create_animals_different_types` — creating `Lion`, `Eagle`, `Crocodile`
2. `test_base_stats_and_properties` — `id`, `name`, `health`, `age`
3. `test_health_clamping` — clamping above 100 and below 0
4. `test_eq_by_id` — `__eq__` by id
5. `test_sorted_by_name` — `__lt__` via `sorted()`
6. `test_invalid_empty_name` — `InvalidAnimalDataError` on empty name
7. `test_str_and_repr` — `__str__` and `__repr__`
8. `test_polymorphism_make_sound_diet` — polymorphism on a mixed list

`tests/test_enclosure.py`:
9. `test_add_animals_to_enclosure` — adding animals
10. `test_enclosure_full_error` — `EnclosureFullError`
11. `test_remove_animal_not_found` — `AnimalNotFoundError`
12. `test_feed_and_feed_all` — `feed()` and `feed_all()`

`tests/test_feeding.py`:
13. `test_feeding_schedule_add_remove` — `FeedingSchedule` add/remove

`tests/test_zoo.py`:
14. `test_isinstance_issubclass` — inheritance checks
15. `test_zoo_report` — zoo report contains expected content

#### Scenario: Capacity exception test uses pytest.raises
- **WHEN** `test_enclosure_full_error` runs
- **THEN** it uses `pytest.raises(EnclosureFullError)` to assert the exception

### Requirement: conftest.py fixtures
`tests/conftest.py` SHALL define reusable pytest fixtures including at minimum: a `zoo` fixture (`Zoo` instance with at least one enclosure) and an `enclosure` fixture (`Enclosure` with animals). Fixtures SHALL use `@pytest.fixture` decorator and SHALL be discovered automatically by every `test_*.py` file in the `tests/` directory.

#### Scenario: Fixtures are reusable across files
- **WHEN** test functions in `test_animals.py`, `test_enclosure.py`, `test_feeding.py`, and `test_zoo.py` declare the `lion` / `enclosure` / `zoo` fixture parameters
- **THEN** each test gets a fresh instance from `conftest.py` (function scope), no per-file fixture duplication is required
