from sqlmodel import create_engine, SQLModel, Session, select
from backend.core.models import Tag, Exercise, ExerciseTagLink, User, UserTagLink, Interaction
from typing import Iterator
import random
import hashlib


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
        # --- User tags ---
        "proficiency": ["beginner", "intermediate", "advanced"],   # unique per user
        "goal": ["exam", "career", "hobby"],
        "interest": ["academic", "business", "casual", "creative"],

        # --- Exercise tags ---
        "genre": ["academic", "business", "creative writing", "persuasive",
                  "expository", "descriptive", "narrative"],
        "formality": ["formal", "informal", "neutral"],
        "purpose": ["inform", "persuade", "entertain", "explain", "analyze", "summarize"],
        "audience": ["students", "teachers", "employer", "colleagues"],
        "difficulty": ["beginner", "intermediate", "advanced"],   # unique per exercise
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
    # Sample exercise templates
    exercise_templates = [
        ("Write a formal email to your professor", "Practice writing a polite, academic email.", 10, 150),
        ("Describe your favorite holiday memory", "Focus on descriptive writing using sensory details.", 15, 200),
        ("Write a business proposal", "Draft a concise business proposal for a new product.", 25, 300),
        ("Summarize a news article", "Practice condensing information into a short summary.", 12, 180),
        ("Write a persuasive essay about social media", "Argue for or against the impact of social media.", 30, 400),
        ("Create a story about a mysterious event", "Use narrative style and build suspense.", 20, 350),
        ("Explain how to cook your favorite dish", "Instructional/expository writing exercise.", 18, 250),
        ("Write an informal message to a friend", "Practice casual tone and personal style.", 5, 80),
        ("Draft a cover letter for a job", "Focus on professional tone and purpose.", 22, 300),
        ("Analyze a poem of your choice", "Critical analysis and academic tone.", 28, 400),
    ]

    # Fetch tags by type
    with Session(engine) as session:
        tags_by_type = {}
        tag_types = ["genre", "formality", "purpose", "audience", "difficulty"]
        for t in tag_types:
            tags_by_type[t] = session.exec(select(Tag).where(Tag.type == t)).all()

        # Create at least 30 exercises (reusing templates with variations)
        for i in range(30):
            title, desc, est_time, min_words = random.choice(exercise_templates)

            exercise = Exercise(
                title=f"{title} (v{i+1})",  # avoid duplicates
                description=desc,
                estimated_time_min=est_time,
                min_words=min_words,
            )
            session.add(exercise)

            # Assign 1 tag from each category
            for tag_type, tags in tags_by_type.items():
                if tags:
                    chosen_tag = random.choice(tags)
                    session.add(
                        ExerciseTagLink(tag_id=chosen_tag.id, score=5.0, exercise=exercise)
                    )

        session.commit()


def fake_password_hash(password: str) -> str:
    # For demo purposes only (replace with real hashing in production, e.g., bcrypt)
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def seed_users():
    usernames = [
        "alice", "bob", "charlie", "diana", "eva",
        "frank", "grace", "henry", "irene", "jack"
    ]

    with Session(engine) as session:
        # Load tags
        prof_tags = session.exec(select(Tag).where(Tag.type == "proficiency")).all()
        goal_tags = session.exec(select(Tag).where(Tag.type == "goal")).all()
        interest_tags = session.exec(select(Tag).where(Tag.type == "interest")).all()

        for i, username in enumerate(usernames):
            email = f"{username}@example.com"
            exists = session.exec(select(User).where(User.email == email)).first()
            if exists:
                continue

            user = User(
                username=username,
                email=email,
                password_hash=fake_password_hash("password123"),
            )
            session.add(user)

            # --- Assign tags ---
            # Proficiency: exactly 1
            prof = random.choice(prof_tags)
            session.add(UserTagLink(user=user, tag_id=prof.id, weight=1.0))

            # Goals: 1–2
            for goal in random.sample(goal_tags, k=random.randint(1, 2)):
                session.add(UserTagLink(user=user, tag_id=goal.id, weight=1.0))

            # Interests: 2–3
            for interest in random.sample(interest_tags, k=random.randint(2, 3)):
                session.add(UserTagLink(user=user, tag_id=interest.id, weight=1.0))

        session.commit()


def seed_interactions():
    sample_reviews = [
        "Very helpful exercise!",
        "A bit too easy for me.",
        "Challenging but rewarding.",
        "Didn't really like the topic.",
        "Great practice, will try again.",
        "Too difficult, need more hints.",
        "Clear instructions and useful.",
    ]
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        exercises = session.exec(select(Exercise)).all()

        for user in users:
            # Pick 5–10 random exercises for this user
            chosen_exercises = random.sample(exercises, k=random.randint(5, 10))

            for ex in chosen_exercises:
                # Check if already exists (avoid duplicates)
                exists = session.exec(
                    select(Interaction).where(
                        Interaction.user_id == user.id,
                        Interaction.exercise_id == ex.id
                    )
                ).first()
                if exists:
                    continue

                finished = random.random() < 0.6   # 60% chance
                quick_bounce = not finished and (random.random() < 0.3)

                fav = None
                rating = None
                review = None
                time_spent_sec = random.randint(0, 60 * 3)

                if finished:
                    fav = random.choice([True, True, False, None, None])
                    rating = random.choices([3, 4, 5], weights=[2, 3, 4])[0]
                    review = random.choice(sample_reviews)
                elif quick_bounce:
                    fav = False
                    rating = random.choice([1, 2])
                else:
                    # just clicked and left
                    if random.random() < 0.2:
                        rating = 3

                interaction = Interaction(
                    user_id=user.id,
                    exercise_id=ex.id,
                    click_within_30s=quick_bounce,
                    finished=finished,
                    fav=fav,
                    rating=rating,
                    review=review,
                    time_spent_sec=time_spent_sec
                )
                session.add(interaction)

        session.commit()

