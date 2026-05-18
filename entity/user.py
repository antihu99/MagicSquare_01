from __future__ import annotations

from dataclasses import dataclass


EMPTY_NAME_ERROR = "name must not be empty"


@dataclass(frozen=True)
class User:
    """Represents a MagicSquare user.

    Attributes:
        name: The user's normalized display name.
    """

    name: str

    def __post_init__(self) -> None:
        normalized_name = self.name.strip()

        if not normalized_name:
            raise ValueError(EMPTY_NAME_ERROR)

        object.__setattr__(self, "name", normalized_name)

    def rename(self, name: str) -> User:
        """Create a user with a new name.

        Args:
            name: The new display name.

        Returns:
            A new user instance with the normalized name.

        Raises:
            ValueError: If the new name is empty.
        """
        return User(name=name)
