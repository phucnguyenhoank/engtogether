from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.api import grammars
from backend.core.config import settings


app = FastAPI(title="EngTogether - Grammar API")
app.include_router(grammars.router)

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