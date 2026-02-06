"""Тест для функции multiply."""

from calc import multiply


def test_multiply() -> None:
    assert multiply(2, 3) == 6
