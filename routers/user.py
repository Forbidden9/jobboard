import uuid
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from schemas.user import ListUserResponse, CreateUserSchema, UserResponse



@user.get('/list_user', response_model=ListUserResponse)
def get_posts(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    users = db.query(User).group_by(User.id).filter(User.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(users), 'users': users}


@user.post('/create_user', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_post(data_user: CreateUserSchema, db: Session = Depends(get_db)):
    new_user = User(**data_user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user.post("/api/create_user")
def create_user(data_user: UserSchema):
    print(data_user)


@user.put("/api/update_user/{id}", response_description="esste es otro")
def update_user(id: str):
    pass


@user.delete("/api/delete_user/{id}", response_description="esste es otro")
async def delete_user(id: str):
    pass
