import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Forbidden Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    ACCESS_TOKEN_EXPIRES_IN: int = os.getenv("ACCESS_TOKEN_EXPIRES_IN")
    # REFRESH_TOKEN_EXPIRES_IN: int = os.getenv("REFRESH_TOKEN_EXPIRES_IN")

    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    # CLIENT_ORIGIN: str

    # JWT_PUBLIC_KEY: str
    # JWT_PRIVATE_KEY: str


settings = Settings()
