"""Tests for Zoo class and class hierarchy in the Zoo Garden system."""

from zoo import (
    Animal,
    Mammal,
    Bird,
    Reptile,
    Lion,
    Eagle,
    Crocodile,
    Zoo,
)


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
# Test 15 — zoo.report() contains expected content
# ---------------------------------------------------------------------------

def test_zoo_report(zoo):
    """zoo.report() returns a string containing the zoo's name."""
    report = zoo.report()
    assert isinstance(report, str)
    assert "Test Zoo" in report
    assert "Savanna" in report
