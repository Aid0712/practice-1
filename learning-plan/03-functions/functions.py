"""Примеры функций с простыми задачами."""


def add(a: int, b: int) -> int:
    """Складывает два числа."""
    # ВАЖНО: функция делает только одну вещь
    return a + b


def greet(name: str) -> str:
    """Говорит привет."""
    return f"Привет, {name}!"


if __name__ == "__main__":
    print(add(2, 3))
    print(greet("Аня"))
