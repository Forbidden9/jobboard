import uuid
from datetime import datetime
from sqlalchemy import Column, text, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP, DateTime
from db.session import Base


class House(Base):
    __tablename__ = "houses"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)

    # Informacion de la casa
    name = Column(String,  nullable=False)
    address = Column(String,  nullable=False)
    phones = Column(String,  nullable=False)
    description_house = Column(String,  nullable=False)
    description_other = Column(String,  nullable=False)

    # Extra information
    latitude = Column(String,  nullable=False)
    longitude = Column(String,  nullable=False)
    general_calification = Column(Integer)

    # Services
    breakfast = Column(Boolean, nullable=False, default=False)
    launch = Column(Boolean, nullable=False, default=False)
    dinner = Column(Boolean, nullable=False, default=False)
    laundry = Column(Boolean, nullable=False, default=False)
    guide = Column(Boolean, nullable=False, default=False)
    minibar = Column(Boolean, nullable=False, default=False)
    # Amenities
    air_conditioning = Column(Boolean, nullable=False, default=False)
    private_bathroom = Column(Boolean, nullable=False, default=False)
    towel = Column(Boolean, nullable=False, default=False)
    private_terrace = Column(Boolean, nullable=False, default=False)
    garden = Column(Boolean, nullable=False, default=False)
    parking_inside = Column(Boolean, nullable=False, default=False)
    # English / French / German spoken
    # Facilities
    freezer_in_room = Column(Boolean, nullable=False, default=False)
    hot_water = Column(Boolean, nullable=False, default=False)
    # 110v / 220v
    airport_pick_up = Column(Boolean, nullable=False, default=False)

    user = relationship('User')
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# descripción de sitios históricos, turísticos o paisajes atractivos que puedan visitarse por su cercanía a tu propiedad
# posición geográfica en que esté ubicada tu propiedad
# impulsar estrategias enfocadas en realzar la aventura que implica explorar lugares poco frecuentados;
# resaltar los atractivos propios que tiene el vecindario y tu propiedad en particular;
# e incluso, de ser necesario, valorar estrategias de exclusividad o de descuento que puedan atraer a los indecisos

# cambiar los precios dependiendo de la temporada
