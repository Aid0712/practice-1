"""API для простого анализа текста."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

POSITIVE_WORDS = {"хорошо", "отлично", "классно", "радость"}
NEGATIVE_WORDS = {"плохо", "грустно", "ужасно", "страх"}


class TextIn(BaseModel):
    text: str


class TextOut(BaseModel):
    length: int
    score: int


@app.post("/analyze", response_model=TextOut)
def analyze_text(payload: TextIn) -> TextOut:
    words = payload.text.lower().split()
    score = 0
    for word in words:
        if word in POSITIVE_WORDS:
            score += 1
        if word in NEGATIVE_WORDS:
            score -= 1
    # ВАЖНО: минимум логики, простой результат
    return TextOut(length=len(payload.text), score=score)
