from pydantic import BaseModel


class ExerciseTagBase(BaseModel):
    tag_id: int
    score: float = 5.0


class ExerciseCreate(BaseModel):
    title: str
    description: str | None = None
    tags: list[ExerciseTagBase] = []


class ExerciseRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    tag_names: list[str]  # return tag names for simplicity

    class Config:
        from_attributes = True
