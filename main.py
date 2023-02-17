from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.config import settings
from db.session import Base, engine
from routers.car.car import car
from routers.user import user
import uvicorn

# origins = [
#     settings.CLIENT_ORIGIN,
# ]


def start_application():
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(user, tags=["user"], prefix='/api/user')
    app.include_router(car, tags=["car"], prefix='/api/car')

    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=origins,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    return app


if __name__ == "__main__":
    uvicorn.run(start_application(), host="127.0.0.1", port=8000, workers=True)
