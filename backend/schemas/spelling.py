from pydantic import BaseModel


class SpellingRequest(BaseModel):
    text: str


class SpellingResponse(BaseModel):
    old_text: str
    no_spelling_text: str
