"""FeedingEntry dataclass for the Zoo Garden system."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FeedingEntry:
    """A single scheduled feeding for an enclosure.

    Attributes:
        enclosure_name: Name of the enclosure to be fed.
        time: Feeding time as a string (e.g. "08:00").
        food_type: Type of food to be provided (e.g. "meat", "fish").
        notes: Optional additional notes. Defaults to "".
    """

    enclosure_name: str
    time: str
    food_type: str
    notes: str = ""
