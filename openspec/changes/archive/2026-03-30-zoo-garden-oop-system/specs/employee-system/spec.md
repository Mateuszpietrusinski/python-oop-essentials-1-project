## ADDED Requirements

### Requirement: Abstract Employee base class
The system SHALL define an abstract base class `Employee` (inheriting from `ABC`) in `src/zoo/employees.py`. It SHALL have a class-level `_next_id: int = 1` auto-increment counter. Constructor: `name: str`, `salary: float`. It SHALL declare `work() -> str` and `role() -> str` as `@abstractmethod`. It SHALL implement `__repr__`, `__eq__` (by `_id`), `__hash__` (by `_id`).

#### Scenario: Direct instantiation raises TypeError
- **WHEN** code attempts `Employee("Alice", 5000)` directly
- **THEN** Python raises `TypeError`

### Requirement: Zookeeper employee
`Zookeeper(Employee)` SHALL implement `work()`, `role()`, `assign_to(enclosure) -> None`, and `feed_animals() -> str`. `assign_to` stores a reference to an `Enclosure` instance. `feed_animals` calls `enclosure.feed_all()` if assigned, otherwise returns a message indicating no assignment.

#### Scenario: Zookeeper feeds assigned enclosure
- **WHEN** zookeeper is assigned to an enclosure and `feed_animals()` is called
- **THEN** it returns a string confirming feeding occurred

#### Scenario: Zookeeper with no assignment
- **WHEN** `feed_animals()` is called before any enclosure is assigned
- **THEN** it returns a descriptive message without raising

### Requirement: Veterinarian employee
`Veterinarian(Employee)` SHALL accept `specialization: str = "general"` (values: `"general"` or `"exotic"`). It SHALL implement `work()` and `role()`, including the specialization in the output. Default salary: 7000.0.

#### Scenario: Veterinarian role
- **WHEN** `vet.role()` is called
- **THEN** it returns a string containing "Veterinarian" and the specialization

### Requirement: Guide employee
`Guide(Employee)` SHALL accept `languages: list[str] | None = None` (defaults to `["English"]`). It SHALL implement `work()` and `role()`. Default salary: 3500.0.

#### Scenario: Guide role with multiple languages
- **WHEN** `guide = Guide("Bob", languages=["English", "Polish"])` and `guide.role()` is called
- **THEN** it returns a string mentioning both languages
