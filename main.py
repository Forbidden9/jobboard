from fastapi import FastAPI
from config.config import settings
from routers.user import user
import uvicorn


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(user, tags=["user"], prefix='/api/user')
    return app


if __name__ == "__main__":
    uvicorn.run(start_application(), host="127.0.0.1", port=8000, workers=True)
