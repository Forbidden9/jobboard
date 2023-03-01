import uuid

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class HouseBaseSchema(BaseModel):
    name: str
    address: str
    phones: str
    description_house: str
    description_other: str
    latitude: str
    longitude: str
    general_calification: int
    breakfast: bool = False
    launch: bool = False
    dinner: bool = False
    laundry: bool = False
    guide: bool = False
    minibar: bool = False
    air_conditioning: bool = False
    private_bathroom: bool = False
    private_terrace: bool = False
    garden: bool = False
    parking_inside: bool = False
    # English / French / German spoken
    freezer_in_room: bool = False
    hot_water: bool = False
    airport_pick_up: bool = False

    class Config:
        orm_mode = True
        

class CreateHouseSchema(HouseBaseSchema):
    user_id: uuid.UUID


class HouseResponse(HouseBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class UpdateHouseSchema(BaseModel):
    name: Optional[str]
    phones: Optional[str]
    description_house: Optional[str]
    description_other: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    general_calification: Optional[int]
    breakfast: Optional[bool]
    launch: Optional[bool]
    dinner: Optional[bool]
    laundry: Optional[bool]
    guide: Optional[bool]
    minibar: Optional[bool]
    air_conditioning: Optional[bool]
    private_bathroom: Optional[bool]
    private_terrace: Optional[bool]
    garden: Optional[bool]
    parking_inside: Optional[bool]
    # English / French / German spoken
    freezer_in_room: Optional[bool]
    hot_water: Optional[bool]
    airport_pick_up: Optional[bool]

    class Config:
        orm_mode = True


class ListHouseResponse(BaseModel):
    status: str
    results: int
    houses: List[HouseResponse]
