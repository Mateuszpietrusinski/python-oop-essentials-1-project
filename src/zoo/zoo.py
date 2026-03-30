"""Top-level Zoo class for the Zoo Garden system.

Zoo composes Enclosure objects (enclosures do not exist without the zoo)
and aggregates Employee objects (employees can exist independently).
"""

from __future__ import annotations

from .animals import Animal
from .employees import Employee
from .enclosure import Enclosure


class Zoo:
    """Represents a complete zoological garden.

    Relationships:
        - Zoo ◆── Enclosure  (composition: enclosures are created by and owned by Zoo)
        - Zoo ◇── Employee   (aggregation: employees are added externally)
    """

    def __init__(self, name: str, city: str = "Lodz") -> None:
        """Initialise a Zoo.

        Args:
            name: Name of the zoo.
            city: City where the zoo is located. Defaults to "Lodz".
        """
        self._name: str = name
        self._city: str = city
        self._enclosures: dict[str, Enclosure] = {}
        self._employees: list[Employee] = []

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def name(self) -> str:
        """Name of the zoo."""
        return self._name

    @property
    def city(self) -> str:
        """City where the zoo is located."""
        return self._city

    # ------------------------------------------------------------------
    # Enclosure management (composition)
    # ------------------------------------------------------------------

    def create_enclosure(self, name: str, capacity: int) -> Enclosure:
        """Create a new enclosure owned by this zoo.

        Args:
            name: Display name for the enclosure.
            capacity: Maximum number of animals the enclosure can hold.

        Returns:
            The newly created Enclosure instance.
        """
        enclosure = Enclosure(name, capacity)
        self._enclosures[name] = enclosure
        return enclosure

    # ------------------------------------------------------------------
    # Employee management (aggregation)
    # ------------------------------------------------------------------

    def hire_employee(self, employee: Employee) -> None:
        """Add an externally created employee to the zoo.

        Args:
            employee: The Employee instance to hire.
        """
        self._employees.append(employee)

    # ------------------------------------------------------------------
    # Query methods
    # ------------------------------------------------------------------

    def total_animals(self) -> int:
        """Return the total number of animals across all enclosures.

        Returns:
            Sum of animals in every enclosure.
        """
        return sum(len(enc) for enc in self._enclosures.values())

    def find_animal(self, name: str) -> Animal | None:
        """Search all enclosures for an animal by name.

        Args:
            name: The animal's display name to search for.

        Returns:
            The first matching Animal instance, or None if not found.
        """
        for enclosure in self._enclosures.values():
            animal = enclosure.find_animal(name)
            if animal is not None:
                return animal
        return None

    def report(self) -> str:
        """Generate a summary report of the zoo's current state.

        Returns:
            A formatted multi-line string containing zoo statistics.
        """
        lines = [
            f"=== {self._name} — Zoo Report ===",
            f"City: {self._city}",
            f"Enclosures: {len(self._enclosures)}",
            f"Total animals: {self.total_animals()}",
            f"Employees: {len(self._employees)}",
            "",
            "--- Enclosures ---",
        ]
        for enc in self._enclosures.values():
            lines.append(
                f"  [{enc.name}] capacity={enc.capacity}, animals={len(enc)}"
            )
            for animal in enc:
                lines.append(f"    • {animal}")
        if self._employees:
            lines.append("")
            lines.append("--- Staff ---")
            for emp in self._employees:
                lines.append(f"  {emp.role()} — {emp.name}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __getitem__(self, name: str) -> Enclosure:
        """Retrieve an enclosure by name.

        Args:
            name: The enclosure's display name.

        Returns:
            The matching Enclosure instance.

        Raises:
            KeyError: If no enclosure with that name exists.
        """
        return self._enclosures[name]

    def __contains__(self, item: object) -> bool:
        """Check whether an Animal or Employee is in the zoo.

        Args:
            item: An Animal or Employee instance to look for.

        Returns:
            True if the item is found, False otherwise.
        """
        if isinstance(item, Animal):
            return any(item in enc for enc in self._enclosures.values())
        if isinstance(item, Employee):
            return item in self._employees
        return False

    def __len__(self) -> int:
        """Return the number of enclosures in the zoo."""
        return len(self._enclosures)

    def __repr__(self) -> str:
        """Machine-readable representation."""
        return f"Zoo(name={self._name!r}, city={self._city!r}, enclosures={len(self._enclosures)})"
