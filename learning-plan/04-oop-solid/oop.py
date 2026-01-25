"""Простой пример ООП с идеей SOLID."""


class User:
    """Класс отвечает только за данные пользователя (S из SOLID)."""

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


class EmailSender:
    """Отдельный класс для отправки писем (разделение ответственности)."""

    def send(self, user: User, message: str) -> None:
        # ВАЖНО: здесь только отправка
        print(f"Отправка письма {user.email}: {message}")


if __name__ == "__main__":
    user = User("Аня", "anya@example.com")
    sender = EmailSender()
    sender.send(user, "Добро пожаловать!")
