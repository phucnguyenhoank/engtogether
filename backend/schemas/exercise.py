from pydantic import BaseModel


class ExerciseTagBase(BaseModel):
    tag_id: int | None = None
    name: str
    type: str | None = None
    score: float = 5.0


class ExerciseCreate(BaseModel):
    title: str
    description: str | None = None
    tags: list[ExerciseTagBase]


class ExerciseRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    tags: list[ExerciseTagBase]

