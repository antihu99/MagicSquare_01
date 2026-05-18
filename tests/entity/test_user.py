import pytest

from entity.user import User


def test_user_stores_trimmed_name() -> None:
    # Arrange
    raw_name = "  Alice  "

    # Act
    user = User(name=raw_name)

    # Assert
    assert user.name == "Alice"


def test_user_rejects_empty_name() -> None:
    # Arrange
    raw_name = "   "

    # Act / Assert
    with pytest.raises(ValueError, match="name must not be empty"):
        User(name=raw_name)


def test_user_can_be_renamed() -> None:
    # Arrange
    user = User(name="Alice")

    # Act
    renamed_user = user.rename("Bob")

    # Assert
    assert renamed_user.name == "Bob"
    assert user.name == "Alice"
