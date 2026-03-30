"""Feeding schedule classes for the Zoo Garden system.

FeedingEntry is a simple dataclass representing a single scheduled feeding.
FeedingSchedule composes FeedingEntry objects — entries do not exist outside a schedule.
"""

from __future__ import annotations

from dataclasses import dataclass, field


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


class FeedingSchedule:
    """A daily feeding schedule composed of FeedingEntry instances.

    Entries are owned by this schedule (composition — entries do not exist
    independently of the FeedingSchedule).

    Attributes:
        day: The day this schedule applies to (e.g. "Monday").
    """

    def __init__(self, day: str = "Monday") -> None:
        """Initialise a FeedingSchedule.

        Args:
            day: The weekday this schedule covers. Defaults to "Monday".
        """
        self._day: str = day
        self._entries: list[FeedingEntry] = []

    @property
    def day(self) -> str:
        """The day this schedule applies to."""
        return self._day

    def add_entry(
        self,
        enclosure_name: str,
        time: str,
        food_type: str,
        notes: str = "",
    ) -> FeedingEntry:
        """Create a new FeedingEntry and add it to the schedule.

        Args:
            enclosure_name: Name of the enclosure to be fed.
            time: Feeding time string (e.g. "08:00").
            food_type: Type of food.
            notes: Optional notes. Defaults to "".

        Returns:
            The newly created FeedingEntry.
        """
        entry = FeedingEntry(
            enclosure_name=enclosure_name,
            time=time,
            food_type=food_type,
            notes=notes,
        )
        self._entries.append(entry)
        return entry

    def remove_entry(self, entry: FeedingEntry) -> None:
        """Remove a FeedingEntry from the schedule.

        Args:
            entry: The entry to remove.

        Raises:
            ValueError: If the entry is not found in this schedule.
        """
        self._entries.remove(entry)

    def get_by_enclosure(self, name: str) -> list[FeedingEntry]:
        """Return all entries for a specific enclosure.

        Args:
            name: The enclosure name to filter by.

        Returns:
            A list of FeedingEntry objects for that enclosure.
        """
        return [e for e in self._entries if e.enclosure_name == name]

    def __len__(self) -> int:
        """Return the total number of scheduled feedings."""
        return len(self._entries)

    def __repr__(self) -> str:
        """Machine-readable representation."""
        return f"FeedingSchedule(day={self._day!r}, entries={len(self._entries)})"
