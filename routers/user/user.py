from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db
from models.user.user import User
from schemas.user.user import ListUserResponse, CreateUserSchema, UserResponse

user = APIRouter()


@user.get('/list_user', response_model=ListUserResponse)
async def get_posts(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    users = db.query(User).group_by(User.id).filter(User.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(users), 'users': users}


@user.post('/create_user', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_post(data_user: CreateUserSchema, db: Session = Depends(get_db)):
    new_user = User(**data_user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@user.put("/update_user/{id}", response_description="esste es otro")
def update_user(id: str):
    pass


@user.delete("/delete_user/{id}", response_description="esste es otro")
async def delete_user(id: str):
    pass
