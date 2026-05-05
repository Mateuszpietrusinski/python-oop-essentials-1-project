"""Guide concrete employee class for the Zoo Garden system."""

from __future__ import annotations

from typing import Optional

from .employee import Employee


class Guide(Employee):
    """A tour guide leading visitors around the zoo.

    Speaks one or more languages to serve international visitors.
    """

    def __init__(
        self,
        name: str,
        languages: Optional[list[str]] = None,
        salary: float = 3500.0,
    ) -> None:
        """Initialise a Guide.

        Args:
            name: Employee's full name.
            languages: List of languages the guide speaks. Defaults to ["English"].
            salary: Monthly salary in PLN. Defaults to 3500.0.
        """
        super().__init__(name, salary)
        self._languages: list[str] = languages if languages is not None else ["English"]

    @property
    def languages(self) -> list[str]:
        """Languages the guide can use for tours."""
        return list(self._languages)

    def work(self) -> str:
        """Describe the guide's work.

        Returns:
            Work activity description.
        """
        langs = ", ".join(self._languages)
        return f"{self._name} is leading a guided tour in: {langs}."

    def role(self) -> str:
        """Return the guide's role description.

        Returns:
            Role string including spoken languages.
        """
        langs = ", ".join(self._languages)
        return f"Guide — languages: {langs}"
