from fastapi import APIRouter
from schemas.user import UserSchema

user = APIRouter()


@user.get("/")
def root():
    return {"message": "Hi, I'm elf"}


@user.post("/api/create_user")
def create_user(data_user: UserSchema):
    print(data_user)
