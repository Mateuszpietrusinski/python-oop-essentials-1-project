"""Tests for animal classes in the Zoo Garden system."""

import pytest

from zoo import (
    Animal,
    Mammal,
    Bird,
    Reptile,
    Lion,
    Elephant,
    Monkey,
    Eagle,
    Penguin,
    Crocodile,
    InvalidAnimalDataError,
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
