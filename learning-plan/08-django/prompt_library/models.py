"""Модель для Django проекта (пример)."""

from django.db import models


class Prompt(models.Model):
    """Промпт для ИИ (простая модель)."""

    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self) -> str:
        # ВАЖНО: удобное отображение в админке
        return self.title
