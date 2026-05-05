## MODIFIED Requirements

### Requirement: Abstract Employee base class
The system SHALL define an abstract base class `Employee` (inheriting from `ABC`) in `src/zoo/employees/employee.py`. It SHALL have a class-level `_next_id: int = 1` auto-increment counter. Constructor: `name: str`, `salary: float`. It SHALL declare `work() -> str` and `role() -> str` as `@abstractmethod`. It SHALL implement `__repr__`, `__eq__` (by `_id`), `__hash__` (by `_id`).

#### Scenario: One class per file
- **WHEN** the file `src/zoo/employees/employee.py` is inspected
- **THEN** it contains exactly one top-level `class` definition (`Employee`)

### Requirement: Concrete employee roles
The system SHALL define three concrete employee roles, each in its own module under `src/zoo/employees/`:

| Class          | Module                                    | Notes                                                      |
|----------------|-------------------------------------------|------------------------------------------------------------|
| `Zookeeper`    | `src/zoo/employees/zookeeper.py`          | May be assigned to an `Enclosure` via `assign_to()`        |
| `Veterinarian` | `src/zoo/employees/veterinarian.py`       | Has a `specialization` attribute                           |
| `Guide`        | `src/zoo/employees/guide.py`              | Has a `languages: list[str]` attribute                     |

Each module SHALL contain exactly one top-level class. Each SHALL implement `work()` and `role()`.

#### Scenario: Zookeeper still imports Enclosure
- **WHEN** `src/zoo/employees/zookeeper.py` resolves its `Enclosure` reference
- **THEN** it uses `from ..enclosure import Enclosure` and the module loads without circular-import errors

#### Scenario: Top-level imports are unchanged
- **WHEN** consumer code runs `from zoo import Zookeeper, Veterinarian, Guide`
- **THEN** all three imports succeed and resolve to the classes defined under `src/zoo/employees/`

### Requirement: employees package barrel
`src/zoo/employees/__init__.py` SHALL re-export `Employee`, `Zookeeper`, `Veterinarian`, `Guide` so that both top-level (`from zoo import Zookeeper`) and sub-package (`from zoo.employees import Zookeeper`) imports resolve to the same class.
