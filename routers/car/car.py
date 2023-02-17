import uuid
from db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response

# from app.oauth2 import require_user

from models.car.car import Car
from schemas.car.car import ListCarResponse, CarResponse, CreateCarSchema, UpdateCarSchema

car = APIRouter()


@car.get('/', response_model=ListCarResponse)
async def get_cars(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    cars = db.query(Car).group_by(Car.id).filter(Car.car_model.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(cars), 'cars': cars}


@car.post('/', status_code=status.HTTP_201_CREATED, response_model=CarResponse)
async def create_car(car: CreateCarSchema, db: Session = Depends(get_db)):
    # car.user_id = uuid.UUID(owner_id)
    new_car = Car(**car.dict())
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


@car.put('/{id}', response_model=CarResponse)
async def update_car(id: str, car: UpdateCarSchema, db: Session = Depends(get_db)):
    car_query = db.query(Car).filter(Car.id == id)
    updated_car = car_query.first()

    if not updated_car:
        raise HTTPException(status_code=status.HTTP_200_OK, detail=f'No car with this id: {id} found')
    # if updated_car.user_id != uuid.UUID(user_id):
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not allowed to perform this action')
    # car.user_id = user_id
    car_query.update(car.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return updated_car


@car.get('/{id}', response_model=CarResponse)
async def get_car(id: str, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == id).first()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No car with this id: {id} found")
    return car


@car.delete('/{id}')
async def delete_car(id: str, db: Session = Depends(get_db)):
    car_query = db.query(Car).filter(Car.id == id)
    car = car_query.first()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No car with this id: {id} found')

    # if str(car.user_id) != user_id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not allowed to perform this action')
    car_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
