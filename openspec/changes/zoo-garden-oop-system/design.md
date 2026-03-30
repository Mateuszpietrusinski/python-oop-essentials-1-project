## Context

This is a greenfield Python project for a university OOP course. There is no existing codebase to migrate. The project specification (`Projekt_A_Zoo_Garden.md`) prescribes exact class names, method signatures, relationships, and required OOP mechanics. The implementation must satisfy the grading checklist (31 OOP checkpoints) and pass exactly 15 pytest tests.

## Goals / Non-Goals

**Goals:**
- Implement all classes exactly as specified in the project skeleton
- Demonstrate all required OOP mechanics: ABC, inheritance, composition, aggregation, association, polymorphism, duck typing, `@property`, dunder methods, operator overloading, custom exceptions, `@dataclass`
- Produce a clean, PEP 8-compliant, fully documented (Google-style docstrings + type hints) package
- Deliver `demo.py` covering all 7 demonstration scenarios
- Deliver exactly 15 pytest tests using fixtures and `pytest.raises`

**Non-Goals:**
- Persistence (no database or file I/O beyond demo output)
- Web interface or REST API
- Real-time simulation or concurrency
- Extensibility beyond the 6 required species and 3 employee types

## Decisions

### D1: Package layout — `src/` layout with `src/zoo/`
**Chosen:** `src/zoo/` layout as specified by the project requirements.
**Why:** Matches the exact directory structure required by the grading rubric. Avoids accidental import of the local directory instead of the installed package during test runs.

### D2: Module split — one class group per file
**Chosen:** `exceptions.py`, `animals.py`, `employees.py`, `enclosure.py`, `feeding.py`, `zoo.py`.
**Why:** Each file maps cleanly to a logical subsystem. Avoids circular imports: `animals.py` has no dependencies on other zoo modules; `enclosure.py` imports `animals` and `exceptions`; `employees.py` imports `enclosure`; `zoo.py` imports all others.

**Import order to avoid circular deps:**
```
exceptions → animals → enclosure → feeding → employees → zoo
```

### D3: `Animal._next_id` as a class-level counter shared across all subclasses
**Chosen:** Single `_next_id = 1` on `Animal`, incremented in `Animal.__init__`, stored as `self._id`.
**Why:** The spec requires a shared auto-increment ID across all animal instances. Each animal gets a unique integer ID regardless of species. `Employee` gets its own separate `_next_id`.

### D4: `health` property with clamping
**Chosen:** Setter clamps with `max(0, min(100, value))` — no exception raised.
**Why:** Spec explicitly says "clamping", not validation. Out-of-range values are silently clamped.

### D5: `Enclosure` stores animals in a plain `list`; `animals` property returns a copy
**Chosen:** `self._animals: list[Animal] = []`; property returns `list(self._animals)`.
**Why:** Prevents external mutation of the internal list (required by spec Q12). `__iter__` iterates over `self._animals` directly.

### D6: Composition vs aggregation encoding in Python
**Chosen:**
- `Zoo` creates `Enclosure` instances internally (`create_enclosure` factory) — composition. Enclosures are stored in `self._enclosures: dict[str, Enclosure]`.
- `Zoo` accepts external `Employee` objects (`hire_employee`) — aggregation.
- `Enclosure` accepts external `Animal` objects (`add_animal`) — aggregation.
- `Zookeeper` holds a reference to an `Enclosure` (`assign_to`) — association.

**Why:** Python has no built-in composition vs aggregation distinction; the difference is expressed through ownership semantics. Factory methods signal composition; `accept external object` methods signal aggregation.

### D7: `FeedingEntry` as `@dataclass`
**Chosen:** Standard `@dataclass` with fields: `enclosure_name: str`, `time: str`, `food_type: str`, `notes: str = ""`.
**Why:** Spec mandates `@dataclass`. Dataclass auto-generates `__init__`, `__repr__`, `__eq__`.

### D8: `__eq__` and `__hash__` strategy
- `Animal`: `__eq__` compares `_id`; `__hash__` returns `hash(self._id)`.
- `Employee`: same pattern with employee `_id`.
- `Enclosure`: `__eq__` compares `name`; `__hash__` returns `hash(self.name)`.
- `__lt__` on `Animal` compares by `name` (for `sorted()` support).

### D9: Test structure — single test file with `conftest.py`
**Chosen:** `tests/conftest.py` for fixtures, `tests/test_zoo.py` for all 15 tests.
**Why:** Keeps test count exact and easy to audit. Fixtures shared via `conftest.py` as required.

## Risks / Trade-offs

- [Risk] `_next_id` shared across all `Animal` subclasses means IDs are globally unique but not predictable per-species → Mitigation: tests should not assert specific ID values, only uniqueness.
- [Risk] `Zoo.__contains__` must handle both `Animal` and `Employee` — type checking needed → Mitigation: use `isinstance` checks inside `__contains__`.
- [Risk] `Penguin` extends `Bird` but cannot fly (`can_fly=False`) — `fly()` method must handle this gracefully → Mitigation: return a descriptive string rather than raising an exception.

## Open Questions

None — all design decisions are derivable from the specification.
