"""Простая оценка похожести текстов."""

import math


def to_vector(text: str) -> dict[str, int]:
    """Преобразует текст в словарь слов -> частота."""
    words = text.lower().split()
    vector: dict[str, int] = {}
    for word in words:
        vector[word] = vector.get(word, 0) + 1
    return vector


def cosine_similarity(a: dict[str, int], b: dict[str, int]) -> float:
    """Считает косинусную похожесть."""
    # ВАЖНО: общие слова дают вклад в похожесть
    common_words = set(a) & set(b)
    numerator = sum(a[word] * b[word] for word in common_words)
    a_norm = math.sqrt(sum(value * value for value in a.values()))
    b_norm = math.sqrt(sum(value * value for value in b.values()))
    if a_norm == 0 or b_norm == 0:
        return 0.0
    return numerator / (a_norm * b_norm)


if __name__ == "__main__":
    text1 = "python учит писать код быстро"
    text2 = "python помогает писать код"
    vector1 = to_vector(text1)
    vector2 = to_vector(text2)
    print(cosine_similarity(vector1, vector2))
