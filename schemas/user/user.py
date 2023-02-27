import uuid
from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
from datetime import datetime
from schemas.user.user_role import UserRole


class UserBaseSchema(BaseModel):
    fullname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    photo: Optional[str] = None
    is_active: Optional[bool] = None


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    user_role: Optional[UserRole]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserResponse):
    pass


# Additional properties stored in DB
class UserInDB(UserResponse):
    password: str  # hashed_password


class FilteredUserResponse(UserBaseSchema):
    id: uuid.UUID


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserResponse]
