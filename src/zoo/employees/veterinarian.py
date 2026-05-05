"""Veterinarian concrete employee class for the Zoo Garden system."""

from __future__ import annotations

from .employee import Employee


class Veterinarian(Employee):
    """A veterinarian providing medical care to zoo animals.

    Can specialise in either general or exotic animal medicine.
    """

    def __init__(
        self,
        name: str,
        specialization: str = "general",
        salary: float = 7000.0,
    ) -> None:
        """Initialise a Veterinarian.

        Args:
            name: Employee's full name.
            specialization: Medical specialization ("general" or "exotic").
            salary: Monthly salary in PLN. Defaults to 7000.0.
        """
        super().__init__(name, salary)
        self._specialization: str = specialization

    @property
    def specialization(self) -> str:
        """Medical specialization ("general" or "exotic")."""
        return self._specialization

    def work(self) -> str:
        """Describe the veterinarian's work.

        Returns:
            Work activity description.
        """
        return f"{self._name} is conducting health checks on {self._specialization} animals."

    def role(self) -> str:
        """Return the veterinarian's role description.

        Returns:
            Role string including specialization.
        """
        return f"Veterinarian ({self._specialization} specialization)"
