"""Пример работы с SQLite."""

import sqlite3

DB_NAME = "notes.db"


def create_table() -> None:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        # ВАЖНО: создаём таблицу, если её нет
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                text TEXT NOT NULL
            )
            """
        )
        connection.commit()


def add_note(text: str) -> None:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO notes (text) VALUES (?)", (text,))
        connection.commit()


def list_notes() -> list[tuple[int, str]]:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, text FROM notes")
        return cursor.fetchall()


if __name__ == "__main__":
    create_table()
    add_note("Первая заметка")
    print(list_notes())
