"""Мини-API заметок на FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NoteIn(BaseModel):
    text: str


class NoteOut(BaseModel):
    id: int
    text: str


notes: list[NoteOut] = []


@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteIn) -> NoteOut:
    # ВАЖНО: простая логика без лишних слоёв (KISS)
    new_note = NoteOut(id=len(notes) + 1, text=note.text)
    notes.append(new_note)
    return new_note


@app.get("/notes", response_model=list[NoteOut])
def list_notes() -> list[NoteOut]:
    return notes
