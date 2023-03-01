import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class CarBaseSchema(BaseModel):
    car_license: str
    car_model: str
    car_color: str
    car_engine: str
    pick_up_at_airports: bool = True
    airport_delivery: bool = True
    short_distance_travel: bool = True
    long_distance_travel: bool = False

    class Config:
        orm_mode = True


class CreateCarSchema(CarBaseSchema):
    user_id: uuid.UUID


class UpdateCarSchema(BaseModel):
    car_license: Optional[str]
    car_model: Optional[str]
    car_color: Optional[str]
    car_engine: Optional[str]
    pick_up_at_airports: Optional[bool]
    airport_delivery: Optional[bool]
    short_distance_travel: Optional[bool]
    long_distance_travel: Optional[bool]
    user_id: Optional[uuid.UUID]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class CarResponse(CarBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class ListCarResponse(BaseModel):
    status: str
    results: int
    cars: List[CarResponse]
