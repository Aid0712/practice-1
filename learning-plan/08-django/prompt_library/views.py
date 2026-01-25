"""Простое представление (пример)."""

from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    # ВАЖНО: минимальная логика
    return HttpResponse("Библиотека промптов")
