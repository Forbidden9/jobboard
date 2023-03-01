import uuid

from db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response, Security

from models.house.house import House
from models.user.user import User
from routers.user.oauth2 import get_current_user_house, get_current_active_user
from schemas.house.house import ListHouseResponse, HouseResponse, CreateHouseSchema, UpdateHouseSchema
from utils.const import Role

house = APIRouter()


@house.get('/', response_model=ListHouseResponse)
async def get_houses(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    houses = db.query(House).group_by(House.id).group_by(House.user_id).filter(House.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': status.HTTP_200_OK, 'results': len(houses), 'houses': houses}


@house.post('/', status_code=status.HTTP_201_CREATED, response_model=HouseResponse)
async def create_house(house: CreateHouseSchema, db: Session = Depends(get_db)):
    house.user_id = uuid.UUID('123e4567-e89b-12d3-a456-426614174000')  # aqui debe ser el id del cliente loguado
    new_house = House(**house.dict())
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house


@house.put('/{id}', response_model=HouseResponse)
async def update_house(id: str, house: UpdateHouseSchema, db: Session = Depends(get_db)):
    house_query = db.query(House).filter(House.id == id)
    updated_house = house_query.first()

    if not updated_house:
        raise HTTPException(status_code=status.HTTP_200_OK, detail=f'No house with this id: {id} found')
    # if updated_house.user_id != uuid.UUID(user_id):
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not allowed to perform this action')
    # house.user_id = user_id
    house_query.update(house.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return updated_house


@house.get('/{id}', response_model=HouseResponse)
async def get_house(id: str, db: Session = Depends(get_db)):
    house = db.query(House).filter(House.id == id).first()
    if not house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No house with this id: {id} found")
    return house


@house.delete('/{id}')
async def delete_house(id: str, db: Session = Depends(get_db)):
    house_query = db.query(House).filter(House.id == id)
    house = house_query.first()
    if not house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No house with this id: {id} found')

    # if str(house.user_id) != user_id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not allowed to perform this action')
    house_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
