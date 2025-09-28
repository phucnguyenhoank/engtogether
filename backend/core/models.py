from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class Tag(SQLModel, table=True):
    """
    Represents a categorical label that can be applied to both Users and Exercises
    in order to describe their attributes and enable personalized recommendations.

    Tags are grouped by `type`, which specifies the category of the tag
    (e.g., "proficiency", "purpose", "genre", etc.). The `name` field
    stores the specific value within that category.

    Examples
    --------
    For Users:
      - Proficiency (one tag per user): beginner / intermediate / advanced
      - Purpose: exam, career, hobby
      - Interest: academic, business, casual, creative

    For Exercises:
      - Genre: academic, business, creative writing, persuasive,
               expository, descriptive, narrative
      - Formality: formal, informal, neutral
      - Purpose: inform, persuade, entertain, explain, analyze, summarize
      - Audience: students, teachers, employer, colleagues
      - Difficulty (one tag per exercise): beginner / intermediate / advanced

    Notes
    -----
    - Users can be linked to multiple tags, except for "proficiency" which
      should be unique per user.
    - Exercises can be linked to multiple tags to describe their nature.
    - Matching between user tags and exercise tags is the basis for
      content-based recommendation.
    """
    id: int | None = Field(default=None, primary_key=True)
    type: str    # The category of the tag (e.g., "genre", "formality", "purpose", "audience")
    name: str    # The specific label within the category (e.g., "business", "formal", "exam")

    exercises_links: list["ExerciseTagLink"] = Relationship(back_populates="tag")



class Exercise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    estimated_time_min: int | None = None
    min_words: int | None = None
    created_at: datetime = Field(default_factory=utc_now)

    tags_links: list["ExerciseTagLink"] = Relationship(back_populates="exercise")
    interactions: list["Interaction"] = Relationship(back_populates="exercise")


class ExerciseTagLink(SQLModel, table=True):
    exercise_id: int | None = Field(default=None, foreign_key="exercise.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)
    score: float = Field(default=5.0)

    exercise: Exercise | None = Relationship(back_populates="tags_links")
    tag: Tag | None = Relationship(back_populates="exercises_links")


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password_hash: str   # never store raw password
    created_at: datetime = Field(default_factory=utc_now)
    last_login: datetime | None = None

    tags_links: list["UserTagLink"] = Relationship(back_populates="user")
    interactions: list["Interaction"] = Relationship(back_populates="user")


class UserTagLink(SQLModel, table=True):
    user_id: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)
    weight: float = Field(default=1.0)   # importance, e.g. proficiency=1.0, minor interest=0.5

    user: User | None = Relationship(back_populates="tags_links")
    tag: Tag | None = Relationship()


class Interaction(SQLModel, table=True):
    # Assume 100% Clicked
    id: int | None = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    exercise_id: int = Field(foreign_key="exercise.id")

    timestamp: datetime = Field(default_factory=utc_now)

    # interaction signals
    click_within_30s: bool = False
    finished: bool = False
    fav: bool | None = None    # 0 = dislike, 1 = like
    rating: int | None = None  # 1–5 stars
    review: str | None = None
    time_spent_sec: int = Field(default=0)

    user: User = Relationship(back_populates="interactions")
    exercise: Exercise = Relationship(back_populates="interactions")


class RecommendationLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    exercise_id: int = Field(foreign_key="exercise.id")
    recommended_at: datetime = Field(default_factory=utc_now)
    was_clicked: bool = False

