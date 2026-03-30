## ADDED Requirements

### Requirement: demo.py covers all 7 required scenarios
The system SHALL include `demo.py` at the project root. It SHALL demonstrate all 7 scenarios required by the specification, printing output to stdout.

#### Scenario: demo.py runs without errors
- **WHEN** `python demo.py` is executed
- **THEN** it exits with code 0 and prints readable output

### Requirement: Scenario 1 — Create zoo with enclosures
`demo.py` SHALL create a `Zoo` instance and at least 2 enclosures using `create_enclosure`.

#### Scenario: Zoo and enclosures created
- **WHEN** demo runs
- **THEN** zoo name and enclosure names are printed

### Requirement: Scenario 2 — Add animals to enclosures
`demo.py` SHALL add at least one animal of each type (Mammal, Bird, Reptile) to enclosures.

#### Scenario: Animals added
- **WHEN** demo runs
- **THEN** animal additions are confirmed in output

### Requirement: Scenario 3 — EnclosureFullError demonstration
`demo.py` SHALL attempt to add an animal to a full enclosure inside a `try/except` block and print the caught `EnclosureFullError`.

#### Scenario: Exception caught and printed
- **WHEN** demo runs
- **THEN** output includes a message about the enclosure being full

### Requirement: Scenario 4 — feed_all
`demo.py` SHALL call `feed_all()` on an enclosure and print the results.

#### Scenario: Feeding output shown
- **WHEN** demo runs
- **THEN** output lists each animal fed

### Requirement: Scenario 5 — Assign zookeeper to enclosure
`demo.py` SHALL create a `Zookeeper`, call `assign_to`, and call `feed_animals()`, printing the result.

#### Scenario: Zookeeper assignment demonstrated
- **WHEN** demo runs
- **THEN** output shows zookeeper feeding through enclosure

### Requirement: Scenario 6 — Zoo report
`demo.py` SHALL call `zoo.report()` and print the result.

#### Scenario: Report printed
- **WHEN** demo runs
- **THEN** output includes zoo name, enclosure count, and animal count

### Requirement: Scenario 7 — Polymorphic method calls
`demo.py` SHALL iterate over a list of at least 3 different animal types and call `make_sound()` and `diet()` on each, printing results.

#### Scenario: Polymorphic output shown
- **WHEN** demo runs
- **THEN** each animal's sound and diet are printed with the animal's name
