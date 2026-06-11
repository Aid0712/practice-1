"""Простой поиск ключевых слов в тексте."""

from collections import Counter

STOP_WORDS = {"и", "в", "на", "это", "а", "но", "мы", "я"}


def clean_text(text: str) -> list[str]:
    """Очищает текст и возвращает список слов."""
    # ВАЖНО: заменяем знаки на пробелы
    for symbol in ",.!?:;":
        text = text.replace(symbol, " ")
    words = text.lower().split()
    return [word for word in words if len(word) > 2 and word not in STOP_WORDS]


def top_keywords(text: str, limit: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ слов по частоте."""
    words = clean_text(text)
    counter = Counter(words)
    return counter.most_common(limit)


if __name__ == "__main__":
    sample = """Python — отличный язык. Python помогает быстро писать код.
    Мы учим Python и делаем проекты."""
    print(top_keywords(sample))
