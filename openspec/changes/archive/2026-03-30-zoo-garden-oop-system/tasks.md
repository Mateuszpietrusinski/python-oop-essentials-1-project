## 1. Project Structure & Setup

- [x] 1.1 Create directory structure: `src/zoo/`, `tests/`, and root files (`demo.py`, `requirements.txt`, `.gitignore`)
- [x] 1.2 Create `src/__init__.py` and `src/zoo/__init__.py`
- [x] 1.3 Create `requirements.txt` with `pytest>=7.0.0` and `pytest-cov>=4.0.0`

## 2. Exceptions Module

- [x] 2.1 Implement `src/zoo/exceptions.py` with `ZooError(Exception)`, `EnclosureFullError(ZooError)`, `AnimalNotFoundError(ZooError)`, `InvalidAnimalDataError(ZooError)` — all with docstrings

## 3. Animal Hierarchy

- [x] 3.1 Implement `Animal(ABC)` base class in `src/zoo/animals.py` with `_next_id`, `__init__`, `id`/`name`/`health`/`age` properties (health clamping, name validation), `feed()`, abstract `make_sound()`/`diet()`, `__repr__`, `__str__`, `__eq__`, `__hash__`, `__lt__`
- [x] 3.2 Implement `Mammal(Animal)` with `fur_color` parameter, `diet()`, `give_birth()`
- [x] 3.3 Implement `Bird(Animal)` with `wingspan`, `can_fly` parameters, `diet()`, `fly()` (handles `can_fly=False`)
- [x] 3.4 Implement `Reptile(Animal)` with `is_venomous` parameter, `diet()`, `bask()`
- [x] 3.5 Implement `Lion(Mammal)` with `mane=True`, `make_sound()`, `diet()` override
- [x] 3.6 Implement `Elephant(Mammal)` with `tusk_length=0.0`, `make_sound()`, `diet()` override
- [x] 3.7 Implement `Monkey(Mammal)` with `make_sound()`
- [x] 3.8 Implement `Eagle(Bird)` with `make_sound()`
- [x] 3.9 Implement `Penguin(Bird)` with `can_fly=False`, `make_sound()`
- [x] 3.10 Implement `Crocodile(Reptile)` with `length=3.0`, `make_sound()`

## 4. Enclosure Module

- [x] 4.1 Implement `Enclosure` in `src/zoo/enclosure.py` with `__init__(name, capacity)`, `_animals` list, `animals` property (returns copy)
- [x] 4.2 Implement `add_animal()` with `EnclosureFullError` enforcement
- [x] 4.3 Implement `remove_animal()` with `AnimalNotFoundError`
- [x] 4.4 Implement `find_animal(name)` returning animal or `None`
- [x] 4.5 Implement `feed_all()` calling `feed()` on each animal
- [x] 4.6 Implement dunder methods: `__len__`, `__contains__`, `__iter__`, `__repr__`, `__eq__`, `__hash__`

## 5. Employee Module

- [x] 5.1 Implement `Employee(ABC)` in `src/zoo/employees.py` with `_next_id`, `__init__(name, salary)`, abstract `work()`/`role()`, `__repr__`, `__eq__`, `__hash__`
- [x] 5.2 Implement `Zookeeper(Employee)` with `_assigned_enclosure`, `assign_to()`, `feed_animals()`, `work()`, `role()`
- [x] 5.3 Implement `Veterinarian(Employee)` with `specialization` parameter, `work()`, `role()`
- [x] 5.4 Implement `Guide(Employee)` with `languages` parameter (default `["English"]`), `work()`, `role()`

## 6. Feeding Module

- [x] 6.1 Implement `FeedingEntry` as `@dataclass` in `src/zoo/feeding.py` with fields: `enclosure_name`, `time`, `food_type`, `notes=""`
- [x] 6.2 Implement `FeedingSchedule` with `day` parameter, `add_entry()`, `remove_entry()`, `get_by_enclosure()`, `__len__()`

## 7. Zoo Module

- [x] 7.1 Implement `Zoo` in `src/zoo/zoo.py` with `__init__(name, city="Lodz")`, `_enclosures: dict`, `_employees: list`
- [x] 7.2 Implement `create_enclosure(name, capacity)` factory method
- [x] 7.3 Implement `hire_employee(employee)`, `total_animals()`, `find_animal(name)`, `report()`
- [x] 7.4 Implement dunder methods: `__getitem__`, `__contains__` (handles Animal and Employee), `__len__`

## 8. Package Init & Exports

- [x] 8.1 Update `src/zoo/__init__.py` to export all public classes: animals, employees, enclosure, feeding, zoo, exceptions

## 9. Tests

- [x] 9.1 Create `tests/conftest.py` with `zoo` and `enclosure` fixtures (plus individual animal fixtures)
- [x] 9.2 Write test 1: creating animals of different types (Lion, Eagle, Crocodile)
- [x] 9.3 Write test 2: base stats and properties (id, name, health, age, species)
- [x] 9.4 Write test 3: adding animals to an enclosure (`len` increases)
- [x] 9.5 Write test 4: capacity validation — `pytest.raises(EnclosureFullError)`
- [x] 9.6 Write test 5: `AnimalNotFoundError` on removing absent animal
- [x] 9.7 Write test 6: `feed()` and `feed_all()` return correct strings
- [x] 9.8 Write test 7: health clamping above 100 and below 0
- [x] 9.9 Write test 8: `__eq__` — same name, different IDs returns `False`
- [x] 9.10 Write test 9: `sorted()` uses `__lt__` by name
- [x] 9.11 Write test 10: `InvalidAnimalDataError` on empty name
- [x] 9.12 Write test 11: `__str__` and `__repr__` are non-empty and differ
- [x] 9.13 Write test 12: polymorphism — `make_sound()` and `diet()` on mixed list
- [x] 9.14 Write test 13: `isinstance()` and `issubclass()` for animal hierarchy
- [x] 9.15 Write test 14: `FeedingSchedule` add/remove entries
- [x] 9.16 Write test 15: `zoo.report()` contains zoo name

## 10. Demo Script

- [x] 10.1 Implement `demo.py` scenario 1: create zoo and enclosures
- [x] 10.2 Implement `demo.py` scenario 2: add animals (Mammal, Bird, Reptile)
- [x] 10.3 Implement `demo.py` scenario 3: catch `EnclosureFullError`
- [x] 10.4 Implement `demo.py` scenario 4: `feed_all()` demonstration
- [x] 10.5 Implement `demo.py` scenario 5: zookeeper assign and feed
- [x] 10.6 Implement `demo.py` scenario 6: print `zoo.report()`
- [x] 10.7 Implement `demo.py` scenario 7: polymorphic `make_sound()` and `diet()` loop

## 11. Documentation

- [x] 11.1 Write `README.md` with project description, class hierarchy, OOP mechanics list, 3 User Stories, setup instructions
- [x] 11.2 Write `CHECKLIST.md` with all 31 OOP checkpoints marked and code locations
- [x] 11.3 Write `JUSTIFICATION.md` with design decision rationale
- [x] 11.4 Verify all public classes and methods have Google-style docstrings and type hints
