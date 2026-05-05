## Why

The current package layout groups multiple classes per file (`animals.py` holds 9 classes across 470 lines, `employees.py` holds 4, `feeding.py` holds 2, `exceptions.py` holds 4). This makes the project look "monolithic per concern" rather than fully modular, and when the teacher (or any reader) asks *"where is class X defined?"* the answer requires grepping inside a file rather than reading a path.

We want a stricter **one class per file** layout, with classes grouped into sub-packages by domain (animals, employees, feeding, exceptions). The public import surface (`from zoo import Lion, Zookeeper, ...`) MUST remain identical — no behavior changes, only file boundaries.

The single test file (`tests/test_zoo.py`, 15 functions, 269 lines) is also split into per-capability test modules so each spec area maps to its own test file, while preserving exactly 15 test functions in total.

## What Changes

### Source layout (`src/zoo/`)

- **NEW sub-package `exceptions/`** with one file per exception class:
  `zoo_error.py`, `enclosure_full_error.py`, `animal_not_found_error.py`, `invalid_animal_data_error.py`. The current flat `exceptions.py` is removed.
- **NEW sub-package `animals/`** with one file per class:
  `animal.py`, `mammal.py`, `bird.py`, `reptile.py`, `lion.py`, `elephant.py`, `monkey.py`, `eagle.py`, `penguin.py`, `crocodile.py`. The current flat `animals.py` is removed.
- **NEW sub-package `employees/`** with one file per class:
  `employee.py`, `zookeeper.py`, `veterinarian.py`, `guide.py`. The current flat `employees.py` is removed.
- **NEW sub-package `feeding/`** with one file per class:
  `feeding_entry.py`, `feeding_schedule.py`. The current flat `feeding.py` is removed.
- `enclosure.py` and `zoo.py` stay as flat modules (each already contains only a single class — wrapping in a folder would be ceremony, not structure).
- `src/zoo/__init__.py` continues to re‑export the entire public API (`Zoo`, `Lion`, `Enclosure`, `Zookeeper`, `ZooError`, …) so all existing imports keep working unchanged.

### Test layout (`tests/`)

- The 15 test functions in `tests/test_zoo.py` are redistributed across capability‑aligned files (still **exactly 15** in total):
  - `tests/test_animals.py` — 8 tests (creation, properties, health clamping, equality, sorting, name validation, str/repr, polymorphism)
  - `tests/test_enclosure.py` — 4 tests (add, capacity error, remove-not-found, feed/feed_all)
  - `tests/test_feeding.py` — 1 test (feeding schedule add/remove)
  - `tests/test_zoo.py` — 2 tests (isinstance/issubclass, zoo report)
- `tests/conftest.py` is unchanged — fixtures stay shared across all test files.

### Documentation

- `README.md` — update *Struktura projektu* tree, the *Mechanizmy OOP* "Lokalizacja" table, and any other module path references.
- `CHECKLIST.md` — every "Lokalizacja" line now points to the new per-class file (e.g. `src/zoo/animals/lion.py: Lion.make_sound`).
- `JUSTIFICATION.md` — rewrite **J9** (tests are now split per capability, not in one file) and **J10** (new module layout and import order).
- `Projekt_A_Zoo_Garden.md` — update the file-tree section and any `# animals.py` / `# employees.py` headings to reflect new paths (this is a working document, not a frozen requirements snapshot).
- All six active specs under `openspec/specs/*/spec.md` have their file-path references updated via this change's spec deltas.

## Capabilities

### Modified Capabilities

- `animal-hierarchy` — file paths only: each `Animal*` / `Mammal` / `Bird` / `Reptile` / concrete species class moves to its own file under `src/zoo/animals/`.
- `employee-system` — file paths only: `Employee` and concrete roles each move to their own file under `src/zoo/employees/`.
- `enclosure-management` — no path change (`Enclosure` stays at `src/zoo/enclosure.py`); included for completeness only if cross‑references to other modules' filenames need refreshing.
- `feeding-schedule` — file paths only: `FeedingEntry` and `FeedingSchedule` each move to their own file under `src/zoo/feeding/`.
- `zoo-core` — no path change (`Zoo` stays at `src/zoo/zoo.py`).
- `test-suite` — the "exactly 15 tests in `tests/test_zoo.py`" requirement is replaced by "exactly 15 tests distributed across `test_animals.py`, `test_enclosure.py`, `test_feeding.py`, `test_zoo.py`".

### Removed Capabilities

None. No public class, method, exception, or behavior is removed.

### Added Capabilities

None. This is a pure structural refactor.

## Impact

- **Public API**: unchanged. Every `from zoo import X` keeps working because `src/zoo/__init__.py` re-exports the same names.
- **Tests**: 15 test functions preserved; only their location changes. `pytest tests/` still discovers and runs all 15.
- **Demo**: `demo.py` is untouched (only top-level `from zoo import …`).
- **External consumers**: none — this is a coursework project. Internal sub-package paths (`from zoo.animals import Lion`) are also supported as a side benefit for developers.
- **Risk**: low. The refactor is mechanical (move class definitions, fix internal imports, update barrels). Test suite remains the safety net — a green `pytest` run after the move is the acceptance signal.
