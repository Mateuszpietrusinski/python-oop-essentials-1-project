## 1. Source layout — exceptions sub-package

- [x] 1.1 Create `src/zoo/exceptions/` directory
- [x] 1.2 Create `src/zoo/exceptions/zoo_error.py` with `ZooError(Exception)` (moved verbatim from `exceptions.py`)
- [x] 1.3 Create `src/zoo/exceptions/enclosure_full_error.py` with `EnclosureFullError(ZooError)`; import `ZooError` via `from .zoo_error import ZooError`
- [x] 1.4 Create `src/zoo/exceptions/animal_not_found_error.py` with `AnimalNotFoundError(ZooError)`
- [x] 1.5 Create `src/zoo/exceptions/invalid_animal_data_error.py` with `InvalidAnimalDataError(ZooError)`
- [x] 1.6 Create `src/zoo/exceptions/__init__.py` re-exporting all four exception names
- [x] 1.7 Delete `src/zoo/exceptions.py`

## 2. Source layout — animals sub-package

- [x] 2.1 Create `src/zoo/animals/` directory
- [x] 2.2 Create `animals/animal.py` with the `Animal(ABC)` class; update its `from .exceptions import InvalidAnimalDataError` → `from ..exceptions import InvalidAnimalDataError`
- [x] 2.3 Create `animals/mammal.py` with `Mammal(Animal)`; import via `from .animal import Animal`
- [x] 2.4 Create `animals/bird.py` with `Bird(Animal)`
- [x] 2.5 Create `animals/reptile.py` with `Reptile(Animal)`
- [x] 2.6 Create `animals/lion.py` with `Lion(Mammal)`; import via `from .mammal import Mammal`
- [x] 2.7 Create `animals/elephant.py` with `Elephant(Mammal)`
- [x] 2.8 Create `animals/monkey.py` with `Monkey(Mammal)`
- [x] 2.9 Create `animals/eagle.py` with `Eagle(Bird)`
- [x] 2.10 Create `animals/penguin.py` with `Penguin(Bird)`
- [x] 2.11 Create `animals/crocodile.py` with `Crocodile(Reptile)`
- [x] 2.12 Create `animals/__init__.py` re-exporting all 10 names (`Animal`, `Mammal`, `Bird`, `Reptile`, `Lion`, `Elephant`, `Monkey`, `Eagle`, `Penguin`, `Crocodile`)
- [x] 2.13 Delete `src/zoo/animals.py`

## 3. Source layout — feeding sub-package

- [x] 3.1 Create `src/zoo/feeding/` directory
- [x] 3.2 Create `feeding/feeding_entry.py` with `FeedingEntry` (`@dataclass`)
- [x] 3.3 Create `feeding/feeding_schedule.py` with `FeedingSchedule`; import via `from .feeding_entry import FeedingEntry`
- [x] 3.4 Create `feeding/__init__.py` re-exporting `FeedingEntry`, `FeedingSchedule`
- [x] 3.5 Delete `src/zoo/feeding.py`

## 4. Source layout — employees sub-package

- [x] 4.1 Create `src/zoo/employees/` directory
- [x] 4.2 Create `employees/employee.py` with `Employee(ABC)`
- [x] 4.3 Create `employees/zookeeper.py` with `Zookeeper(Employee)`; update `Enclosure` import to `from ..enclosure import Enclosure`
- [x] 4.4 Create `employees/veterinarian.py` with `Veterinarian(Employee)`
- [x] 4.5 Create `employees/guide.py` with `Guide(Employee)`
- [x] 4.6 Create `employees/__init__.py` re-exporting `Employee`, `Zookeeper`, `Veterinarian`, `Guide`
- [x] 4.7 Delete `src/zoo/employees.py`

## 5. Source layout — enclosure & zoo (flat files retained)

- [x] 5.1 Update `src/zoo/enclosure.py` imports: `from .exceptions import …`, `from .animals import Animal` (now resolved via sub-package barrels)
- [x] 5.2 Update `src/zoo/zoo.py` imports: `from .animals import Animal`, `from .employees import Employee, Zookeeper`, `from .enclosure import Enclosure`, `from .exceptions import …`

## 6. Top-level package barrel

- [x] 6.1 Update `src/zoo/__init__.py` to import from sub-packages instead of flat modules: `from .exceptions import …`, `from .animals import …`, `from .feeding import …`, `from .employees import …`. The `__all__` list and exported names stay byte-identical to today.
- [x] 6.2 Verify `python -c "from zoo import Lion, Zoo, Zookeeper, FeedingSchedule, EnclosureFullError; print('ok')"` prints `ok`

## 7. Test split

- [x] 7.1 Create `tests/test_animals.py` with the 8 animal tests (numbers 1, 2, 7, 8, 9, 10, 11, 12 from current `test_zoo.py`); preserve original function names verbatim
- [x] 7.2 Create `tests/test_enclosure.py` with the 4 enclosure tests (3, 4, 5, 6); preserve names
- [x] 7.3 Create `tests/test_feeding.py` with test 14 (`test_feeding_schedule_add_remove`)
- [x] 7.4 Replace `tests/test_zoo.py` with the 2 zoo-core tests (13 `test_isinstance_issubclass`, 15 `test_zoo_report`)
- [x] 7.5 Verify `tests/conftest.py` is unchanged and fixtures still resolve for all four files
- [x] 7.6 Run `pytest tests/ -v` and confirm exactly 15 tests pass

## 8. Documentation updates

- [x] 8.1 Update `README.md` *Struktura projektu* tree to show the new sub-package layout
- [x] 8.2 Update `README.md` *Mechanizmy OOP* table — replace every `animals.py: …` / `employees.py: …` / `feeding.py: …` / `exceptions.py: …` with the per-class path (e.g. `animals/lion.py: Lion`)
- [x] 8.3 Update every "Lokalizacja:" bullet in `CHECKLIST.md` to reference the new per-class file paths
- [x] 8.4 Rewrite `JUSTIFICATION.md` **J9** — explain that tests are split per capability for readability, not in one file. Total still 15 (auditable via grep)
- [x] 8.5 Rewrite `JUSTIFICATION.md` **J10** — describe the new module layout and the updated dependency order
- [x] 8.6 Update `Projekt_A_Zoo_Garden.md` — replace `# animals.py`, `# employees.py`, `# enclosure.py`, `# feeding.py`, `# zoo.py`, `# exceptions.py` headings and the file-tree section to reflect the new layout
- [x] 8.7 Verify no other doc/markdown file references `src/zoo/<module>.py` paths that no longer exist (`grep -rn "src/zoo/animals\.py\|src/zoo/employees\.py\|src/zoo/feeding\.py\|src/zoo/exceptions\.py" --include='*.md' .` should return nothing)

## 9. OpenSpec spec updates (handled via change deltas)

- [x] 9.1 Apply `specs/animal-hierarchy/spec.md` delta (file path: `animals.py` → `animals/<class>.py`)
- [x] 9.2 Apply `specs/employee-system/spec.md` delta (file path: `employees.py` → `employees/<class>.py`)
- [x] 9.3 Apply `specs/feeding-schedule/spec.md` delta (file path: `feeding.py` → `feeding/<class>.py`)
- [x] 9.4 Apply `specs/test-suite/spec.md` delta (15 tests now distributed across 4 files)
- [x] 9.5 Verify `enclosure-management`, `zoo-core`, `demo-script` specs need no path-related updates

## 10. Acceptance verification

- [x] 10.1 `pytest tests/` → 15 passed
- [x] 10.2 `python demo.py` runs to completion without errors and produces equivalent output
- [x] 10.3 `grep -rE '^def test_' tests/ | wc -l` → `15`
- [x] 10.4 `find src/zoo -name '*.py' -exec grep -lE '^class ' {} \; | xargs -I{} sh -c 'echo "=={}=="; grep -cE "^class " "{}"'` shows count `1` for every file (one class per file invariant)
- [x] 10.5 Archive this change: moved to `openspec/changes/archive/2026-05-05-restructure-one-class-per-file/`
