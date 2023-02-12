import uuid
from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
from datetime import datetime


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    username: str
    password: constr(min_length=8)
    password_confirm: str
    is_active: bool = True
    is_superuser: bool = False


# role: str = 'user'
# verified: bool = False

# year: int = Field(..., gt=0, lt=9)
# gpa: float = Field(..., le=4.0)
#
# class Config:
#     schema_extra = {
#         "example": {
#             "fullname": "John Doe",
#             "email": "jdoe@x.edu.ng",
#             "course_of_study": "Water resources engineering",
#             "year": 2,
#             "gpa": "3.0",
#         }
#     }


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserResponse]
