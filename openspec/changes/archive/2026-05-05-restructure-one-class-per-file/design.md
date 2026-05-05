# Design — One‑class‑per‑file restructure

## Target source layout

```
src/zoo/
├── __init__.py                       # public API barrel (UNCHANGED contract)
│
├── exceptions/
│   ├── __init__.py                   # re-exports ZooError, EnclosureFullError, …
│   ├── zoo_error.py                  # ZooError(Exception)
│   ├── enclosure_full_error.py       # EnclosureFullError(ZooError)
│   ├── animal_not_found_error.py     # AnimalNotFoundError(ZooError)
│   └── invalid_animal_data_error.py  # InvalidAnimalDataError(ZooError)
│
├── animals/
│   ├── __init__.py                   # re-exports Animal, Mammal, …, Crocodile
│   ├── animal.py                     # Animal(ABC)            — abstract base
│   ├── mammal.py                     # Mammal(Animal)         — abstract intermediate
│   ├── bird.py                       # Bird(Animal)           — abstract intermediate
│   ├── reptile.py                    # Reptile(Animal)        — abstract intermediate
│   ├── lion.py                       # Lion(Mammal)
│   ├── elephant.py                   # Elephant(Mammal)
│   ├── monkey.py                     # Monkey(Mammal)
│   ├── eagle.py                      # Eagle(Bird)
│   ├── penguin.py                    # Penguin(Bird)
│   └── crocodile.py                  # Crocodile(Reptile)
│
├── employees/
│   ├── __init__.py                   # re-exports Employee, Zookeeper, Veterinarian, Guide
│   ├── employee.py                   # Employee(ABC)
│   ├── zookeeper.py                  # Zookeeper(Employee)
│   ├── veterinarian.py               # Veterinarian(Employee)
│   └── guide.py                      # Guide(Employee)
│
├── feeding/
│   ├── __init__.py                   # re-exports FeedingEntry, FeedingSchedule
│   ├── feeding_entry.py              # FeedingEntry (@dataclass)
│   └── feeding_schedule.py           # FeedingSchedule
│
├── enclosure.py                      # Enclosure  (single class — flat file kept)
└── zoo.py                            # Zoo        (single class — flat file kept)
```

### Why `enclosure.py` and `zoo.py` stay flat

The "one class per file" rule is satisfied trivially by a file containing one class. Wrapping a single‑class module inside a folder named after the same class adds ceremony with zero structural payoff. We keep the flat form and apply the sub‑package treatment only where there are ≥ 2 classes that benefit from being navigable by path.

## Internal import order

```
exceptions/  ──►  animals/  ──►  enclosure.py  ──►  feeding/  ──►  employees/  ──►  zoo.py
```

This preserves the acyclic chain documented in `JUSTIFICATION.md` J10:

- `exceptions/*` depends on nothing in the package.
- `animals/animal.py` imports `InvalidAnimalDataError` from `..exceptions`.
- `animals/mammal.py`, `bird.py`, `reptile.py` import `Animal` from `.animal`.
- `animals/lion.py`, `elephant.py`, `monkey.py` import `Mammal` from `.mammal`. Same pattern for birds/reptiles.
- `enclosure.py` imports `Animal` from `.animals` and exceptions from `.exceptions`.
- `feeding/feeding_entry.py` is standalone (`@dataclass`); `feeding/feeding_schedule.py` imports `FeedingEntry` from `.feeding_entry`.
- `employees/zookeeper.py` imports `Enclosure` from `..enclosure`.
- `zoo.py` imports from every other sub‑package.

No cycles are introduced. The sub‑package `__init__.py` files do flat re‑exports of their own classes only — they never import upward into `zoo`.

## Public API contract (invariant)

The top-level `src/zoo/__init__.py` continues to expose **exactly** the same names as today:

```python
from zoo import (
    ZooError, EnclosureFullError, AnimalNotFoundError, InvalidAnimalDataError,
    Animal, Mammal, Bird, Reptile,
    Lion, Elephant, Monkey, Eagle, Penguin, Crocodile,
    Enclosure,
    FeedingEntry, FeedingSchedule,
    Employee, Zookeeper, Veterinarian, Guide,
    Zoo,
)
```

Every external consumer (`demo.py`, `tests/conftest.py`, `tests/test_*.py`, README examples) continues to use top-level imports. They are not edited as part of the move.

## Sub-package imports as a side benefit

After the refactor, developers can also write:

```python
from zoo.animals import Lion
from zoo.exceptions import EnclosureFullError
from zoo.employees.zookeeper import Zookeeper
```

These are additional valid paths, not required ones. README documents the top-level form as canonical.

## Test layout

```
tests/
├── conftest.py            # shared fixtures — UNCHANGED
├── test_animals.py        # 8 tests
├── test_enclosure.py      # 4 tests
├── test_feeding.py        # 1 test
└── test_zoo.py            # 2 tests
```

### Test redistribution map (15 → 15)

| # | Current name in `test_zoo.py`        | New file              | Spec area              |
|---|--------------------------------------|-----------------------|------------------------|
| 1 | `test_create_animals_different_types`| `test_animals.py`     | animal-hierarchy       |
| 2 | `test_base_stats_and_properties`     | `test_animals.py`     | animal-hierarchy       |
| 3 | `test_add_animals_to_enclosure`      | `test_enclosure.py`   | enclosure-management   |
| 4 | `test_enclosure_full_error`          | `test_enclosure.py`   | enclosure-management   |
| 5 | `test_remove_animal_not_found`       | `test_enclosure.py`   | enclosure-management   |
| 6 | `test_feed_and_feed_all`             | `test_enclosure.py`   | animal-hierarchy + enc |
| 7 | `test_health_clamping`               | `test_animals.py`     | animal-hierarchy       |
| 8 | `test_eq_by_id`                      | `test_animals.py`     | animal-hierarchy       |
| 9 | `test_sorted_by_name`                | `test_animals.py`     | animal-hierarchy       |
| 10| `test_invalid_empty_name`            | `test_animals.py`     | animal-hierarchy       |
| 11| `test_str_and_repr`                  | `test_animals.py`     | animal-hierarchy       |
| 12| `test_polymorphism_make_sound_diet`  | `test_animals.py`     | animal-hierarchy       |
| 13| `test_isinstance_issubclass`         | `test_zoo.py`         | zoo-core               |
| 14| `test_feeding_schedule_add_remove`   | `test_feeding.py`     | feeding-schedule       |
| 15| `test_zoo_report`                    | `test_zoo.py`         | zoo-core               |

Function names are preserved verbatim — the audit "exactly 15 test functions" is still trivially verifiable via `grep -rE '^def test_' tests/ | wc -l`.

## Documents that need editing

Discovered by `grep -rln "animals\.py\|employees\.py\|enclosure\.py\|feeding\.py\|zoo\.py\|exceptions\.py\|src/zoo/"`:

- `README.md` — *Struktura projektu* tree (lines ~278-303) and *Mechanizmy OOP* table "Lokalizacja" column (lines ~248-272).
- `CHECKLIST.md` — every "Lokalizacja:" bullet that names a `.py` file (~30 occurrences).
- `JUSTIFICATION.md` — sections **J9** (test file rationale — now split per capability) and **J10** (module layout — new sub‑package structure and import order).
- `Projekt_A_Zoo_Garden.md` — code-block headings (`# animals.py`, `# employees.py`, …) and the file-tree at line ~445.
- `openspec/specs/animal-hierarchy/spec.md` — `src/zoo/animals.py` → `src/zoo/animals/<class>.py`.
- `openspec/specs/employee-system/spec.md` — `src/zoo/employees.py` → `src/zoo/employees/<class>.py`.
- `openspec/specs/enclosure-management/spec.md` — no path change; verify cross-refs only.
- `openspec/specs/feeding-schedule/spec.md` — `src/zoo/feeding.py` → `src/zoo/feeding/<class>.py`.
- `openspec/specs/test-suite/spec.md` — single-file requirement replaced with multi-file distribution.
- `openspec/specs/zoo-core/spec.md` — no path change; verify cross-refs only.
- `openspec/specs/demo-script/spec.md` — verify no module path references.

The archived change at `openspec/changes/archive/2026-03-30-zoo-garden-oop-system/` is **not** edited — archives are historical records of what was true at archive time.

## Acceptance signal

1. `pytest tests/` reports **15 passed** with exit code 0.
2. `python demo.py` runs end-to-end without changes to the file.
3. `python -c "from zoo import Lion, Zoo, Zookeeper, EnclosureFullError; print('ok')"` succeeds.
4. `grep -rE '^def test_' tests/ | wc -l` returns `15`.
5. No `.py` file under `src/zoo/` defines more than one top-level `class` (excluding nested classes, of which there are none today).
