"""Tests for Enclosure class in the Zoo Garden system."""

import pytest

from zoo import (
    Lion,
    Eagle,
    Enclosure,
    EnclosureFullError,
    AnimalNotFoundError,
)


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
