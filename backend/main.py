from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.api import coedits, spellings, exercises
from backend.core.config import settings
from backend.core.database import create_db_and_tables, seed_tags, seed_exercises, seed_users, seed_interactions


@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs *before* the application starts serving requests
    create_db_and_tables()
    seed_tags()
    seed_exercises()
    seed_users()
    seed_interactions()

    yield  # after this, the app runs

    # This code runs when the app is shutting down (after all requests are done)
    # (You can put cleanup code here if needed)

app = FastAPI(title="EngTogether API", lifespan=lifespan)


app.include_router(coedits.router)
app.include_router(spellings.router)
app.include_router(exercises.router)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

# allow the simple frontend origin used in this starter (adjust in config.py if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def serve_index():
    return FileResponse("frontend/index.html")