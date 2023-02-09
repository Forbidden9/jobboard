from fastapi import APIRouter
from db.session import SessionLocal
from schemas.user import UserSchema

user = APIRouter(tags=["user"])


# Conexion con una session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@user.get("/")
def root():
    return {"message": "Hi, I'm elf"}


@user.post("/api/create_user")
def create_user(data_user: UserSchema):
    print(data_user)


@user.put("/api/update_user/{id}", response_description="esste es otro")
def update_user(id: str):
    pass


@user.delete("/api/delete_user/{id}", response_description="esste es otro")
async def delete_user(id: str):
    pass
