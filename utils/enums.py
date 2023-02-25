import enum


# Roles
class RolesTypes(str, enum.Enum):
    guest = "guest"
    superuser = "superuser"
    house_property = "house property"
    car_property = "car property"


# Room booking status
class RoomAvailabilityStatus(str, enum.Enum):
    vacant = "vacant"
    occupied = "occupied"
