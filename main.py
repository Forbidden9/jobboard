from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.config import settings
from db.session import engine
from db.base_class import Base


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    return app


app = start_application()
