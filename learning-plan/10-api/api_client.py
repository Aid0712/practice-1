"""Пример запроса к API (тут простой мок)."""

import json


def parse_user(data: str) -> dict:
    """Парсим JSON-строку в словарь."""
    # ВАЖНО: json.loads превращает строку в dict
    return json.loads(data)


if __name__ == "__main__":
    fake_response = '{"name": "Аня", "age": 16}'
    user = parse_user(fake_response)
    print(user["name"], user["age"])
