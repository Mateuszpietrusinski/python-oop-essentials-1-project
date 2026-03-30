"""15 test scenarios for the Zoo Garden system.

Tests cover:
 1. Creating animals of different types
 2. Base stats and properties
 3. Adding animals to enclosure
 4. Capacity validation (EnclosureFullError)
 5. AnimalNotFoundError on removal
 6. feed() and feed_all()
 7. Health clamping
 8. __eq__ by ID
 9. __lt__ / sorted()
10. InvalidAnimalDataError on empty name
11. __str__ and __repr__
12. Polymorphism — make_sound() / diet()
13. isinstance / issubclass hierarchy
14. FeedingSchedule add/remove
15. zoo.report() content
"""

import pytest

from zoo import (
    Lion,
    Eagle,
    Crocodile,
    Mammal,
    Bird,
    Reptile,
    Animal,
    Enclosure,
    Zoo,
    FeedingSchedule,
    EnclosureFullError,
    AnimalNotFoundError,
    InvalidAnimalDataError,
    Penguin,
    Elephant,
    Monkey,
)


# ---------------------------------------------------------------------------
# Test 1 — Creating animals of different types
# ---------------------------------------------------------------------------

def test_create_animals_different_types(lion, eagle, crocodile):
    """Animals of different types can be created successfully."""
    assert isinstance(lion, Lion)
    assert isinstance(eagle, Eagle)
    assert isinstance(crocodile, Crocodile)
    assert lion.name == "Simba"
    assert eagle.name == "Sam"
    assert crocodile.name == "Rex"


# ---------------------------------------------------------------------------
# Test 2 — Base stats and properties
# ---------------------------------------------------------------------------

def test_base_stats_and_properties(lion):
    """Animal exposes id, name, health, age, species correctly."""
    assert lion.name == "Simba"
    assert lion.age == 5
    assert lion.health == 100
    assert lion.species == "Panthera leo"
    assert isinstance(lion.id, int)
    assert lion.id >= 1


# ---------------------------------------------------------------------------
# Test 3 — Adding animals to enclosure
# ---------------------------------------------------------------------------

def test_add_animals_to_enclosure():
    """Adding animals to an enclosure increases its length."""
    enc = Enclosure("Test", 5)
    a1 = Lion("Leo", 3)
    a2 = Eagle("Sky", 2)
    assert len(enc) == 0
    enc.add_animal(a1)
    assert len(enc) == 1
    enc.add_animal(a2)
    assert len(enc) == 2


# ---------------------------------------------------------------------------
# Test 4 — Capacity validation (EnclosureFullError)
# ---------------------------------------------------------------------------

def test_enclosure_full_error():
    """Adding an animal to a full enclosure raises EnclosureFullError."""
    enc = Enclosure("Small", 2)
    enc.add_animal(Lion("A", 1))
    enc.add_animal(Lion("B", 2))
    with pytest.raises(EnclosureFullError):
        enc.add_animal(Lion("C", 3))
    assert len(enc) == 2


# ---------------------------------------------------------------------------
# Test 5 — AnimalNotFoundError on removing absent animal
# ---------------------------------------------------------------------------

def test_remove_animal_not_found(enclosure):
    """Removing an animal not in the enclosure raises AnimalNotFoundError."""
    outsider = Lion("Stranger", 1)
    with pytest.raises(AnimalNotFoundError):
        enclosure.remove_animal(outsider)


# ---------------------------------------------------------------------------
# Test 6 — feed() and feed_all()
# ---------------------------------------------------------------------------

def test_feed_and_feed_all(lion, enclosure):
    """feed() returns a string with the animal name; feed_all() returns one entry per animal."""
    result = lion.feed()
    assert "Simba" in result

    all_results = enclosure.feed_all()
    assert len(all_results) == len(enclosure)
    for r in all_results:
        assert isinstance(r, str)
        assert len(r) > 0


# ---------------------------------------------------------------------------
# Test 7 — Health clamping
# ---------------------------------------------------------------------------

def test_health_clamping(lion):
    """Health is clamped to [0, 100] silently."""
    lion.health = 150
    assert lion.health == 100

    lion.health = -20
    assert lion.health == 0

    lion.health = 75
    assert lion.health == 75


# ---------------------------------------------------------------------------
# Test 8 — __eq__ compares by ID
# ---------------------------------------------------------------------------

def test_eq_by_id():
    """Two animals with the same name but different IDs are not equal."""
    a = Lion("Simba", 5)
    b = Lion("Simba", 5)
    assert a != b
    assert a == a


# ---------------------------------------------------------------------------
# Test 9 — sorted() uses __lt__ by name
# ---------------------------------------------------------------------------

def test_sorted_by_name():
    """sorted() orders animals lexicographically by name."""
    c_lion = Lion("Charlie", 3)
    a_eagle = Eagle("Alpha", 2)
    b_penguin = Penguin("Beta", 1)
    result = sorted([c_lion, a_eagle, b_penguin])
    assert result[0].name == "Alpha"
    assert result[1].name == "Beta"
    assert result[2].name == "Charlie"


# ---------------------------------------------------------------------------
# Test 10 — InvalidAnimalDataError on empty name
# ---------------------------------------------------------------------------

def test_invalid_empty_name():
    """Setting an empty or whitespace name raises InvalidAnimalDataError."""
    lion = Lion("Valid", 1)
    with pytest.raises(InvalidAnimalDataError):
        lion.name = ""
    with pytest.raises(InvalidAnimalDataError):
        lion.name = "   "


# ---------------------------------------------------------------------------
# Test 11 — __str__ and __repr__
# ---------------------------------------------------------------------------

def test_str_and_repr(lion):
    """__str__ and __repr__ are non-empty and differ from each other."""
    s = str(lion)
    r = repr(lion)
    assert len(s) > 0
    assert len(r) > 0
    assert s != r


# ---------------------------------------------------------------------------
# Test 12 — Polymorphism: make_sound() and diet()
# ---------------------------------------------------------------------------

def test_polymorphism_make_sound_diet(lion, eagle, crocodile):
    """make_sound() and diet() work polymorphically on a mixed list."""
    animals = [lion, eagle, crocodile]
    sounds = [a.make_sound() for a in animals]
    diets = [a.diet() for a in animals]

    # All results must be non-empty strings
    for s in sounds:
        assert isinstance(s, str) and len(s) > 0
    for d in diets:
        assert isinstance(d, str) and len(d) > 0

    # Sounds must be distinct
    assert len(set(sounds)) == 3


# ---------------------------------------------------------------------------
# Test 13 — isinstance / issubclass hierarchy
# ---------------------------------------------------------------------------

def test_isinstance_issubclass(lion, eagle, crocodile):
    """isinstance and issubclass correctly reflect the class hierarchy."""
    # isinstance checks
    assert isinstance(lion, Mammal)
    assert isinstance(lion, Animal)
    assert isinstance(eagle, Bird)
    assert isinstance(eagle, Animal)
    assert isinstance(crocodile, Reptile)
    assert isinstance(crocodile, Animal)

    # issubclass checks
    assert issubclass(Lion, Mammal)
    assert issubclass(Mammal, Animal)
    assert issubclass(Eagle, Bird)
    assert issubclass(Bird, Animal)
    assert issubclass(Crocodile, Reptile)
    assert issubclass(Reptile, Animal)


# ---------------------------------------------------------------------------
# Test 14 — FeedingSchedule add/remove entries
# ---------------------------------------------------------------------------

def test_feeding_schedule_add_remove():
    """FeedingSchedule add_entry and remove_entry work correctly."""
    schedule = FeedingSchedule("Tuesday")
    assert len(schedule) == 0

    entry = schedule.add_entry("Savanna", "08:00", "meat", notes="fresh")
    assert len(schedule) == 1

    by_enc = schedule.get_by_enclosure("Savanna")
    assert len(by_enc) == 1
    assert by_enc[0].food_type == "meat"

    schedule.remove_entry(entry)
    assert len(schedule) == 0


# ---------------------------------------------------------------------------
# Test 15 — zoo.report() contains expected content
# ---------------------------------------------------------------------------

def test_zoo_report(zoo):
    """zoo.report() returns a string containing the zoo's name."""
    report = zoo.report()
    assert isinstance(report, str)
    assert "Test Zoo" in report
    assert "Savanna" in report
