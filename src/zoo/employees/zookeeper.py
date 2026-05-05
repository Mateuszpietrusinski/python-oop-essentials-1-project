"""Zookeeper concrete employee class for the Zoo Garden system."""

from __future__ import annotations

from typing import Optional

from ..enclosure import Enclosure
from .employee import Employee


class Zookeeper(Employee):
    """A zookeeper responsible for the day-to-day care of animals.

    Associated with a single Enclosure (association relationship).
    The enclosure can exist independently of the zookeeper.
    """

    def __init__(self, name: str, salary: float = 4500.0) -> None:
        """Initialise a Zookeeper.

        Args:
            name: Employee's full name.
            salary: Monthly salary in PLN. Defaults to 4500.0.
        """
        super().__init__(name, salary)
        self._assigned_enclosure: Optional[Enclosure] = None

    def assign_to(self, enclosure: Enclosure) -> None:
        """Assign this zookeeper to an enclosure.

        Args:
            enclosure: The Enclosure to be responsible for.
        """
        self._assigned_enclosure = enclosure

    def feed_animals(self) -> str:
        """Feed all animals in the assigned enclosure.

        Returns:
            A summary string of the feeding activity, or a message
            indicating no enclosure is assigned.
        """
        if self._assigned_enclosure is None:
            return f"{self._name} is not assigned to any enclosure."
        results = self._assigned_enclosure.feed_all()
        summary = "\n  ".join(results)
        return (
            f"{self._name} fed animals in '{self._assigned_enclosure.name}':\n  {summary}"
        )

    def work(self) -> str:
        """Describe the zookeeper's work.

        Returns:
            Work activity description.
        """
        if self._assigned_enclosure:
            return (
                f"{self._name} is cleaning and maintaining '{self._assigned_enclosure.name}'."
            )
        return f"{self._name} is waiting for an enclosure assignment."

    def role(self) -> str:
        """Return the zookeeper's role description.

        Returns:
            Role string including assigned enclosure if any.
        """
        enc = self._assigned_enclosure.name if self._assigned_enclosure else "unassigned"
        return f"Zookeeper — assigned to: {enc}"
