import uuid
from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from db.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String,  nullable=False)
    username = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=True)
    is_superuser = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

    # photo = Column(String, nullable=True)
    # verified = Column(Boolean, nullable=False, server_default='False')
    # verification_code = Column(String, nullable=True, unique=True)
    # role = Column(String, server_default='user', nullable=False)


# users = Table("users", meta_data,
#               Column("id", Integer, primary_key=True, index=True),
#               Column("name", String(255), nullable=False),
#               Column("username", String(255), nullable=False),
#               Column("email", String(255), nullable=False, unique=True, index=True),
#               Column("password", String(255), nullable=False, unique=True),
#               Column("is_active", Boolean, default=True),
#               Column("is_superuser", Boolean, default=False)
#               )
