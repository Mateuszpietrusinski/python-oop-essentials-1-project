## ADDED Requirements

### Requirement: Zoo class with composition of enclosures
`Zoo` SHALL be defined in `src/zoo/zoo.py`. Constructor: `name: str`, `city: str = "Lodz"`. Enclosures SHALL be created internally via `create_enclosure(name: str, capacity: int) -> Enclosure` and stored in `self._enclosures: dict[str, Enclosure]`. Enclosures SHALL NOT exist independently of the `Zoo` instance (composition).

#### Scenario: create_enclosure returns and stores enclosure
- **WHEN** `zoo.create_enclosure("Savanna", 5)` is called
- **THEN** the returned `Enclosure` is accessible via `zoo["Savanna"]`

### Requirement: Zoo aggregation of employees
`hire_employee(employee: Employee) -> None` SHALL add an externally-created `Employee` to the zoo's internal list. Employees SHALL be able to exist outside the zoo (aggregation).

#### Scenario: hire_employee stores the employee
- **WHEN** `zoo.hire_employee(zookeeper)` is called
- **THEN** the employee is included in zoo operations (e.g., reflected in report)

### Requirement: Zoo query methods
- `total_animals() -> int`: returns the total count of animals across all enclosures
- `find_animal(name: str) -> Animal | None`: searches all enclosures and returns the first match, or `None`

#### Scenario: total_animals sums all enclosures
- **WHEN** two enclosures each have 3 animals
- **THEN** `zoo.total_animals()` returns `6`

#### Scenario: find_animal returns None for missing animal
- **WHEN** no animal named "Ghost" exists in any enclosure
- **THEN** `zoo.find_animal("Ghost")` returns `None`

### Requirement: Zoo report method
`report() -> str` SHALL return a multi-line string summarizing: zoo name, city, number of enclosures, total animals, and a list of enclosures with their animal counts.

#### Scenario: report contains zoo name
- **WHEN** `zoo.report()` is called
- **THEN** the returned string contains the zoo's name

### Requirement: Zoo dunder methods
`Zoo` SHALL implement: `__getitem__(name: str) -> Enclosure` (returns enclosure by name, raises `KeyError` if missing), `__contains__(item) -> bool` (returns `True` if item is an `Animal` found in any enclosure OR an `Employee` in the employee list), `__len__() -> int` (returns number of enclosures).

#### Scenario: __getitem__ retrieves enclosure by name
- **WHEN** `zoo["Savanna"]` is called after creating that enclosure
- **THEN** the correct `Enclosure` instance is returned

#### Scenario: __contains__ works for both Animal and Employee
- **WHEN** a lion in an enclosure is checked with `lion in zoo`
- **THEN** it returns `True`
