from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.core.database import get_session
from backend.schemas.exercise import ExerciseCreate, ExerciseRead
from backend.services import exercise_service

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get("/", response_model=list[ExerciseRead])
def read_exercises(session: Session = Depends(get_session)):
    return exercise_service.read_exercises(session)


@router.post("/", response_model=ExerciseRead)
def create_exercise(data: ExerciseCreate, session: Session = Depends(get_session)):
    return exercise_service.create_exercise(data, session)
