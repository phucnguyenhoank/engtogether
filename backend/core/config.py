from pydantic_settings  import BaseSettings


class Settings(BaseSettings):
    # change this to match where you will serve the frontend (port 5500 used below)
    frontend_origin: str = "http://127.0.0.1:5500"

settings = Settings()