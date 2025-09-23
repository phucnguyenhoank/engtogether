from sqlmodel import SQLModel, Field, Relationship

class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: str    # genre, formality, purpose, audience, etc.

    exercises_links: list["ExerciseTagLink"] = Relationship(back_populates="tag")

class Exercise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None

    tags_links: list["ExerciseTagLink"] = Relationship(back_populates="exercise")

class ExerciseTagLink(SQLModel, table=True):
    exercise_id: int | None = Field(default=None, foreign_key="exercise.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)
    score: float = Field(default=5.0)

    exercise: Exercise | None = Relationship(back_populates="tags_links")
    tag: Tag | None = Relationship(back_populates="exercises_links")
