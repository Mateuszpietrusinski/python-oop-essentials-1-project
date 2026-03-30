"""Shared pytest fixtures for the Zoo Garden test suite."""

import sys
import os

# Ensure src/ is on the path so we can import zoo without installing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest

from zoo import (
    Zoo,
    Enclosure,
    Lion,
    Eagle,
    Penguin,
    Crocodile,
    Elephant,
    Monkey,
    Zookeeper,
    Veterinarian,
    Guide,
)


@pytest.fixture
def lion() -> Lion:
    """Return a fresh Lion instance."""
    return Lion("Simba", 5)


@pytest.fixture
def eagle() -> Eagle:
    """Return a fresh Eagle instance."""
    return Eagle("Sam", 3)


@pytest.fixture
def crocodile() -> Crocodile:
    """Return a fresh Crocodile instance."""
    return Crocodile("Rex", 8)


@pytest.fixture
def penguin() -> Penguin:
    """Return a fresh Penguin instance."""
    return Penguin("Pete", 2)


@pytest.fixture
def elephant() -> Elephant:
    """Return a fresh Elephant instance."""
    return Elephant("Dumbo", 10, tusk_length=1.5)


@pytest.fixture
def monkey() -> Monkey:
    """Return a fresh Monkey instance."""
    return Monkey("George", 4)


@pytest.fixture
def enclosure(lion, eagle, crocodile) -> Enclosure:
    """Return an Enclosure with capacity 5 pre-populated with lion, eagle, crocodile."""
    enc = Enclosure("Savanna", 5)
    enc.add_animal(lion)
    enc.add_animal(eagle)
    enc.add_animal(crocodile)
    return enc


@pytest.fixture
def zoo(enclosure) -> Zoo:
    """Return a Zoo with one enclosure ('Savanna') already created."""
    z = Zoo("Test Zoo", "Warsaw")
    z._enclosures["Savanna"] = enclosure
    return z


@pytest.fixture
def zookeeper() -> Zookeeper:
    """Return a fresh Zookeeper instance."""
    return Zookeeper("Alice")


@pytest.fixture
def veterinarian() -> Veterinarian:
    """Return a fresh Veterinarian instance."""
    return Veterinarian("Dr. Smith", specialization="exotic")


@pytest.fixture
def guide() -> Guide:
    """Return a fresh Guide instance."""
    return Guide("Bob", languages=["English", "Polish"])
