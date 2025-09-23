from pydantic import BaseModel


class CoEdITRequest(BaseModel):
    instruction: str | None = None
    text: str


class CoEdITResponse(BaseModel):
    instruction: str
    old_text: str
    improved_text: str
