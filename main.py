from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.config import settings
from db.session import engine
from db.base_class import Base
from router.router import user
import uvicorn


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(user)
    return app


# app = start_application()

if __name__ == "__main__":
    uvicorn.run(start_application(), host="127.0.0.1", port=8000, workers=True)
