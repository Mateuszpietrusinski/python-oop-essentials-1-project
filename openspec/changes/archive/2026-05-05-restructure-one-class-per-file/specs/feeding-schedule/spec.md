## MODIFIED Requirements

### Requirement: FeedingEntry dataclass
The system SHALL define `FeedingEntry` in `src/zoo/feeding/feeding_entry.py` using `@dataclass`. Fields: `enclosure_name: str`, `time: str`, `food_type: str`, `notes: str = ""`. The dataclass SHALL auto-generate `__init__`, `__repr__`, and `__eq__`. The module SHALL contain exactly one top-level class.

#### Scenario: Sub-package import resolves
- **WHEN** code runs `from zoo.feeding import FeedingEntry` or `from zoo import FeedingEntry`
- **THEN** both resolve to the class defined in `src/zoo/feeding/feeding_entry.py`

### Requirement: FeedingSchedule composition
`FeedingSchedule` SHALL be defined in `src/zoo/feeding/feeding_schedule.py`. Constructor: `day: str = "Monday"`. It SHALL own its `FeedingEntry` instances (composition — entries do not exist outside the schedule). It SHALL provide: `add_entry(enclosure_name, time, food_type, notes="") -> FeedingEntry`, `remove_entry(entry: FeedingEntry) -> None`, `get_by_enclosure(name: str) -> list[FeedingEntry]`, `__len__ -> int`. The module SHALL contain exactly one top-level class and SHALL import `FeedingEntry` via `from .feeding_entry import FeedingEntry`.

#### Scenario: One class per file
- **WHEN** `src/zoo/feeding/feeding_schedule.py` is inspected
- **THEN** it contains exactly one top-level `class` definition (`FeedingSchedule`)

### Requirement: feeding package barrel
`src/zoo/feeding/__init__.py` SHALL re-export `FeedingEntry` and `FeedingSchedule`.
