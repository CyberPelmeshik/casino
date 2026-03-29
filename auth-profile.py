"""Модуль модели пользователя интернет-казино."""

class User:
    """Представляет пользователя системы.

    Attributes:
        username: Логин пользователя.
        email: Электронная почта пользователя.
        is_verified: Признак подтверждения почты.
    """

    def __init__(self, username: str, email: str) -> None:
        """Создает нового пользователя.

        Args:
            username: Логин пользователя.
            email: Электронная почта пользователя.
        """
        self.username = username
        self.email = email
        self.is_verified = False

    def verify_email(self) -> None:
        """Подтверждает электронную почту пользователя."""
        self.is_verified = True

    def __str__(self) -> str:
        """Возвращает строковое представление пользователя."""
        return (
            f"User(username={self.username}, "
            f"email={self.email}, verified={self.is_verified})"
        )