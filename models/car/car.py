import uuid
from sqlalchemy import Table, Column, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from db.session import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)

    # Informacion del vehiculo
    car_license = Column(String,  nullable=False)
    car_model = Column(String,  nullable=False)
    car_color = Column(String,  nullable=False)
    car_engine = Column(String,  nullable=False)

    # Servicios por distancia o kilometraje
    pick_up_at_airports = Column(Boolean, nullable=False, default=True)
    airport_delivery = Column(Boolean, nullable=False, default=True)
    short_distance_travel = Column(Boolean, nullable=False, default=True)
    long_distance_travel = Column(Boolean, nullable=False, default=True)

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


# meta_data.create_all(bind=engine)

# class Car(TimeStampedModel):
#
#     user = models.ForeignKey(verbose_name='Propietario de vehículo', to=CustomUser, on_delete=models.CASCADE)  # Dueño
#     # driver = models.ManyToManyField(verbose_name='Chofer', to=Driver)
#     # user = models.ManyToManyField(User, on_delete=models.CASCADE) -- Huesped
#
#     transmission = models.ForeignKey(verbose_name='Transmisión', to=TransmissionType, blank=True, on_delete=models.CASCADE)
#     engine_direction = models.ForeignKey(verbose_name='Dirección', to=EngineDirection, blank=True, on_delete=models.CASCADE)
#     description_car = models.TextField(verbose_name='Descripción del vehículo', max_length=500, blank=True)
#
#     province = models.ForeignKey(verbose_name='Provincia', to=Province, blank=True, on_delete=models.CASCADE)
#
#     checkin_time = models.TimeField(verbose_name='Check-in', blank=False, null=True)
#     checkout_time = models.TimeField(verbose_name='Check-out', blank=False, null=True)
#
#     # Especificaciones
#
#     guests_seats_number = models.IntegerField(verbose_name='Cantidad de asientos para huespedes')
#     seats_number = models.IntegerField(verbose_name='Cantidad de asientos')
#
#     imagen = models.ImageField(upload_to='static/home', verbose_name="Home", null=True,
#                                default='static/home/homeDefault.png')
#     # No se q poner
#
#     # Precios
#     one_night = models.DecimalField(verbose_name='Una noche', default=0, max_digits=8, decimal_places=2)
#     weekend = models.DecimalField(verbose_name='Fin de semana', default=0, max_digits=8, decimal_places=2)
#     seven_nights = models.DecimalField(verbose_name='Siete noches', default=0, max_digits=8, decimal_places=2)
#     thirty_nights = models.DecimalField(verbose_name='Treinta noches', default=0, max_digits=8, decimal_places=2)

#
#     # Mas informacion
#
#     def __str__(self):
#         return f'Usuario: {self.user} - Matrícula {self.car_license_plate})'
#
#     class Meta:
#         verbose_name = 'Vehículo'
#         verbose_name_plural = 'Vehículos'
