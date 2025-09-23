from fastapi import HTTPException
from sqlmodel import Session, select
from backend.core.models import Exercise, ExerciseTagLink, Tag
from backend.schemas.exercise import ExerciseCreate, ExerciseRead, ExerciseTagBase


def read_exercises(session: Session) -> list[ExerciseRead]:
    exercises = session.exec(select(Exercise)).all()
    results = []
    for ex in exercises:
        exercise_tags = [
            ExerciseTagBase(
                tag_id=link.tag_id,
                name=link.tag.name,
                type=link.tag.type,
                score=link.score
            )
            for link in ex.tags_links
        ]
        results.append(
            ExerciseRead(
                id=ex.id,
                title=ex.title,
                description=ex.description,
                tags=exercise_tags,
            )
        )
    return results


def create_exercise(data: ExerciseCreate, session: Session) -> ExerciseRead:
    # Create exercise
    exercise = Exercise(title=data.title, description=data.description)

    # Attach tags
    for tag_data in data.tags:
        tag = session.get(Tag, tag_data.tag_id)
        if not tag:
            raise HTTPException(status_code=404, detail=f"Tag {tag_data.tag_id} not found")
        link = ExerciseTagLink(exercise=exercise, tag=tag, score=tag_data.score)
        session.add(link)

    session.commit()
    session.refresh(exercise)

    return ExerciseRead(
        id=exercise.id,
        title=exercise.title,
        description=exercise.description,
        tag_names=[link.tag.name for link in exercise.tags_links if link.tag],
    )
