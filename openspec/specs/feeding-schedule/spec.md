## ADDED Requirements

### Requirement: FeedingEntry dataclass
The system SHALL define `FeedingEntry` in `src/zoo/feeding.py` using `@dataclass`. Fields: `enclosure_name: str`, `time: str`, `food_type: str`, `notes: str = ""`. The dataclass SHALL auto-generate `__init__`, `__repr__`, and `__eq__`.

#### Scenario: FeedingEntry equality
- **WHEN** two `FeedingEntry` instances with identical fields are compared
- **THEN** `entry1 == entry2` returns `True`

### Requirement: FeedingSchedule composition class
`FeedingSchedule` SHALL be defined in `src/zoo/feeding.py`. Constructor: `day: str = "Monday"`. It SHALL own its `FeedingEntry` instances (composition — entries do not exist outside the schedule). It SHALL provide: `add_entry(enclosure_name, time, food_type, notes="") -> FeedingEntry`, `remove_entry(entry: FeedingEntry) -> None`, `get_by_enclosure(name: str) -> list[FeedingEntry]`, `__len__ -> int`.

#### Scenario: add_entry creates and stores an entry
- **WHEN** `schedule.add_entry("Savanna", "08:00", "meat")` is called
- **THEN** `len(schedule)` increases by 1 and the entry is returned

#### Scenario: get_by_enclosure filters correctly
- **WHEN** entries for two different enclosures exist and `get_by_enclosure("Savanna")` is called
- **THEN** only entries for "Savanna" are returned

#### Scenario: remove_entry removes the entry
- **WHEN** a known entry is passed to `remove_entry`
- **THEN** `len(schedule)` decreases by 1
