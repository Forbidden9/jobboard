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
    pass


class CarResponse(CarBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class UpdateCarSchema(BaseModel):  # no hereda de CarBaseSchema
    pass
    # created_at: Optional[datetime, None] = None
    # updated_at: Optional[datetime, None] = None

    # class Config:
    #     orm_mode = True


class ListCarResponse(BaseModel):
    status: str
    results: int
    cars: List[CarResponse]
