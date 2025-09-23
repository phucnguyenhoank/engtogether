from sqlmodel import create_engine, SQLModel, Session, select
from backend.core.models import Tag, Exercise, ExerciseTagLink
from typing import Iterator
import random

DATABASE_FILENAME = "database.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILENAME}"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session

def seed_tags():
    tags_data = {
        "genre": ["narrative", "descriptive", "expository", "persuasive", "business", "academic", "creative writing"],
        "formality": ["formal", "informal", "neutral"],
        "purpose": ["inform", "persuade", "entertain", "explain", "analyze", "summarize"],
        "audience": ["general public", "students", "teachers", "employer", "colleagues", "customers"],
    }

    with Session(engine) as session:
        for tag_type, names in tags_data.items():
            for name in names:
                exists = session.exec(
                    select(Tag).where(Tag.name == name, Tag.type == tag_type)
                ).first()
                if not exists:
                    session.add(Tag(name=name, type=tag_type))
        session.commit()

def seed_exercises():
    exercises_data = [
        {
            "title": "Write a short story about a childhood memory",
            "description": "Practice narrative writing by recalling a memorable childhood experience.",
            "tags": [("genre", "narrative"), ("purpose", "entertain"), ("audience", "general public")]
        },
        {
            "title": "Describe your favorite place",
            "description": "Practice descriptive writing with vivid details about a familiar location.",
            "tags": [("genre", "descriptive"), ("purpose", "inform"), ("audience", "students")]
        },
        {
            "title": "Explain how photosynthesis works",
            "description": "Practice expository writing with a scientific explanation.",
            "tags": [("genre", "expository"), ("purpose", "explain"), ("audience", "teachers")]
        },
        {
            "title": "Convince your friend to adopt a healthy lifestyle",
            "description": "Practice persuasive writing by arguing for healthy choices.",
            "tags": [("genre", "persuasive"), ("purpose", "persuade"), ("audience", "students")]
        },
        {
            "title": "Write a formal business email to request information",
            "description": "Practice business writing in a professional setting.",
            "tags": [("genre", "business"), ("formality", "formal"), ("audience", "employer")]
        },
        {
            "title": "Summarize the article about climate change",
            "description": "Practice academic summarizing skills.",
            "tags": [("genre", "academic"), ("purpose", "summarize"), ("audience", "teachers")]
        },
        {
            "title": "Write a creative short poem about friendship",
            "description": "Practice creative writing through poetry.",
            "tags": [("genre", "creative writing"), ("purpose", "entertain"), ("audience", "general public")]
        },
        {
            "title": "Explain the rules of your favorite sport",
            "description": "Expository writing focusing on clarity and structure.",
            "tags": [("genre", "expository"), ("purpose", "inform"), ("audience", "students")]
        },
        {
            "title": "Write a casual message to your friend about your weekend",
            "description": "Practice informal writing in a friendly tone.",
            "tags": [("formality", "informal"), ("purpose", "inform"), ("audience", "friends")]
        },
        {
            "title": "Analyze the theme of justice in a short story",
            "description": "Practice academic analysis with textual evidence.",
            "tags": [("genre", "academic"), ("purpose", "analyze"), ("audience", "teachers")]
        },
        {
            "title": "Write an email to a customer apologizing for a late delivery",
            "description": "Business writing with a professional and empathetic tone.",
            "tags": [("genre", "business"), ("formality", "formal"), ("audience", "customers")]
        },
        {
            "title": "Create a product description for a new smartphone",
            "description": "Persuasive writing focusing on marketing.",
            "tags": [("genre", "business"), ("purpose", "persuade"), ("audience", "customers")]
        },
        {
            "title": "Summarize a TED Talk in 150 words",
            "description": "Concise academic summarization exercise.",
            "tags": [("genre", "academic"), ("purpose", "summarize"), ("audience", "students")]
        },
        {
            "title": "Write a story starting with 'It was a dark and stormy night...'",
            "description": "Creative writing prompt to spark imagination.",
            "tags": [("genre", "creative writing"), ("purpose", "entertain"), ("audience", "general public")]
        },
        {
            "title": "Explain how to cook your favorite dish",
            "description": "Instructional expository writing exercise.",
            "tags": [("genre", "expository"), ("purpose", "explain"), ("audience", "students")]
        },
        {
            "title": "Write a formal cover letter for a job application",
            "description": "Business writing focusing on professionalism.",
            "tags": [("genre", "business"), ("formality", "formal"), ("audience", "employer")]
        },
        {
            "title": "Write a persuasive essay on why reading is important",
            "description": "Formal persuasive writing with supporting arguments.",
            "tags": [("genre", "persuasive"), ("formality", "formal"), ("purpose", "persuade"), ("audience", "teachers")]
        },
        {
            "title": "Describe your daily routine in English",
            "description": "Simple descriptive writing exercise for beginners.",
            "tags": [("genre", "descriptive"), ("purpose", "inform"), ("audience", "students")]
        },
        {
            "title": "Analyze a character from your favorite movie",
            "description": "Practice academic writing with critical thinking.",
            "tags": [("genre", "academic"), ("purpose", "analyze"), ("audience", "students")]
        },
        {
            "title": "Write a short dialogue between two friends arguing",
            "description": "Creative writing focused on dialogue and voice.",
            "tags": [("genre", "creative writing"), ("formality", "informal"), ("audience", "general public")]
        },
    ]

    with Session(engine) as session:
        for ex in exercises_data:
            # Check if it already exists
            exists = session.exec(
                select(Exercise).where(Exercise.title == ex["title"])
            ).first()
            if exists:
                continue

            exercise = Exercise(title=ex["title"], description=ex["description"])

            # Attach tags
            for tag_type, tag_name in ex["tags"]:
                tag = session.exec(
                    select(Tag).where(Tag.type == tag_type, Tag.name == tag_name)
                ).first()
                if tag:
                    session.add(ExerciseTagLink(exercise=exercise, tag=tag, score=round(random.uniform(0, 10), 1)))
            session.commit()
